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

"""
TODO doc
"""

'''
    // AAL CORE
    AALprogram    ::= (Declaration | Clause | Comment | Macro | MacroCall)*
    Declaration   ::= AgentDec | ServiceDec | DataDec
    AgentDec      ::= AGENT Id TYPE'('Type*')' REQUIRED'('service*')' PROVIDED'('service*')'
    ServiceDec    ::= SERVICE Id TYPE'('Type*')' [PURPOSE '(' Id* ')']
    DataDec       ::= DATA Id TYPE'('Type*')' [REQUIRED'('service*')' PROVIDED'('service*')'] SUBJECT agent
    Clause        ::= CLAUSE Id '(' [Usage] [Audit Rectification] ')'
    Usage         ::= ActionExp
    Audit         ::= AUDITING [ActionExp THEN] agent.audit'['agent']' '()'
    Rectification ::= IF_VIOLATED_THEN ActionExp (??Usage)
    ActionExp     ::= Action | NOT ActionExp | Modality ActionExp | Condition
                    | ActionExp (AND|OR|ONLYWHEN|UNTIL|UNLESS) ActionExp | Author | Quant*
                    | IF ActionExp THEN ActionExp
    Exp           ::= Variable | Constant | Variable.Attribute
    Condition     ::= [NOT] Exp | Exp ['==' | '!='] Exp | Condition (AND|OR) Condition
    Author        ::= (PERMIT | DENY) Action
    Action        ::= agent.service ['['[agent]']'] '('Exp')' [Time] [Purpose]
    Quant         ::= (FORALL | EXISTS) Var [WHERE Condition]
    Variable      ::= Var ':' Type
    Modality      ::= MUST | MUSTNOT | ALWAYS | NEVER | SOMETIME
    Time          ::= (AFTER | BEFORE) Date | Time (AND | OR) Time
    Date          ::= hh ':' mm ':' ss  DD '/' MM '/' YYYY (use string)
    Type, var, val, attr Id, agent, Constant, Purpose ::= literal


    // AAL Type extension
    TypesDec      ::= TYPE Id [EXTENDS '(' Type* ')'] ATTRIBUTES '(' AttributeDec* ')' ACTIONS '(' ActionDec* ')'
    AttributeDec  ::= Id ':' Type
    ActionDec     ::= Id
    Type, Id      ::= litteral
    Affectation   ::= var.id '=' val


    // Reflexion extension
    Macro         ::= MACRO Id '(' param* ')' '(' mcode ')'
    MCode         ::= Meta model api + Python3 code (subset)
    MCall         ::= CALL Id '(' param* ')'
'''


from enum import Enum
from LTLOperators import *
from tools.color import Color
from tools.hottie import hot
# TODO: add until to modals
# TODO: handle quantifications scope
# TODO: complete children walk


##########################
########## aalmm #########
##########################
# All meta model classes are prefixed by "m_"
class aalmm():
    """
    AAL meta model class

    Attributes
        - errors: a list that contains all internal compiler error
        - parsingErrors: a list that contains all semantics parsing errors
        - aalprog: the aal program node
    """
    def __init__(self):
        self.errors = []
        self.parsingErrors = []
        self.aalprog = m_aalprog()


