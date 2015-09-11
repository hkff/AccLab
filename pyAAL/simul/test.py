from tulip.transys.export import save_d3

__author__ = 'walid'
import os
from tulip.transys import *
from tulip.interfaces.ltl2ba import *
from tulip.spec import LTL
from tulip.transys.automata import *
from tulip.transys.export.graph2dot import *


# f = LTL("! spawn U init && b => c")
# out = call_ltl3ba(f, args=['-M1'])
# print(out)
# b = ltl3baHOAtoBuchi(out)
# print(b)
# b.save("toto", "svg")


# save_d3.labeled_digraph2d3(b, "test.html")
nfa = NFA()
dfa = nfa2dfa(nfa)
print(dfa)