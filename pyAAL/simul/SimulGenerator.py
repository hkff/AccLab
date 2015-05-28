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

from AALMetaModel import *
from simul.Simul import *


# m_behavior to behavior
def m_behavior_to_behavior(b: m_behavior, name=""):
    res = Behavior(name=name)

    # Getting all authorizations
    m_authors = b.walk(filter_type=m_aexpAuthor)
    for at in m_authors:
        if type(at.parent) is not m_aexpIfthen:
            x = at.action
            ac = Action(service=str(x.service), agent1=str(x.agent1), agent2=str(x.agent2), args=str(x.args),
                        time=x.time, purpose=x.purpose)
            res.author.append(Author(author=at.author, action=ac))

    # Getting all actions
    m_actions = b.walk(filter_type=m_aexpAction)
    for ae in m_actions:
        if type(ae.parent) is not m_aexpIfthen:
            x = ae.action
            res.actions.append(Action(service=str(x.service), agent1=str(x.agent1), agent2=str(x.agent2),
                                      args=str(x.args), time=x.time, purpose=x.purpose))

    # Getting all triggers
    m_ifthen = b.walk(filter_type=m_aexpIfthen)
    for x in m_ifthen:
        res.triggers.append(x)

    return res


# Generate Simulation
def generate_simulation(aalprog: m_aalprog):
    # Create new simulation
    sim = Simulation()

    actors = []
    agents = []
    behaviors = {}

    # Getting all behaviors
    for b in aalprog.behaviors:
        behaviors[str(b.name)] = m_behavior_to_behavior(b, name=str(b.name))

    # Getting all agents
    for x in aalprog.declarations["agents"]:
        agents.append(str(x.name))

    # Creating all actors with their Reference monitors
    for x in agents:
        actors.append(MyActor.start(x, proxy=sim.watcher, behavior=behaviors.get(x)))
        actors.append(RefMonitor.start("RM_" + x, actor=actors[-1], proxy=sim.watcher, behavior=Behavior()))

    sim.eval_action("bob.read[alice](d)")

    sim.run_shell()
    sim.stop()
