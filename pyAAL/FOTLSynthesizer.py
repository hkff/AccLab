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
__author__ = 'walid'

from grammar.tspass.TSPASSListener import *
# TODO: in test


# Action
class Action():
    """

    """
    def __init__(self, action=None, sender=None, receiver=None, data=None):
        self.action = action
        self._action = action
        self.sender = sender
        self.receiver = receiver
        self.data = data

    def __str__(self):
        return (str(self.action) + (("(" + str(self.sender)) if self.sender is not None else "")
                + (("," + str(self.receiver)) if self.receiver is not None else "")
                + (("," + str(self.data)) if self.data is not None else "")
                + (")" if self.sender is not None else ""))

    def to_out(self):
        self.action = self._action + "O"
        return self

    def to_in(self):
        self.action = self._action + "I"
        return self

    def clear(self):
        self.action = self._action
        return self



class FOTLCompilerListener(TSPASSListener):

    def __init__(self):
        self.specs = {}
        self.comms = {}

    # Exit atom
    def exitAtom(self, ctx):
        action = str(ctx.predicate().ID()) if ctx.predicate() is not None else None
        # Check the number of vars
        vars = ctx.variable()
        sender = str(ctx.variable()[0].ID()) if len(vars) >= 1 else None
        receiver = str(ctx.variable()[1].ID()) if len(vars) >= 2 else None
        data = str(ctx.variable()[2].ID()) if len(vars) >= 3 else None

        # print("Action : " + str(action) + " -Sender : " + str(sender) +
        #        " -Receiver : " + str(receiver) + " -Data : " + str(data))
        ac = Action(action=action, sender=sender, receiver=receiver, data=data)
        print(str(ac))
        print(str(ac.to_in()))
        print(str(ac.to_out()))
        ###################
        # Generate Spec i
        ###################
        speci = str(ac.to_out())
        if self.specs.get(sender) is None:
            self.specs[sender] = speci
        else:
            self.specs[sender] += " & " + speci


        ###################
        # Generate Spec j
        ###################
        specj = str(ac.to_in())
        if self.specs.get(receiver) is None:
            self.specs[receiver] = specj
        else:
            self.specs[receiver] += " & " + specj


        ######################
        # Generate Comms(i,j)
        ######################
        commsij = ""
        if self.comms.get(sender+","+receiver) is None:
            self.comms[sender+","+receiver] = commsij
        else:
            self.comms[sender+","+receiver] += " & " + commsij

        ######################
        # Generate Comms(i,j)
        ######################
        commsji = ""
        if self.comms.get(receiver+","+sender) is None:
            self.comms[receiver+","+sender] = commsji
        else:
            self.comms[receiver+","+sender] += " & " + commsji



    # Exit a parse tree produced by TSPASSParser#atom.
    def exitVariable(self, ctx):
        # print(str(ctx.ID()))
        pass

    # Exit formula
    def exitProgram(self, ctx):
        print(self.specs)
        print(self.comms)