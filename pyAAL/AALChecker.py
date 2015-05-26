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
# TODO check p valid and u valid

from AALMetaModel import *
from pprint import pprint
from tools.color import *
from AALtoFOTL import *

# TODO optimize pre_cond...  to remove
# -------------------------------------------------------------
pre_cond = "(oneMonth => twoMonths) & " + "(oneMonth => threeMonths) & " + "(oneMonth => fourMonths) & " +\
            "(oneMonth => fiveMonths) & " + "(oneMonth => sixMonths) & " + "(oneMonth => sevenMonths) & " +\
            "(oneMonth => eightMonths) & " + "(oneMonth => nineMonths) & " + "(oneMonth => tenMonths) & " +\
            "(oneMonth => elevenMonths) & " + "(oneMonth => twelveMonths)\n"
pre_cond += "(twoMonths => threeMonths) & " + "(twoMonths => fourMonths) & " + "(twoMonths => fiveMonths) & " +\
            "(twoMonths => sixMonths) & " + "(twoMonths => sevenMonths) & " + "(twoMonths => eightMonths) & " +\
            "(twoMonths => nineMonths) & " + "(twoMonths => tenMonths) & " + "(twoMonths => elevenMonths) & " +\
            "(twoMonths => twelveMonths)\n"
pre_cond += "(threeMonths => fourMonths) & " + "(threeMonths => fiveMonths) & " + "(threeMonths => sixMonths) & " +\
            "(threeMonths => sevenMonths) & " + "(threeMonths => eightMonths) & " + "(threeMonths => nineMonths) & " +\
            "(threeMonths => tenMonths) & " + "(threeMonths => elevenMonths) & " + "(threeMonths => twelveMonths)\n"
pre_cond += "(fourMonths => fiveMonths) & " + "(fourMonths => sixMonths) & " + "(fourMonths => sevenMonths) & " +\
            "(fourMonths => eightMonths) & " + "(fourMonths => nineMonths) & " + "(fourMonths => tenMonths) & " +\
            "(fourMonths => elevenMonths) & " + "(fourMonths => twelveMonths)\n"
pre_cond += "(fiveMonths => sixMonths) & " + "(fiveMonths => sevenMonths) & " + "(fiveMonths => eightMonths) & " +\
            "(fiveMonths => nineMonths) & " + "(fiveMonths => tenMonths) & " + "(fiveMonths => elevenMonths) & " +\
            "(fiveMonths => twelveMonths)\n"
pre_cond += "(sixMonths => sevenMonths) & " + "(sixMonths => eightMonths) & " + "(sixMonths => nineMonths) & " +\
            "(sixMonths => tenMonths) & " + "(sixMonths => elevenMonths) & " + "(sixMonths => twelveMonths)\n"
pre_cond += "(sevenMonths => eightMonths) & " + "(sevenMonths => nineMonths) & " + "(sevenMonths => tenMonths) & " +\
            "(sevenMonths => elevenMonths) & " + "(sevenMonths => twelveMonths)\n"
pre_cond += "(eightMonths => nineMonths) & " + "(eightMonths => tenMonths) & " + "(eightMonths => elevenMonths) & " +\
            "(eightMonths => twelveMonths)\n"
pre_cond += "(nineMonths => tenMonths) & " + "(nineMonths => elevenMonths) & " + "(nineMonths => twelveMonths)\n"
pre_cond += "(tenMonths => elevenMonths) & " + "(tenMonths => twelveMonths)\n"
pre_cond += "(elevenMonths => twelveMonths)\n"

pre_condYears = pre_cond.replace("Month", "Year")
pre_condDays = pre_cond.replace("Month", "Day")

pre_cond += pre_condYears + pre_condDays

pre_cond += "always( ![a,x,y,z] ~(PERMIT(a, x, y, z) & DENY(a, x, y, z))) &  "  # Translation not valid

# -------------------------------------------------------------
pre_cond = ""