# Meta model node
class aalmmnode():
    """
    AAL meta model node

    Attributes
        - name: node's name, used as Id by some nodes type
        - parent: parent's node
            "\n\t -  aalprog    " + "\t Get the AAL program instance" \
            ""\
            "\n{autoblue} - Methods{/blue}" \
            "\n\t - isDeclared(name, klass, ret=bool)    " + "\t Check if element 'name' with type 'klass is declared" \
            "\n\t - children()                           " + "\t " \
            "\n\t - get_refs(pprint=bool)                " + "\t " \
            "\n\t - walk(filters=bool, filter_type=bool) " + "\t " \
            "\n\t - man()                                " + "\t Print this manual" \
            "\n\t - to_ltl()                             " + "\t Translate to ltl"
    """
    def __init__(self, name: str=None):
        """
        :param name:
        :return:
        """
        self.name = name
        self.parent = None

    def children(self):
        """ return a list that contains node's children """
        return []

    def walk(self, filters: str=None, filter_type: type=None, pprint=False):
        """
        Iterate tree in pre-order wide-first search order

        :param filters:
        :param filter_type:
        :return:
        """
        children = self.children()
        if children is None:
            children = []
        res = []
        for child in children:
            if isinstance(child, aalmmnode) or isinstance(child, sEnum):
                tmp = child.walk(filters=filters, filter_type=filter_type, pprint=pprint)
                if tmp:
                    res.extend(tmp)

        if filter_type is None:
            if filters is not None:
                if eval(filters) is True:
                    res.append(self)
            else:
                res.append(self)
        elif isinstance(self, filter_type):
            if filters is not None:
                if eval(filters) is True:
                    res.append(self)
            else:
                res.append(self)

        if pprint:
            res = [str(x) + " " for x in res]
            res = "\n".join(res)
        return res

    def remove(self):
        """
        Remove child
        Param child
        :return:
        """
        pass

    def replace(self, child, node):
        """
        Replace child
        :param child:
        :param node:
        :return:
        """
        pass

    def get_refs(self, pprint=False):
        """ Get all refs used in the node """
        res = []
        children = self.children()
        if children is None:
            children = []
        for child in children:
            if isinstance(child, aalmmnode) or isinstance(child, sEnum):
                res.extend(child.get_refs())

        if pprint:
            res = [str(x.target) + " " for x in res]
            res = "\n".join(res)

        return res

    def to_ltl(self):
        """ Get LTL translation """
        pass

    def to_nnf(self,bool):
        """

        :param bool: true if action is not negated, false if action is negated
        :return:negation propagated action
        """
        return

    def to_natural(self):
        """ Get the natural language translation """
        res = ""
        children = self.children()
        for c in children:
            if isinstance(c, aalmmnode) or isinstance(c, sEnum):
                res += c.to_natural()
        return res

    def get_line(self):
        """ Get line number in the source code """
        return str(self.name.parentCtx.getPayload().start.line)

    @classmethod
    def man(cls):
        """ print the doc of the class"""
        return Color(cls.__doc__)

    # Type test
    def is_a(self, ttype):
        pass

    # Get AST
    def to_ast(self):
        """ Get AST Format """
        # return ("<" + str(self.__class__) + "> ".join([ (str(x.to_ast()) if isinstance(x, aalmmnode) else "")
        #                                                for x in self.children() ]) +\
        #        "</" + str(self.__class__) + "> ").replace("class 'AALMetaModel.", "")
        res = '{"name": "' + str(self.__class__.__name__) + '", "code": "' + '", "children": ['
        for x in self.children():
            if isinstance(x, aalmmnode) or isinstance(x, sEnum):
                res += x.to_ast()
        if res[-1] == ",":
            res = res[:-1]
        res += ']},'
        return res


# aal prog
class m_aalprog(aalmmnode):
    """
    AAL program class.
    Note that clauses and macros extends a declarable type, but are not in the declarations dict

    Attributes
        - clauses: a list that contains all program clauses
        - declarations: a dictionary that contains lists of typed declarations
        - comments: a list that contains program's comment
        - macros: a list that contains program's macros declarations
        - macroCalls: a list that contains program's comment
    """
    def __init__(self, name: str=None):
        super().__init__(name)
        self.clauses = []
        self.declarations = dict(agents=[], services=[], data=[], types=[])
        self.comments = []
        self.macros = []
        self.macroCalls = []
        self.checks = []
        self.checksApply = []

    def __str__(self):
        """
        Print AAL program in pretty format
        :return: return the formate string
        """
        res = ""
        res += "// Types Declarations\n"
        res += "\n".join([str(x) for x in self.declarations["types"]])+"\n\n"
        res += "// Agents Declarations\n"
        res += "\n".join([str(x) for x in self.declarations["agents"]])+"\n\n"
        res += "// Service Declarations\n"
        res += "\n".join([str(x) for x in self.declarations["services"]])+"\n\n"
        res += "// Data Declarations\n"
        res += "\n".join([str(x) for x in self.declarations["data"]])+"\n\n"
        res += "// Clauses \n"
        res += "\n".join([str(x) for x in self.clauses])+"\n\n"
        res += "// Macros \n"
        res += "\n".join([str(x) for x in self.macros])+"\n\n"
        res += "// Checks \n"
        res += "\n".join([str(x) for x in self.checks])+"\n\n"
        return res

    # isDeclared
    def isDeclared(self, name: str, klass: "class", ret=bool) -> bool:
        """
        Check if the element with name=name of type klass is declared
        :param name: Name of declarable element to check
        :param klass: Type of element to check (m_agent, m_data, m_service, _m_type, m_clause, m_macro)
        :param ret: if type of bool, return true if the element is declared, otherwise return false.
         if type of int, return the element if the element is declare, otherwise return None
        :return:
        """
        decList = ""
        if klass == m_agent:
            decList = self.declarations["agents"]
        elif klass == m_data:
            decList = self.declarations["data"]
        elif klass == m_service:
            decList = self.declarations["services"]
        elif klass == m_type:
            decList = self.declarations["types"]
        elif klass == m_clause:  # Handle special case for clause
            decList = self.clauses
            #if ret == int:
             #   p = [x for x in self.clauses if str(x.name) == str(name)]
            #    return p[0] if len(p) > 0 else None
            #else:
                #p = [str(x.name) for x in self.clauses]
                #return str(name) in p

        # Handle common case for declarable
        if ret == int:
            p = [x for x in decList if str(x.name) == str(name)]
            return p[0] if len(p) > 0 else None
        else:
            p = [str(x.name) for x in decList]
            return str(name) in p

    # To ltl
    def to_ltl(self):
        return "".join([str(x.to_ltl()) + " " for x in self.clauses])

    def to_nnf(self,bool):
        return "".join([str(x.to_nnf(True)) + " " for x in self.clauses])

    # Children
    def children(self):
        res = []
        res.extend(self.clauses)
        res.extend(self.declarations["agents"])
        res.extend(self.declarations["services"])
        res.extend(self.declarations["data"])
        res.extend(self.declarations["types"])
        res.extend(self.comments)
        res.extend(self.macros)
        res.extend(self.macroCalls)
        res.extend(self.checks)
        res.extend(self.checksApply)
        return res


