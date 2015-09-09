# Edited by Walid Benghabrit 07/09/2015
#
# Copyright (c) 2014 by California Institute of Technology
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the California Institute of Technology nor
#    the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior
#    written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL CALTECH
# OR THE CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
# USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
"""Interface to ltl2ba"""
import logging
logger = logging.getLogger(__name__)
import subprocess
from tulip.transys.automata import BuchiAutomaton
import os, sys

def handle_state(state):
    """
    Handle a state
    :param state:
    :return: Object {"name": "state_name", "init": Bool, "accept": Bool}
    """
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

    res["name"] = state.replace('\n', '')
    return res


def ltl3baHOAtoBuchi(out):
    """
    Return the automata
    Transition Format # state, state, (1)?, 1 (if accept);
    :param out:
    :return:
    """
    transitions = out.split('\n')
    transitions = transitions[1:]

    states = []
    init = []
    accept = []
    trans = []

    for s in transitions:
        tstates = s.split(',')
        if len(tstates) > 2:
            s1 = handle_state(tstates[0])
            if s1 is not None:
                states.append(s1["name"])
                if s1["init"]:
                    init.append(s1["name"])
                if s1["accept"]:
                    accept.append(s1["name"])

            s2 = handle_state(tstates[1])
            if s2 is not None:
                states.append(s2["name"])
                if s2["init"]:
                    init.append(s2["name"])
                if s2["accept"]:
                    accept.append(s2["name"])
            # Add transition
            trans.append({"from": s1["name"], "to": s2["name"], "label": str(tstates[-2])[3:-2]})

    states = list(set(states))
    init = list(set(init))
    accept = list(set(accept))

    # Creating Buchi Automaton
    b = BuchiAutomaton(atomic_proposition_based=True)
    # Adding states
    b.states.add_from(states)

    # Adding initial states
    b.states.initial.add_from(init)

    # Adding accepting states
    b.states.accepting.add_from(accept)

    # Adding transitions
    for t in trans:
        t["label"] = t["label"]
        b.atomic_propositions |= {t["label"]}
        b.transitions.add(t["from"], t["to"], letter=t["label"])

    return b


# PATCHED by Walid Benghabrit on 04/09/2015
# Adding ltl3ba supports
def call_ltlba(formula, v=3, args=[]):
    """Load a Buchi Automaton from a Never Claim.

    TODO
    ====
    Make sure guard semantics properly accounted for:
    'prop' | '!prop' | '1' and skip

    Depends
    =======
    ltl2ba: http://www.lsv.ens-cachan.fr/~gastin/ltl2ba/

    @param formula: LTL formula for input to ltl2ba
    @type formula: str

    @return: Buchi Automaton
    @rtype: byte
    """
    ltlba = 'ltl2ba' if v == 2 else 'ltl3ba'
    prefix = ""
    try:
        subprocess.call([ltlba, '-h'], stdout=subprocess.PIPE)
    except OSError:
        # Setting up the ltlxba path
        p = sys.platform
        if p.startswith("linux"):
            os_name = "linux"
        elif p.startswith("darwin"):
            os_name = "mac"
        else:
            print("OS not supported !")
            return
        prefix = str(os.path.realpath(__file__)).split("pyAAL")[0] + "pyAAL/tools/" + os_name + "/"

    p = subprocess.Popen(
        [prefix + ltlba, '-T3'] + args + ['-f', '"{f}"'.format(f=formula)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    p.wait()
    ltl2ba_output = p.stdout.read()
    logger.info(ltlba +' output:\n\n{s}\n'.format(s=ltl2ba_output))
    if p.returncode != 0:
        raise Exception('Error when converting LTL to Buchi.' + str(ltl2ba_output.decode("utf-8")))
    return ltl2ba_output


def call_ltl2ba(formula, args=[]):
    return call_ltlba(formula, v=2, args=args).decode("utf-8")


def call_ltl3ba(formula, args=[]):
    return call_ltlba(formula, v=3, args=args).decode("utf-8")

