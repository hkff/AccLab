# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .TSPASSListener import TSPASSListener
else:
    from TSPASSListener import TSPASSListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3$")
        buf.write("\u010b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\7\13P\n\13\f\13\16\13S\13\13")
        buf.write("\3\13\3\13\7\13W\n\13\f\13\16\13Z\13\13\3\13\3\13\7\13")
        buf.write("^\n\13\f\13\16\13a\13\13\3\13\3\13\3\13\7\13f\n\13\f\13")
        buf.write("\16\13i\13\13\3\13\3\13\3\13\7\13n\n\13\f\13\16\13q\13")
        buf.write("\13\3\13\3\13\3\13\7\13v\n\13\f\13\16\13y\13\13\3\13\3")
        buf.write("\13\3\13\7\13~\n\13\f\13\16\13\u0081\13\13\3\13\3\13\3")
        buf.write("\13\3\13\7\13\u0087\n\13\f\13\16\13\u008a\13\13\5\13\u008c")
        buf.write("\n\13\3\13\3\13\7\13\u0090\n\13\f\13\16\13\u0093\13\13")
        buf.write("\3\13\3\13\3\13\7\13\u0098\n\13\f\13\16\13\u009b\13\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00a1\n\13\3\13\7\13\u00a4\n")
        buf.write("\13\f\13\16\13\u00a7\13\13\3\13\3\13\7\13\u00ab\n\13\f")
        buf.write("\13\16\13\u00ae\13\13\3\13\3\13\3\13\3\13\7\13\u00b4\n")
        buf.write("\13\f\13\16\13\u00b7\13\13\7\13\u00b9\n\13\f\13\16\13")
        buf.write("\u00bc\13\13\3\f\3\f\3\f\3\f\5\f\u00c2\n\f\3\f\3\f\3\f")
        buf.write("\5\f\u00c7\n\f\7\f\u00c9\n\f\f\f\16\f\u00cc\13\f\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\7\25")
        buf.write("\u00e5\n\25\f\25\16\25\u00e8\13\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u00f1\n\26\f\26\16\26\u00f4\13\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\5\27\u00fb\n\27\3\30\3\30\5")
        buf.write("\30\u00ff\n\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\35\2\3\24\36\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668\2\6\4\2\f\f\21\21\4\2")
        buf.write("\b\b\33\33\3\2\22\23\4\2\26\26\30\30\u0110\2:\3\2\2\2")
        buf.write("\4<\3\2\2\2\6>\3\2\2\2\b@\3\2\2\2\nB\3\2\2\2\fD\3\2\2")
        buf.write("\2\16F\3\2\2\2\20H\3\2\2\2\22J\3\2\2\2\24\u008b\3\2\2")
        buf.write("\2\26\u00bd\3\2\2\2\30\u00cf\3\2\2\2\32\u00d1\3\2\2\2")
        buf.write("\34\u00d3\3\2\2\2\36\u00d5\3\2\2\2 \u00d7\3\2\2\2\"\u00d9")
        buf.write("\3\2\2\2$\u00db\3\2\2\2&\u00dd\3\2\2\2(\u00df\3\2\2\2")
        buf.write("*\u00eb\3\2\2\2,\u00fa\3\2\2\2.\u00fe\3\2\2\2\60\u0100")
        buf.write("\3\2\2\2\62\u0102\3\2\2\2\64\u0104\3\2\2\2\66\u0106\3")
        buf.write("\2\2\28\u0108\3\2\2\2:;\7\32\2\2;\3\3\2\2\2<=\7\17\2\2")
        buf.write("=\5\3\2\2\2>?\7\t\2\2?\7\3\2\2\2@A\7\24\2\2A\t\3\2\2\2")
        buf.write("BC\7\7\2\2C\13\3\2\2\2DE\7\4\2\2E\r\3\2\2\2FG\7\25\2\2")
        buf.write("G\17\3\2\2\2HI\7\n\2\2I\21\3\2\2\2JK\7\31\2\2K\23\3\2")
        buf.write("\2\2LM\b\13\1\2MQ\5\32\16\2NP\7 \2\2ON\3\2\2\2PS\3\2\2")
        buf.write("\2QO\3\2\2\2QR\3\2\2\2R\u008c\3\2\2\2SQ\3\2\2\2TX\5\34")
        buf.write("\17\2UW\7 \2\2VU\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2")
        buf.write("Y\u008c\3\2\2\2ZX\3\2\2\2[_\5\26\f\2\\^\7 \2\2]\\\3\2")
        buf.write("\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\u008c\3\2\2\2a_\3")
        buf.write("\2\2\2bc\5\36\20\2cg\5\24\13\2df\7 \2\2ed\3\2\2\2fi\3")
        buf.write("\2\2\2ge\3\2\2\2gh\3\2\2\2h\u008c\3\2\2\2ig\3\2\2\2jk")
        buf.write("\5(\25\2ko\5\24\13\2ln\7 \2\2ml\3\2\2\2nq\3\2\2\2om\3")
        buf.write("\2\2\2op\3\2\2\2p\u008c\3\2\2\2qo\3\2\2\2rs\5*\26\2sw")
        buf.write("\5\24\13\2tv\7 \2\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3")
        buf.write("\2\2\2x\u008c\3\2\2\2yw\3\2\2\2z{\5,\27\2{\177\5\24\13")
        buf.write("\2|~\7 \2\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\u008c\3\2\2\2\u0081\177\3\2\2\2\u0082")
        buf.write("\u0083\5\6\4\2\u0083\u0084\5\24\13\2\u0084\u0088\5\b\5")
        buf.write("\2\u0085\u0087\7 \2\2\u0086\u0085\3\2\2\2\u0087\u008a")
        buf.write("\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008bL\3\2\2\2\u008b")
        buf.write("T\3\2\2\2\u008b[\3\2\2\2\u008bb\3\2\2\2\u008bj\3\2\2\2")
        buf.write("\u008br\3\2\2\2\u008bz\3\2\2\2\u008b\u0082\3\2\2\2\u008c")
        buf.write("\u00ba\3\2\2\2\u008d\u0091\f\3\2\2\u008e\u0090\7 \2\2")
        buf.write("\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0094\u00b9\5\24\13\4\u0095\u0099\f\n\2\2\u0096")
        buf.write("\u0098\7 \2\2\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u00a0\3")
        buf.write("\2\2\2\u009b\u0099\3\2\2\2\u009c\u00a1\5 \21\2\u009d\u00a1")
        buf.write("\5\"\22\2\u009e\u00a1\5$\23\2\u009f\u00a1\5&\24\2\u00a0")
        buf.write("\u009c\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a4\7")
        buf.write(" \2\2\u00a3\u00a2\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a8\u00ac\5\24\13\2\u00a9\u00ab\7 \2")
        buf.write("\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00b9\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00af\u00b0\f\6\2\2\u00b0\u00b1\5.\30\2")
        buf.write("\u00b1\u00b5\5\24\13\2\u00b2\u00b4\7 \2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b8\u008d\3\2\2\2\u00b8\u0095\3\2\2\2\u00b8\u00af\3")
        buf.write("\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\25\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be")
        buf.write("\5\30\r\2\u00be\u00c1\5\6\4\2\u00bf\u00c2\5\32\16\2\u00c0")
        buf.write("\u00c2\5\34\17\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3\2\2")
        buf.write("\2\u00c2\u00ca\3\2\2\2\u00c3\u00c6\7\6\2\2\u00c4\u00c7")
        buf.write("\5\32\16\2\u00c5\u00c7\5\34\17\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c3\3\2\2\2")
        buf.write("\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce")
        buf.write("\5\b\5\2\u00ce\27\3\2\2\2\u00cf\u00d0\7\36\2\2\u00d0\31")
        buf.write("\3\2\2\2\u00d1\u00d2\7\36\2\2\u00d2\33\3\2\2\2\u00d3\u00d4")
        buf.write("\t\2\2\2\u00d4\35\3\2\2\2\u00d5\u00d6\t\3\2\2\u00d6\37")
        buf.write("\3\2\2\2\u00d7\u00d8\7\5\2\2\u00d8!\3\2\2\2\u00d9\u00da")
        buf.write("\7\34\2\2\u00da#\3\2\2\2\u00db\u00dc\t\4\2\2\u00dc%\3")
        buf.write("\2\2\2\u00dd\u00de\t\5\2\2\u00de\'\3\2\2\2\u00df\u00e0")
        buf.write("\7\35\2\2\u00e0\u00e1\7\7\2\2\u00e1\u00e6\7\36\2\2\u00e2")
        buf.write("\u00e3\7\6\2\2\u00e3\u00e5\7\36\2\2\u00e4\u00e2\3\2\2")
        buf.write("\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7")
        buf.write("\3\2\2\2\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9")
        buf.write("\u00ea\7\4\2\2\u00ea)\3\2\2\2\u00eb\u00ec\7\r\2\2\u00ec")
        buf.write("\u00ed\7\7\2\2\u00ed\u00f2\7\36\2\2\u00ee\u00ef\7\6\2")
        buf.write("\2\u00ef\u00f1\7\36\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\7\4\2\2")
        buf.write("\u00f6+\3\2\2\2\u00f7\u00fb\5\60\31\2\u00f8\u00fb\5\62")
        buf.write("\32\2\u00f9\u00fb\5\64\33\2\u00fa\u00f7\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2\2\u00fc")
        buf.write("\u00ff\5\66\34\2\u00fd\u00ff\58\35\2\u00fe\u00fc\3\2\2")
        buf.write("\2\u00fe\u00fd\3\2\2\2\u00ff/\3\2\2\2\u0100\u0101\7\27")
        buf.write("\2\2\u0101\61\3\2\2\2\u0102\u0103\7\20\2\2\u0103\63\3")
        buf.write("\2\2\2\u0104\u0105\7\3\2\2\u0105\65\3\2\2\2\u0106\u0107")
        buf.write("\7\16\2\2\u0107\67\3\2\2\2\u0108\u0109\7\13\2\2\u0109")
        buf.write("9\3\2\2\2\32QX_gow\177\u0088\u008b\u0091\u0099\u00a0\u00a5")
        buf.write("\u00ac\u00b5\u00b8\u00ba\u00c1\u00c6\u00ca\u00e6\u00f2")
        buf.write("\u00fa\u00fe")
        return buf.getvalue()
		

class TSPASSParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__26=1
    T__25=2
    T__24=3
    T__23=4
    T__22=5
    T__21=6
    T__20=7
    T__19=8
    T__18=9
    T__17=10
    T__16=11
    T__15=12
    T__14=13
    T__13=14
    T__12=15
    T__11=16
    T__10=17
    T__9=18
    T__8=19
    T__7=20
    T__6=21
    T__5=22
    T__4=23
    T__3=24
    T__2=25
    T__1=26
    T__0=27
    ID=28
    INT=29
    NEWLINE=30
    WS=31
    BLANK=32
    STRING=33
    COMMENT=34

    tokenNames = [ "<INVALID>", "'sometime'", "']'", "'&'", "','", "'['", 
                   "'not'", "'('", "':'", "'unless'", "'false'", "'?'", 
                   "'until'", "'y'", "'next'", "'true'", "'->'", "'=>'", 
                   "')'", "'.'", "'<->'", "'always'", "'<=>'", "'='", "'x'", 
                   "'~'", "'|'", "'!'", "ID", "INT", "NEWLINE", "WS", "BLANK", 
                   "STRING", "COMMENT" ]

    RULE_x = 0
    RULE_y = 1
    RULE_h_lpar = 2
    RULE_h_rpar = 3
    RULE_h_lbar = 4
    RULE_h_rbar = 5
    RULE_h_dot = 6
    RULE_h_colon = 7
    RULE_h_equal = 8
    RULE_formula = 9
    RULE_atom = 10
    RULE_predicate = 11
    RULE_variable = 12
    RULE_constants = 13
    RULE_negation = 14
    RULE_conjunction = 15
    RULE_disjunction = 16
    RULE_implication = 17
    RULE_equivalence = 18
    RULE_uQuant = 19
    RULE_eQuant = 20
    RULE_utOperators = 21
    RULE_btOperators = 22
    RULE_always = 23
    RULE_snext = 24
    RULE_sometime = 25
    RULE_until = 26
    RULE_unless = 27

    ruleNames =  [ "x", "y", "h_lpar", "h_rpar", "h_lbar", "h_rbar", "h_dot", 
                   "h_colon", "h_equal", "formula", "atom", "predicate", 
                   "variable", "constants", "negation", "conjunction", "disjunction", 
                   "implication", "equivalence", "uQuant", "eQuant", "utOperators", 
                   "btOperators", "always", "snext", "sometime", "until", 
                   "unless" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class XContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_x

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterX(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitX(self)




    def x(self):

        localctx = TSPASSParser.XContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_x)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(self.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class YContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_y

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterY(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitY(self)




    def y(self):

        localctx = TSPASSParser.YContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_y)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(self.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_lparContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_lpar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_lpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_lpar(self)




    def h_lpar(self):

        localctx = TSPASSParser.H_lparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_h_lpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(self.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_rparContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_rpar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_rpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_rpar(self)




    def h_rpar(self):

        localctx = TSPASSParser.H_rparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_h_rpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(self.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_lbarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_lbar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_lbar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_lbar(self)




    def h_lbar(self):

        localctx = TSPASSParser.H_lbarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_h_lbar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(self.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_rbarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_rbar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_rbar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_rbar(self)




    def h_rbar(self):

        localctx = TSPASSParser.H_rbarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_h_rbar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(self.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_dotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_dot

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_dot(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_dot(self)




    def h_dot(self):

        localctx = TSPASSParser.H_dotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_h_dot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(self.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_colonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_colon

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_colon(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_colon(self)




    def h_colon(self):

        localctx = TSPASSParser.H_colonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_h_colon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(self.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_equalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_h_equal

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterH_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitH_equal(self)




    def h_equal(self):

        localctx = TSPASSParser.H_equalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_h_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(self.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eQuant(self):
            return self.getTypedRuleContext(TSPASSParser.EQuantContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TSPASSParser.NEWLINE)
            else:
                return self.getToken(TSPASSParser.NEWLINE, i)

        def constants(self):
            return self.getTypedRuleContext(TSPASSParser.ConstantsContext,0)


        def variable(self):
            return self.getTypedRuleContext(TSPASSParser.VariableContext,0)


        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSPASSParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TSPASSParser.FormulaContext,i)


        def negation(self):
            return self.getTypedRuleContext(TSPASSParser.NegationContext,0)


        def atom(self):
            return self.getTypedRuleContext(TSPASSParser.AtomContext,0)


        def h_lpar(self):
            return self.getTypedRuleContext(TSPASSParser.H_lparContext,0)


        def disjunction(self):
            return self.getTypedRuleContext(TSPASSParser.DisjunctionContext,0)


        def btOperators(self):
            return self.getTypedRuleContext(TSPASSParser.BtOperatorsContext,0)


        def uQuant(self):
            return self.getTypedRuleContext(TSPASSParser.UQuantContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(TSPASSParser.H_rparContext,0)


        def equivalence(self):
            return self.getTypedRuleContext(TSPASSParser.EquivalenceContext,0)


        def utOperators(self):
            return self.getTypedRuleContext(TSPASSParser.UtOperatorsContext,0)


        def conjunction(self):
            return self.getTypedRuleContext(TSPASSParser.ConjunctionContext,0)


        def implication(self):
            return self.getTypedRuleContext(TSPASSParser.ImplicationContext,0)


        def getRuleIndex(self):
            return TSPASSParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitFormula(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TSPASSParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 75 
                self.variable()
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 76
                        self.match(self.NEWLINE) 
                    self.state = 81
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 2:
                self.state = 82 
                self.constants()
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 83
                        self.match(self.NEWLINE) 
                    self.state = 88
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 3:
                self.state = 89 
                self.atom()
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 90
                        self.match(self.NEWLINE) 
                    self.state = 95
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 4:
                self.state = 96 
                self.negation()
                self.state = 97 
                self.formula(0)
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 98
                        self.match(self.NEWLINE) 
                    self.state = 103
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 5:
                self.state = 104 
                self.uQuant()
                self.state = 105 
                self.formula(0)
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 106
                        self.match(self.NEWLINE) 
                    self.state = 111
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 6:
                self.state = 112 
                self.eQuant()
                self.state = 113 
                self.formula(0)
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 114
                        self.match(self.NEWLINE) 
                    self.state = 119
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 7:
                self.state = 120 
                self.utOperators()
                self.state = 121 
                self.formula(0)
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 122
                        self.match(self.NEWLINE) 
                    self.state = 127
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass

            elif la_ == 8:
                self.state = 128 
                self.h_lpar()
                self.state = 129 
                self.formula(0)
                self.state = 130 
                self.h_rpar()
                self.state = 134
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 131
                        self.match(self.NEWLINE) 
                    self.state = 136
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 182
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = TSPASSParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 139
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 143
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==TSPASSParser.NEWLINE:
                            self.state = 140
                            self.match(self.NEWLINE)
                            self.state = 145
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 146 
                        self.formula(2)
                        pass

                    elif la_ == 2:
                        localctx = TSPASSParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 147
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 151
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==TSPASSParser.NEWLINE:
                            self.state = 148
                            self.match(self.NEWLINE)
                            self.state = 153
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 158
                        token = self._input.LA(1)
                        if token in [self.T__24]:
                            self.state = 154 
                            self.conjunction()

                        elif token in [self.T__1]:
                            self.state = 155 
                            self.disjunction()

                        elif token in [self.T__11, self.T__10]:
                            self.state = 156 
                            self.implication()

                        elif token in [self.T__7, self.T__5]:
                            self.state = 157 
                            self.equivalence()

                        else:
                            raise NoViableAltException(self)

                        self.state = 163
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==TSPASSParser.NEWLINE:
                            self.state = 160
                            self.match(self.NEWLINE)
                            self.state = 165
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 166 
                        self.formula(0)
                        self.state = 170
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 167
                                self.match(self.NEWLINE) 
                            self.state = 172
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                        pass

                    elif la_ == 3:
                        localctx = TSPASSParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 173
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 174 
                        self.btOperators()
                        self.state = 175 
                        self.formula(0)
                        self.state = 179
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 176
                                self.match(self.NEWLINE) 
                            self.state = 181
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                        pass

             
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(TSPASSParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(TSPASSParser.H_rparContext,0)


        def constants(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSPASSParser.ConstantsContext)
            else:
                return self.getTypedRuleContext(TSPASSParser.ConstantsContext,i)


        def predicate(self):
            return self.getTypedRuleContext(TSPASSParser.PredicateContext,0)


        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TSPASSParser.VariableContext)
            else:
                return self.getTypedRuleContext(TSPASSParser.VariableContext,i)


        def getRuleIndex(self):
            return TSPASSParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitAtom(self)




    def atom(self):

        localctx = TSPASSParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187 
            self.predicate()
            self.state = 188 
            self.h_lpar()
            self.state = 191
            token = self._input.LA(1)
            if token in [self.ID]:
                self.state = 189 
                self.variable()

            elif token in [self.T__17, self.T__12]:
                self.state = 190 
                self.constants()

            else:
                raise NoViableAltException(self)

            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSPASSParser.T__23:
                self.state = 193
                self.match(self.T__23)
                self.state = 196
                token = self._input.LA(1)
                if token in [self.ID]:
                    self.state = 194 
                    self.variable()

                elif token in [self.T__17, self.T__12]:
                    self.state = 195 
                    self.constants()

                else:
                    raise NoViableAltException(self)

                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TSPASSParser.ID, 0)

        def getRuleIndex(self):
            return TSPASSParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = TSPASSParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TSPASSParser.ID, 0)

        def getRuleIndex(self):
            return TSPASSParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitVariable(self)




    def variable(self):

        localctx = TSPASSParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_constants

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterConstants(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitConstants(self)




    def constants(self):

        localctx = TSPASSParser.ConstantsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            _la = self._input.LA(1)
            if not(_la==TSPASSParser.T__17 or _la==TSPASSParser.T__12):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NegationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_negation

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitNegation(self)




    def negation(self):

        localctx = TSPASSParser.NegationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_negation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==TSPASSParser.T__21 or _la==TSPASSParser.T__2):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitConjunction(self)




    def conjunction(self):

        localctx = TSPASSParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(self.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitDisjunction(self)




    def disjunction(self):

        localctx = TSPASSParser.DisjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_disjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(self.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImplicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_implication

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterImplication(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitImplication(self)




    def implication(self):

        localctx = TSPASSParser.ImplicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_implication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==TSPASSParser.T__11 or _la==TSPASSParser.T__10):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EquivalenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_equivalence

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterEquivalence(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitEquivalence(self)




    def equivalence(self):

        localctx = TSPASSParser.EquivalenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_equivalence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==TSPASSParser.T__7 or _la==TSPASSParser.T__5):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UQuantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TSPASSParser.ID)
            else:
                return self.getToken(TSPASSParser.ID, i)

        def getRuleIndex(self):
            return TSPASSParser.RULE_uQuant

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterUQuant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitUQuant(self)




    def uQuant(self):

        localctx = TSPASSParser.UQuantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_uQuant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(self.T__0)
            self.state = 222
            self.match(self.T__22)
            self.state = 223
            self.match(self.ID)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSPASSParser.T__23:
                self.state = 224
                self.match(self.T__23)
                self.state = 225
                self.match(self.ID)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(self.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EQuantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TSPASSParser.ID)
            else:
                return self.getToken(TSPASSParser.ID, i)

        def getRuleIndex(self):
            return TSPASSParser.RULE_eQuant

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterEQuant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitEQuant(self)




    def eQuant(self):

        localctx = TSPASSParser.EQuantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_eQuant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(self.T__16)
            self.state = 234
            self.match(self.T__22)
            self.state = 235
            self.match(self.ID)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSPASSParser.T__23:
                self.state = 236
                self.match(self.T__23)
                self.state = 237
                self.match(self.ID)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
            self.match(self.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UtOperatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sometime(self):
            return self.getTypedRuleContext(TSPASSParser.SometimeContext,0)


        def always(self):
            return self.getTypedRuleContext(TSPASSParser.AlwaysContext,0)


        def snext(self):
            return self.getTypedRuleContext(TSPASSParser.SnextContext,0)


        def getRuleIndex(self):
            return TSPASSParser.RULE_utOperators

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterUtOperators(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitUtOperators(self)




    def utOperators(self):

        localctx = TSPASSParser.UtOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_utOperators)
        try:
            self.state = 248
            token = self._input.LA(1)
            if token in [self.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245 
                self.always()

            elif token in [self.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246 
                self.snext()

            elif token in [self.T__26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247 
                self.sometime()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BtOperatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unless(self):
            return self.getTypedRuleContext(TSPASSParser.UnlessContext,0)


        def until(self):
            return self.getTypedRuleContext(TSPASSParser.UntilContext,0)


        def getRuleIndex(self):
            return TSPASSParser.RULE_btOperators

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterBtOperators(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitBtOperators(self)




    def btOperators(self):

        localctx = TSPASSParser.BtOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_btOperators)
        try:
            self.state = 252
            token = self._input.LA(1)
            if token in [self.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250 
                self.until()

            elif token in [self.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251 
                self.unless()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlwaysContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_always

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterAlways(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitAlways(self)




    def always(self):

        localctx = TSPASSParser.AlwaysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_always)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(self.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SnextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_snext

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterSnext(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitSnext(self)




    def snext(self):

        localctx = TSPASSParser.SnextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_snext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(self.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SometimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_sometime

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterSometime(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitSometime(self)




    def sometime(self):

        localctx = TSPASSParser.SometimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sometime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(self.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UntilContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_until

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterUntil(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitUntil(self)




    def until(self):

        localctx = TSPASSParser.UntilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_until)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(self.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnlessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TSPASSParser.RULE_unless

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterUnless(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitUnless(self)




    def unless(self):

        localctx = TSPASSParser.UnlessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unless)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(self.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         