# Usage
class m_usage(aalmmnode):
    """
    Usage class. Contains a list of action expressions
    """
    def __init__(self, name=None):
        super().__init__(name)
        self.actionExp = []

    def __str__(self):
        return "".join([str(x) for x in self.actionExp if x is not None])

    def children(self):
        return self.actionExp

    def to_ltl(self):
        return "".join([str(x.to_ltl()) + " " for x in self.actionExp])

    def to_nnf(self,bool):
        return "".join([str(x.to_nnf(bool)) + " " for x in self.actionExp])

# Audit
class m_audit(aalmmnode):
    """
    Audit class. Contains a list of action expressions
    """
    def __init__(self, name=None):
        super().__init__(name)
        self.usage = None

    def __str__(self):
        return "AUDITING " + str(self.usage)  #"".join([str(x) for x in self.actionExp if x is not None])

    def children(self):
        return [self.usage]

    def to_ltl(self):
        return self.usage.to_ltl()  #"".join([str(x.to_ltl()) + " " for x in self.actionExp])

    def to_nnf(self,bool):
        return self.usage.to_nnf(bool)

# Rectification
class m_rectification(aalmmnode):
    """
    Rectificaiton class. Contains an usage object
    """
    def __init__(self, name=None):
        super().__init__(name)
        self.usage = None

    def __str__(self):
        return "IF_VIOLATED_THEN " + str(self.usage)

    def children(self):
        return [self.usage]

    def to_ltl(self):
        return self.usage.to_ltl()

    def to_nnf(self,bool):
        return self.usage.to_nnf(bool)


##########################
####### Declarable #######
##########################

# Declarable element class
class m_declarable(aalmmnode):
    def __init__(self, name=None):
        super().__init__(name)
        self.types = []

    # Type test
    def is_a(self, ttype):
        t = [str(x.label) for x in self.types]
        return ttype in t


# Clause
class m_clause(m_declarable):
    def __init__(self, init=False, name=None, usage: m_usage=None, audit: m_audit=None, rectification: m_rectification=None):
        super().__init__(name)
        self.usage = usage if usage is not None else m_usage()
        self.audit = audit if audit is not None else m_audit()
        self.rectification = rectification if rectification is not None else m_rectification()

    def __str__(self):
        return "CLAUSE " + str(self.name) + " (\n " +\
            ("" + str(self.usage) + "\n " if self.usage is not None else "") +\
            ("" + str(self.audit) + "\n " if self.audit is not None else "") +\
            ("" + str(self.rectification) + "\n" if self.rectification is not None else "") + ")"

    def children(self):
        res = []
        if self.usage is not None:
            res.append(self.usage)
        if self.audit is not None:
            res.append(self.audit)
        if self.rectification is not None:
            res.append(self.rectification)
        return res

    def to_ltl(self):
        ue = str(self.usage.to_ltl()) if self.usage is not None else "false"
        ae = str(self.audit.to_ltl()) if self.audit.usage is not None else "false"
        re = str(self.rectification.to_ltl()) if self.rectification.usage is not None else "false"
        return ae + " & always(" + ue + " | ((~(" + ue + ")) & (always(" + ae + " => (" + re + ")))))"

    def to_nnf(self,bool):
        ue = str(self.usage.to_nnf(bool)) if self.usage is not None else "false"
        ae = str(self.audit.to_nnf(bool)) if self.audit.usage is not None else "false"
        re = str(self.rectification.to_nnf(bool)) if self.rectification.usage is not None else "false"
        return ue + ae + re


# Agent
class m_agent(m_declarable):
    def __init__(self, name=None):
        super().__init__(name)
        self.required = []
        self.provided = []

    def __str__(self):
        sltypes = [str(elt.label) for elt in self.types]
        slrequired = [str(elt.label) for elt in self.required]
        slprovided = [str(elt.label) for elt in self.provided]
        return "AGENT " + str(self.name) + " TYPES(" + " ".join(sltypes) + ") REQUIRED(" + " ".join(slrequired) + \
               ") PROVIDED(" + " ".join(slprovided) + ")"


