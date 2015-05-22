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

from AALMetaModel import *

# Build environment
def build_env(prog: m_aalprog=None):
    pre_cond = "\n%%%%%%%%% START EVN %%%%%%%%%%%"
    pre_cond += "\n%%% Types knowledge\n"
    for x in prog.get_declared(m_type):
        pre_cond += str(x.to_ltl()) + " & "

    pre_cond += "\n\n%%% Action authorizations \n"
    for x in prog.get_declared(m_service):
        pre_cond += str(x.to_ltl()) + " & "

    # pre_cond += "\n\n%%% Actors knowledge \n"
    # for x in mm.get_declared(m_agent):
    #     pre_cond += str(x.to_ltl()) + " & "

    pre_cond += "\n%%%%%%%%% END EVN %%%%%%%%%%%\n"
    return pre_cond


# AALtoFOTL
def AALtoFOTL(mm: aalmm=None):
    """

    :param mm:
    :return:
    """
    # TODO: define Algo
    print("Entering TSPASS translation...")
    """
    INTER[clause] :
        INTER[ae] AND Always (INTER[ue] OR ((~ INTER[ue]) AND (Always audit => INTER[re])))

    INTER[actionExp] :
        action        -> time => serviceId(agentId1, agentId2, INTER[exp], purpose)
        not action    -> ~ INTER[action]
        modal         -> modal INTER[actionExp]
        condition     -> INTER[exp]
        booleanopExp  -> INTER[actionExp1] booleanOp INTER[actionExp2]
        Author        : PERMIT action -> P_INTER[action]
                        DENY action   -> ~ P_INTER[action]
        ifthen        -> INTER[actionExp1] => INTER[actionExp2]
        qvar          -> quant INTER[var]
    """

    return build_env(mm.aalprog) + "\n" + mm.aalprog.to_ltl()
