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
    :param verbose: True -> verbose checks; False -> Monodic check on clauses
    :return:
    """
    res = ""
    res += "{autogreen}------------------------- Start Checking -------------------------{/autogreen}"
    if verbose:
        agentsCount = len(mm.aalprog.get_declared(m_agent))
        servicesCount = len(mm.aalprog.get_declared(m_service))
        dataCount = len(mm.aalprog.get_declared(m_data))
        typesCount = len(mm.aalprog.get_declared(m_type))

        res += "\n\n{autoblue}** DECLARATIONS{/autoblue}"
        res += "\n[DECLARED AGENTS]   : " + str(agentsCount)
        res += "\n[DECLARED SERVICES] : " + str(servicesCount)
        res += "\n[DECLARED DATA]     : " + str(dataCount)
        res += "\n[DECLARED TYPES]    : " + str(typesCount)

        res += "\n\n{autoblue}*** Forwards references check{/autoblue}"
        res += "\n[AGENTS]   : " + str(len(mm.refForwardAgents))
        res += "\n[SERVICES] : " + str(len(mm.refForwardServices))
        res += "\n[DATA]     : " + str(len(mm.refForwardData))
        res += "\n[TYPES]    : " + str(len(mm.refForwardTypes))
        res += "\n" + mm.checkForwardsRef()

        res += "\n\n{autoblue}*** Unused declarations{/autoblue}"
        res += "\n\n" + check_unused_dec(mm)

        res += "\n\n{autoblue}** LOADED libraries{/autoblue}"
        res += "\n[LIBS] : " + str(len(mm.aalprog.libs))

        res += "\n\n{autoblue}** CLAUSES{/autoblue}"
        res += "\n[CLAUSES] : " + str(len(mm.aalprog.clauses))

        res += "\n\n{autoblue}*** Miscellaneous{/autoblue}"
        res += "\n[PERMISSIONS]   : " + str(len(mm.aalprog.walk(filter_type=m_aexpAuthor,
                                                                filters="self.author == m_author.A_permit ")))
        res += "\n[PROHIBITIONS   : " + str(len(mm.aalprog.walk(filter_type=m_aexpAuthor,
                                                                filters="self.author == m_author.A_deny ")))
        res += "\n\n{autoblue}*** Sat test {/autoblue}\n"
        for c in mm.aalprog.clauses:
            res += "\n---------- " + str(c.name) + " ----------\n"
            res += validate2(mm, c.to_ltl(), check=True, verbose=False)["res"]
            # res += " |" + str(c.name) + (' ' * (15-len(str(c.name)))) + "->   " + check_monodic(c)["tmonodic"] + " \n"
    else:
        res += "\n\n*** Monodic test :\n"
        for c in mm.aalprog.clauses:
            res += " |" + str(c.name) + (' ' * (15-len(str(c.name)))) + "->   " + check_monodic(c)["tmonodic"] + " \n"

    res += "{autogreen}-------------------------- Checking End -------------------------{/autogreen}"
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
def validate(compiler, c1, c2, resolve: bool=False, verbose: bool=False, no_print=False, use_always=True, acc_formula=1, chk="all"):
    """
    Perform validity test between two aal clauses
    :param compiler: the compiler instance
    :param c1: clause 1
    :param c2: clause 2
    :param resolve: try to detect conflicts if exists
    :param verbose: verbose print
    :param use_always: prefix clauses with always operator
    :param acc_formula: the accountability formula to use for clause translation
            0 : only usage
            1 : (always(AE1 & always(UE1 | (~UE1 & (AE1 => RE1)) )) )
    :param chk: perform only the selected check
            "all" : all checks
            "and" : &
            "imply" : =>
            "neg" : ~(=>)
    :return:
    """
    # TODO  check if c1 and c2 exists
    fres = {"res": "", "sat": "", "neg": "", "monodic": "", "psat": "", "pneg": ""}

    # Custom printer
    def print2(x):
        if not no_print:
            print(x)

    # Monodic test
    print2("------------------------- Monodic check -------------------------")
    mc1 = check_monodic(c1)
    mc2 = check_monodic(c2)
    if not mc1["monodic"]:
        print2(mc1["print"])
        print2(Color("{autored}Please correct your clause. Exiting... {/red}"))
        return fres
    if not mc2["monodic"]:
        print2(mc2["print"])
        print2(Color("{autored}Please correct your clause. Exiting... {/red}"))
        return fres
    print2(Color("{autogreen}Monodic check passed ! {/green}"))

    v = True

    if chk == "all":
        print2("------------------------- Starting Validity check -------------------------")

    c1_id = str(c1.name)
    c2_id = str(c2.name)
    print2("c1 : " + c1_id + "\nc2 : " + c2_id)

    # clauses
    c1_ltl = c1.to_ltl_obj()
    c2_ltl = c2.to_ltl_obj()
    c1_cond = ("((always(UE1 <=> %s)) & (always(AE1 <=> %s)) & (always(RE1 <=> %s)))" % (c1_ltl["ue"], c1_ltl["ae"], c1_ltl["re"]))
    c2_cond = ("((always(UE2 <=> %s)) & (always(AE2 <=> %s)) & (always(RE2 <=> %s)))" % (c2_ltl["ue"], c2_ltl["ae"], c2_ltl["re"]))

    extra = ("\n%%%% %s\n%s \n&\n%%%% %s\n%s" %(c1_id, c1_cond, c2_id, c2_cond))
    pre_cond = build_env(compiler.aalprog, extra=extra)

    ##
    # Choosing acc formula
    ##
    if acc_formula == 0:
        c1_formula = "(always(UE1) )"
        c2_formula = "(always(UE2) )"
    elif acc_formula == 1:
        c1_formula = "(always(AE1 & always(UE1 | ((~(UE1)) & ((AE1 => (RE1)))))) )"
        c2_formula = "(always(AE2 & always(UE2 | ((~(UE2)) & ((AE2 => (RE2)))))) )"
    elif acc_formula == 2:
        c1_formula = "(always(AE1) )"
        c2_formula = "(always(AE2) )"
    elif acc_formula == 3:
        c1_formula = "(always(RE1) )"
        c2_formula = "(always(RE2) )"
    else:
        c1_formula = "(always(UE1) )"
        c2_formula = "(always(UE2) )"
    ##
    # C1 & C2
    ##
    if chk == "and" or chk == "all":
        print2("----- Checking c1 & c2 consistency :")
        # code = ("%s &\n(\n%% %s\n %s & \n%% %s\n %s & \n\n %s & %s \n)"
        #        % (pre_cond, c1_id, c1_cond, c2_id, c2_cond, c1_formula, c2_formula))
        code = ("%s &\n(\n %s & %s \n)"
                % (pre_cond, c1_formula, c2_formula))
        # print2(code)
        res = compiler.apply_check(code=code, show=False, verbose=verbose, extended_mode=False)
        if res["res"] == "Unsatisfiable":
            print2(Color("{autored}  -> " + res["res"] + " : c1 & c2 are not consistent{/red}"))
            v = v and False
            fres["sat"] = "Unsatisfiable"
            fres["psat"] = "{autored}  -> " + res["res"] + "{/red}"
            return fres
        else:
            print2(Color("{autogreen}  -> " + res["res"] + "{/green}"))
            fres["sat"] = "Satisfiable"
            fres["psat"] = "{autogreen}  -> " + res["res"] + "{/green}"

        if res["res"] == "":
            print2(res["print"])

    if chk == "&":
        return fres

    ##
    # C1 => C2
    ##
    if chk == "imply" or chk == "all":
        print2("----- Checking c1 => c2 :")
        # code = ("%s =>\n(\n%% %s\n %s & \n%% %s\n %s & \n\n %s => %s \n)"
        #        % (pre_cond, c1_id, c1_cond, c2_id, c2_cond, c1_formula, c2_formula))
        code = ("%s =>\n(\n %s => %s \n)"
                % (pre_cond, c1_formula, c2_formula))
        # print2(code)
        res = compiler.apply_check(code=code, show=False, verbose=verbose, extended_mode=False)
        if res["res"] == "Unsatisfiable":
            v = v and False
            print2(Color("{autored}  -> " + res["res"] + "{/red}"))
        else:
            print2(Color("{autogreen}  -> " + res["res"] + "{/green}"))

        if res["res"] == "":
            print2(res["print"])

    if chk == "imply":
        return fres

    ##
    # ~(C1 => C2)
    ##
    if chk == "neg" or chk == "all":
        print2("----- Checking ~(c1 => c2) :")
        # code = ("~(%s =>\n(\n%% %s\n %s & \n%% %s\n %s & \n\n %s => %s \n))"
        #        % (pre_cond, c1_id, c1_cond, c2_id, c2_cond, c1_formula, c2_formula))
        code = ("~(%s =>\n(\n %s => %s \n))"
                % (pre_cond, c1_formula, c2_formula))
        # print2(code)
        res = compiler.apply_check(code=code, show=False, verbose=verbose, extended_mode=False)
        if res["res"] == "Unsatisfiable":
            print2(Color("{autogreen}  -> " + res["res"] + "{/green}"))
            fres["sat"] = "Unsatisfiable"
            fres["psat"] = "{autogreen}  -> " + res["res"] + "{/green}"
        else:
            print2(Color("{autored}  -> " + res["res"] + "{/red}"))
            fres["sat"] = "Satisfiable"
            fres["psat"] = "{autored}  -> " + res["res"] + "{/red}"
            v = v and False

        if res["res"] == "":
            print2(res["print"])

        if res["res"] == "Unsatisfiable":
            v = v and True

    if chk == "neg":
        return fres

    if chk == "all":
        ##
        # Validity result
        ##
        if v:
            print2(Color("\n{autogreen}[VALIDITY] Formula is valid !{/green}"))
        else:
            print2(Color("\n{autored}[VALIDITY] Formula is not valid !{/red}"))

        print2("------------------------- Validity check End -------------------------\n")
    return fres


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
    res = ""
    fres = {"res": "", "sat": "", "neg": "", "monodic": "", "psat": "", "pneg": ""}

    # Monodic test
    res += "------------------------- Monodic check -------------------------\n"
    mc1 = check_monodic(c1)
    if not mc1["monodic"]:
        res += mc1["print"] + "\n"
        res += "{autored}Please correct your clause. Exiting... {/red}\n"
        return
    res += "{autogreen}Monodic check passed ! {/green}\n"
    fres["monodic"] = mc1["monodic"]

    ##
    # Satisfiability
    ##
    v = False
    pre_cond = build_env(compiler.aalprog)
    res += "------------------------ Starting " + ("Validity" if not check else "") + " check ---------------------\n"
    res += "----- Checking c1 :\n"
    res2 = compiler.apply_check(code="(" + pre_cond + " & " + c1 + ")", show=False, verbose=verbose)
    if res2["res"] == "Unsatisfiable":
        v = False
        res += "{autored}  -> " + res2["res"] + "{/red}\n"
        fres["psat"] = "{autored}  -> " + res2["res"] + "{/red}"
    else:
        res += "{autogreen}  -> " + res2["res"] + "{/green}\n"
        fres["psat"] = "{autogreen}  -> " + res2["res"] + "{/green}"

    if res2["res"] == "":
        res += res2["print"] + "\n"
    fres["sat"] = res2["res"]

    ##
    # Validity
    ##
    if not check:
        res += "----- Checking ~(c1) :\n"
        res2 = compiler.apply_check(code="~((" + pre_cond + " & " + c1 + "))", show=False, verbose=verbose)
        if res2["res"] == "Unsatisfiable":
            res += "{autogreen}  -> " + res2["res"] + "{/green}\n"
            fres["pneg"] = "{autogreen}  -> " + res2["res"] + "{/green}"
        else:
            res += "{autored}  -> " + res2["res"] + "{/red}\n"
            fres["pneg"] = "{autored}  -> " + res2["res"] + "{/red}"

        if res2["res"] == "":
            res += res2["print"] + "\n"

        if res2["res"] == "Unsatisfiable":
            v = True

        if v:
            res += "\n{autogreen}[VALIDITY] Formula is valid !{/green}\n"
        else:
            res += "\n{autored}[VALIDITY] Formula is not valid !{/red}\n"

        fres["neg"] = res2["res"]

    res += "------------------------- " + ("Validity" if not check else "") + " check End -------------------------\n\n"

    fres["res"] = Color(res)
    return fres


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
    return
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
    return
    # FIXME this is adhoc to remove
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


# Conflict detection
def conflict(compiler, c1, c2=None, resolve=False, verbose=False):
    """
    Detect conflicts in a clause / between two clauses using masking
    :param compiler:
    :param c1:
    :param c2:
    :param resolve:
    :param verbose:
    :return:
    """
    # Check type Val/Sat
    def chk():
        if c2 is None:
            return validate2(compiler, "(always (" + c1.usage.to_ltl() + "))", check=True, verbose=verbose2)
        else:
            return validate(compiler, c1, c2, resolve=False, verbose=verbose2, no_print=True, use_always=True, acc_formula=0, chk="neg")

    # Masking aexComb expression
    def masking(c):
        if isinstance(c, m_aexpComb):
            e1 = c.actionExp1
            e2 = c.actionExp2
        elif isinstance(c, m_aexpIfthen):
            e1 = c.condition
            e2 = c.branchTrue
        else:
            return "Type %s not handled !" % type(c)
        if verbose:
            print("\n\n" + "="*20 + " Handling expression " + "="*20 + "\n" +
                  "== e1 : " + str(e1) + "\n== e2 : " + str(e2))

        ##
        # Masking e1
        ##
        before_masking_e1 = chk()
        if verbose:
            print(Color("\n====== Before masking e1 : " + before_masking_e1["psat"]))

        if verbose:
            print(Color("{autoblue}Masking e1...{/autoblue}"))

        e1.mask()
        after_masking_e1 = chk()
        if verbose:
            print(Color("====== After Masking e1  : " + after_masking_e1["psat"]))
        e1.unmask()

        if c2 is None:
            if before_masking_e1["sat"] == "Unsatisfiable" and after_masking_e1["sat"] == "Satisfiable":
                res.append(e1)
        else:
            if before_masking_e1["sat"] == "Satisfiable" and after_masking_e1["sat"] == "Unsatisfiable":
                res.append(e1)

        ##
        # Masking e2
        ##
        before_masking_e2 = chk()
        if verbose:
            print(Color("\n====== Before masking e2 : " + before_masking_e2["psat"]))

        if verbose:
            print(Color("{autoblue}Masking e2...{/autoblue}"))

        e2.mask()
        after_masking_e2 = chk()
        if verbose:
            print(Color("====== After Masking e2  : " + after_masking_e2["psat"]))
        e2.unmask()

        if c2 is None:
            if before_masking_e2["sat"] == "Unsatisfiable" and after_masking_e2["sat"] == "Satisfiable":
                res.append(e2)
        else:
            if before_masking_e2["sat"] == "Satisfiable" and after_masking_e2["sat"] == "Unsatisfiable":
                res.append(e2)

    print("============================= Starting conflict detection ===========================")
    # Enable masking
    enable_masking()
    verbose2 = False
    res = []

    # Getting all comb in c1
    if c1 is not None:
        cmbs = c1.usage.walk(filter_type=m_aexpComb)
        if len(cmbs) == 0:  # if there are no comb try with ifThenExp
            cmbs = c1.usage.walk(filter_type=m_aexpIfthen)

        for x in cmbs:
            masking(x)

    # Getting all comb in c2
    if c2 is not None:
        cmbs2 = c2.usage.walk(filter_type=m_aexpComb)
        if len(cmbs2) == 0:  # if there are no comb try with ifThenExp
            cmbs2 = c2.usage.walk(filter_type=m_aexpIfthen)

        for x in cmbs2:
            masking(x)

    print("\n\n=============================================================================\n\n")

    ##
    # Minimizing unsat set
    ##
    if verbose:
        print("Expressions causing unsat are :\n")
        [print(Color(" * E {automagenta}at line %s{/automagenta} : %s" % (x.get_line(), x))) for x in res]

    print("\n\nMinimized Expressions causing unsat are :\n")
    min = minimize(compiler, res)
    [print(Color(" * E {automagenta}at line %s{/automagenta} : %s" % (x.get_line(), x))) for x in min]
    print("\n------------------------- conflict detection End -------------------------\n")

    ##
    # Resolving
    ##
    if resolve:
        before_resolving = chk() # validate2(compiler, "(always (" + c1.usage.to_ltl() + "))", check=True, verbose=verbose2)
        print(Color("\n====== Before Resolving : " + before_resolving["psat"] + "\n"))

        for x in min:
            if isinstance(x, m_aexpAuthor):
                print(Color("  -> Changing permission PERMIT/DENY in %s {automagenta}at line %s{/automagenta}"
                            % (x, x.get_line())))
                x.author = m_author.A_deny if x.author == m_author.A_permit else m_author.A_permit

        after_resolving = chk() # validate2(compiler, "(always (" + c1.usage.to_ltl() + "))", check=True, verbose=verbose2)
        print(Color("\n====== After Resolving : " + after_resolving["psat"] + "\n"))


def minimize(compiler, l):
    to_rem = []
    for b in l:
        for s in l:
            if b.is_my_child(s):
                to_rem.append(b)
    for x in to_rem:
        if x in l:
            l.remove(x)
    return l
