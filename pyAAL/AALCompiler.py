"""
AALCompiler ANTLR listener for AAL language
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

from grammar.aal import AALListener
# from _pickle import Pickler
# from AALMetaModel import *
from AALChecker import *
from grammar.aal.AALLexer import AALLexer
from grammar.aal.AALParser import AALParser
from antlr4 import *
import pickle
import sys
import os
import re
from tools.color import Color, disable_all_colors, set_light_background, Windows
import tools.hottie as hottie
from tools.hottie import hot
from AALChecker import *


# Note : To avoid cyclic import
class AALCompilerListener(AALListener.AALListener):
    def __init__(self, loadlibs: bool=True, serialize: bool=False, file: str="",
                 libs_path="libs/aal/", root_path=None, recompile=False, errors_listener=None):
        pass

from aalc import *


# This class defines a complete listener for a parse tree produced by AALParser.
@hot
class AALCompilerListener(AALListener.AALListener):
    """
    Attributes :
        - loadlibs: boolean, enable or disable library loading
        - serialize = serialize
        - aalmm: Current AAL meta model instance
        - aalprog = m_aalprog()
        - currentClause = m_clause()
        - currentUsage = m_usage()
        - currentAudit = m_audit()
        - currentRectification = m_rectification()
        - currentAction = m_action()
        - currentVar = []
        - refForwardAgents = dict()
        - refForwardData = dict()
        - refForwardServices = dict()
        - refForwardTypes = dict()
        - actionExpStack = []
        - expStack = []
        - condStack = []
        - quantStack = []
        - qvarsStack = []
        - libs: libraries array
        - DEBUG: False
        - isRectification = False
        - isAudit = False
        - isBehavior = False
        - libsPath = libs_path
        - file = file
        - output = ""
        - recompile = recompile
        - root_path = root_path
        - errors_listener = errors_listener
    """
    # Initializer
    def __init__(self, loadlibs: bool=True, serialize: bool=False, file: str="",
                 libs_path="libs/aal/", root_path=None, recompile=False,
                 hotswaping=False, errors_listener=None):
        self.loadlibs = loadlibs
        self.serialize = serialize
        self.aalmm = aalmm()
        self.aalprog = m_aalprog()
        self.currentClause = m_clause()
        self.currentUsage = m_usage()
        self.currentAudit = m_audit()
        self.currentRectification = m_rectification()
        self.currentAction = m_action()
        self.currentVar = []
        self.refForwardAgents = dict()
        self.refForwardData = dict()
        self.refForwardServices = dict()
        self.refForwardTypes = dict()
        self.actionExpStack = []
        self.expStack = []
        self.condStack = []
        self.quantStack = []
        self.qvarsStack = []
        self.libs = []
        self.DEBUG = False
        self.isRectification = False
        self.isAudit = False
        self.isBehavior = False
        self.libsPath = libs_path
        self.file = file
        self.output = ""
        self.recompile = recompile
        self.root_path = root_path
        self.errors_listener = errors_listener

        # FIXME
        if hotswaping:
            hot = hottie.hot
        else:
            hot = hottie.identity

    # Manual
    @staticmethod
    def man():
        doc = "Manual for aal compiler visitor\n" \
              "{autoblue} - Attributes{/blue}" \
              "\n\t -  aalprog    " + "\t Get the AAL program instance" \
              "\n\t -  file       " + "\t The AAL source file" \
              "\n\t -  libs       " + "\t Show the loaded libraries" \
              "\n\t -  libsPath   " + "\t Print the standard lib path" \
              "" \
              "\n{autoblue} - Methods{/blue}" \
              "\n\t - load_lib(lib_name)  " + "\t Load an aal file" \
              "\n\t - clause(clauseId)    " + "\t Lookup for clause cluaseId" \
              "\n\t - show_clauses()      " + "\t Show all clauses (names" \
              "\n\t - get_clauses()       " + "\t Get all clauses (objects)" \
              "\n\t - get_macros()        " + "\t Get all macros (objects)"

        print(Color(doc))
        return Color(doc)

    def errors(self):
        return self.errors_listener.errors

    # TODO: load libs properly (ascendant scope) !
    # Load lib
    def load_lib(self, lib_name: str, internal: bool=False):
        """
        Load a library in the current program
        :param lib_name: library name
        :return:
        """
        found_lib_path = None
        tmp = self.file.split("/")
        root_path = tmp[0] + "/" if len(tmp) > 0 else "./"

        if self.root_path is not None:
            root_path = root_path + self.root_path + "/"

        lib_path = lib_name.replace('"', '').replace(".", "/") + ".aal"
        # print(root_path)
        #  Search in the file scope before
        # FIXME
        if not internal:
            lib_path2 = root_path + lib_path
            # print(lib_path2)
            # print(os.path.abspath(lib_path2))
            if not self.recompile and os.path.exists(lib_path2 + "c"):
                found_lib_path = lib_path2 + "c"
            elif os.path.exists(lib_path2):
                found_lib_path = lib_path2

                # for root, dirs, files in os.walk(root_path):
                #     for file in files:
                #         tmp = os.path.join(root, file)
                #         if tmp == lib_path2:
                #             if self.DEBUG:
                #                 print("file founded 0 ! " + tmp)
                #             found_lib_path = lib_path2
                #         elif tmp == lib_path2 + "c" and not self.recompile:
                #             if self.DEBUG:
                #                 print("file founded 0 ! " + tmp)
                #             found_lib_path = lib_path2 + "c"
                #             break

        if found_lib_path is None:
            # Search in internal libs
            root_path = self.libsPath
            lib_path2 = self.libsPath + lib_path
            if os.path.exists(lib_path2 + "c"):
                found_lib_path = lib_path2 + "c"
            elif os.path.exists(lib_path2):
                found_lib_path = lib_path2

                # for root, dirs, files in os.walk(root_path):
                #     for file in files:
                #         tmp = os.path.join(root, file)
                #         if tmp == lib_path2:
                #             if self.DEBUG:
                #                 print("file founded ! " + tmp)
                #             found_lib_path = lib_path2
                #         elif tmp == lib_path2 + "c" and not self.recompile:
                #             if self.DEBUG:
                #                 print("file founded ! " + tmp)
                #             found_lib_path = lib_path2 + "c"
                #             break

        # Try absolute path
        if os.path.exists(lib_name.replace("\"", "")):
            found_lib_path = lib_name.replace("\"", "")

        if found_lib_path is None:
            print(Color("{autored}[ERROR]{/red} lib " + str(lib_name) + " not found !"))
            return

        if found_lib_path.endswith(".aalc"):
            print("loading compiled version")
            sys.setrecursionlimit(3000)
            with open(found_lib_path, "rb") as f:
                l = pickle.load(f)
        else:
            input_file = FileStream(found_lib_path)
            lexer = AALLexer(input_file)
            stream = CommonTokenStream(lexer)
            parser = AALParser(stream)
            # !IMPORTANT : set loadlibs false to avoid infinite rec
            parser.addParseListener(AALCompilerListener(file=found_lib_path,
                                                        loadlibs=False, serialize=False))
            parser.buildParseTrees = True
            tr = parser.main()
            l = parser.getParseListeners().pop(0)

        # TODO : replace lib context (parent by this)

        # Check if the lib is already loaded, if it is the case replace it
        for lib in self.libs:
            # print(lib.file)
            if str(lib.file) == str(l.file):
                self.libs.remove(lib)

        # Add the lib
        self.libs.append(l)  # FIXME : may be removed ??
        self.aalprog.libs.append(l)

    # Start parsing
    def enterAalprog(self, ctx):
        self.aalprog = m_aalprog()
        # if self.loadlibs:
        #    self.load_lib("libs/aal/core/types.aal")

    # Exit AALprog
    def exitAalprog(self, ctx):
        self.checkForwardsRef()
        if self.DEBUG:
            print("\n")
            print(self.aalprog)
            print("\n")

        # Serialize result
        if self.serialize:
            sys.setrecursionlimit(3000)
            with open(self.file + "c", "wb") as f:
                pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    # Enter ClauseR
    def enterClause(self, ctx):
        self.currentClause = m_clause()

    # Exit ClauseR
    def exitClause(self, ctx):
        self.currentClause.name = ctx.h_clauseId().ID()
        # Check if clause is already declared
        if self.aalprog.isDeclared(self.currentClause.name, m_clause) is True:
            print(Color("{autored}[ERROR]{/red} clause " + self.currentClause.name + "{automagenta} at line " +
                        str(ctx.getPayload().start.line) + "{/magenta} already declared !"))
            return

        self.aalprog.clauses.append(self.currentClause)  # Add the clause to the aalProg clauses

        if self.DEBUG:
            print(self.refForwardServices)

    # Enter Usage
    def enterUsage(self, ctx):
        self.currentUsage = m_usage()  # Set the current usage

    # Exit Usage
    def exitUsage(self, ctx):
        if len(self.actionExpStack) == 1:
            self.currentUsage.actionExp.append(self.actionExpStack.pop())
            # self.currentUsage.children.append(self.currentUsage.actionExp[0])  # Add child
            self.currentUsage.actionExp[0].parent = self.currentUsage  # Set parent

        self.currentUsage.parent = self.currentClause  # Set the parent
        # self.currentClause.children.append(self.currentUsage)  # Add to parent's children

        if self.isRectification:  # Select usage or rectification or audit
            self.currentRectification.usage = self.currentUsage
        elif self.isAudit:
            self.currentAudit.usage = self.currentUsage
        else:
            self.currentClause.usage = self.currentUsage

    # Enter Audit
    def enterAudit(self, ctx):
        self.isAudit = True
        self.currentAudit = m_audit()

    # Exit Audit
    def exitAudit(self, ctx):
        self.currentAudit.parent = self.currentClause  # Set the parent
        # self.currentClause.children.append(self.currentAudit)  # Add to parent's children

        self.currentClause.audit = self.currentAudit
        self.isAudit = False

    # Enter Rectification
    def enterRectification(self, ctx):
        self.isRectification = True
        self.currentRectification = m_rectification()

    # Exit Rectification
    def exitRectification(self, ctx):
        self.currentRectification.parent = self.currentClause  # Set the parent
        # self.currentClause.children.append(self.currentRectification)  # Add to parent's children

        self.currentClause.rectification = self.currentRectification
        self.isRectification = False

    # Check forwards ref
    def checkForwardsRef(self) -> None:
        """
        Check forwards references.
        :return:
        """
        # Disable check in lib context
        if not self.loadlibs:
            return
        if len(self.refForwardAgents) > 0:
            print(Color("{autoyellow}[WARNING]{/yellow} Agents declarations missing !"))
            for d in self.refForwardAgents:
                print(Color("  -> " + d + " {automagenta}at line " + str(self.refForwardAgents[d].get_line()) +
                            "{/magenta}"))
        if len(self.refForwardData) > 0:
            print(Color("{autoyellow}[WARNING]{/yellow} Data declarations missing !"))
            for d in self.refForwardData:
                print(Color("  -> " + d + " {automagenta}at line " + str(self.refForwardData[d].get_line()) +
                            "{/magenta}"))
        if len(self.refForwardServices) > 0:
            print(Color("{autoyellow}[WARNING]{/yellow} Services declarations missing !"))
            for d in self.refForwardServices:
                print(Color("  -> " + d + " {automagenta}at line " + str(self.refForwardServices[d].get_line()) +
                            "{/magenta}"))
        if len(self.refForwardTypes) > 0:
            print(Color("{autoyellow}[WARNING]{/yellow} Types declarations missing !"))
            for d in self.refForwardTypes:
                print(Color("  -> " + d + " {automagenta}at line " + str(self.refForwardTypes[d].get_line()) +
                            "{/magenta}"))

    ##########################
    ####### Declarable #######
    ##########################
    # checkAgentDec
    def checkAgentDec(self, agent, declare: bool=True, quant: bool=True) -> None or m_quant or m_agent:
        """
        Check and declare an agent
        :param agent: agent's name to check
        :param declare: if true, declare agent if it is not declared
        :param quant: if true, check in quantified variables before
        :return:
        """
        agentId = str(agent)
        # Checck in libs
        for l in self.libs:
            res = l.checkAgentDec(agentId, declare=False)  # !IMPORTANT : set declare to false
            if res is not None:
                return res

        # Check in quant stack
        if quant:
            s = [x for x in self.quantStack if str(x.variable.name) == agentId]
            if len(s) > 0:  # Variable is quantified
                if self.DEBUG:
                    print("Quantified var : " + str(s[0]))
                return s[0]

        # Check if agent is already declared
        dec = self.aalprog.isDeclared(agentId, m_agent, ret=int)
        if dec is not None:
            return dec
        elif declare:  # Declare it and add it in forwards ref
            ag = m_agent(name=agent)  # Put the ID() to keep the context
            self.refForwardAgents[str(ag.name)] = ag
            self.aalprog.declarations["agents"].append(ag)  # Add agent to prog declarations
            return ag
        return None

    # checkDataDec
    def checkDataDec(self, data, declare: bool=True, quant: bool=True) -> None or m_quant or m_data:
        """
        Check and declare a data
        :param data:
        :param declare:
        :param quant:
        :return:
        """
        dataId = str(data)
        # Checck in libs
        for l in self.libs:
            res = l.checkDataDec(dataId, declare=False)  # !IMPORTANT : set declare to false
            if res is not None:
                return res

        # Check in quant stack
        if quant:
            s = [x for x in self.quantStack if str(x.variable.name) == dataId]
            if len(s) > 0:  # Variable is quantified
                if self.DEBUG:
                    print("Quantified var : " + str(s[0]))
                return s[0]

        # Check if data is already declared
        dec = self.aalprog.isDeclared(dataId, m_data, ret=int)
        if dec is not None:
            return dec
        elif declare:  # Declare it and add it in forwards ref
            ag = m_data(name=data)  # Put the ID() to keep the context
            self.refForwardData[str(ag.name)] = ag
            self.aalprog.declarations["data"].append(ag)  # Add dat to prog declarations
            return ag
        return None

    # checkServiceDec
    def checkServiceDec(self, service, declare=True, quant=True) -> None or m_quant or m_service:
        """
        Check and declare a service
        :param service: the service to declare
        """
        serviceId = str(service)
        # Checck in libs
        for l in self.libs:
            res = l.checkServiceDec(serviceId, declare=False)  # !IMPORTANT : set declare to false
            if res is not None:
                return res

        # Check in quant stack
        if quant:
            s = [x for x in self.quantStack if str(x.variable.name) == serviceId]
            if len(s) > 0:  # Variable is quantified
                if self.DEBUG:
                    print("Quantified var : " + str(s[0]))
                return s[0]

        # Check if service is already declared
        dec = self.aalprog.isDeclared(serviceId, m_service, ret=int)
        if dec is not None:
            return dec
        elif declare:  # Declare it and add it in forwards ref
            sv = m_service(name=service)  # Put the ID() to keep the context
            self.refForwardServices[str(sv.name)] = sv
            self.aalprog.declarations["services"].append(sv)  # Add service to prog declarations
            return sv
        return None

    # checkTypeDec
    def checkTypeDec(self, ttype, declare=True, quant=True) -> None or m_quant or m_type:
        """
        Check and declare a type
        :param ttype: the ttype to declare
        """
        ttypeId = str(ttype)
        # Check in libs # TODO
        for l in self.libs:
            res = l.checkTypeDec(ttype, declare=False)  # !IMPORTANT : set declare to false
            if res is not None:
                return res

        # Check in quant stack
        if quant:
            s = [x for x in self.quantStack if str(x.variable.name) == ttypeId]
            if len(s) > 0:  # Variable is quantified
                if self.DEBUG:
                    print("Quantified var : " + str(s[0]))
                return s[0]

        # Check if type is already declared
        dec = self.aalprog.isDeclared(ttypeId, m_type, ret=int)
        if dec is not None:
            return dec
        elif declare:  # Declare it and add it in forwards ref
            tp = m_type(name=ttype)  # Put the ID() to keep the context
            self.refForwardTypes[str(tp.name)] = tp
            self.aalprog.declarations["types"].append(tp)  # Add type to prog declarations
            return tp
        return None

    # Check var
    def checkVarDec(self, var, quant=True) -> None or m_agent or m_service or m_data or m_type:
        res = self.checkAgentDec(var, declare=False, quant=quant)
        if res is not None:
            return res
        res = self.checkServiceDec(var, declare=False, quant=quant)
        if res is not None:
            return res
        res = self.checkDataDec(var, declare=False, quant=quant)
        if res is not None:
            return res
        res = self.checkTypeDec(var, declare=False, quant=quant)
        if res is not None:
            return res
        return res

    # Exit agent declaration
    def exitAgentDec(self, ctx):
        agName = str(ctx.h_agentId().ID())
        agDec = m_agent(name=ctx.h_agentId().ID())  # Declare agent (put the ID() to keep context)

        # Check if agent is already declared
        if self.aalprog.isDeclared(agName, m_agent) is True:
            if agName in self.refForwardAgents:  # Check if agent is in forwards ref
                del self.refForwardAgents[agName]  # Remove it to resolve forwards ref
                # Remove it from the declarations list
                self.aalprog.declarations["agents"].remove(self.aalprog.isDeclared(agName, m_agent, ret=int))
            else:  # The agent was effectively declared
                print(Color("{autored}[ERROR]{/red} agent " + agName + "{automagenta} at line " +
                            str(ctx.getPayload().start.line) + "{/magenta} already declared !"))
                return

        # Handling types
        for agType in ctx.agentType():
            tmp = self.checkTypeDec(agType.ID())
            ref = m_ref()
            ref.label = tmp.name
            ref.target = tmp
            agDec.types.append(ref)

        # Handling Required services
        if ctx.rsService():
            for service in ctx.rsService().h_serviceId():
                tmp = self.checkServiceDec(service.ID())
                ref = m_ref()
                ref.label = tmp.name
                ref.target = tmp
                agDec.required.append(ref)

        # Handling Provided services
        if ctx.psService():
            for service in ctx.psService().h_serviceId():
                tmp = self.checkServiceDec(service.ID())
                ref = m_ref()
                ref.label = tmp.name
                ref.target = tmp
                agDec.provided.append(ref)

        self.aalprog.declarations["agents"].append(agDec)  # Add agent declaration to prog

    # Exit service declaration
    def exitServiceDec(self, ctx):
        sv_name = str(ctx.h_serviceId().ID())
        sv_dec = m_service(name=ctx.h_serviceId().ID())  # Declare service (put the ID() to keep context)
        # Check if service is already declared
        if self.aalprog.isDeclared(sv_name, m_service) is True:
            if sv_name in self.refForwardServices:  # Check if service is in forwards ref
                del self.refForwardServices[sv_name]  # Remove it to resolve forwards ref
                # Remove it from the declarations list
                self.aalprog.declarations["services"].remove(self.aalprog.isDeclared(sv_name, m_service, ret=int))
            else:  # The service was effectively declared
                print(Color("{autored}[ERROR]{/red} service " + sv_name + "{automagenta} at line " +
                            str(ctx.getPayload().start.line) + "{/magenta} already declared !"))
                return

        # Handling types
        for sv_type in ctx.serviceType():
            tmp = self.checkTypeDec(sv_type.ID())
            ref = m_ref()
            ref.label = tmp.name
            ref.target = tmp
            sv_dec.types.append(ref)

        # Handling purpose
        for purpose in ctx.h_purposeId():
            sv_dec.purpose.append(purpose.ID())

        self.aalprog.declarations["services"].append(sv_dec)  # Add service declaration to prog

    # Exit data declaration
    def exitDataDec(self, ctx):
        dtName = str(ctx.h_dataId().ID())
        dt_dec = m_data(name=ctx.h_dataId().ID())  # Declare data (put the ID() to keep context)

        # Check if data is already declared
        if self.aalprog.isDeclared(dtName, m_data) is True:
            if dtName in self.refForwardData:  # Check if data is in forwards ref
                del self.refForwardData[dtName]  # Remove it to resolve forwards ref
                # Remove it from the declarations list
                self.aalprog.declarations["data"].remove(self.aalprog.isDeclared(dtName, m_data, ret=int))
            else:  # The data was effectively declared
                print(Color("{autored}[ERROR]{/red} data " + dtName + "{automagenta} at line " +
                            str(ctx.getPayload().start.line) + "{/magenta} already declared !"))
                return

        # Handling types
        for dt_type in ctx.dataType():
            tmp = self.checkTypeDec(dt_type.ID())
            ref = m_ref()
            ref.label = tmp.name
            ref.target = tmp
            dt_dec.types.append(ref)

        # Handling Required services
        if ctx.rsService() is not None:
            for service in ctx.rsService().h_serviceId():
                tmp = self.checkServiceDec(service.ID())
                ref = m_ref()
                ref.label = tmp.name
                ref.target = tmp
                dt_dec.required.append(ref)

        # Handling Provided services
        if ctx.psService() is not None:
            for service in ctx.psService().h_serviceId():
                tmp = self.checkServiceDec(service.ID())
                ref = m_ref()
                ref.label = tmp.name
                ref.target = tmp
                dt_dec.provided.append(ref)

        # Handling subject
        if ctx.h_agentId() is not None:
            dt_dec.subject = ctx.h_agentId().ID()

        self.aalprog.declarations["data"].append(dt_dec)  # Add data declaration to prog

    # Exit Type declaration
    def exitTypeDec(self, ctx):
        dtName = str(ctx.ID())
        dtDec = m_type(name=ctx.ID())  # Declare type (put the ID() to keep context)

        # Check if type is already declared
        # print("Type : " + dtName + " " + str(self.aalprog.isDeclared(dtName, m_type)) + " "+ str(dtName in self.refForwardTypes))
        if self.aalprog.isDeclared(dtName, m_type) is True:
            if dtName in self.refForwardTypes:  # Check if type is in forwards ref
                del self.refForwardTypes[dtName]  # Remove it to resolve forwards ref
                # Remove it from the declarations list
                self.aalprog.declarations["services"].remove(self.aalprog.isDeclared(dtName, m_type, ret=int))
            else:  # The data was effectively declared
                print(Color("{autored}[ERROR]{/red} type " + dtName + "{automagenta} at line " +
                            str(ctx.getPayload().start.line) + "{/magenta} already declared !"))
                return

        # Handle type superTypes
        if ctx.type_super():
            for x in ctx.type_super().ID():
                dtDec.superTypes.append(x)

        # Handle type attributes
        if ctx.type_attr():
            for x in ctx.type_attr().ID():
                dtDec.attributes.append(x)

        # Handle type actions
        if ctx.type_actions():
            for x in ctx.type_actions().ID():
                dtDec.actions.append(x)
        self.aalprog.declarations["types"].append(dtDec)  # Add type declaration to prog

    # Enter Behavior
    def enterBehavior(self, ctx):
        self.isBehavior = True

    # Exit Behavior
    def exitBehavior(self, ctx):
        name = str(ctx.ID())
        behavior = m_behavior(name=name)
        behavior.actionExp = self.actionExpStack.pop()
        self.aalprog.behaviors.append(behavior)
        self.isBehavior = False


    ##########################
    ####### ActionExp  #######
    ##########################
    # FIXME quantif
    # Exit Action
    def exitAction(self, ctx):
        ac = m_action()
        ag1 = self.checkAgentDec(ctx.h_agentId()[0].ID())
        ac.agent1 = m_ref(label=ag1.name, target=ag1)
        ag2 = self.checkAgentDec(ctx.h_agentId()[1].ID())
        ac.agent2 = m_ref(label=ag2.name, target=ag2)

        action = self.checkServiceDec(ctx.h_serviceId().ID())
        ac.service = m_ref(label=action.name, target=action)
        if len(self.expStack):
            ac.args = self.expStack.pop()
        ac.name = ctx.h_serviceId().ID()

        self.currentAction = ac

        if ctx.time() is not None:
            tm = m_time()
            if ctx.time().O_after() is not None:
                tm.action = m_booleanOp.O_after
            elif ctx.time().O_before() is not None:
                tm.action = m_booleanOp.O_before

            tm.time = ctx.time().h_date().STRING()
            ac.time = tm
            # TODO: hanle purpose

    # Enter ActionExp
    def enterActionExp(self, ctx):
        pass

    # Exit ActionEXp
    def exitActionExp(self, ctx):
        if ctx.booleanOp() is not None:  # Handle booleanOp
            aex = m_aexpComb()
            aex.operator = m_booleanOp.fromStr(ctx.booleanOp().children[0])
            aex.actionExp2 = self.actionExpStack.pop()
            aex.actionExp1 = self.actionExpStack.pop()
            # Set parent for actionExp1/2
            aex.actionExp1.parent = aex
            aex.actionExp2.parent = aex
            self.actionExpStack.append(aex)

    # ActionExp1Action
    def enterActionExp1Action(self, ctx):
        aex = m_aexpAction()
        self.actionExpStack.append(aex)

    def exitActionExp1Action(self, ctx):
        if self.actionExpStack[-1].__class__ is m_aexpAction:  # Check actionExp type (Do not use subtype test)
            self.currentAction.parent = self.actionExpStack[-1]  # Set the parent
            self.actionExpStack[-1].action = self.currentAction  # Set the current action in the actionExp
        else:
            print("Unexpected type found " + str(self.actionExpStack[-1].__class__) + " expected m_aexpAction")

    # ActionExp2notAction
    def enterActionExp2notAction(self, ctx):
        aex = m_aexpNotAexp()
        self.actionExpStack.append(aex)

    def exitActionExp2notAction(self, ctx):
        args = self.actionExpStack.pop()  # Get the args
        if self.actionExpStack[-1].__class__ is m_aexpNotAexp:
            self.actionExpStack[-1].actionExpression = args
        else:
            print("Unexpected type found " + str(self.actionExpStack[-1].__class__) + " expected m_aexpNotAexp")

    # ActionExp3modalAction
    def enterActionExp3modalAction(self, ctx):
        aex = m_aexpModal()
        self.actionExpStack.append(aex)

    def exitActionExp3modalAction(self, ctx):
        ax = self.actionExpStack.pop()  # Get the actionExp
        if self.actionExpStack[-1].__class__ is m_aexpModal:
            p = ctx.modal()
            if len(p.children) > 0:
                self.actionExpStack[-1].modality = m_modal.fromStr(p.children[0])
            ax.parent = self.actionExpStack[-1]  # Set parent
            # self.actionExpStack[-1].children.append(ax)  # Add child
            self.actionExpStack[-1].actionExpression = ax

        else:
            print("Unexpected type found " + str(self.actionExpStack[-1].__class__) + " expected m_aexpModal")

    # ActionExp4condition
    def enterActionExp4condition(self, ctx):
        aex = m_aexpCondition()
        self.actionExpStack.append(aex)

    def exitActionExp4condition(self, ctx):
        self.actionExpStack[-1].condition = self.condStack.pop()  # Pop the condition from the stack

    # ActionExp6Author
    def enterActionExp6Author(self, ctx):
        aex = m_aexpAuthor()
        self.actionExpStack.append(aex)

    def exitActionExp6Author(self, ctx):
        action = self.currentAction
        if ctx.author().A_permit() is not None:
            self.actionExpStack[-1].author = m_author.A_permit
            self.actionExpStack[-1].name = ctx.author().A_permit()
        elif ctx.author().A_deny() is not None:
            self.actionExpStack[-1].author = m_author.A_deny
            self.actionExpStack[-1].name = ctx.author().A_deny()
        self.actionExpStack[-1].action = action

    # ActionExp7ifthen
    def enterActionExp7ifthen(self, ctx):
        aex = m_aexpIfthen()
        self.actionExpStack.append(aex)

    def exitActionExp7ifthen(self, ctx):
        branchTrue = self.actionExpStack.pop()
        condition = self.actionExpStack.pop()
        self.actionExpStack[-1].branchTrue = branchTrue
        self.actionExpStack[-1].condition = condition
        self.actionExpStack[-1].name = ctx.ifthen().O_if()

    # ActionExp8Qvar
    def enterActionExp8qvar(self, ctx):
        aex = m_aexpQvar()
        self.actionExpStack.append(aex)

    def exitActionExp8qvar(self, ctx):
        aexp = self.actionExpStack.pop()  # Pop the args

        # Handle all qvars
        # for qv in ctx.qvar():  # Reverse to get the right order of vars
        # qvar = self.qvarsStack.pop()
        # TODO: check qvar and qv
        # self.actionExpStack[-1].qvars.insert(0, qvar)
        self.actionExpStack[-1].qvars.insert(0, self.qvarsStack.pop())

        self.actionExpStack[-1].actionExp = aexp

        # if ctx.qvar().quant().Q_forall() is not None:
        #     self.actionExpStack[-1].quant = m_quant.Q_forall
        # elif ctx.qvar().quant().Q_exists is not None:
        #     self.actionExpStack[-1].quant = m_quant.Q_exists
        #
        # self.actionExpStack[-1].name = self.currentVar.name  # name the quantification with var name
        # ref = m_ref()
        # ref.label = self.currentVar.name
        # ref.name = self.currentVar.name
        # ref.target = self.checkVarDec(self.currentVar.name)
        # if ref.target is not None:
        #     print("redeclared var ")
        # ref.target = self.currentVar
        # #else:
        # #    ref.target = ref.target.name
        # self.actionExpStack[-1].variable = ref
        # self.actionExpStack[-1].condition = self.condStack.pop() if ctx.qvar().condition() is not None else None

    # Exit qvar
    def exitQvar(self, ctx):
        qvar = m_qvar()
        if ctx.quant().Q_forall() is not None:
            qvar.quant = m_quant.Q_forall
        elif ctx.quant().Q_exists is not None:
            qvar.quant = m_quant.Q_exists

        currentVar = self.currentVar.pop()
        qvar.name = currentVar.name  # Set the name
        #  Set the target
        ref = m_ref()
        ref.label = currentVar.name
        ref.name = currentVar.name
        ref.target = self.checkVarDec(currentVar.name)
        if ref.target is not None:
            if self.DEBUG:
                print("redeclared var ")
        ref.target = currentVar
        #else:
        #    ref.target = ref.target.name
        qvar.variable = ref
        qvar.condition = self.condStack.pop() if ctx.condition() is not None else None
        self.qvarsStack.append(qvar)  # TMP fr
        self.quantStack.append(qvar)  # Permanent for monodic check

    ##########################
    ####### Condition  #######
    ##########################
    def enterCondition(self, ctx):
        pass

    # ConditionNotExp
    def enterCondition1notExp(self, ctx):
        cond = m_conditionNotComb()
        self.condStack.append(cond)

    def exitCondition1notExp(self, ctx):
        self.condStack[-1].operand = m_booleanOp.O_not  # Set the operator TODO: test the not
        self.condStack[-1].exp = self.expStack.pop()  # Set the expression

    # ConditionCmp
    def enterCondition2cmpExp(self, ctx):
        cond = m_conditionCmp()
        self.condStack.append(cond)

    def exitCondition2cmpExp(self, ctx):
        self.condStack[-1].exp2 = self.expStack.pop()  # Set the second param
        self.condStack[-1].exp1 = self.expStack.pop()  # Set the first param
        if ctx.h_equal() is not None:
            self.condStack[-1].operator = m_booleanOp.O_equal
        elif ctx.h_inequal() is not None:
            self.condStack[-1].operator = m_booleanOp.O_inequal

    # Condition
    def exitCondition(self, ctx):
        # We handle to third case here
        if len(ctx.condition()) > 0:
            cond = m_conditionComb()
            cond.cond2 = self.condStack.pop()  # Set the second param
            cond.cond1 = self.condStack.pop()  # Set the first param
            if ctx.O_and() is not None:
                cond.operator = m_booleanOp.O_and
            elif ctx.O_or() is not None:
                cond.operator = m_booleanOp.O_or
            self.condStack.append(cond)

    ##########################
    ########## Exp  ##########
    ##########################
    def enterExp(self, ctx):
        exp = m_exp()
        self.expStack.append(exp)  # Push the exp

    def exitExp(self, ctx):
        # Test all cases
        # Update exp
        if ctx.h_variable() is not None:  # Test variable
            ref = m_ref()
            currentVar = self.currentVar.pop()
            ref.label = currentVar.name
            ref.name = currentVar.name
            ref.target = self.checkVarDec(currentVar.name)
            if ref.target is None:
                ref.target = currentVar
            self.expStack[-1] = ref

        elif ctx.h_constant() is not None:  # Test constants
            cts = m_constant()
            if ctx.h_constant().STRING() is not None:
                cts.name = ctx.h_constant().STRING()
            elif ctx.h_constant().INT() is not None:
                cts.name = ctx.h_constant().INT()
            self.expStack[-1] = cts

        elif ctx.h_predicate() is not None:  # Test Predicate
            cts = m_predicate()
            if ctx.h_predicate().ID() is not None:
                cts.name = ctx.h_predicate().ID()[0]
                for x in ctx.h_predicate().ID():
                    cts.args.append(x)
            self.expStack[-1] = cts

        elif (ctx.ID() is not None) and (ctx.h_attribute() is not None):  # Test attribute var
            vatt = m_varAttr()
            ref = m_ref()
            ref.label = ctx.ID()
            ref.name = ctx.ID()
            ref.target = self.checkVarDec(ctx.ID())
            vatt.variable = ref
            vatt.attribute = ctx.h_attribute().ID()
            self.expStack[-1] = vatt

    # Exit variable
    def exitH_variable(self, ctx):
        var = m_variable()
        var.name = ctx.ID()
        if ctx.h_type() is not None:
            tmp = self.checkTypeDec(ctx.h_type().ID())
            ref = m_ref()
            ref.label = tmp.name
            ref.target = tmp
            var.type = ref
        self.currentVar.append(var)

    ################################################################
    ################################################################
    ################################################################
    ################################################################

    # Exit check
    def exitLtlCheck(self, ctx):
        ch = m_ltlCheck()
        ch.name = ctx.ID()
        # ch.code = ctx.check().getText()
        # Simplified handling (without parsing) (use read file to keep spaces)
        a = ctx.check().start.start
        b = ctx.check().stop.stop
        with open(self.file, mode='r') as f:
            res = f.read()
        ch.code = res[a:int(b) + 1]

        self.aalprog.checks.append(ch)
        if self.DEBUG:
            print("Check " + str(ch.name) + " added to " + str(self.file))

    # Exit check apply
    def exitCheckApply(self, ctx):
        check_name = str(ctx.ID())
        chk = [x for x in self.aalprog.checks if str(x.name) == check_name]
        if len(chk) == 0:  # Search in libs
            for l in self.libs:
                if self.DEBUG:
                    print("Searching in lib : " + str(l.file))
                chk = [x for x in l.aalprog.checks if str(x.name) == check_name]
                if len(chk) > 0:
                    self.apply_check(chk=chk[0])
                    break
                    # TODO add warning if not found ...
        else:
            self.apply_check(chk=chk[0])
            # print("Check not found !")

    # Apply check
    def apply_check(self, chk=None, code=None, verbose=False, show=True):
        """
        Apply an FOTL check
        """
        from aalc import tspassc

        if chk is None:
            chk = m_ltlCheck(name="tmp", code=code)

        #  Generating LTL formula
        code = str(chk.code)
        ltl = code

        # Check if build env
        ltl = ltl.replace('@buildenv', build_env(self.aalprog))
        ltl = ltl.replace('"""', '')

        # Check for extra commands
        _verbose = len(re.findall('@verbose', ltl)) > 0  # TODO : optimize
        if _verbose:
            ltl = ltl.replace('@verbose', '')
            verbose = True

        for x in re.finditer('clause\(\w+\)', code):
            clauseId = x.group().replace('clause(', '').replace(')', '')  # Get clause's id
            cl = self.clause(clauseId)

            if cl is not None:
                end = x.end()
                node = aalmmnode()
                replace = str(x.group())
                # Check if we have usage/audit or rectification after
                tmp = code[end:]

                if tmp.startswith(".get_usage") or tmp.startswith(".ue"):
                    node = cl.usage
                    replace += (".ue" if tmp.startswith(".ue") else ".get_usage")
                elif tmp.startswith(".get_audit") or tmp.startswith(".ae"):
                    node = cl.audit
                    replace += (".ae" if tmp.startswith(".ae") else ".get_audit")
                elif tmp.startswith(".get_rectification") or tmp.startswith(".re"):
                    node = cl.rectification
                    replace += (".re" if tmp.startswith(".re") else ".get_rectification")
                else:
                    node = cl
                ltl = ltl.replace(replace, node.to_ltl())  # Replace clause with its ltl formulae
        if verbose:
            print("========= ltl :" + ltl)
        # exec("from aalc import tspassc")
        res = tspassc(code=ltl, use_shell=False, debug=False, reparse=False)
        if show:
            print(Color("{autoblue}" + str(chk.name) + " : " + str(res["print"]) + "{/autoblue}"))
        return res

    # Exit macro
    def exitMacro(self, ctx):
        tmp = []
        if ctx.args() is not None:
            for x in ctx.args().ID():
                tmp.append(str(x))
        self.new_macro(ctx.ID(), tmp, ctx.MCODE())

    # TODO complete
    # Exit macro call
    def exitMacroCall(self, ctx):
        # Check if there is parsing errors
        if len(self.errors()) > 0:
            print(Color("{autored}[ERROR]{/red} There are syntax errors in your code. Macros calls are disabled !"))
            return

        macro_name = str(ctx.ID())
        args = ctx.STRING()
        # print(self.macro_call(macro_name, args))
        self.macro_call(macro_name, args)

    # Exit exec
    def exitExec(self, ctx):
        exec(str(ctx.MCODE()).replace('"""', ''))

    # Search a macro
    def macro_find(self, macro_name: str=None, args: []=None, strict=True):
        pass

    # Call a macro TODO macro_find
    def macro_call(self, macro_name: str, args: []):
        __res__ = ""
        macro = [x for x in self.aalprog.macros if str(x.name) == macro_name and len(x.param) == len(args)]
        if len(macro) == 0:  # Search in libs
            for l in self.libs:
                macro = [x for x in l.aalprog.macros if str(x.name) == macro_name]
                if len(macro) > 0:
                    break

        if len(macro) > 0:
            macro = macro[0]
            # TODO Securing env call
            # Macro code is stored with comments to avoid arbitrary exec
            # try:
            code = ""
            if macro.param is not None:
                params = iter(macro.param)
                for x in args:
                    # code += str(next(params)) + " = " + str(x).replace('"', '') + "\n"
                    code += str(next(params)) + " = " + str(x) + "\n"
            code += macro.code.replace('"""', '').replace("return", "__res__ = ")  # FIXME
            exec(code)
            # except:
            # print("Macro eval error !")

        else:
            print(Color("{autored}[ERROR]{/red} Macro '" + macro_name + "' not found !"))

        return __res__

    # Exit load lib
    def exitLoadlib(self, ctx):
        lib_name = str(ctx.STRING())
        self.load_lib(lib_name, internal=False)
        if self.DEBUG:
            print("lib loaded !")

    ################################################################
    ################## Utils/Shortcuts functions ###################
    ################################################################

    # Meta function
    def clause(self, clauseId):
        res = [x for x in self.aalprog.clauses if str(x.name) == str(clauseId)]
        if len(res) > 0:
            return res[0]
        else:
            print("Clause " + clauseId + " not found !")
            return None

    def show_clauses(self):
        x = [str(x.name) + " " for x in self.aalprog.clauses]
        return "".join(x)

    def get_clauses(self):
        x = [str(x.name) + " " for x in self.aalprog.clauses]
        return "".join(x)

    def get_macros(self):
        res = [str(x.name) + "(" + " ".join(x.param) + ")" for x in self.aalprog.macros]
        return "\n".join(res)

    def get_declared(self, dtype="agent"):
        lst = ['"'+str(x.name)+'"' for x in self.aalprog.declarations[dtype]]
        for l in self.libs:
            tmp = ['"'+str(y.name)+'"' for y in l.aalprog.declarations[dtype]]
            lst = lst + tmp
        return sorted(list(set(lst)))

    # Create a new macro
    def new_macro(self, name, param, code):
        """
        Create a new macro
        :param name: macro name
        :param param: macro arguments
        :param code: macro code
        :return:
        """
        # TODO handle redef
        macro = m_macro()
        macro.name = name
        if param is not None:
            tmp = []
            for x in param:
                tmp.append(str(x))
            macro.param = tmp
        macro.code = str(code).replace('//', '#')
        self.aalprog.macros.append(macro)

    @staticmethod
    def pprinter(ltl_code: str=None):
        from grammar.tspass.TSPASSLexer import TSPASSLexer
        from grammar.tspass.TSPASSParser import TSPASSParser
        from ASTprinter import Trees2
        from antlr4.InputStream import InputStream

        inputfile = InputStream(ltl_code)
        lexer = TSPASSLexer(inputfile)
        stream = CommonTokenStream(lexer)
        parser = TSPASSParser(stream)
        parser.buildParseTrees = True
        tr = parser.formula()
        bt = Trees2.tspassTree(tr, recog=parser)
        print("\n\n\n BT")
        print(bt)

    # Test
    # noinspection PyMethodMayBeStatic

    def test(self, msg, test, expected):
        """
        !IMPORTANT! Do not turn this method into static (self may be used inside eval)
        :param msg:
        :param test:
        :param expected:
        :return:
        """
        print(Color("{autoblue}------- " + msg + "{/autoblue}"))
        res = eval(test)  # !IMPORTANT! Do not turn this method into static (self may be used inside eval)
        ret = (res == expected)
        if ret:
            print(Color("{autogreen}OK{/autogreen}"))
        else:
            print(Color("{autored}FAILED{/autoblue}"))
            print("  Found value " + str(res) + " for test " + str(test) + " while " +
                  str(expected) + " was expected !")
        return ret