# Data
class m_data(m_agent):
    def __init__(self, name=None):
        super().__init__(name)
        self.required = []
        self.provided = []
        self.subject = None

    def __str__(self):
        sltypes = [str(elt.label) for elt in self.types]
        slrequired = [str(elt.label) for elt in self.required]
        slprovided = [str(elt.label) for elt in self.provided]
        return "DATA " + str(self.name) + " TYPES(" + " ".join(sltypes) + ") REQUIRED(" + " ".join(slrequired) + \
               ") PROVIDED(" + " ".join(slprovided) + ") SUBJECT(" + str(self.subject) + ")"


# Service
class m_service(m_declarable):
    def __init__(self, name=None):
        super().__init__(name)
        self.purpose = []

    def __str__(self):
        sltypes = [str(elt.label) for elt in self.types]
        slpurpose = [str(elt) for elt in self.purpose]
        return "SERVICE " + str(self.name) + " TYPES(" + " ".join(sltypes) + ") PURPOSE(" + " ".join(slpurpose) + ")"


# Type
class m_type(m_declarable):
    def __init__(self, name=None):
        super().__init__(name)
        self.superTypes = []
        self.attributes = []
        self.actions = []

    def __str__(self):
        slsuperTypes = [str(elt) for elt in self.superTypes]
        slattributes = [str(elt) for elt in self.attributes]
        slactions = [str(elt) for elt in self.actions]
        return "TYPE " + str(self.name) + " EXTENDS(" + " ".join(slsuperTypes) + ") ATTRIBUTES(" + " ".join(
            slattributes) + ") ACTIONS(" + " ".join(slactions) + ")"


# Macro
class m_macro(aalmmnode):
    def __init__(self, name="", param=[], code=None):
        super().__init__()
        self.name = name
        self.code = code
        self.param = param

    def __str__(self):
        return "MACRO " + str(self.name) + (" (" + " ".join(self.param) + " )" if len(self.param) > 0 else "")\
               + "(" + str(self.code) + ")"


# LTLCheck
class m_ltlCheck(aalmmnode):
    def __init__(self, name=None, code=None):
        super().__init__()
        self.name = name
        self.code = code

    def __str__(self):
        return "CHECK " + str(self.name) + " (" + str(self.code) + ")"


# Declarable Reference
class m_ref(aalmmnode):
    def __init__(self, label=None, target=None):
        super().__init__()
        self.name = label
        self.label = label
        self.target = target

    def __str__(self):
        return str(self.label)

    def get_refs(self):
        return [self]

    def to_ltl(self):
        return self.label # TODO: check

    def to_nnf(self,bool):
        return self.label # TODO: check

    # Type test
    def is_a(self, ttype):
        return self.target.is_a(ttype)

    # def children(self):
    #     return [self.target]


#########################
####### ActionExp #######
#########################

# ActionExp
class m_aexp(aalmmnode):
    def __init__(self):
        super().__init__()


# ActionExpr Action
class m_aexpAction(m_aexp):
    def __init__(self):
        super().__init__()
        self.action = None

    def __str__(self):
        return str(self.action)

    def children(self):
        return [self.action]

    def to_ltl(self):
        return str(self.action.to_ltl())

    def to_nnf(self,bool):

        if bool:
            return str(self)
        else:
            return str(self.negate())

    def negate(self):
        neg = m_aexpNotAexp()
        neg.actionExpression = self
        self.parent.replace(self, neg)


# ActionExp negation
class m_aexpNotAexp(m_aexp):
    def __init__(self):
        super().__init__()
        self.negation = m_booleanOp.O_not
        self.actionExpression = None

    def __str__(self):
        return str(self.negation) + " " + str(self.actionExpression)

    def children(self):
        return [self.negation, self.actionExpression]

    def to_ltl(self):
        return str(self.negation.to_ltl()) + "(" + str(self.actionExpression.to_ltl()) + ")"

    def to_nnf(self,bool):
        self.remove()
        return str(self.actionExpression.to_nnf(not bool))

    def remove(self):
        #self.actionExpression.parent = self.parent
        self.parent.replace(self, self.actionExpression)

    def replace(self, child, node):
        if child == self.actionExpression:
            self.actionExpression = node
            node.parent = self
        else:
            print("You are not my child !")


# ActionExp modality
class m_aexpModal(m_aexp):
    def __init__(self):
        super().__init__()
        self.modality = None
        self.actionExpression = None

    def __str__(self):
        return str(self.modality) + " " + str(self.actionExpression)

    def children(self):
        return [self.modality, self.actionExpression]

    def to_ltl(self):
        return str(self.modality.to_ltl()) + "(" + str(self.actionExpression.to_ltl()) + ")"

    def to_nnf(self,bool):
        return str(self.modality.to_nnf(bool)) + "(" + str(self.actionExpression.to_nnf(bool)) + ")"


    def replace(self, child, node):
        if child == self.actionExpression:
            self.actionExpression = node
            node.parent = self
        else:
            print("You are not my child !")


