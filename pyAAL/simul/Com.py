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
from enum import Enum
import re
__author__ = 'walid'


# Action
class Action:
    def __init__(self, service=None, agent1=None, agent2=None, args=None, time=None, purpose=[]):
        super().__init__()
        self.service = service
        self.agent1 = agent1
        self.agent2 = agent2
        self.args = args
        self.time = time
        self.purpose = purpose

    def __str__(self):
        res = str(self.agent1) + "." + str(self.service) +\
            ("[" + str(self.agent2) + "]" if self.agent2 is not None else "") + \
            "(" + (str(self.args) if self.args is not None else "") + ") " +\
            (str(self.time) if self.time is not None else "")

        if len(self.purpose) > 0:
            res += " PURPOSE(" + str(self.purpose) + ")"

        return res

    def to_trace(self):
        return "%s('%s', '%s', '%s')" % (self.service, self.agent1, self.agent2, self.args)

    # Action builder
    @staticmethod
    def action_builder(msg):
        """
        Build action from string
        :param msg:
        :return:
        """
        t = re.search(r".*\.", msg)
        agent1 = "" if t is None else msg[t.start():t.end()-1]

        t = re.search(r"\[.*\]", msg)
        agent2 = agent1 if t is None else msg[t.start()+1:t.end()-1]

        t = re.search(r"\(.*\)", msg)
        args = "" if t is None else msg[t.start()+1:t.end()-1]

        t = re.search(r"\..*\(", msg) if agent2 == "" else re.search(r"\..*\[", msg)
        service = "" if t is None else msg[t.start()+1:t.end()-1]

        ac = Action()
        ac.agent1 = agent1
        ac.agent2 = agent2
        ac.service = service
        ac.args = args

        return ac

    def equal(self, ac):
        return (self.agent1 == ac.agent1) and (self.agent2 == ac.agent2) and \
               (self.service == ac.service) and (self.args == ac.args) and \
               (self.time == ac.time) and (self.purpose == ac.purpose)


# Author
class Author:
    def __init__(self, author=None, action=None):
        self.action = action
        self.author = author

    def __str__(self):
        return str(self.author) + " " + str(self.action)


# Msg Protocol
class MsgProtocol(Enum):
    INTERNAL = "INTERNAL"
    CALL = "CALL"
    CALL_CHECK = "CALL_CHECK"
    CALL_OK = "CALL_OK"
    LOG = "LOG"
    GET_TRACE = "GET_TRACE"
    PRINT_TRACE = "PRINT_TRACE"
    GET_FORMULA = "GET_FORMULA"
    PRINT_FORMULA = "PRINT_FORMULA"

    def __str__(self):
        return self.value


# Message
class Message(dict):
    def __init__(self, sender, receiver, msg, protocol):
        super(Message).__init__()
        self.protocol = ""
        self["protocol"] = protocol
        self["sender"] = sender.proxy().name.get()
        self["receiver"] = receiver.proxy().name.get()
        self["msg"] = msg

    def build(self, sender, receiver, msg, protocol):
        res = {}
        res["protocol"] = protocol
        res["sender"] = sender.proxy().name.get()
        res["receiver"] = receiver.proxy().name.get()
        res["msg"] = msg
        return res

    def __str__(self):
        return "%s %s->%s : [%s]" % (self["protocol"], self["sender"], self["receiver"], self["msg"])
