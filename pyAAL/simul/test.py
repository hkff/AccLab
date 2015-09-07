__author__ = 'walid'
import os
from tulip.transys import *
from tulip.interfaces.ltl2ba import *
from tulip.spec import LTL
from tulip.transys.automata import *

prefix = (str(os.path.realpath(__file__)).split("pyAAL")[0] + "pyAAL/tools/linux/")
f = LTL("! spawn U init")
# print(f)

out = call_ltl3ba("! spawn U init && b", prefix=prefix)
out = out.decode("utf-8")
print(out)


transitions = out.split('\n')
transitions = transitions[1:]


states = []
init = []
accept = []

def handle_state(state):
    res = {"name": "", "init": False, "accept": False}
    state = state.strip()

    if state is '':
        return None

    if state.endswith("_init"):
        res["init"] = True
        state = state.replace("_init", "")
    elif state.startswith("accept_"):
        res["accept"] = True
        state = state.replace("accept_", "")

    res["name"] = state
    return res


for s in transitions:
    tstates = s.split(',')

    if len(tstates) > 2:
        s1 = handle_state(tstates[0])
        print(s1)
        if s1 is not None:
            states.append(s1["name"])
            if s1["init"]: init.append(s1["name"])
            if s1["accept"]: accept.append(s1["name"])

        s2 = handle_state(tstates[1])
        if s1 is not None:
            states.append(s2["name"])
            if s2["init"]: init.append(s2["name"])
            if s2["accept"]: accept.append(s2["name"])


states = list(set(states))
init = list(set(init))
accept = list(set(accept))
# state, state, (1)?, 1 (if accept);

print(states)
print(accept)
print(init)

exit()
b = BuchiAutomaton(atomic_proposition_based=True)
b.states.add("t0")
b.states.add("t1")
b.states.initial.add("t0")
b.states.accepting.add("t1")
b.atomic_propositions |= {'spawn', 'l'}
b.transitions.add("t0", "t1", letter={'l'})
b.transitions.add("t0", "t1")
print(b.dot_str())
