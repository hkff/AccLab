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


def ltl3baHOAtoBuchi(a):
    """
    Return the automata
    :param a:
    :return:
    """

    return a

# PATCHED by Walid Benghabrit on 04/09/2015
# Adding ltl3ba supports
def call_ltlba(formula, prefix='', v=3):
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
    @rtype: tulip.transys.BA
    """
    ltlba = 'ltl2ba' if v == 2 else 'ltl3ba'

    try:
        subprocess.call([ltlba, '-h'], stdout=subprocess.PIPE)
    except OSError:
        # print(Exception('cannot find ' + ltlba + ' on path'))
        pass
    p = subprocess.Popen(
        [prefix + ltlba, '-T3', '-f', '"{f}"'.format(f=formula)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    p.wait()
    ltl2ba_output = p.stdout.read()
    logger.info(ltlba +' output:\n\n{s}\n'.format(s=ltl2ba_output))
    if p.returncode != 0:
        raise Exception('Error when converting LTL to Buchi.')
    return ltl2ba_output


def call_ltl2ba(formula, prefix=''):
    return call_ltlba(formula, prefix=prefix, v=2)


def call_ltl3ba(formula, prefix=''):
    return call_ltlba(formula, prefix=prefix, v=3)


def parse_spot(self, ltl2ba_output):
    """Return a Buchi automaton from parsing C{ltl3ba_output}.

    @return: Buchi automaton as a 3-`tuple` containing:
      - `dict` mapping symbols to types (all `"boolean"`)
      - `networkx.MultiDiGraph`, each edge labeled with a
        `"guard"` that is a Boolean formula as `str`
      - `set` of initial nodes
      - `set` of accepting nodes
    """
    self.initial_nodes = set()
    self.accepting_nodes = set()
    self.symbols = dict()
    return (self.symbols, self.initial_nodes, self.accepting_nodes)
