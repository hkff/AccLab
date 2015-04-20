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
        buf.write("\u0103\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\7\fT\n\f\f\f")
        buf.write("\16\fW\13\f\3\f\3\f\3\f\7\f\\\n\f\f\f\16\f_\13\f\3\f\3")
        buf.write("\f\3\f\7\fd\n\f\f\f\16\fg\13\f\3\f\3\f\3\f\7\fl\n\f\f")
        buf.write("\f\16\fo\13\f\3\f\3\f\3\f\7\ft\n\f\f\f\16\fw\13\f\3\f")
        buf.write("\3\f\3\f\3\f\7\f}\n\f\f\f\16\f\u0080\13\f\5\f\u0082\n")
        buf.write("\f\3\f\3\f\7\f\u0086\n\f\f\f\16\f\u0089\13\f\3\f\3\f\3")
        buf.write("\f\7\f\u008e\n\f\f\f\16\f\u0091\13\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u0097\n\f\3\f\7\f\u009a\n\f\f\f\16\f\u009d\13\f\3\f")
        buf.write("\3\f\7\f\u00a1\n\f\f\f\16\f\u00a4\13\f\3\f\3\f\3\f\3\f")
        buf.write("\7\f\u00aa\n\f\f\f\16\f\u00ad\13\f\7\f\u00af\n\f\f\f\16")
        buf.write("\f\u00b2\13\f\3\r\3\r\3\r\3\r\5\r\u00b8\n\r\3\r\3\r\3")
        buf.write("\r\5\r\u00bd\n\r\7\r\u00bf\n\r\f\r\16\r\u00c2\13\r\3\r")
        buf.write("\3\r\5\r\u00c6\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u00dd\n\26\f\26\16\26\u00e0\13\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\7\27\u00e9\n\27\f")
        buf.write("\27\16\27\u00ec\13\27\3\27\3\27\3\30\3\30\3\30\5\30\u00f3")
        buf.write("\n\30\3\31\3\31\5\31\u00f7\n\31\3\32\3\32\3\33\3\33\3")
        buf.write("\34\3\34\3\35\3\35\3\36\3\36\3\36\2\3\26\37\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:\2")
        buf.write("\6\4\2\f\f\21\21\4\2\b\b\33\33\3\2\22\23\4\2\26\26\30")
        buf.write("\30\u0104\2<\3\2\2\2\4>\3\2\2\2\6@\3\2\2\2\bB\3\2\2\2")
        buf.write("\nD\3\2\2\2\fF\3\2\2\2\16H\3\2\2\2\20J\3\2\2\2\22L\3\2")
        buf.write("\2\2\24N\3\2\2\2\26\u0081\3\2\2\2\30\u00b3\3\2\2\2\32")
        buf.write("\u00c7\3\2\2\2\34\u00c9\3\2\2\2\36\u00cb\3\2\2\2 \u00cd")
        buf.write("\3\2\2\2\"\u00cf\3\2\2\2$\u00d1\3\2\2\2&\u00d3\3\2\2\2")
        buf.write("(\u00d5\3\2\2\2*\u00d7\3\2\2\2,\u00e3\3\2\2\2.\u00f2\3")
        buf.write("\2\2\2\60\u00f6\3\2\2\2\62\u00f8\3\2\2\2\64\u00fa\3\2")
        buf.write("\2\2\66\u00fc\3\2\2\28\u00fe\3\2\2\2:\u0100\3\2\2\2<=")
        buf.write("\7\32\2\2=\3\3\2\2\2>?\7\17\2\2?\5\3\2\2\2@A\7\t\2\2A")
        buf.write("\7\3\2\2\2BC\7\24\2\2C\t\3\2\2\2DE\7\7\2\2E\13\3\2\2\2")
        buf.write("FG\7\4\2\2G\r\3\2\2\2HI\7\25\2\2I\17\3\2\2\2JK\7\n\2\2")
        buf.write("K\21\3\2\2\2LM\7\31\2\2M\23\3\2\2\2NO\5\26\f\2O\25\3\2")
        buf.write("\2\2PQ\b\f\1\2QU\5\30\r\2RT\7 \2\2SR\3\2\2\2TW\3\2\2\2")
        buf.write("US\3\2\2\2UV\3\2\2\2V\u0082\3\2\2\2WU\3\2\2\2XY\5 \21")
        buf.write("\2Y]\5\26\f\2Z\\\7 \2\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2")
        buf.write("]^\3\2\2\2^\u0082\3\2\2\2_]\3\2\2\2`a\5*\26\2ae\5\26\f")
        buf.write("\2bd\7 \2\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\u0082")
        buf.write("\3\2\2\2ge\3\2\2\2hi\5,\27\2im\5\26\f\2jl\7 \2\2kj\3\2")
        buf.write("\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\u0082\3\2\2\2om\3")
        buf.write("\2\2\2pq\5.\30\2qu\5\26\f\2rt\7 \2\2sr\3\2\2\2tw\3\2\2")
        buf.write("\2us\3\2\2\2uv\3\2\2\2v\u0082\3\2\2\2wu\3\2\2\2xy\5\6")
        buf.write("\4\2yz\5\26\f\2z~\5\b\5\2{}\7 \2\2|{\3\2\2\2}\u0080\3")
        buf.write("\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0082\3\2\2\2\u0080")
        buf.write("~\3\2\2\2\u0081P\3\2\2\2\u0081X\3\2\2\2\u0081`\3\2\2\2")
        buf.write("\u0081h\3\2\2\2\u0081p\3\2\2\2\u0081x\3\2\2\2\u0082\u00b0")
        buf.write("\3\2\2\2\u0083\u0087\f\3\2\2\u0084\u0086\7 \2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3")
        buf.write("\2\2\2\u008a\u00af\5\26\f\4\u008b\u008f\f\n\2\2\u008c")
        buf.write("\u008e\7 \2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2")
        buf.write("\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0096\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0092\u0097\5\"\22\2\u0093")
        buf.write("\u0097\5$\23\2\u0094\u0097\5&\24\2\u0095\u0097\5(\25\2")
        buf.write("\u0096\u0092\3\2\2\2\u0096\u0093\3\2\2\2\u0096\u0094\3")
        buf.write("\2\2\2\u0096\u0095\3\2\2\2\u0097\u009b\3\2\2\2\u0098\u009a")
        buf.write("\7 \2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u00a2\5\26\f\2\u009f\u00a1")
        buf.write("\7 \2\2\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00af\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a5\u00a6\f\6\2\2\u00a6\u00a7\5")
        buf.write("\60\31\2\u00a7\u00ab\5\26\f\2\u00a8\u00aa\7 \2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2")
        buf.write("\u00ab\u00ac\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ae\u0083\3\2\2\2\u00ae\u008b\3\2\2\2\u00ae\u00a5")
        buf.write("\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\27\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3")
        buf.write("\u00c5\5\32\16\2\u00b4\u00b7\5\6\4\2\u00b5\u00b8\5\34")
        buf.write("\17\2\u00b6\u00b8\5\36\20\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\u00c0\3\2\2\2\u00b9\u00bc\7\6\2\2")
        buf.write("\u00ba\u00bd\5\34\17\2\u00bb\u00bd\5\36\20\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00bf\3\2\2\2\u00be")
        buf.write("\u00b9\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3")
        buf.write("\2\2\2\u00c3\u00c4\5\b\5\2\u00c4\u00c6\3\2\2\2\u00c5\u00b4")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\31\3\2\2\2\u00c7\u00c8")
        buf.write("\7\36\2\2\u00c8\33\3\2\2\2\u00c9\u00ca\7\36\2\2\u00ca")
        buf.write("\35\3\2\2\2\u00cb\u00cc\t\2\2\2\u00cc\37\3\2\2\2\u00cd")
        buf.write("\u00ce\t\3\2\2\u00ce!\3\2\2\2\u00cf\u00d0\7\5\2\2\u00d0")
        buf.write("#\3\2\2\2\u00d1\u00d2\7\34\2\2\u00d2%\3\2\2\2\u00d3\u00d4")
        buf.write("\t\4\2\2\u00d4\'\3\2\2\2\u00d5\u00d6\t\5\2\2\u00d6)\3")
        buf.write("\2\2\2\u00d7\u00d8\7\35\2\2\u00d8\u00d9\7\7\2\2\u00d9")
        buf.write("\u00de\7\36\2\2\u00da\u00db\7\6\2\2\u00db\u00dd\7\36\2")
        buf.write("\2\u00dc\u00da\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0")
        buf.write("\u00de\3\2\2\2\u00e1\u00e2\7\4\2\2\u00e2+\3\2\2\2\u00e3")
        buf.write("\u00e4\7\r\2\2\u00e4\u00e5\7\7\2\2\u00e5\u00ea\7\36\2")
        buf.write("\2\u00e6\u00e7\7\6\2\2\u00e7\u00e9\7\36\2\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ea\3\2\2\2")
        buf.write("\u00ed\u00ee\7\4\2\2\u00ee-\3\2\2\2\u00ef\u00f3\5\62\32")
        buf.write("\2\u00f0\u00f3\5\64\33\2\u00f1\u00f3\5\66\34\2\u00f2\u00ef")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3")
        buf.write("/\3\2\2\2\u00f4\u00f7\58\35\2\u00f5\u00f7\5:\36\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\61\3\2\2\2\u00f8")
        buf.write("\u00f9\7\27\2\2\u00f9\63\3\2\2\2\u00fa\u00fb\7\20\2\2")
        buf.write("\u00fb\65\3\2\2\2\u00fc\u00fd\7\3\2\2\u00fd\67\3\2\2\2")
        buf.write("\u00fe\u00ff\7\16\2\2\u00ff9\3\2\2\2\u0100\u0101\7\13")
        buf.write("\2\2\u0101;\3\2\2\2\31U]emu~\u0081\u0087\u008f\u0096\u009b")
        buf.write("\u00a2\u00ab\u00ae\u00b0\u00b7\u00bc\u00c0\u00c5\u00de")
        buf.write("\u00ea\u00f2\u00f6")
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
    RULE_program = 9
    RULE_formula = 10
    RULE_atom = 11
    RULE_predicate = 12
    RULE_variable = 13
    RULE_constants = 14
    RULE_negation = 15
    RULE_conjunction = 16
    RULE_disjunction = 17
    RULE_implication = 18
    RULE_equivalence = 19
    RULE_uQuant = 20
    RULE_eQuant = 21
    RULE_utOperators = 22
    RULE_btOperators = 23
    RULE_always = 24
    RULE_snext = 25
    RULE_sometime = 26
    RULE_until = 27
    RULE_unless = 28

    ruleNames =  [ "x", "y", "h_lpar", "h_rpar", "h_lbar", "h_rbar", "h_dot", 
                   "h_colon", "h_equal", "program", "formula", "atom", "predicate", 
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
            self.state = 58
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
            self.state = 60
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
            self.state = 62
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
            self.state = 64
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
            self.state = 66
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
            self.state = 68
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
            self.state = 70
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
            self.state = 72
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
            self.state = 74
            self.match(self.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(TSPASSParser.FormulaContext,0)


        def getRuleIndex(self):
            return TSPASSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, TSPASSListener ):
                listener.exitProgram(self)




    def program(self):

        localctx = TSPASSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76 
            self.formula(0)
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            token = self._input.LA(1)
            if token in [self.ID]:
                self.state = 79 
                self.atom()
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 80
                        self.match(self.NEWLINE) 
                    self.state = 85
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)


            elif token in [self.T__21, self.T__2]:
                self.state = 86 
                self.negation()
                self.state = 87 
                self.formula(0)
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 88
                        self.match(self.NEWLINE) 
                    self.state = 93
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)


            elif token in [self.T__0]:
                self.state = 94 
                self.uQuant()
                self.state = 95 
                self.formula(0)
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 96
                        self.match(self.NEWLINE) 
                    self.state = 101
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)


            elif token in [self.T__16]:
                self.state = 102 
                self.eQuant()
                self.state = 103 
                self.formula(0)
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 104
                        self.match(self.NEWLINE) 
                    self.state = 109
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)


            elif token in [self.T__26, self.T__13, self.T__6]:
                self.state = 110 
                self.utOperators()
                self.state = 111 
                self.formula(0)
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 112
                        self.match(self.NEWLINE) 
                    self.state = 117
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)


            elif token in [self.T__20]:
                self.state = 118 
                self.h_lpar()
                self.state = 119 
                self.formula(0)
                self.state = 120 
                self.h_rpar()
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 121
                        self.match(self.NEWLINE) 
                    self.state = 126
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)


            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 174
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 172
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = TSPASSParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 129
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 133
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==TSPASSParser.NEWLINE:
                            self.state = 130
                            self.match(self.NEWLINE)
                            self.state = 135
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 136 
                        self.formula(2)
                        pass

                    elif la_ == 2:
                        localctx = TSPASSParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 137
                        if not self.precpred(self._ctx, 8):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 141
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==TSPASSParser.NEWLINE:
                            self.state = 138
                            self.match(self.NEWLINE)
                            self.state = 143
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 148
                        token = self._input.LA(1)
                        if token in [self.T__24]:
                            self.state = 144 
                            self.conjunction()

                        elif token in [self.T__1]:
                            self.state = 145 
                            self.disjunction()

                        elif token in [self.T__11, self.T__10]:
                            self.state = 146 
                            self.implication()

                        elif token in [self.T__7, self.T__5]:
                            self.state = 147 
                            self.equivalence()

                        else:
                            raise NoViableAltException(self)

                        self.state = 153
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==TSPASSParser.NEWLINE:
                            self.state = 150
                            self.match(self.NEWLINE)
                            self.state = 155
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 156 
                        self.formula(0)
                        self.state = 160
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 157
                                self.match(self.NEWLINE) 
                            self.state = 162
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                        pass

                    elif la_ == 3:
                        localctx = TSPASSParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 163
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 164 
                        self.btOperators()
                        self.state = 165 
                        self.formula(0)
                        self.state = 169
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 166
                                self.match(self.NEWLINE) 
                            self.state = 171
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                        pass

             
                self.state = 176
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177 
            self.predicate()
            self.state = 195
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 178 
                self.h_lpar()
                self.state = 181
                token = self._input.LA(1)
                if token in [self.ID]:
                    self.state = 179 
                    self.variable()

                elif token in [self.T__17, self.T__12]:
                    self.state = 180 
                    self.constants()

                else:
                    raise NoViableAltException(self)

                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TSPASSParser.T__23:
                    self.state = 183
                    self.match(self.T__23)
                    self.state = 186
                    token = self._input.LA(1)
                    if token in [self.ID]:
                        self.state = 184 
                        self.variable()

                    elif token in [self.T__17, self.T__12]:
                        self.state = 185 
                        self.constants()

                    else:
                        raise NoViableAltException(self)

                    self.state = 192
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 193 
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
        self.enterRule(localctx, 24, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
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
        self.enterRule(localctx, 26, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
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
        self.enterRule(localctx, 28, self.RULE_constants)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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
        self.enterRule(localctx, 30, self.RULE_negation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
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
        self.enterRule(localctx, 32, self.RULE_conjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
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
        self.enterRule(localctx, 34, self.RULE_disjunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
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
        self.enterRule(localctx, 36, self.RULE_implication)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
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
        self.enterRule(localctx, 38, self.RULE_equivalence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
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
        self.enterRule(localctx, 40, self.RULE_uQuant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(self.T__0)
            self.state = 214
            self.match(self.T__22)
            self.state = 215
            self.match(self.ID)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSPASSParser.T__23:
                self.state = 216
                self.match(self.T__23)
                self.state = 217
                self.match(self.ID)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
        self.enterRule(localctx, 42, self.RULE_eQuant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(self.T__16)
            self.state = 226
            self.match(self.T__22)
            self.state = 227
            self.match(self.ID)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TSPASSParser.T__23:
                self.state = 228
                self.match(self.T__23)
                self.state = 229
                self.match(self.ID)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
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
        self.enterRule(localctx, 44, self.RULE_utOperators)
        try:
            self.state = 240
            token = self._input.LA(1)
            if token in [self.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237 
                self.always()

            elif token in [self.T__13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238 
                self.snext()

            elif token in [self.T__26]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239 
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
        self.enterRule(localctx, 46, self.RULE_btOperators)
        try:
            self.state = 244
            token = self._input.LA(1)
            if token in [self.T__15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242 
                self.until()

            elif token in [self.T__18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243 
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
        self.enterRule(localctx, 48, self.RULE_always)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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
        self.enterRule(localctx, 50, self.RULE_snext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
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
        self.enterRule(localctx, 52, self.RULE_sometime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
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
        self.enterRule(localctx, 54, self.RULE_until)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
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
        self.enterRule(localctx, 56, self.RULE_unless)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
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
        self._predicates[10] = self.formula_sempred
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
         



