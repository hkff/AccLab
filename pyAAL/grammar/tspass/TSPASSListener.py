# Generated from grammar/tspass/TSPASS.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSPASSParser import TSPASSParser
else:
    from TSPASSParser import TSPASSParser

# This class defines a complete listener for a parse tree produced by TSPASSParser.
class TSPASSListener(ParseTreeListener):

    # Enter a parse tree produced by TSPASSParser#x.
    def enterX(self, ctx:TSPASSParser.XContext):
        pass

    # Exit a parse tree produced by TSPASSParser#x.
    def exitX(self, ctx:TSPASSParser.XContext):
        pass


    # Enter a parse tree produced by TSPASSParser#y.
    def enterY(self, ctx:TSPASSParser.YContext):
        pass

    # Exit a parse tree produced by TSPASSParser#y.
    def exitY(self, ctx:TSPASSParser.YContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_lpar.
    def enterH_lpar(self, ctx:TSPASSParser.H_lparContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_lpar.
    def exitH_lpar(self, ctx:TSPASSParser.H_lparContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_rpar.
    def enterH_rpar(self, ctx:TSPASSParser.H_rparContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_rpar.
    def exitH_rpar(self, ctx:TSPASSParser.H_rparContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_lbar.
    def enterH_lbar(self, ctx:TSPASSParser.H_lbarContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_lbar.
    def exitH_lbar(self, ctx:TSPASSParser.H_lbarContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_rbar.
    def enterH_rbar(self, ctx:TSPASSParser.H_rbarContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_rbar.
    def exitH_rbar(self, ctx:TSPASSParser.H_rbarContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_dot.
    def enterH_dot(self, ctx:TSPASSParser.H_dotContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_dot.
    def exitH_dot(self, ctx:TSPASSParser.H_dotContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_colon.
    def enterH_colon(self, ctx:TSPASSParser.H_colonContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_colon.
    def exitH_colon(self, ctx:TSPASSParser.H_colonContext):
        pass


    # Enter a parse tree produced by TSPASSParser#h_equal.
    def enterH_equal(self, ctx:TSPASSParser.H_equalContext):
        pass

    # Exit a parse tree produced by TSPASSParser#h_equal.
    def exitH_equal(self, ctx:TSPASSParser.H_equalContext):
        pass


    # Enter a parse tree produced by TSPASSParser#program.
    def enterProgram(self, ctx:TSPASSParser.ProgramContext):
        pass

    # Exit a parse tree produced by TSPASSParser#program.
    def exitProgram(self, ctx:TSPASSParser.ProgramContext):
        pass


    # Enter a parse tree produced by TSPASSParser#formula.
    def enterFormula(self, ctx:TSPASSParser.FormulaContext):
        pass

    # Exit a parse tree produced by TSPASSParser#formula.
    def exitFormula(self, ctx:TSPASSParser.FormulaContext):
        pass


    # Enter a parse tree produced by TSPASSParser#atom.
    def enterAtom(self, ctx:TSPASSParser.AtomContext):
        pass

    # Exit a parse tree produced by TSPASSParser#atom.
    def exitAtom(self, ctx:TSPASSParser.AtomContext):
        pass


    # Enter a parse tree produced by TSPASSParser#predicate.
    def enterPredicate(self, ctx:TSPASSParser.PredicateContext):
        pass

    # Exit a parse tree produced by TSPASSParser#predicate.
    def exitPredicate(self, ctx:TSPASSParser.PredicateContext):
        pass


    # Enter a parse tree produced by TSPASSParser#variable.
    def enterVariable(self, ctx:TSPASSParser.VariableContext):
        pass

    # Exit a parse tree produced by TSPASSParser#variable.
    def exitVariable(self, ctx:TSPASSParser.VariableContext):
        pass


    # Enter a parse tree produced by TSPASSParser#constants.
    def enterConstants(self, ctx:TSPASSParser.ConstantsContext):
        pass

    # Exit a parse tree produced by TSPASSParser#constants.
    def exitConstants(self, ctx:TSPASSParser.ConstantsContext):
        pass


    # Enter a parse tree produced by TSPASSParser#negation.
    def enterNegation(self, ctx:TSPASSParser.NegationContext):
        pass

    # Exit a parse tree produced by TSPASSParser#negation.
    def exitNegation(self, ctx:TSPASSParser.NegationContext):
        pass


    # Enter a parse tree produced by TSPASSParser#conjunction.
    def enterConjunction(self, ctx:TSPASSParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by TSPASSParser#conjunction.
    def exitConjunction(self, ctx:TSPASSParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by TSPASSParser#disjunction.
    def enterDisjunction(self, ctx:TSPASSParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by TSPASSParser#disjunction.
    def exitDisjunction(self, ctx:TSPASSParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by TSPASSParser#implication.
    def enterImplication(self, ctx:TSPASSParser.ImplicationContext):
        pass

    # Exit a parse tree produced by TSPASSParser#implication.
    def exitImplication(self, ctx:TSPASSParser.ImplicationContext):
        pass


    # Enter a parse tree produced by TSPASSParser#equivalence.
    def enterEquivalence(self, ctx:TSPASSParser.EquivalenceContext):
        pass

    # Exit a parse tree produced by TSPASSParser#equivalence.
    def exitEquivalence(self, ctx:TSPASSParser.EquivalenceContext):
        pass


    # Enter a parse tree produced by TSPASSParser#uQuant.
    def enterUQuant(self, ctx:TSPASSParser.UQuantContext):
        pass

    # Exit a parse tree produced by TSPASSParser#uQuant.
    def exitUQuant(self, ctx:TSPASSParser.UQuantContext):
        pass


    # Enter a parse tree produced by TSPASSParser#eQuant.
    def enterEQuant(self, ctx:TSPASSParser.EQuantContext):
        pass

    # Exit a parse tree produced by TSPASSParser#eQuant.
    def exitEQuant(self, ctx:TSPASSParser.EQuantContext):
        pass


    # Enter a parse tree produced by TSPASSParser#utOperators.
    def enterUtOperators(self, ctx:TSPASSParser.UtOperatorsContext):
        pass

    # Exit a parse tree produced by TSPASSParser#utOperators.
    def exitUtOperators(self, ctx:TSPASSParser.UtOperatorsContext):
        pass


    # Enter a parse tree produced by TSPASSParser#btOperators.
    def enterBtOperators(self, ctx:TSPASSParser.BtOperatorsContext):
        pass

    # Exit a parse tree produced by TSPASSParser#btOperators.
    def exitBtOperators(self, ctx:TSPASSParser.BtOperatorsContext):
        pass


    # Enter a parse tree produced by TSPASSParser#always.
    def enterAlways(self, ctx:TSPASSParser.AlwaysContext):
        pass

    # Exit a parse tree produced by TSPASSParser#always.
    def exitAlways(self, ctx:TSPASSParser.AlwaysContext):
        pass


    # Enter a parse tree produced by TSPASSParser#snext.
    def enterSnext(self, ctx:TSPASSParser.SnextContext):
        pass

    # Exit a parse tree produced by TSPASSParser#snext.
    def exitSnext(self, ctx:TSPASSParser.SnextContext):
        pass


    # Enter a parse tree produced by TSPASSParser#sometime.
    def enterSometime(self, ctx:TSPASSParser.SometimeContext):
        pass

    # Exit a parse tree produced by TSPASSParser#sometime.
    def exitSometime(self, ctx:TSPASSParser.SometimeContext):
        pass


    # Enter a parse tree produced by TSPASSParser#until.
    def enterUntil(self, ctx:TSPASSParser.UntilContext):
        pass

    # Exit a parse tree produced by TSPASSParser#until.
    def exitUntil(self, ctx:TSPASSParser.UntilContext):
        pass


    # Enter a parse tree produced by TSPASSParser#unless.
    def enterUnless(self, ctx:TSPASSParser.UnlessContext):
        pass

    # Exit a parse tree produced by TSPASSParser#unless.
    def exitUnless(self, ctx:TSPASSParser.UnlessContext):
        pass


