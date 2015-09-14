"""
AALtoFOTL AAL translation to FOTL
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


# Time array to set
def time_to_set(times):
    res = []
    lng = len(times)
    y = 0
    for x in range(0, lng):
        for y in range(x+1, lng):
            if str(times[x].time) == str(times[y].time):
                break
        if y+1 == lng:
            res.append(times[x])
    return res


# Build environment
def build_env(prog: m_aalprog=None):
    """
    Build the environment
    :param prog: AAL program
    :return: the environment
    """
    pre_cond = "\n%%%%%%%%% START EVN %%%%%%%%%%%\n"
    pre_cond += "always(\n"
    pre_cond += "\n%%% Types knowledge\n"

    for x in prog.get_declared(m_type):
        pre_cond += str(x.to_ltl()) + " & \n"

    pre_cond += "\n\n%%% Action authorizations \n"
    for x in prog.get_declared(m_service):
        pre_cond += str(x.to_ltl()) + " & \n"

    pre_cond += "\n\n%%% Actors knowledge \n"
    for x in prog.get_declared(m_agent):
        pre_cond += str(x.to_ltl()) + " & \n"

    pre_cond += "\n\n%%% Time knowledge \n"
    times = []
    index = 0
    tmp = time_to_set(prog.walk(filter_type=m_time))
    for x in tmp:
        index = 0
        if len(times) == 0:
            times.append(x)
        else:
            for y in times:
                if y.compare(x) == 1:
                    times.insert(index, x)
                    break
                index += 1
            if index == len(times):
                times.append(x)

    times = times[::-1]
    # print([str(x.time) + " " for x in times])
    for i in range(0, len(times)):
        for j in range(i+1, len(times)):
            pre_cond += "(" + str(times[i].to_ltl()) + " => " + str(times[j].to_ltl()) + ") &"

    data_decs = "\n\n%%% Data knowledge \n"
    data_decs += "".join(["?[d](subject(d, " + str(x.name) + ")) &\n" for x in prog.get_declared(m_agent)])
    # data_decs = ""
    pre_cond += data_decs + "\nCTE ) &"
    #pre_cond = pre_cond[:-2] + "& true )\n" if pre_cond[-2].startswith("&") else pre_cond + ")\n"

    pre_cond += "\n%%%%%%%%% END EVN %%%%%%%%%%%\n\n"
    return pre_cond


# AALtoFOTL
def AALtoFOTL(mm: aalmm=None):
    """
    Generate the FOTL formula of the given aal prgram
    :param mm: AAL meta model / or AAL prog
    :return: FOTL formula
    """
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
    print(mm)
    if isinstance(mm, m_aalprog):
        return build_env(mm) + "\n" + mm.to_ltl()
    else:
        return build_env(mm.aalprog) + "\n" + mm.aalprog.to_ltl()
