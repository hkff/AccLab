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

from simul.Actors import *
import readline
import curses
# from shell import Completer
import sys
import re
from enum import Enum


# Simulation
class Simulation():

    def __init__(self):
        self.watcher = Proxy.start("Proxy")

    # Stopping simulation
    def stop(self):
        """

        :return:
        """
        # Stopping all actors
        # actors = self.watcher .proxy().get_all().get()
        actors = ActorRegistry.get_all()
        for x in actors:
            x.stop()
        # self.watcher.stop()

    # EvalAction
    def eval_action(self, ac: str or Action):
        """
        Evaluate AAL action
        :param ac:
        :return:
        """
        if isinstance(ac, str):
            ac = Action.action_builder(ac)

        ag1 = str(ac.agent1)
        ag2 = str(ac.agent2)

        # Get only reference monitors
        senders = [x for x in ActorRegistry.get_all() if x.proxy().name.get() == ag1]
        receivers = [x for x in ActorRegistry.get_all() if x.proxy().name.get() == ag2]

        for sender in senders:
            for receiver in receivers:
                sender.ask(Message(sender, receiver, ac, MsgProtocol.INTERNAL))

    # Run shell
    def run_shell(self):
        """

        :return:
        """
        # comp = Completer()
        # we want to treat '/' as part of a word, so override the delimiters
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab: complete")
        # readline.set_completer(comp.complete)
        stop = False

        while not stop:
            cmd = input("shell >")
            if cmd == "quit" or cmd == "q":
                stop = True
            else:
                try:
                    res = self.eval_action(cmd)
                    if res is not None:
                        print(res)
                except:
                    print("Eval error !",  sys.exc_info()[:2])


#####################
# Simulation start
#####################
# sim = Simulation()

# bob = MyActor.start("bob", proxy=sim.watcher)
# alice = MyActor.start("alice", proxy=sim.watcher)

# rm_bob = RefMonitor.start("RM_bob", actor=bob, proxy=sim.watcher, behavior=Behavior())
# rm_alice = RefMonitor.start("RM_alice", actor=alice, proxy=sim.watcher, behavior=Behavior())

# sim.eval_action("bob.read[alice](d)")
# sim.eval_action("alice.read(d)")
# sim.eval_action("bob.read(d)")
# sim.eval_action("bob.read[alice]()")
# sim.eval_action("bob.read()")

# sim.run_shell()
# sim.stop()

