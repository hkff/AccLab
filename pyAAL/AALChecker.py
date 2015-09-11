"""
AALChecker contains validation methods
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


# Check unused dec
def check_unused_dec(mm) -> str:
    """
    Check forwards references.
    :return:
    """
    res = ""
    # Disable check in lib context
    if not mm.loadlibs:
        return ""
    agents = mm.aalprog.get_declared(m_agent)
    services = mm.aalprog.get_declared(m_service)
    data = mm.aalprog.get_declared(m_data)
    types = mm.aalprog.get_declared(m_type)

    refs_agents = [x.target for x in mm.aalprog.walk(filter_type=m_ref, filters="self.target.is_a(m_agent) ")]
    refs_services = [x.target for x in mm.aalprog.walk(filter_type=m_ref, filters="self.target.is_a(m_service) ")]

    for a in agents:
        if not (a in refs_agents):
            res += ("{autoyellow}[WARNING]{/yellow} Unused agent declaration : " + str(a.name) +
                    "  ->  {automagenta}at line " + str(a.get_line()) + "{/magenta}\n")

    for a in services:
        if not (a in refs_services):
            res += ("{autoyellow}[WARNING]{/yellow} Unused service declaration : " + str(a.name) +
                    "  ->  {automagenta}at line " + str(a.get_line()) + "{/magenta}\n")

    return res

# Check AAL global
def check_aal(mm=None, verbose=False):
    """
    Check an AAL program
    :param mm: AAL compiler instance
    :param verbose: verbose print
    :return:
    """
    res = ""
    res += "------------------------- Start Checking -------------------------"
    if verbose:
        agentsCount = len(mm.aalprog.get_declared(m_agent))
        servicesCount = len(mm.aalprog.get_declared(m_service))
        dataCount = len(mm.aalprog.get_declared(m_data))
        typesCount = len(mm.aalprog.get_declared(m_type))

        res += "\n\n** DECLARATIONS"
        res += "\n[DECLARED AGENTS]   : " + str(agentsCount)
        res += "\n[DECLARED SERVICES] : " + str(servicesCount)
        res += "\n[DECLARED DATA]     : " + str(dataCount)
        res += "\n[DECLARED TYPES]    : " + str(typesCount)

        res += "\n\n*** Forwards references check"
        res += "\n[AGENTS]   : " + str(len(mm.refForwardAgents))
        res += "\n[SERVICES] : " + str(len(mm.refForwardServices))
        res += "\n[DATA]     : " + str(len(mm.refForwardData))
        res += "\n[TYPES]    : " + str(len(mm.refForwardTypes))
        res += "\n" + mm.checkForwardsRef()

        res += "\n\n*** Unused declarations"
        res += "\n\n" + check_unused_dec(mm)

        res += "\n\n** LOADED libraries"
        res += "\n[LIBS] : " + str(len(mm.aalprog.libs))

        res += "\n\n** CLAUSES"
        res += "\n[CLAUSES] : " + str(len(mm.aalprog.clauses))

        res += "\n\n*** Miscellaneous"
        res += "\n[PERMISSIONS]   : " + str(len(mm.aalprog.walk(filter_type=m_aexpAuthor,
                                                                filters="self.author == m_author.A_permit ")))
        res += "\n[PROHIBITIONS   : " + str(len(mm.aalprog.walk(filter_type=m_aexpAuthor,
                                                                filters="self.author == m_author.A_deny ")))

        res += "\n\n*** Monodic test :\n"

    for c in mm.aalprog.clauses:
        res += " |" + str(c.name) + (' ' * (15-len(str(c.name)))) + "->   " + check_monodic(c)["tmonodic"] + " \n"

    res += "-------------------------- Checking End -------------------------"
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
        res = Color("{autogreen}Formula is monodic !{/green}")
    else:
        res = Color("{autored}Formula is not monodic !{/red}")

    p["tmonodic"] = res

    if not p["monodic"]:
        res += "\n"
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
def check_monodic_exp(aexp):
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
    # print(aexp)
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
            if q.target not in quant:
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

    v = True
    print("------------------------- Starting Validity check -------------------------")
    c1_id = str(c1.name)
    c2_id = str(c2.name)
    print("c1 : " + c1_id + "\nc2 : " + c2_id)
    pre_cond = build_env(compiler.aalprog)

    print("----- Checking c1 & c2 consistency :")
    res = compiler.apply_check(code=pre_cond + "\n%%  " + c1_id + "\nclause(" + c1_id + ").ue " + "\n & \n\n%%  " +
                                    c2_id + "\nclause(" + c2_id + ").ue",
                               show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        print(Color("{autored}  -> " + res["res"] + " : c1 & c2 are not consistent{/red}"))
        v = v and False

        solve_auth(compiler, p=c1, u=c2, resolve=resolve)
        solve_triggers(compiler, p=c1, u=c2, resolve=resolve)
        return
    else:
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))

    if res["res"] == "":
        print(res["print"])

    print("----- Checking c1 => c2 :")
    res = compiler.apply_check(code="always(" + pre_cond + "\n%%  " + c1_id + "\nclause(" + c1_id
                                    + ")\n =>\n\n " + "%%  " + c2_id + "\nclause(" + c2_id + "))",
                               show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        v = v and False
        print(Color("{autored}  -> " + res["res"] + "{/red}"))
    else:
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))

    if res["res"] == "":
        print(res["print"])

    print("----- Checking ~(c1 => c2) :")
    res = compiler.apply_check(code="~(always(" + pre_cond + "\n%%  " + c1_id + "\nclause(" + c1_id
                                    + ")\n =>\n\n " + "%%  " + c2_id + "\nclause(" + c2_id + ")))",
                               show=False, verbose=verbose)
    if res["res"] == "Unsatisfiable":
        print(Color("{autogreen}  -> " + res["res"] + "{/green}"))
    else:
        print(Color("{autored}  -> " + res["res"] + "{/red}"))
        v = v and False

    if res["res"] == "":
        print(res["print"])

    if res["res"] == "Unsatisfiable":
        v = v and True
    else:
        solve_auth(compiler, p=c1, u=c2, resolve=resolve)
        solve_triggers(compiler, p=c1, u=c2, resolve=resolve)

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

    print(
        "------------------------- Starting " + ("Validity" if not check else "") + " check -------------------------")
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

    pre_cond = build_env(compiler.aalprog)
    authors = p.usage.walk(filter_type=m_aexpAuthor)

    for op in ["&", "=>"]:
        for x in authors:
            res = compiler.apply_check(code=pre_cond + str(quant) +
                                        "( " + str(x.to_ltl()) + " " + op + " clause(" + u_id + ").ue )" + (")"*len(quants)),
                                       show=False, verbose=False)

            if verbose:
                print("  " + str(x) + " " + op + " c1" + " : " + res["res"])
            #print("===== res : " + str(res))
            if res["res"] == "Unsatisfiable":
                print(Color("\n  Authorization <<" + str(x) + ">> found {automagenta}at line " +
                            str(x.name.parentCtx.getPayload().start.line) +
                            "{/magenta} does not match with user preference"))
                if resolve:
                    print(Color("{autogreen}    |-> Resolving conflict {/green}"))
                    if x.author == m_author.A_permit:
                        x.author = m_author.A_deny
                    else:
                        x.author = m_author.A_permit


# Check triggers
def solve_triggers(compiler, p=None, u=None, verbose=False, resolve=False):
    """
    Conflict detection
    :param compiler: the compiler instance
    :param p: clause 1
    :param u: clause 2
    :param verbose: verbose print
    :param resolve:
    :return:
    """
    # FIXME this is adhoc
    print(Color("{autoblue}:: Solving trigger{/blue}"))
    pre_cond = build_env(compiler.aalprog)
    u_id = str(u.name)
    p_id = str(p.name)

    ifthens = u.usage.walk(filter_type=m_aexpIfthen)
    for x in ifthens:
        res = compiler.apply_check(code=pre_cond + "~(clause(" + p_id + ").ue => " + x.to_ltl() + ")", show=False,
                                   verbose=verbose)
        if verbose:
            print("  " + str(x) + " & c1" + " : " + res["res"])

        if res["res"] == "Satisfiable":
            print(Color("\n  Implication <<" + str(x) + ">> found {automagenta}at line " +
                        str(x.name.parentCtx.getPayload().start.line) + "{/magenta} is not guaranteed by provider"))
            if resolve:
                print(Color("{autogreen}    |-> Resolving conflict {/green}"))
                # x.parent.remove(x) # TODO remove me from parent