# ActionExp condition
class m_aexpCondition(m_aexp):
    def __init__(self):
        super().__init__()
        self.condition = None

    def __str__(self):
        return str(self.condition)

    def children(self):
        return [self.condition]

    def to_ltl(self):
        return str(self.condition.to_ltl())

#[NOT] Exp | Exp ['==' | '!='] Exp | Condition (AND|OR) Condition
    def to_nnf(self,bool):
        return str(self.condition.to_nnf(bool))


# ActionExpComb
class m_aexpComb(m_aexp):
    def __init__(self):
        super().__init__()
        self.actionExp1 = None
        self.actionExp2 = None
        self.operator = None

    def __str__(self):
        return "(" + str(self.actionExp1) + " " + str(self.operator) + " " + str(self.actionExp2) + ")"

    def children(self):
        return [self.actionExp1, self.operator, self.actionExp2]

    def to_ltl(self):
        return "(" + str(self.actionExp1.to_ltl()) + " " + str(self.operator.to_ltl()) + " " + str(self.actionExp2.to_ltl()) + ")"



    def to_nnf(self,bool):
        if bool:
            return  "(" + str(self.actionExp1.to_nnf(True)) + " " + str(self.operator) + " " + str(self.actionExp2.to_nnf(True)) + ")"
        else:
            if self.operator==m_booleanOp.O_and:
                self.operator=m_booleanOp.O_or
                return "(" + str(self.actionExp1.to_nnf(False)) + " " + str(self.operator) + " " + str(self.actionExp2.to_nnf(False)) + ")"
            elif self.operator==m_booleanOp.O_or:
                self.operator=m_booleanOp.O_and
                return "(" + str(self.actionExp1.to_nnf(False)) + " " + str(self.operator) + " " + str(self.actionExp2.to_nnf(False)) + ")"
            elif self.operator==m_booleanOp.O_onlywhen:
                self.operator=m_booleanOp.O_and
                return "(" + str(self.actionExp1.to_nnf(True)) + " " + str(self.operator) + " " + str(self.actionExp2.to_nnf(False)) + ")"
            elif self.operator==m_booleanOp.T_unless:
                self.operator==m_booleanOp.T_until
                return "(" + str(self.actionExp1.to_nnf(False)) + " " + str(self.operator) + " " + str(self.actionExp2.to_nnf(False)) + ")"
            elif self.operator==m_booleanOp.T_until:
                self.operator==m_booleanOp.T_unless
                return "(" + str(self.actionExp1.to_nnf(False)) + " " + str(self.operator) + " " + str(self.actionExp2.to_nnf(False)) + ")"

    def replace(self, child, node):
        if child == self.actionExp1:
            self.actionExp1 = node
            node.parent = self
        elif child == self.actionExp2:
            self.actionExp2 = node
            node.parent = self
        else:
            print("You are not my child !")


# ActionExp Authorization
class m_aexpAuthor(m_aexp):
    def __init__(self):
        super().__init__()
        self.author = None
        self.action = None

    def __str__(self):
        return str(self.author) + " " + str(self.action)

    def children(self):
        return [self.author, self.action]

    def to_ltl(self):
        # return str(self.author.to_ltl()) + "(" + str(self.action.to_ltl(auth=True)) + ")"
        return str(self.author.to_ltl()) + str(self.action.to_ltl(auth=True))

#    def to_nnf(self,bool):
 #       #TODO: check
  #      self.action.to_nnf(bool)
   #     return str(self.author) + str(self.action.negate())

    def to_nnf(self,bool):
        if bool:
            return str(self)
        else:
            return str(self.negate())

    def negate(self):
        neg = m_aexpNotAexp()
        neg.actionExpression = self
        self.parent.replace(self, neg)

# ActionExp ifthen
class m_aexpIfthen(m_aexp):
    def __init__(self):
        super().__init__()
        self.condition = None
        self.branchTrue = None

    def __str__(self):
        return str(m_booleanOp.O_if) + " (" + str(self.condition) + ") " + str(m_booleanOp.O_then) + " (" + \
            str(self.branchTrue) + ")"

    def children(self):
        return [self.condition, self.branchTrue]

    def to_ltl(self):
        return " (" + str(self.condition.to_ltl()) + " " + str(m_booleanOp.O_then.to_ltl()) + " " + \
               str(self.branchTrue.to_ltl()) + ")"

    def to_nnf(self,bool):
        self.branchTrue.to_nnf(bool)
        return "(" + str(self.condition.to_nnf(True)) + " " + str(m_booleanOp.O_then) +" " + str(self.branchTrue.to_nnf(bool))

    def replace(self, child, node):
        if child == self.condition:
            self.condition = node
            node.parent = self
        elif child == self.branchTrue:
            self.branchTrue = node
            node.parent = self
        else:
            print("You are not my child !")


