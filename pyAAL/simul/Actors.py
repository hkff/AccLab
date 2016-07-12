"""
<one line to give the program's name and a brief idea of what it does.>
Copyright (C) 2014 Walid Benghabrit

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = 'hkff'

from pykka import *
import logging
from tools.color import *
from simul.Com import *
from subprocess import Popen, PIPE

# logging.basicConfig(level=logging.DEBUG)


# Behavior
class Behavior:
    def __init__(self, name=""):
        self.name = name
        self.actions = []
        self.author = []
        self.triggers = []

    def is_permitted(self, action):
        for x in self.author:
            print(str(x.action.equal(action)) + " " + str(x.action) + " " + str(action))
            if str(x.author) == "PERMIT" and x.action.equal(action):
                return True
        return False

    def __str__(self):
        at = [str(x) for x in self.author]
        ac = [str(x) for x in self.actions]
        tr = [str(x) for x in self.triggers]
        return "Behavior " + str(self.name) + \
               "\n- Authorizations : " + str(" ".join(at)) + \
               "\n- Actions : " + str(" ".join(ac)) + \
               "\n- Triggers : " + str(" ".join(tr)) + "\n"

    def to_json(self):
        return {"name": self.name, "actions": [str(x.to_trace()) for x in self.actions],
                "author": [str(x.to_trace()) for x in self.author],
                "triggers": [str(x.to_ltl()) for x in self.triggers]}


# AActor
class AActor(ThreadingActor):
    def __init__(self, name, proxy=None, behavior=None):
        """
        Init
        :param name: Actor name
        :param proxy: The network proxy
        :param behavior: Actor's behavior
        :return:
        """
        super(AActor, self).__init__()
        self.name = name
        self.proxy = proxy
        self.behavior = behavior

    def on_start(self):
        super(AActor, self).on_start()
        # print("[" + str(self.name) + "]" + " my behavior : " + str(self.behavior))

    def on_stop(self):
        super(AActor, self).on_stop()

    def on_failure(self, exception_type, exception_value, traceback):
        super(AActor, self).on_failure()

    def on_receive(self, msg):
        super(AActor, self).on_receive(msg)
        print("[" + str(self.name) + "]" + " MSG received : " + str(msg))

    def load_behavior(self):
        pass


# Monitor
class Monitor:
    """
    Internal monitor
    """
    def __init__(self, rootmon=None, formula="", trace=None, kv=None):
        self.trace = [] if trace is None else trace
        self.formula = formula
        self.rootmon = rootmon
        self.KV = {} if kv is None else kv

    def monitor(self):
        # Handling trace
        tmp = []
        for e in self.trace:
            tmp.append("{" + ", ".join(e) + "}" if isinstance(e, list) else "{" + str(e) + "}")
        trace = ", ".join(tmp)

        # Replace kv in formula
        formula = self.formula
        for k in self.KV:
            formula.replace(k, self.KV[k])

        # p = Popen(['echo', trace, '|', 'java -jar tools/ltlfo2mon.jar -p', formula],
        #           stdout=PIPE, stderr=PIPE, stdin=PIPE)
        # res = p.stdout.read().decode("utf-8")
        print("\t-Trace : " + trace)
        print("\t-Formula : " + formula)
        res = os.system('echo "' + trace + '" | java -jar tools/ltlfo2mon.jar -p "' + formula + '"')
        # print(res)


# RefMonitor
class RefMonitor(AActor):

    def __init__(self, name, actor: ThreadingActor=None, proxy=None, behavior=None, formula="", trace=[], kv={}):
        """
        Reference monitor
        :param name:
        :param actor:
        :param proxy:
        :param behavior:
        :param formula:
        :param trace:
        :param kv:
        :return:
        """
        super(RefMonitor, self).__init__(name, proxy=proxy, behavior=behavior)
        self.actor = actor
        self.trace = trace
        self.KV = kv
        self.formula = formula
        self.sub_mons = {}
        self.main_mon = Monitor(rootmon=self, formula=formula, trace=trace, kv=kv)

    def on_receive(self, msg):
        # super(RefMonitor, self).on_receive(message)
        print(Color("{autoblue}[" + str(self.name) + "]" + " MSG received : " + str(msg) + "{/autoblue}"))

        proto = msg.get("protocol")
        if proto == MsgProtocol.CALL_CHECK:
            # Handling msg via policy
            # Reply to proxy
            if self.behavior.is_permitted(msg):
                msg["protocol"] = MsgProtocol.CALL_OK
                self.proxy.tell(msg)
            else:
                print(Color("[" + str(self.name) + "]" + "{autored} My agent tries an unauthorized call{/autored} " + str(msg)))

        elif proto == MsgProtocol.CALL:
            # Handling msg via policy
            # Forward to agent
            if self.behavior.is_permitted(msg):
                self.actor.tell(msg)

                # Check if it is from/to agent

        elif proto == MsgProtocol.PRINT_TRACE:
            print("[" + self.name + "]" + str(self.trace))

        elif proto == MsgProtocol.PRINT_FORMULA:
            print("[" + self.name + "]" + str(self.trace))

    def init_submonitors(self):
        pass

    def monitor(self):
        self.main_mon.monitor()




# LoggerRefMonitor
class LoggerRefMonitor(RefMonitor):
    def __init__(self, name, actor: ThreadingActor=None, proxy=None, behavior=None, formula="", trace=[], kv={}):
        super(LoggerRefMonitor, self).__init__(name, proxy=proxy, behavior=behavior, formula=formula, trace=trace, kv=kv)
        self.actor = actor

    def on_receive(self, msg):
        # super(RefMonitor, self).on_receive(message)
        print(Color("{autoblue}[" + str(self.name) + "]" + " MSG received : " + str(msg) + "{/autoblue}"))
        msg["protocol"] = MsgProtocol.LOG
        self.trace.append("data('" + msg["msg"].args + "')")
        self.trace.append(msg["msg"].to_trace())
        # self.proxy.tell(msg)
        self.monitor()


# MyActor
class MyActor(AActor):
    def __init__(self, name, proxy=None, behavior=None):
        super(MyActor, self).__init__(name, proxy=proxy, behavior=behavior)

    def on_receive(self, msg):
        print("[" + str(self.name) + "]" + " MSG received : " + str(msg))
        protocol = msg.get("protocol")

        if protocol == MsgProtocol.INTERNAL:
            if self.behavior.is_permitted(msg.get("msg")):
                msg["protocol"] = MsgProtocol.CALL
                self.proxy.ask(msg)
            else:
                print(Color("{autored}Unauthorized call{/autored} " + str(msg) + " " + str(self.behavior)))

        elif protocol == MsgProtocol.CALL:
            print("[" + str(self.name) + "]" + " Running action")

    def name(self):
        return self.name


# MyActor
class MyActor2(AActor):
    def __init__(self, name, proxy=None, behavior=None):
        super(MyActor2, self).__init__(name, proxy=proxy, behavior=behavior)

    def on_receive(self, msg):
        print("[" + str(self.name) + "]" + " MSG received : " + str(msg))
        protocol = msg.get("protocol")

        if protocol == MsgProtocol.INTERNAL:
            msg["protocol"] = MsgProtocol.CALL
            self.proxy.ask(msg)

        elif protocol == MsgProtocol.CALL:
            print("[" + str(self.name) + "]" + " Running action")

    def name(self):
        return self.name


# Proxy
class Proxy(AActor):
    def __init__(self, name, behavior=None, debug=False):
        super(Proxy, self).__init__(name, behavior=behavior)
        self.DEBUG = debug

    def on_receive(self, msg):
        if self.DEBUG:
            print("[PROXY]" + " MSG received : " + str(msg))

        protocol = msg.get("protocol")
        receiver = msg.get("receiver")
        sender = msg.get("sender")
        receivers = []

        if protocol == MsgProtocol.CALL:
            # If the msg comes from an agent, forward it to his Reference monitor
            # Get only reference monitors
            receivers = [x for x in ActorRegistry.get_by_class_name("LoggerRefMonitor")
                         if x.proxy().name.get() == "RM_" + sender]
            msg["protocol"] = MsgProtocol.CALL_CHECK

        elif protocol == MsgProtocol.CALL_OK:
            # If the msg comes from a RM, forward it to the destination RM
            # Get only reference monitors
            receivers = [x for x in ActorRegistry.get_by_class_name("RefMonitor") if
                         x.proxy().name.get() == "RM_" + receiver]
            msg["protocol"] = MsgProtocol.CALL

        elif protocol == MsgProtocol.INTERNAL:
            # If the msg is an internal actor action, forward it to the destination
            receivers = [x for x in ActorRegistry.get_all() if x.proxy().name.get() == receiver]

        # Sending the message
        for receiver in receivers:
            receiver.tell(msg)

            #  and add signature
