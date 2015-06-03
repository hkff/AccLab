"""
ASTprinter
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

from antlr4.tree.Trees import Trees, RuleNode, ErrorNode, TerminalNode, Tree, ParseTree
from antlr4.Utils import escapeWhitespace
from io import StringIO
from antlr4 import *


# Tree2
class Trees2(Trees):
    """
    Prety printer for ANTLR 4, that support aal and tspass files
    """
    @classmethod
    def tspassTree(cls, t: Tree, ruleNames: list=None, recog: Parser=None):
        res = cls.toStringTree(t=t, ruleNames=ruleNames, recog=recog, lg="tspass")
        return res

    @classmethod
    def aalTree(cls, t: Tree, ruleNames: list=None, recog: Parser=None):
        res = cls.toStringTree(t=t, ruleNames=ruleNames, recog=recog, lg="aal")
        return res

    @classmethod
    def toStringTree(cls, t: Tree, ruleNames: list=None, recog: Parser=None, depth=None, lg=None):
        if depth is None:
            depth = 0
        if recog is not None:
            ruleNames = recog.ruleNames
        s = escapeWhitespace(cls.getNodeText(t, ruleNames), False)
        if t.getChildCount() == 0:
            return s
        with StringIO() as buf:
            p = ""
            for i in range(0, depth):
                p += " "
            if s != "-1":
                buf.write(u"(")
            # buf.write("p")
            if s != "-1":
                buf.write(s)
                buf.write(' ')
            for i in range(0, t.getChildCount()):
                if i > 0:
                    if lg is not "tspass":
                        buf.write(' ')
                buf.write(cls.toStringTree(t.getChild(i), ruleNames, depth=depth+1, lg=lg))
            if s != "-1":
                buf.write(u")")
            tmp = buf.getvalue()
            # print(tmp)
            if tmp.startswith('('):
                buf.write('')

            return buf.getvalue()

    @classmethod
    def getNodeText(cls, t: Tree, ruleNames: list=None, recog: Parser=None):
        if recog is not None:
            ruleNames = recog.ruleNames
        if ruleNames is not None:
            if isinstance(t, RuleNode):
                return "-1"   #ruleNames[t.getRuleContext().getRuleIndex()]
            elif isinstance(t, ErrorNode):
                return str(t)
            elif isinstance(t, TerminalNode):
                if t.symbol is not None:
                    return t.symbol.text
        # no recog for rule names
        payload = t.getPayload()
        if isinstance(payload, Token):
            return payload.text

        return str(t.getPayload())