# Qvar
class m_qvar(aalmmnode):
    def __init__(self):
        super().__init__()
        self.quant = None
        self.variable = None
        self.condition = None

    def __str__(self):
        return str(self.quant) + " " + str(self.variable.target) + ((" WHERE " + str(self.condition))
                                                                    if self.condition is not None else "")

    def children(self):
        res = []
        if self.quant is not None:
            res.append(self.quant)
        if self.variable is not None:
            res.append(self.variable)
        if self.condition is not None:
            res.append(self.condition)
        return res

    def to_ltl(self):
        return str(self.quant.to_ltl()) + "[" + str(self.variable.target.name) + "]"

    def to_nnf(self,bool):
        if bool:
            return str(self.quant) + "[" + str(self.variable.target.name) + "]"
        else:
            if self.quant == m_quant.Q_forall:
                self.quant=m_quant.Q_exists
                self.condition.to_nnf(False)
                return str(self.quant) + "[" + str(self.variable.target.name) + "]"
            elif self.quant == m_quant.Q_exists:
                self.quant =m_quant.Q_forall
                self.condition.to_nnf(False)
                return str(self.quant) + "[" + str(self.variable.target.name) + "]"

    # Type test
    def is_a(self, ttype):
        return self.variable.is_a(ttype)


# ActionExp Qvar
class m_aexpQvar(m_aexp):
    def __init__(self):
        super().__init__()
        self.qvars = []
        self.actionExp = None

    def __str__(self):
        qvars = [str(x) + " " for x in self.qvars]
        return "".join(qvars) + "(" + str(self.actionExp) + ")"

    def children(self):
        res = []
        if self.qvars is not None:
            res.extend(self.qvars)
        if self.actionExp is not None:
            res.append(self.actionExp)
        return res

    def to_ltl(self):
        q = [str(x.to_ltl()) for x in self.qvars]
        return str(" ".join(q)) + "(" + str(self.actionExp.to_ltl()) + ")"

    def to_nnf(self,bool):
        q = [str(x.to_nnf(bool)) for x in self.qvars]
        return str(" ".join(q)) + "(" + str(self.actionExp.to_nnf(bool)) + ")"

# Expression
class m_exp(aalmmnode):
    def __init__(self):
        super().__init__()
        pass

# Variable
class m_variable(m_exp):
    def __init__(self):
        super().__init__()
        self.type = None
        pass

    def __str__(self):
        return str(self.name) + ":" + str(self.type)

    def children(self):
        return [self.type]

    # Type test
    def is_a(self, ttype):
        return str(ttype) == str(self.type)


# Constant
class m_constant(m_exp):
    def __str__(self):
        return str(self.name)


# Var Attribute
class m_varAttr(m_exp):
    def __init__(self):
        super().__init__()
        self.variable = None
        self.attribute = None

    def __str__(self):
        return str(self.variable) + "." + str(self.attribute)

    def to_ltl(self):
        return str(self.attribute) + "(" + str(self.variable) + ")"

#########################
####### Condition #######
#########################


# Condition
class m_condition(m_aexp):
    pass


# Condition Comparison
class m_conditionCmp(m_condition):
    def __init__(self):
        super().__init__()
        self.exp1 = None
        self.exp2 = None
        self.operator = None

    def __str__(self):
        return str(self.exp1) + " " + str(self.operator) + " " + str(self.exp2)

    def to_ltl(self):
        return str(self.operator.to_ltl()) + "(" + str(self.exp1.to_ltl()) + ", " + str(self.exp1.to_ltl()) + ")"

    def to_nnf(self,bool):
        if bool:
            return str(self.operator) + "(" + str(self.exp1.to_nnf(True)) + ", " + str(self.exp2.to_nnf(True))
        else:
            if self.operator==m_booleanOp.O_equal:
                self.operator=m_booleanOp.O_inequal
                return "(" + str(self.exp1.to_nnf(True)) + " " + str(self.operator) + " " + str(self.exp2.to_nnf(True)) + ")"
            elif self.operator==m_booleanOp.O_or:
                self.operator=m_booleanOp.O_equal
                return "(" + str(self.exp1.to_nnf(True)) + " " + str(self.operator) + " " + str(self.exp2.to_nnf(True)) + ")"





# Condition combination
class m_conditionComb(m_condition):
    def __init__(self):
        super().__init__()
        self.cond1 = None
        self.cond2 = None
        self.operator = None

    def __str__(self):
        return str(self.cond1) + " " + str(self.operator) + " \n" + str(self.cond2)

    def to_ltl(self):
        #return str(self.cond1.to_ltl()) + " " + str(self.operator.to_ltl()) + " " + str(self.cond2.to_ltl())
        return str(self.cond1.to_ltl()) + " " + str(self.operator.to_ltl()) + " " + str(self.cond2.to_ltl())

    def to_nnf(self,bool):
        if bool:
            return str(self.operator) + "(" + str(self.cond1.to_nnf(True)) + ", " + str(self.cond2.to_nnf(True))
        else:
            if self.operator==m_booleanOp.O_and:
                self.operator=m_booleanOp.O_or
                return "(" + str(self.cond1.to_nnf(False)) + " " + str(self.operator) + " " + str(self.cond2.to_nnf(False)) + ")"
            elif self.operator==m_booleanOp.O_or:
                self.operator=m_booleanOp.O_and
                return "(" + str(self.cond1.to_nnf(False)) + " " + str(self.operator) + " " + str(self.cond2.to_nnf(False)) + ")"


