__author__ = 'walid'
import os
from tulip.transys import *
from tulip.interfaces.ltl2ba import *
from tulip.spec import LTL
from tulip.transys.automata import *
from tulip.transys.export.graph2dot import *


prefix = (str(os.path.realpath(__file__)).split("pyAAL")[0] + "pyAAL/tools/linux/")
f = LTL("! spawn U init")
# print(f)

out = call_ltl3ba("! spawn U init", prefix=prefix)
out = out.decode("utf-8")
# print(out)
b = ltl3baHOAtoBuchi(out)
print(b)
b.save("toto", "svg")