# Check AAL global
def check_aal(mm=None, verbose=False):
    """
    Check an AAL program
    :param mm: AAL metamodel instance
    :param verbose: verbose print
    :return:
    """
    # TODO : make it user friendly
    # TODO : add some stats
    res = ""
    res += "------------------------- Checking Monodic test -------------------------"
    if verbose:
        agentsCount = len(mm.aalprog.declarations["agents"])
        servicesCount = len(mm.aalprog.declarations["services"])
        dataCount = len(mm.aalprog.declarations["data"])
        typesCount = len(mm.aalprog.declarations["types"])

        res += "\n\n** DECLARATIONS"
        res += "\n[DECLARED AGENTS] : " + str(agentsCount) + ""
        res += "\n[DECLARED SERVICES] : " + str(servicesCount) + ""
        res += "\n[DECLARED DATA] : " + str(dataCount) + ""
        res += "\n[DECLARED TYPES] : " + str(typesCount) + ""

        res += "\n\n*** Forwards references check..."
        res += "\n[AGENTS] : " + str(len(mm.refForwardAgents))
        res += "\n[SERVICES] : " + str(len(mm.refForwardServices))
        res += "\n[DATA] : " + str(len(mm.refForwardData))
        res += "\n[TYPES] : " + str(len(mm.refForwardTypes))

        res += "\n\n** CLAUSES"
        res += "\n[CLAUSES] : " + str(len(mm.aalprog.clauses))
        res += "\nMonodic test :"
    p = check_monodic(mm.aalprog)
    res += "\n" + p["print"]
    res += "-------------------------- Checking Monodic End -------------------------"
    return res


# Check if aal node expression is monodic
def check_monodic(node=None, verbose: bool=False):
    """
    Check if the node is monodic fragment. A monodic fragment is an FOTL formula that contains at least one
    free variable inside a temporal modality
    :param node: an AAL metaModel node
    :param verbose: verbose output
    :return:
    """
    p = {"monodic": True, "info": []}
    # Check node type
    if isinstance(node, aalmm):
        p = check_monodic_exp(node.aalprog)
    elif isinstance(node, m_aalprog):
        for c in node.clauses:
            t = check_monodic_exp(c)
            p["monodic"] = p["monodic"] and t["monodic"]
            p["info"].extend(t["info"])
    elif isinstance(node, m_clause):
        p = check_monodic_exp(node)

    if p["monodic"]:
        res = Color("{autogreen}Formula is monodic !{/green}\n")
    else:
        res = Color("{autored}Formula is not monodic !{/red}\n")

    if not p["monodic"]:
        for info in p["info"]:
            res += " - found " + str(len(info["vars"])) + " free variables in [" + str(info["exp"]) + "]\n"
            tmp = [str(x.label) + " -> " + str(x.target) + " at line " +
                   str(x.target.name.parentCtx.getPayload().start.line) + "\n   " for x in info["vars"]]
            res += "   " + "".join(tmp)

    # Print the result
    if verbose:
        print(res)

    p["print"] = res
    return p


# TODO: check forwards refs before ! this can make monodic test wrong ??
# checkMonadic Exp
def check_monodic_exp(aexp: m_aexp):
    """
    Check if an action expression is monodic
    :param aexp: the action expression
    :return: {"monodic": boolean , "info": detailled result}
    """
    res = True
    info = []

    # Find modalities
    if isinstance(aexp, m_aexpModal):  # Do the check
        free_vars = get_free_vars(aexp)
        res = res and len(free_vars) <= 1
        # TODO: conditions info
        if not res:
            info.append({"exp": aexp, "vars": free_vars})

    # Handle in children
    if isinstance(aexp, aalmmnode) or isinstance(aexp, sEnum):
        for child in aexp.children():
            children = check_monodic_exp(child)
            res = res and children["monodic"]
            info.extend(children["info"])

    return {"monodic": res, "info": info}


# getFreeVar
def get_free_vars(aexp: m_aexp):
    return get_vars(aexp, vtype="free")


# get_linked_var
def get_linked_vars(aexp: m_aexp):
    return get_vars(aexp, vtype="linked")