# Not
class m_conditionNotComb(m_condition):
    def __init__(self):
        super().__init__()
        self.operator = None
        self.exp = None

    def __str__(self):
        return str(self.operator) + " " + str(self.exp)

    def to_ltl(self):
        return (str(self.operator) + "(" + str(self.exp.to_ltl()) + ")") if self.operator is not None else str(self.exp.to_ltl())

    def to_nnf(self,bool):
        if bool:
            if self.operator==m_booleanOp.O_not:
                self.operator=None
                return str(self.exp.to_nnf(False))
        else:
            if self.operator==m_booleanOp.O_not:
                self.operator=None
                return str(self.exp.to_nnf(True))

#########################
####### ActionExp #######
#########################
# Action
class m_action(m_aexp):
    def __init__(self):
        super().__init__()
        self.service = None
        self.agent1 = None
        self.agent2 = None
        self.args = None
        self.time = None
        self.purpose = []

    def __str__(self):
        res = str(self.agent1) + "." + str(self.service.name) +\
            ("[" + str(self.agent2) + "]" if self.agent2 is not None else "") + \
            "(" + (str(self.args) if self.args is not None else "") + ") " +\
            (str(self.time) if self.time is not None else "")

        if len(self.purpose) > 0:
            res += " PURPOSE(" + str(self.purpose) + ")"
        return res

    def children(self):
        res = []
        if self.agent1 is not None:
            res.append(self.agent1)
        if self.service is not None:
            res.append(self.service)
        if self.agent2 is not None:
            res.append(self.agent2)
        if self.args is not None:
            res.append(self.args)
        if self.time is not None:
            res.append(self.time)
        if self.purpose is not None:
            res.append(self.purpose)
        return res

    def to_ltl(self, auth=False):
        args = []
        res = ""
        if self.time is not None:
            res += "(~" + str(self.time.to_ltl()) + " => "
        # HANDLE time
        # res += ("A" if not auth else "") + str(self.service) + (", " if auth else "(")
        res += str(self.service) + "("

        if self.agent1 is not None:
            args.append(str(self.agent1))

        if self.agent2 is not None:
            args.append(str(self.agent2))

        if self.args is not None:
            args.append(str(self.args.to_ltl()))

        res += ", ".join(args)
        res += ")"
        if self.time is not None:
            res += ")"
        return res


    def to_ast(self):
        p = super().to_ast()
        p = p.replace('"m_action", "code": ""', '"m_action", "code": "' +
                      str(self).replace("\"", "'") + '"')
        return p

# m_time
class m_time(aalmmnode):
    def __init__(self):
        super().__init__()
        self.action = None
        self.time = None

    def __str__(self):
        res = str(self.action) + " " + str(self.time)
        return res

    def to_ltl(self, auth=False):
        res = str(self.time).replace("\"", "")
        res = res.replace("1 ", "one")
        res = res.replace("2 ", "two")
        res = res.replace("3 ", "three")
        res = res.replace("4", "four")
        res = res.replace("5 ", "five")
        res = res.replace("6 ", "six")
        res = res.replace("7 ", "seven")
        res = res.replace("8 ", "eight")
        res = res.replace("9 ", "nine")
        res = res.replace("10 ", "ten")
        res = res.replace("11 ", "eleven")
        res = res.replace("12 ", "twelve")
        res = res.replace(" ", "")
        return res

#########################
##### Enumerations ######
#########################
# Enumeration
class sEnum(Enum):
    def __str__(self):
        return self.value

    @classmethod
    def fromStr(cls, string):
        m = [x for x in cls.__members__.values() if x.value == str(string).upper()]
        if len(m) > 0:
            return m[0]
        else:
            return None

    def walk(self, filters: str=None, filter_type: type=None, pprint=False):
        #print("child [" + str(self.__class__) + "] : " + str(self))
        return []

# TODO: modal quant <=? quant Modal

    def get_refs(self):
        return []

    def children(self):
        return []

    def to_ltl(self):
        return ""

    def to_natural(self):
        """ Get the natural language translation """
        return ""

    def man(self):
        pass

    # Get AST
    def to_ast(self):
        """ Get AST Format """
        # return ("<" + str(self.__class__) + "> ".join([ (str(x.to_ast()) if isinstance(x, aalmmnode) else "")
        #                                                for x in self.children() ]) +\
        #        "</" + str(self.__class__) + "> ").replace("class 'AALMetaModel.", "")
        res = '{"name": "' + str(self.__class__.__name__) + '", "children": ['
        for x in self.children():
            if isinstance(x, aalmmnode) or isinstance(x, sEnum):
                res += x.to_ast()
        if res[-1] == ",":
            res = res[:-1]
        res += ']},'
        return res



