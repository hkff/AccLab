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

# logging.basicConfig(level=logging.DEBUG)


# Behavior
class Behavior():
    def __init__(self, name=""):
        self.name = name
        self.actions = []
        self.author = []
        self.triggers = []

    def is_permited(self, action):
        # return True
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


# AActor
class AActor(ThreadingActor):
    def __init__(self, name, proxy=None, behavior=None):
        super(AActor, self).__init__()
        self.name = name
        self.proxy = proxy
        self.behavior = behavior

    def on_start(self):
        super(AActor, self).on_start()
        # print("[" + str(self.name) + "]" + " my behavior : " + str(self.behavior))
        # My optional setup code in same context as on_receive()

    def on_stop(self):
        super(AActor, self).on_stop()
        # My optional cleanup code in same context as on_receive()

    def on_failure(self, exception_type, exception_value, traceback):
        super(AActor, self).on_failure()
        # My optional cleanup code in same context as on_receive()

    def on_receive(self, msg):
        super(AActor, self).on_receive(msg)
        print("[" + str(self.name) + "]" + " MSG received : " + str(msg))
        # My optional message handling code for a plain actor

    def load_behavior(self):
        pass


# RefMonitor
class RefMonitor(AActor):
    def __init__(self, name, actor: ThreadingActor=None, proxy=None, behavior=None):
        super(RefMonitor, self).__init__(name, proxy=proxy, behavior=behavior)
        self.actor = actor

    def on_start(self):
        super(RefMonitor, self).on_start()

    def on_stop(self):
        super(RefMonitor, self).on_stop()

    def on_failure(self, exception_type, exception_value, traceback):
        super(RefMonitor, self).on_failure()

    def on_receive(self, msg):
        # super(RefMonitor, self).on_receive(message)
        print(Color("{autoblue}[" + str(self.name) + "]" + " MSG received : " + str(msg) + "{/autoblue}"))

        proto = msg.get("protocol")
        if proto == MsgProtocol.CALL_CHECK:
            # Handling msg via policy
            # Reply to proxy
            if self.behavior.is_permited(msg):
                msg["protocol"] = MsgProtocol.CALL_OK
                self.proxy.tell(msg)
            else:
                print(Color("[" + str(self.name) + "]" + "{autored} My agent tries an unauthorized call{/autored} " + str(msg)))

        elif proto == MsgProtocol.CALL:
            # Handling msg via policy
            # Forward to agent
            if self.behavior.is_permited(msg):
                self.actor.tell(msg)

                # Check if it is from/to agent


# MyActor
class MyActor(AActor):
    def __init__(self, name, proxy=None, behavior=None):
        super(MyActor, self).__init__(name, proxy=proxy, behavior=behavior)

    def on_start(self):
        super(MyActor, self).on_start()
        pass

    def on_stop(self):
        pass

    def on_failure(self, exception_type, exception_value, traceback):
        pass

    def on_receive(self, msg):
        print("[" + str(self.name) + "]" + " MSG received : " + str(msg))
        protocol = msg.get("protocol")

        if protocol == MsgProtocol.INTERNAL:
            if self.behavior.is_permited(msg.get("msg")):
                msg["protocol"] = MsgProtocol.CALL
                self.proxy.ask(msg)
            else:
                print(Color("{autored}Unauthorized call{/autored} " + str(msg) + " " + str(self.behavior)))

        elif protocol == MsgProtocol.CALL:
            print("[" + str(self.name) + "]" + " Running action")

    def name(self):
        return self.name


# Proxy
class Proxy(AActor):
    def __init__(self, name, behavior=None):
        super(Proxy, self).__init__(name, behavior=behavior)

    def on_receive(self, msg):
        print("[PROXY]" + " MSG received : " + str(msg))
        protocol = msg.get("protocol")
        receiver = msg.get("receiver")
        sender = msg.get("sender")
        receivers = []

        if protocol == MsgProtocol.CALL:
            # If the msg comes from an agent, forward it to his Reference monitor
            # Get only reference monitors
            receivers = [x for x in ActorRegistry.get_by_class_name("RefMonitor") if
                         x.proxy().name.get() == "RM_" + sender]
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

        for receiver in receivers:
            receiver.tell(msg)

            #  and add signature