# Get_vars TODO: handle shadowed vars
def get_vars(aexp: m_aexp, vtype=None):
    """
    Get all variables of type vtype in the action expression aexp
    :param aexp: the action expression to explore
    :param vtype: free | linked
    :return: array of vars
    """
    res = []
    refs = aexp.get_refs()  # Get all used refs in the aexp
    qrefs = [r for r in refs if isinstance(r.target, m_qvar) is True]  # Filter refs to get just quantified vars
    # Handle shadowed
    for x in qrefs:
        for y in qrefs:
            if str(x.name) == str(y.name) and (x is not y):
                qrefs.remove(y)

    quant = aexp.walk(filter_type=m_qvar)  # Get all quantification inside the aexp


    # if DEBUG:
    #     print(aexp)
    #     print("---- refs : -----")
    #     for x in refs:
    #         print(str(x) + "  " + str(x.target.__class__))
    #     print("------")
    #     print("---- Qrefs : -----")
    #     for x in qrefs:
    #         print(x)
    #     print("------")
    #     print("----- Quants : -----")
    #     for x in quant:
    #         print(x)
    #     print("------")

    if vtype == "free":  # Get free vars
        # For all quantified vars check if the quantification is not declared inside
        for q in qrefs:
            if not (q.target in quant):
                res.append(q)
        return res

    elif vtype == "linked":  # Get linked vars
        # For all qantified vars check if the quantification is declared inside
        for q in qrefs:
            if q.target in quant:
                res.append(q)
        return res


# Check validity between two clauses
def validate(compiler, c1, c2, resolve: bool=False, verbose: bool=False):
    """
    Perform validity test between two aal clauses
    :param compiler: the compiler instance
    :param c1: clause 1
    :param c2: clause 2
    :param resolve: try to detect conflicts if exists
    :param verbose: verbose print
    :return:
    """
    # TODO  check if c1 and c2 exists

    # Monodic test
    print("------------------------- Monodic check -------------------------")
    mc1 = check_monodic(c1)
    mc2 = check_monodic(c2)
    if not mc1["monodic"]:
        print(mc1["print"])
        print(Color("{autored}Please correct your clause. Exiting... {/red}"))
        return
    if not mc2["monodic"]:
        print(mc2["print"])
        print(Color("{autored}Please correct your clause. Exiting... {/red}"))
        return
    print(Color("{autogreen}Monodic check passed ! {/green}"))

    v = False
    print("------------------------- Starting Validity check -------------------------")
    c1_id = str(c1.name)
    c2_id = str(c2.name)
    print("c1 : " + c1_id + "\nc2 : " + c2_id)
    pre_cond = build_env(compiler.aalprog)

    print("----- Checking c1 & c2 consistency :")
    res = compiler.apply_check(code=pre_cond + "clause(" + c1_id + ").ue & clause(" + c2_id + ").ue",
                               show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        print(Color("{autored}  -> " + res["res"] + " : c1 & c2 are not consistent{/red}"))

        solve_auth(compiler, p=c2, u=c1, resolve=resolve)
        # return
    else:
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))

    if res["res"] == "":
        print(res["print"])

    print("----- Checking c1 => c2 :")
    res = compiler.apply_check(code="always(" + pre_cond + "clause(" + c1_id + ").ue => clause(" + c2_id + ").ue)",
                               show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        v = False
        print(Color("{autored}  -> " + res["res"] + "{/red}"))
    else:
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))

    if res["res"] == "":
        print(res["print"])

    print("----- Checking ~(c1 => c2) :")
    res = compiler.apply_check(code="~(always(" + pre_cond + "clause(" + c1_id + ").ue => clause(" + c2_id + ").ue))",
                               show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))
    else:
        print(Color("{autored}  -> " + res["res"] + "{/red}"))

    if res["res"] == "":
        print(res["print"])

    if res["res"] == "Unsatisfiable":
        v = True
    else:
        solve_triggers(compiler, p=c2, u=c1, resolve=resolve)

    if v:
        print(Color("\n{autogreen}[VALIDITY] Formula is valid !{/green}"))
    else:
        print(Color("\n{autored}[VALIDITY] Formula is not valid !{/red}"))

    print("------------------------- Validity check End -------------------------\n")
    return ""