# Boolean Op
class m_booleanOp(sEnum):
    O_and = ("AND" or ",")
    O_or = "OR"
    O_onlywhen = "ONLYWHEN"
    O_if = "IF"
    O_then = "THEN"
    O_after = "AFTER"
    O_before = "BEFORE"
    O_not = "NOT"
    O_equal = "=="
    O_inequal = "!="
    O_true = "TRUE"
    O_false = "FALSE"
    T_until = "UNTIL"
    T_unless = "UNLESS"

    def to_ltl(self):
        if self == m_booleanOp.O_and:
            return str(LTLOperators.t_and)
        elif self == m_booleanOp.O_or:
            return str(LTLOperators.t_or)
        elif self == m_booleanOp.O_onlywhen:
            return "not supported"
        elif self == m_booleanOp.O_if:
            return "not supported"
        elif self == m_booleanOp.O_then:
            return str(LTLOperators.t_implication)
        elif self == m_booleanOp.O_after:
            return "not supported"
        elif self == m_booleanOp.O_before:
            return "not supported"
        elif self == m_booleanOp.O_not:
            return str(LTLOperators.t_not)
        elif self == m_booleanOp.O_equal:
            return "<=>"
        elif self == m_booleanOp.O_inequal:
            return "not supported"
        elif self == m_modal.T_until:
            return str(LTLOperators.t_until)
        elif self == m_modal.T_unless:
            return str(LTLOperators.t_unless)

# Author
class m_author(sEnum):
    A_permit = "PERMIT"
    A_deny = "DENY"

    def to_ltl(self):
        if self == m_author.A_permit:
            return "P"
        elif self == m_author.A_deny:
            return "~P"


# Quant
class m_quant(sEnum):
    Q_forall = "FORALL"
    Q_exists = "EXISTS"

    def to_ltl(self):
        if self == m_quant.Q_forall:
            return str(LTLOperators.t_forall)
        elif self == m_quant.Q_exists:
            return str(LTLOperators.t_exists)


# Modal
class m_modal(sEnum):
    T_must = "MUST"
    T_mustnot = "MUSTNOT"
    T_always = "ALWAYS"
    T_never = "NEVER"
    T_sometime = "SOMETIME"


    def to_ltl(self):
        if self == m_modal.T_must:
            return str(LTLOperators.t_sometime)
        elif self == m_modal.T_mustnot:
            return str(LTLOperators.t_always) + "(" + str(LTLOperators.t_not)
        elif self == m_modal.T_always:
            return str(LTLOperators.t_always)
        elif self == m_modal.T_never:
            return str(LTLOperators.t_not) + " " + str(LTLOperators.t_always)
        elif self == m_modal.T_sometime:
            return str(LTLOperators.t_sometime)

    def to_nnf(self,bool):
        if bool:
            return ""+str(self)
        else:
            if self==m_modal.T_always:
                return str(m_modal.T_sometime)
            if self==m_modal.T_never:
                return str(m_modal.T_sometime)
            if self==m_modal.T_sometime:
                return str(m_modal.T_never)

# Get AALMetaModel classes
def get_mm_classes():
    import inspect
    import AALMetaModel
    res = []
    for name in dir(AALMetaModel):
        obj = getattr(AALMetaModel, name)
        if inspect.isclass(obj):
            res.append(obj)
    return res


# pprint for AAL code in terminal
def aal_pprint(code):
    keywords1 = [',','after','and','before','exists','forall','if','not','onlywhen','or','then','where']
    keywords2 = ['agent','apply','auditing','call','check','clause','data','if_violated_then','load','macro','service','type','types']
    keywords3 = ['always','must','mustnot','never','sometime','until']
    keywords4 = ['aa','actions','attributes','deny','extends','get_audit','get_rectification','get_usage',
                 'permit','provided','ps','purpose','rc','required','rs','uc']

    res = code
    for key in keywords1:
        key =  " " + key + " "
        res = res.replace(" " + key + " ", " {autoyellow}" + key + "{/yellow} ")
        res = res.replace(key.upper(), " {autoyellow}" + key.upper() + "{/yellow} ")

    for key in keywords2:
        key = " " + key + " "
        res = res.replace(key, " {automagenta}" + key + "{/magenta} ")
        res = res.replace(key.upper(), " {automagenta}" + key.upper() + "{/magenta} ")

    for key in keywords3:
        key = " " + key + " "
        res = res.replace(key, " {autogreen}" + key + "{/green} ")
        res = res.replace(key.upper(), " {autogreen}" + key.upper() + "{/green} ")

    for key in keywords4:
        key = " " + key + " "
        res = res.replace(key, " {autored}" + key + "{/red} ")
        res = res.replace(key.upper(), " {autored}" + key.upper() + "{/red} ")
    return Color(res)