# Check validity / satisfiability
def validate2(compiler, c1, check: bool=False, verbose: bool=False):
    """
    Perform validity/satisfiability test of an FOTL formula
    :param compiler: the compiler instance
    :param c1: formula
    :param check: True -> performs a sat test; False -> performs a validity test
    :param verbose: verbose print
    :return:
    """
    # Monodic test
    print("------------------------- Monodic check -------------------------")
    mc1 = check_monodic(c1)
    if not mc1["monodic"]:
        print(mc1["print"])
        print(Color("{autored}Please correct your clause. Exiting... {/red}"))
        return

    print(Color("{autogreen}Monodic check passed ! {/green}"))

    v = False

    print("------------------------- Starting " + ("Validity" if not check else "") + " check -------------------------")
    print("----- Checking c1 :")
    res = compiler.apply_check(code=c1, show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        v = False
        print(Color("{autored}  -> " + res["res"] + "{/red}"))
    else:
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))

    if res["res"] == "":
        print(res["print"])

    if not check:
        print("----- Checking ~(c1) :")
        res = compiler.apply_check(code="~(" + c1 + ")", show=False, verbose=verbose)
        if res["res"] == "Unsatisfiable":
            print(Color("{autogreen}  -> " + res["res"] + "{/green}"))
        else:
            print(Color("{autored}  -> " + res["res"] + "{/red}"))

        if res["res"] == "":
            print(res["print"])

        if res["res"] == "Unsatisfiable":
            v = True

        if v:
            print(Color("\n{autogreen}[VALIDITY] Formula is valid !{/green}"))
        else:
            print(Color("\n{autored}[VALIDITY] Formula is not valid !{/red}"))

    print("------------------------- " + ("Validity" if not check else "") + " check End -------------------------\n")
    return ""


# Check authorisations
def solve_auth(compiler, p=None, u=None, verbose=False, resolve=False):
    """
    Conflict detection
    :param compiler: the compiler instance
    :param p: clause 1
    :param u: clause 2
    :param verbose: verbose print
    :param resolve:
    :return:
    """
    print(Color("{autoblue}:: Solving authorization{/blue}"))
    u_id = str(u.name)
    p_id = str(p.name)

    quants = p.usage.walk(filter_type=m_qvar)
    quant = ""
    for x in quants:
        quant += str(x.to_ltl())

    authors = p.usage.walk(filter_type=m_aexpAuthor)
    for x in authors:
        res = compiler.apply_check(code=pre_cond + str(quant) + " " + str(x.to_ltl()) + " & clause(" + u_id + ").uc",
                                   show=False)
        if verbose:
            print("  " + str(x) + " & c1" + " : " + res["res"])

        if res["res"] == "Unsatisfiable":
            print(Color("  Authorization <<" + str(x) + ">> found {automagenta}at line " +
                        str(x.name.parentCtx.getPayload().start.line) + "{/magenta} does not match with user preference"))
            if resolve:
                print(Color("{autogreen}    |-> Resolving conflict {/green}"))
                if x.author == m_author.A_permit:
                    x.author = m_author.A_deny
                else:
                    x.author = m_author.A_permit


# Check triggers
def solve_triggers(compiler, p=None, u=None, verbose=False, resolve=False):
    """

    :param compiler:
    :param p:
    :param u:
    :param verbose:
    :param resolve:
    :return:
    """
    # FIXME this is adhoc
    print(Color("{autoblue}:: Solving trigger{/blue}"))
    # pre_cond = "always( ![a,x,y,z] ~(PERMIT(a, x, y, z) & DENY(a, x, y, z))) &  "
    u_id = str(u.name)
    p_id = str(p.name)

    ifthens = u.usage.walk(filter_type=m_aexpIfthen)
    for x in ifthens:
        res = compiler.apply_check(code=pre_cond + "~(clause(" + p_id + ").uc => " + x.to_ltl() + ")", show=False,
                                   verbose=verbose)
        if verbose:
            print("  " + str(x) + " & c1" + " : " + res["res"])

        if res["res"] == "Satisfiable":
            print(Color("  Implication <<" + str(x) + ">> found {automagenta}at line " +
                        str(x.name.parentCtx.getPayload().start.line) + "{/magenta} is not guaranteed by provider"))
            if resolve:
                print(Color("{autogreen}    |-> Resolving conflict {/green}"))
        # x.parent.remove(x) # TODO remove me from parent