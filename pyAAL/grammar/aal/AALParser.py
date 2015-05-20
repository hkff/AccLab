# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .AALListener import AALListener
else:
    from AALListener import AALListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3N")
        buf.write("\u02f7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\5\17\u00c1\n")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u00d9\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\5\33\u00e3\n\33\3\34\3\34\3\34\3\34\5\34\u00e9")
        buf.write("\n\34\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u00f1\n\36\3")
        buf.write("\37\3\37\3\37\3\37\7\37\u00f7\n\37\f\37\16\37\u00fa\13")
        buf.write("\37\3\37\3\37\3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\7!\u0109")
        buf.write("\n!\f!\16!\u010c\13!\3\"\3\"\3\"\3\"\3\"\5\"\u0113\n\"")
        buf.write("\3\"\5\"\u0116\n\"\3#\3#\3#\3#\3#\7#\u011d\n#\f#\16#\u0120")
        buf.write("\13#\3#\3#\3#\3#\3#\3#\3#\5#\u0129\n#\5#\u012b\n#\3$\3")
        buf.write("$\3$\3$\3$\7$\u0132\n$\f$\16$\u0135\13$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\5$\u013e\n$\3$\3$\5$\u0142\n$\3%\3%\3%\7%\u0147")
        buf.write("\n%\f%\16%\u014a\13%\3%\3%\3&\3&\3&\7&\u0151\n&\f&\16")
        buf.write("&\u0154\13&\3&\3&\3\'\3\'\3\'\3\'\3\'\7\'\u015d\n\'\f")
        buf.write("\'\16\'\u0160\13\'\3\'\3\'\5\'\u0164\n\'\3\'\3\'\3\'\7")
        buf.write("\'\u0169\n\'\f\'\16\'\u016c\13\'\3\'\3\'\5\'\u0170\n\'")
        buf.write("\3(\3(\3(\7(\u0175\n(\f(\16(\u0178\13(\3)\3)\3)\7)\u017d")
        buf.write("\n)\f)\16)\u0180\13)\3)\3)\3*\3*\3*\5*\u0187\n*\3*\5*")
        buf.write("\u018a\n*\3*\5*\u018d\n*\3+\3+\3+\7+\u0192\n+\f+\16+\u0195")
        buf.write("\13+\3+\3+\3,\3,\3,\7,\u019c\n,\f,\16,\u019f\13,\3,\3")
        buf.write(",\3-\3-\3-\7-\u01a6\n-\f-\16-\u01a9\13-\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u01b8\n\61")
        buf.write("\3\61\3\61\5\61\u01bc\n\61\5\61\u01be\n\61\3\61\3\61\5")
        buf.write("\61\u01c2\n\61\5\61\u01c4\n\61\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01dc\n\65\3\65\3")
        buf.write("\65\3\65\3\65\7\65\u01e2\n\65\f\65\16\65\u01e5\13\65\3")
        buf.write("\66\3\66\3\67\3\67\3\67\38\38\38\38\38\39\39\3:\3:\3;")
        buf.write("\3;\3<\3<\7<\u01f9\n<\f<\16<\u01fc\13<\3<\3<\3=\3=\3>")
        buf.write("\3>\3>\3>\5>\u0206\n>\3?\3?\3@\3@\3@\5@\u020d\n@\3A\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\5A\u021d\nA\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\5B\u0226\nB\3C\3C\3C\5C\u022b\nC\3C\3")
        buf.write("C\3C\7C\u0230\nC\fC\16C\u0233\13C\3D\5D\u0236\nD\3D\3")
        buf.write("D\3E\3E\3E\5E\u023d\nE\3E\3E\3F\3F\3F\3F\3F\5F\u0246\n")
        buf.write("F\3F\3F\5F\u024a\nF\3F\3F\5F\u024e\nF\3F\3F\5F\u0252\n")
        buf.write("F\3F\3F\3F\7F\u0257\nF\fF\16F\u025a\13F\3F\3F\5F\u025e")
        buf.write("\nF\3G\3G\3H\3H\3H\3H\3H\3H\3H\7H\u0269\nH\fH\16H\u026c")
        buf.write("\13H\3I\3I\3I\5I\u0271\nI\3I\3I\3I\3I\3J\3J\7J\u0279\n")
        buf.write("J\fJ\16J\u027c\13J\3J\3J\3K\3K\3K\3K\7K\u0284\nK\fK\16")
        buf.write("K\u0287\13K\3K\3K\3L\3L\3L\3M\3M\3M\3N\3N\3N\5N\u0294")
        buf.write("\nN\3N\3N\3N\3N\3O\3O\3P\3P\3P\3P\7P\u02a0\nP\fP\16P\u02a3")
        buf.write("\13P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02ae\nQ\3Q\5Q\u02b1")
        buf.write("\nQ\3R\3R\3R\7R\u02b6\nR\fR\16R\u02b9\13R\3R\3R\7R\u02bd")
        buf.write("\nR\fR\16R\u02c0\13R\3R\3R\3R\7R\u02c5\nR\fR\16R\u02c8")
        buf.write("\13R\3R\3R\3R\3R\7R\u02ce\nR\fR\16R\u02d1\13R\5R\u02d3")
        buf.write("\nR\3R\3R\7R\u02d7\nR\fR\16R\u02da\13R\3R\3R\3R\7R\u02df")
        buf.write("\nR\fR\16R\u02e2\13R\3R\3R\7R\u02e6\nR\fR\16R\u02e9\13")
        buf.write("R\3R\3R\7R\u02ed\nR\fR\16R\u02f0\13R\7R\u02f2\nR\fR\16")
        buf.write("R\u02f5\13R\3R\2\6h\u0084\u008e\u00a2S\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a0\u00a2\2\n\3\2+,\4\2\30\32&\'")
        buf.write("\3\2)*\3\2\30\31\3\2!%\3\2\37 \3\2;=\3\2IL\u0301\2\u00a4")
        buf.write("\3\2\2\2\4\u00a6\3\2\2\2\6\u00a8\3\2\2\2\b\u00aa\3\2\2")
        buf.write("\2\n\u00ac\3\2\2\2\f\u00ae\3\2\2\2\16\u00b0\3\2\2\2\20")
        buf.write("\u00b2\3\2\2\2\22\u00b4\3\2\2\2\24\u00b6\3\2\2\2\26\u00b8")
        buf.write("\3\2\2\2\30\u00ba\3\2\2\2\32\u00bc\3\2\2\2\34\u00c0\3")
        buf.write("\2\2\2\36\u00c2\3\2\2\2 \u00c4\3\2\2\2\"\u00c6\3\2\2\2")
        buf.write("$\u00c8\3\2\2\2&\u00ca\3\2\2\2(\u00cc\3\2\2\2*\u00ce\3")
        buf.write("\2\2\2,\u00d0\3\2\2\2.\u00d2\3\2\2\2\60\u00d8\3\2\2\2")
        buf.write("\62\u00da\3\2\2\2\64\u00e2\3\2\2\2\66\u00e8\3\2\2\28\u00ea")
        buf.write("\3\2\2\2:\u00ec\3\2\2\2<\u00f2\3\2\2\2>\u00fd\3\2\2\2")
        buf.write("@\u010a\3\2\2\2B\u0112\3\2\2\2D\u0117\3\2\2\2F\u012c\3")
        buf.write("\2\2\2H\u0143\3\2\2\2J\u014d\3\2\2\2L\u0157\3\2\2\2N\u0171")
        buf.write("\3\2\2\2P\u0179\3\2\2\2R\u0183\3\2\2\2T\u018e\3\2\2\2")
        buf.write("V\u0198\3\2\2\2X\u01a2\3\2\2\2Z\u01ac\3\2\2\2\\\u01ae")
        buf.write("\3\2\2\2^\u01b0\3\2\2\2`\u01b2\3\2\2\2b\u01c7\3\2\2\2")
        buf.write("d\u01c9\3\2\2\2f\u01cc\3\2\2\2h\u01db\3\2\2\2j\u01e6\3")
        buf.write("\2\2\2l\u01e8\3\2\2\2n\u01eb\3\2\2\2p\u01f0\3\2\2\2r\u01f2")
        buf.write("\3\2\2\2t\u01f4\3\2\2\2v\u01f6\3\2\2\2x\u01ff\3\2\2\2")
        buf.write("z\u0201\3\2\2\2|\u0207\3\2\2\2~\u0209\3\2\2\2\u0080\u021c")
        buf.write("\3\2\2\2\u0082\u0225\3\2\2\2\u0084\u022a\3\2\2\2\u0086")
        buf.write("\u0235\3\2\2\2\u0088\u0239\3\2\2\2\u008a\u0240\3\2\2\2")
        buf.write("\u008c\u025f\3\2\2\2\u008e\u0261\3\2\2\2\u0090\u026d\3")
        buf.write("\2\2\2\u0092\u0276\3\2\2\2\u0094\u027f\3\2\2\2\u0096\u028a")
        buf.write("\3\2\2\2\u0098\u028d\3\2\2\2\u009a\u0290\3\2\2\2\u009c")
        buf.write("\u0299\3\2\2\2\u009e\u029b\3\2\2\2\u00a0\u02b0\3\2\2\2")
        buf.write("\u00a2\u02d2\3\2\2\2\u00a4\u00a5\7\t\2\2\u00a5\3\3\2\2")
        buf.write("\2\u00a6\u00a7\7\5\2\2\u00a7\5\3\2\2\2\u00a8\u00a9\7\6")
        buf.write("\2\2\u00a9\7\3\2\2\2\u00aa\u00ab\7\3\2\2\u00ab\t\3\2\2")
        buf.write("\2\u00ac\u00ad\7\13\2\2\u00ad\13\3\2\2\2\u00ae\u00af\7")
        buf.write("\16\2\2\u00af\r\3\2\2\2\u00b0\u00b1\7\4\2\2\u00b1\17\3")
        buf.write("\2\2\2\u00b2\u00b3\7\b\2\2\u00b3\21\3\2\2\2\u00b4\u00b5")
        buf.write("\7\r\2\2\u00b5\23\3\2\2\2\u00b6\u00b7\7\n\2\2\u00b7\25")
        buf.write("\3\2\2\2\u00b8\u00b9\7\f\2\2\u00b9\27\3\2\2\2\u00ba\u00bb")
        buf.write("\7?\2\2\u00bb\31\3\2\2\2\u00bc\u00bd\5\66\34\2\u00bd\33")
        buf.write("\3\2\2\2\u00be\u00c1\5&\24\2\u00bf\u00c1\5\62\32\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\35\3\2\2\2\u00c2")
        buf.write("\u00c3\7?\2\2\u00c3\37\3\2\2\2\u00c4\u00c5\7?\2\2\u00c5")
        buf.write("!\3\2\2\2\u00c6\u00c7\7?\2\2\u00c7#\3\2\2\2\u00c8\u00c9")
        buf.write("\7?\2\2\u00c9%\3\2\2\2\u00ca\u00cb\7D\2\2\u00cb\'\3\2")
        buf.write("\2\2\u00cc\u00cd\7?\2\2\u00cd)\3\2\2\2\u00ce\u00cf\7?")
        buf.write("\2\2\u00cf+\3\2\2\2\u00d0\u00d1\7?\2\2\u00d1-\3\2\2\2")
        buf.write("\u00d2\u00d3\7?\2\2\u00d3/\3\2\2\2\u00d4\u00d5\7E\2\2")
        buf.write("\u00d5\u00d9\7A\2\2\u00d6\u00d7\7F\2\2\u00d7\u00d9\7A")
        buf.write("\2\2\u00d8\u00d4\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\61")
        buf.write("\3\2\2\2\u00da\u00db\7@\2\2\u00db\u00dc\7@\2\2\u00dc\u00dd")
        buf.write("\5\20\t\2\u00dd\u00de\7@\2\2\u00de\u00df\7@\2\2\u00df")
        buf.write("\63\3\2\2\2\u00e0\u00e3\5\66\34\2\u00e1\u00e3\5:\36\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\65\3\2")
        buf.write("\2\2\u00e4\u00e9\7@\2\2\u00e5\u00e6\7\17\2\2\u00e6\u00e7")
        buf.write("\7D\2\2\u00e7\u00e9\7\17\2\2\u00e8\u00e4\3\2\2\2\u00e8")
        buf.write("\u00e5\3\2\2\2\u00e9\67\3\2\2\2\u00ea\u00eb\7?\2\2\u00eb")
        buf.write("9\3\2\2\2\u00ec\u00f0\7?\2\2\u00ed\u00ee\5\20\t\2\u00ee")
        buf.write("\u00ef\58\35\2\u00ef\u00f1\3\2\2\2\u00f0\u00ed\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1;\3\2\2\2\u00f2\u00f3\7\7\2")
        buf.write("\2\u00f3\u00f4\7?\2\2\u00f4\u00f8\5\2\2\2\u00f5\u00f7")
        buf.write("\7?\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fb\u00fc\5\4\3\2\u00fc=\3\2\2")
        buf.write("\2\u00fd\u00fe\5@!\2\u00fe?\3\2\2\2\u00ff\u0109\5`\61")
        buf.write("\2\u0100\u0109\5B\"\2\u0101\u0109\5\60\31\2\u0102\u0109")
        buf.write("\5\u0090I\2\u0103\u0109\5\u0094K\2\u0104\u0109\5\u0098")
        buf.write("M\2\u0105\u0109\5\u009aN\2\u0106\u0109\5\u009eP\2\u0107")
        buf.write("\u0109\5\u0096L\2\u0108\u00ff\3\2\2\2\u0108\u0100\3\2")
        buf.write("\2\2\u0108\u0101\3\2\2\2\u0108\u0102\3\2\2\2\u0108\u0103")
        buf.write("\3\2\2\2\u0108\u0104\3\2\2\2\u0108\u0105\3\2\2\2\u0108")
        buf.write("\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010bA\3\2\2")
        buf.write("\2\u010c\u010a\3\2\2\2\u010d\u0113\5D#\2\u010e\u0113\5")
        buf.write("L\'\2\u010f\u0113\5F$\2\u0110\u0113\5R*\2\u0111\u0113")
        buf.write("\5N(\2\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2\u0112\u010f")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113")
        buf.write("\u0115\3\2\2\2\u0114\u0116\7A\2\2\u0115\u0114\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116C\3\2\2\2\u0117\u0118\7\21\2")
        buf.write("\2\u0118\u012a\5\36\20\2\u0119\u011a\7\25\2\2\u011a\u011e")
        buf.write("\5\2\2\2\u011b\u011d\5Z.\2\u011c\u011b\3\2\2\2\u011d\u0120")
        buf.write("\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f")
        buf.write("\u0121\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0128\5\4\3\2")
        buf.write("\u0122\u0123\5H%\2\u0123\u0124\5J&\2\u0124\u0129\3\2\2")
        buf.write("\2\u0125\u0126\5J&\2\u0126\u0127\5H%\2\u0127\u0129\3\2")
        buf.write("\2\2\u0128\u0122\3\2\2\2\u0128\u0125\3\2\2\2\u0129\u012b")
        buf.write("\3\2\2\2\u012a\u0119\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("E\3\2\2\2\u012c\u012d\7\22\2\2\u012d\u012e\5$\23\2\u012e")
        buf.write("\u012f\7\25\2\2\u012f\u0133\5\2\2\2\u0130\u0132\5^\60")
        buf.write("\2\u0131\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0136\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0136\u013d\5\4\3\2\u0137\u0138\5H%\2\u0138")
        buf.write("\u0139\5J&\2\u0139\u013e\3\2\2\2\u013a\u013b\5J&\2\u013b")
        buf.write("\u013c\5H%\2\u013c\u013e\3\2\2\2\u013d\u0137\3\2\2\2\u013d")
        buf.write("\u013a\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0141\3\2\2\2")
        buf.write("\u013f\u0140\7-\2\2\u0140\u0142\5\36\20\2\u0141\u013f")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142G\3\2\2\2\u0143\u0144")
        buf.write("\7.\2\2\u0144\u0148\5\2\2\2\u0145\u0147\5*\26\2\u0146")
        buf.write("\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014b\u014c\5\4\3\2\u014cI\3\2\2\2\u014d\u014e")
        buf.write("\7/\2\2\u014e\u0152\5\2\2\2\u014f\u0151\5*\26\2\u0150")
        buf.write("\u014f\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0152\u0153\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0152\3")
        buf.write("\2\2\2\u0155\u0156\5\4\3\2\u0156K\3\2\2\2\u0157\u0158")
        buf.write("\7\20\2\2\u0158\u0163\5*\26\2\u0159\u015a\7\25\2\2\u015a")
        buf.write("\u015e\5\2\2\2\u015b\u015d\5\\/\2\u015c\u015b\3\2\2\2")
        buf.write("\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162")
        buf.write("\5\4\3\2\u0162\u0164\3\2\2\2\u0163\u0159\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u016f\3\2\2\2\u0165\u0166\7\60\2")
        buf.write("\2\u0166\u016a\5\2\2\2\u0167\u0169\5(\25\2\u0168\u0167")
        buf.write("\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016d\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016d\u016e\5\4\3\2\u016e\u0170\3\2\2\2\u016f\u0165\3")
        buf.write("\2\2\2\u016f\u0170\3\2\2\2\u0170M\3\2\2\2\u0171\u0172")
        buf.write("\5 \21\2\u0172\u0176\5\"\22\2\u0173\u0175\5P)\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177O\3\2\2\2\u0178\u0176\3\2\2")
        buf.write("\2\u0179\u017a\5.\30\2\u017a\u017e\5\2\2\2\u017b\u017d")
        buf.write("\7?\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0181\u0182\5\4\3\2\u0182Q\3\2\2")
        buf.write("\2\u0183\u0184\7\24\2\2\u0184\u0186\7?\2\2\u0185\u0187")
        buf.write("\5T+\2\u0186\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189")
        buf.write("\3\2\2\2\u0188\u018a\5V,\2\u0189\u0188\3\2\2\2\u0189\u018a")
        buf.write("\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u018d\5X-\2\u018c\u018b")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018dS\3\2\2\2\u018e\u018f")
        buf.write("\7\61\2\2\u018f\u0193\5\2\2\2\u0190\u0192\7?\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0193\u0194\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193\3")
        buf.write("\2\2\2\u0196\u0197\5\4\3\2\u0197U\3\2\2\2\u0198\u0199")
        buf.write("\7\62\2\2\u0199\u019d\5\2\2\2\u019a\u019c\7?\2\2\u019b")
        buf.write("\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2")
        buf.write("\u019d\u019e\3\2\2\2\u019e\u01a0\3\2\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u01a0\u01a1\5\4\3\2\u01a1W\3\2\2\2\u01a2\u01a3")
        buf.write("\7\63\2\2\u01a3\u01a7\5\2\2\2\u01a4\u01a6\7?\2\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3")
        buf.write("\2\2\2\u01aa\u01ab\5\4\3\2\u01abY\3\2\2\2\u01ac\u01ad")
        buf.write("\7?\2\2\u01ad[\3\2\2\2\u01ae\u01af\7?\2\2\u01af]\3\2\2")
        buf.write("\2\u01b0\u01b1\7?\2\2\u01b1_\3\2\2\2\u01b2\u01b3\7\23")
        buf.write("\2\2\u01b3\u01b4\5,\27\2\u01b4\u01b5\5\2\2\2\u01b5\u01b7")
        buf.write("\5b\62\2\u01b6\u01b8\7A\2\2\u01b7\u01b6\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01bd\3\2\2\2\u01b9\u01bb\5d\63\2")
        buf.write("\u01ba\u01bc\7A\2\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01b9\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01c3\3\2\2\2\u01bf\u01c1\5f\64\2\u01c0")
        buf.write("\u01c2\7A\2\2\u01c1\u01c0\3\2\2\2\u01c1\u01c2\3\2\2\2")
        buf.write("\u01c2\u01c4\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c6\5\4\3\2\u01c6a")
        buf.write("\3\2\2\2\u01c7\u01c8\5h\65\2\u01c8c\3\2\2\2\u01c9\u01ca")
        buf.write("\7\26\2\2\u01ca\u01cb\5b\62\2\u01cbe\3\2\2\2\u01cc\u01cd")
        buf.write("\7\27\2\2\u01cd\u01ce\5b\62\2\u01ceg\3\2\2\2\u01cf\u01d0")
        buf.write("\b\65\1\2\u01d0\u01dc\5j\66\2\u01d1\u01dc\5l\67\2\u01d2")
        buf.write("\u01dc\5n8\2\u01d3\u01dc\5p9\2\u01d4\u01dc\5r:\2\u01d5")
        buf.write("\u01dc\5t;\2\u01d6\u01dc\5v<\2\u01d7\u01d8\5\2\2\2\u01d8")
        buf.write("\u01d9\5h\65\2\u01d9\u01da\5\4\3\2\u01da\u01dc\3\2\2\2")
        buf.write("\u01db\u01cf\3\2\2\2\u01db\u01d1\3\2\2\2\u01db\u01d2\3")
        buf.write("\2\2\2\u01db\u01d3\3\2\2\2\u01db\u01d4\3\2\2\2\u01db\u01d5")
        buf.write("\3\2\2\2\u01db\u01d6\3\2\2\2\u01db\u01d7\3\2\2\2\u01dc")
        buf.write("\u01e3\3\2\2\2\u01dd\u01de\f\7\2\2\u01de\u01df\5|?\2\u01df")
        buf.write("\u01e0\5h\65\b\u01e0\u01e2\3\2\2\2\u01e1\u01dd\3\2\2\2")
        buf.write("\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3")
        buf.write("\2\2\2\u01e4i\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e7")
        buf.write("\5\u008aF\2\u01e7k\3\2\2\2\u01e8\u01e9\7\35\2\2\u01e9")
        buf.write("\u01ea\5h\65\2\u01eam\3\2\2\2\u01eb\u01ec\5\u008cG\2\u01ec")
        buf.write("\u01ed\5\2\2\2\u01ed\u01ee\5h\65\2\u01ee\u01ef\5\4\3\2")
        buf.write("\u01efo\3\2\2\2\u01f0\u01f1\5\u0084C\2\u01f1q\3\2\2\2")
        buf.write("\u01f2\u01f3\5~@\2\u01f3s\3\2\2\2\u01f4\u01f5\5\u0080")
        buf.write("A\2\u01f5u\3\2\2\2\u01f6\u01fa\5z>\2\u01f7\u01f9\5z>\2")
        buf.write("\u01f8\u01f7\3\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3")
        buf.write("\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fd\u01fe\5h\65\2\u01few\3\2\2\2\u01ff\u0200")
        buf.write("\t\2\2\2\u0200y\3\2\2\2\u0201\u0202\5x=\2\u0202\u0205")
        buf.write("\5:\36\2\u0203\u0204\7\36\2\2\u0204\u0206\5\u0084C\2\u0205")
        buf.write("\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206{\3\2\2\2\u0207")
        buf.write("\u0208\t\3\2\2\u0208}\3\2\2\2\u0209\u020a\t\4\2\2\u020a")
        buf.write("\u020c\5\u008aF\2\u020b\u020d\7A\2\2\u020c\u020b\3\2\2")
        buf.write("\2\u020c\u020d\3\2\2\2\u020d\177\3\2\2\2\u020e\u020f\7")
        buf.write("\34\2\2\u020f\u0210\5\2\2\2\u0210\u0211\5h\65\2\u0211")
        buf.write("\u0212\5\4\3\2\u0212\u0213\7\33\2\2\u0213\u0214\5\n\6")
        buf.write("\2\u0214\u0215\5h\65\2\u0215\u0216\5\f\7\2\u0216\u021d")
        buf.write("\3\2\2\2\u0217\u0218\7\34\2\2\u0218\u0219\5h\65\2\u0219")
        buf.write("\u021a\7\33\2\2\u021a\u021b\5h\65\2\u021b\u021d\3\2\2")
        buf.write("\2\u021c\u020e\3\2\2\2\u021c\u0217\3\2\2\2\u021d\u0081")
        buf.write("\3\2\2\2\u021e\u0226\5:\36\2\u021f\u0226\5\66\34\2\u0220")
        buf.write("\u0226\5<\37\2\u0221\u0222\7?\2\2\u0222\u0223\5\16\b\2")
        buf.write("\u0223\u0224\5.\30\2\u0224\u0226\3\2\2\2\u0225\u021e\3")
        buf.write("\2\2\2\u0225\u021f\3\2\2\2\u0225\u0220\3\2\2\2\u0225\u0221")
        buf.write("\3\2\2\2\u0226\u0083\3\2\2\2\u0227\u0228\bC\1\2\u0228")
        buf.write("\u022b\5\u0086D\2\u0229\u022b\5\u0088E\2\u022a\u0227\3")
        buf.write("\2\2\2\u022a\u0229\3\2\2\2\u022b\u0231\3\2\2\2\u022c\u022d")
        buf.write("\f\3\2\2\u022d\u022e\t\5\2\2\u022e\u0230\5\u0084C\4\u022f")
        buf.write("\u022c\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0232\3\2\2\2\u0232\u0085\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0234\u0236\7\35\2\2\u0235\u0234\3\2\2\2\u0235")
        buf.write("\u0236\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0238\5\u0082")
        buf.write("B\2\u0238\u0087\3\2\2\2\u0239\u023c\5\u0082B\2\u023a\u023d")
        buf.write("\5\22\n\2\u023b\u023d\5\24\13\2\u023c\u023a\3\2\2\2\u023c")
        buf.write("\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\5\u0082")
        buf.write("B\2\u023f\u0089\3\2\2\2\u0240\u0241\5\36\20\2\u0241\u0242")
        buf.write("\5\16\b\2\u0242\u0249\5*\26\2\u0243\u0245\5\6\4\2\u0244")
        buf.write("\u0246\5\36\20\2\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2")
        buf.write("\2\u0246\u0247\3\2\2\2\u0247\u0248\5\b\5\2\u0248\u024a")
        buf.write("\3\2\2\2\u0249\u0243\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("\u024b\3\2\2\2\u024b\u024d\5\2\2\2\u024c\u024e\5\u0082")
        buf.write("B\2\u024d\u024c\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u024f")
        buf.write("\3\2\2\2\u024f\u0251\5\4\3\2\u0250\u0252\5\u008eH\2\u0251")
        buf.write("\u0250\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u025d\3\2\2\2")
        buf.write("\u0253\u0254\7\60\2\2\u0254\u0258\5\2\2\2\u0255\u0257")
        buf.write("\5(\25\2\u0256\u0255\3\2\2\2\u0257\u025a\3\2\2\2\u0258")
        buf.write("\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2")
        buf.write("\u025a\u0258\3\2\2\2\u025b\u025c\5\4\3\2\u025c\u025e\3")
        buf.write("\2\2\2\u025d\u0253\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u008b")
        buf.write("\3\2\2\2\u025f\u0260\t\6\2\2\u0260\u008d\3\2\2\2\u0261")
        buf.write("\u0262\bH\1\2\u0262\u0263\t\7\2\2\u0263\u0264\5&\24\2")
        buf.write("\u0264\u026a\3\2\2\2\u0265\u0266\f\3\2\2\u0266\u0267\t")
        buf.write("\5\2\2\u0267\u0269\5\u008eH\4\u0268\u0265\3\2\2\2\u0269")
        buf.write("\u026c\3\2\2\2\u026a\u0268\3\2\2\2\u026a\u026b\3\2\2\2")
        buf.write("\u026b\u008f\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u026e\7")
        buf.write("\64\2\2\u026e\u0270\7?\2\2\u026f\u0271\5\u0092J\2\u0270")
        buf.write("\u026f\3\2\2\2\u0270\u0271\3\2\2\2\u0271\u0272\3\2\2\2")
        buf.write("\u0272\u0273\5\2\2\2\u0273\u0274\7G\2\2\u0274\u0275\5")
        buf.write("\4\3\2\u0275\u0091\3\2\2\2\u0276\u027a\5\2\2\2\u0277\u0279")
        buf.write("\7?\2\2\u0278\u0277\3\2\2\2\u0279\u027c\3\2\2\2\u027a")
        buf.write("\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u027d\3\2\2\2")
        buf.write("\u027c\u027a\3\2\2\2\u027d\u027e\5\4\3\2\u027e\u0093\3")
        buf.write("\2\2\2\u027f\u0280\7\65\2\2\u0280\u0281\7?\2\2\u0281\u0285")
        buf.write("\5\2\2\2\u0282\u0284\7D\2\2\u0283\u0282\3\2\2\2\u0284")
        buf.write("\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2")
        buf.write("\u0286\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0289\5")
        buf.write("\4\3\2\u0289\u0095\3\2\2\2\u028a\u028b\79\2\2\u028b\u028c")
        buf.write("\7G\2\2\u028c\u0097\3\2\2\2\u028d\u028e\7\66\2\2\u028e")
        buf.write("\u028f\7D\2\2\u028f\u0099\3\2\2\2\u0290\u0291\7\67\2\2")
        buf.write("\u0291\u0293\7?\2\2\u0292\u0294\5\u0092J\2\u0293\u0292")
        buf.write("\3\2\2\2\u0293\u0294\3\2\2\2\u0294\u0295\3\2\2\2\u0295")
        buf.write("\u0296\5\2\2\2\u0296\u0297\5\u009cO\2\u0297\u0298\5\4")
        buf.write("\3\2\u0298\u009b\3\2\2\2\u0299\u029a\5\u00a2R\2\u029a")
        buf.write("\u009d\3\2\2\2\u029b\u029c\78\2\2\u029c\u029d\7?\2\2\u029d")
        buf.write("\u02a1\5\2\2\2\u029e\u02a0\7D\2\2\u029f\u029e\3\2\2\2")
        buf.write("\u02a0\u02a3\3\2\2\2\u02a1\u029f\3\2\2\2\u02a1\u02a2\3")
        buf.write("\2\2\2\u02a2\u02a4\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a4\u02a5")
        buf.write("\5\4\3\2\u02a5\u009f\3\2\2\2\u02a6\u02a7\7:\2\2\u02a7")
        buf.write("\u02a8\5\2\2\2\u02a8\u02a9\5,\27\2\u02a9\u02ad\5\4\3\2")
        buf.write("\u02aa\u02ab\5\16\b\2\u02ab\u02ac\t\b\2\2\u02ac\u02ae")
        buf.write("\3\2\2\2\u02ad\u02aa\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae")
        buf.write("\u02b1\3\2\2\2\u02af\u02b1\7N\2\2\u02b0\u02a6\3\2\2\2")
        buf.write("\u02b0\u02af\3\2\2\2\u02b1\u00a1\3\2\2\2\u02b2\u02b3\b")
        buf.write("R\1\2\u02b3\u02b7\7M\2\2\u02b4\u02b6\7A\2\2\u02b5\u02b4")
        buf.write("\3\2\2\2\u02b6\u02b9\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b7")
        buf.write("\u02b8\3\2\2\2\u02b8\u02d3\3\2\2\2\u02b9\u02b7\3\2\2\2")
        buf.write("\u02ba\u02be\5\u00a0Q\2\u02bb\u02bd\7A\2\2\u02bc\u02bb")
        buf.write("\3\2\2\2\u02bd\u02c0\3\2\2\2\u02be\u02bc\3\2\2\2\u02be")
        buf.write("\u02bf\3\2\2\2\u02bf\u02d3\3\2\2\2\u02c0\u02be\3\2\2\2")
        buf.write("\u02c1\u02c2\7H\2\2\u02c2\u02c6\5\u00a2R\2\u02c3\u02c5")
        buf.write("\7A\2\2\u02c4\u02c3\3\2\2\2\u02c5\u02c8\3\2\2\2\u02c6")
        buf.write("\u02c4\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u02d3\3\2\2\2")
        buf.write("\u02c8\u02c6\3\2\2\2\u02c9\u02ca\5\2\2\2\u02ca\u02cb\5")
        buf.write("\u00a2R\2\u02cb\u02cf\5\4\3\2\u02cc\u02ce\7A\2\2\u02cd")
        buf.write("\u02cc\3\2\2\2\u02ce\u02d1\3\2\2\2\u02cf\u02cd\3\2\2\2")
        buf.write("\u02cf\u02d0\3\2\2\2\u02d0\u02d3\3\2\2\2\u02d1\u02cf\3")
        buf.write("\2\2\2\u02d2\u02b2\3\2\2\2\u02d2\u02ba\3\2\2\2\u02d2\u02c1")
        buf.write("\3\2\2\2\u02d2\u02c9\3\2\2\2\u02d3\u02f3\3\2\2\2\u02d4")
        buf.write("\u02d8\f\3\2\2\u02d5\u02d7\7A\2\2\u02d6\u02d5\3\2\2\2")
        buf.write("\u02d7\u02da\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d8\u02d9\3")
        buf.write("\2\2\2\u02d9\u02db\3\2\2\2\u02da\u02d8\3\2\2\2\u02db\u02f2")
        buf.write("\5\u00a2R\4\u02dc\u02e0\f\6\2\2\u02dd\u02df\7A\2\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02df\u02e2\3\2\2\2\u02e0\u02de\3\2\2\2")
        buf.write("\u02e0\u02e1\3\2\2\2\u02e1\u02e3\3\2\2\2\u02e2\u02e0\3")
        buf.write("\2\2\2\u02e3\u02e7\t\t\2\2\u02e4\u02e6\7A\2\2\u02e5\u02e4")
        buf.write("\3\2\2\2\u02e6\u02e9\3\2\2\2\u02e7\u02e5\3\2\2\2\u02e7")
        buf.write("\u02e8\3\2\2\2\u02e8\u02ea\3\2\2\2\u02e9\u02e7\3\2\2\2")
        buf.write("\u02ea\u02ee\5\u00a2R\2\u02eb\u02ed\7A\2\2\u02ec\u02eb")
        buf.write("\3\2\2\2\u02ed\u02f0\3\2\2\2\u02ee\u02ec\3\2\2\2\u02ee")
        buf.write("\u02ef\3\2\2\2\u02ef\u02f2\3\2\2\2\u02f0\u02ee\3\2\2\2")
        buf.write("\u02f1\u02d4\3\2\2\2\u02f1\u02dc\3\2\2\2\u02f2\u02f5\3")
        buf.write("\2\2\2\u02f3\u02f1\3\2\2\2\u02f3\u02f4\3\2\2\2\u02f4\u00a3")
        buf.write("\3\2\2\2\u02f5\u02f3\3\2\2\2I\u00c0\u00d8\u00e2\u00e8")
        buf.write("\u00f0\u00f8\u0108\u010a\u0112\u0115\u011e\u0128\u012a")
        buf.write("\u0133\u013d\u0141\u0148\u0152\u015e\u0163\u016a\u016f")
        buf.write("\u0176\u017e\u0186\u0189\u018c\u0193\u019d\u01a7\u01b7")
        buf.write("\u01bb\u01bd\u01c1\u01c3\u01db\u01e3\u01fa\u0205\u020c")
        buf.write("\u021c\u0225\u022a\u0231\u0235\u023c\u0245\u0249\u024d")
        buf.write("\u0251\u0258\u025d\u026a\u0270\u027a\u0285\u0293\u02a1")
        buf.write("\u02ad\u02b0\u02b7\u02be\u02c6\u02cf\u02d2\u02d8\u02e0")
        buf.write("\u02e7\u02ee\u02f1\u02f3")
        return buf.getvalue()
		

class AALParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__12=1
    T__11=2
    T__10=3
    T__9=4
    T__8=5
    T__7=6
    T__6=7
    T__5=8
    T__4=9
    T__3=10
    T__2=11
    T__1=12
    T__0=13
    D_service=14
    D_agent=15
    D_data=16
    D_clause=17
    D_type=18
    D_types=19
    C_auditing=20
    C_ifviolated=21
    O_or=22
    O_and=23
    O_onlywhen=24
    O_then=25
    O_if=26
    O_not=27
    O_where=28
    O_after=29
    O_before=30
    T_must=31
    T_mustnot=32
    T_always=33
    T_never=34
    T_sometime=35
    T_until=36
    T_unless=37
    T_next=38
    A_permit=39
    A_deny=40
    Q_forall=41
    Q_exists=42
    M_subject=43
    M_rservice=44
    M_pservice=45
    M_purpose=46
    M_extends=47
    M_attr=48
    M_actions=49
    M_macro=50
    M_call=51
    M_load=52
    M_check=53
    M_apply=54
    M_exec=55
    C_clause=56
    C_usage=57
    C_audit=58
    C_rectification=59
    C_violation=60
    ID=61
    INT=62
    NEWLINE=63
    WS=64
    BLANK=65
    STRING=66
    COMMENT=67
    MLCOMMENT=68
    MCODE=69
    NEGATION=70
    CONJUNCTION=71
    DISJUNCTION=72
    IMPLICATION=73
    EQUIVALENCE=74
    CONSTANTS=75
    PREDICATE=76

    tokenNames = [ "<INVALID>", "']'", "'.'", "')'", "'['", "'@'", "':'", 
                   "'('", "'!='", "'{'", "'/'", "'=='", "'}'", "'\"'", "D_service", 
                   "D_agent", "D_data", "D_clause", "D_type", "D_types", 
                   "C_auditing", "C_ifviolated", "O_or", "O_and", "O_onlywhen", 
                   "O_then", "O_if", "O_not", "O_where", "O_after", "O_before", 
                   "T_must", "T_mustnot", "T_always", "T_never", "T_sometime", 
                   "T_until", "T_unless", "T_next", "A_permit", "A_deny", 
                   "Q_forall", "Q_exists", "M_subject", "M_rservice", "M_pservice", 
                   "M_purpose", "M_extends", "M_attr", "M_actions", "M_macro", 
                   "M_call", "M_load", "M_check", "M_apply", "M_exec", "C_clause", 
                   "C_usage", "C_audit", "C_rectification", "C_violation", 
                   "ID", "INT", "NEWLINE", "WS", "BLANK", "STRING", "COMMENT", 
                   "MLCOMMENT", "MCODE", "NEGATION", "'&'", "'|'", "IMPLICATION", 
                   "EQUIVALENCE", "CONSTANTS", "PREDICATE" ]

    RULE_h_lpar = 0
    RULE_h_rpar = 1
    RULE_h_lbar = 2
    RULE_h_rbar = 3
    RULE_h_lmar = 4
    RULE_h_rmar = 5
    RULE_h_dot = 6
    RULE_h_colon = 7
    RULE_h_equal = 8
    RULE_h_inequal = 9
    RULE_h_slash = 10
    RULE_h_data = 11
    RULE_h_value = 12
    RULE_h_time = 13
    RULE_h_agentId = 14
    RULE_h_varTypeId = 15
    RULE_h_varId = 16
    RULE_h_dataId = 17
    RULE_h_date = 18
    RULE_h_purposeId = 19
    RULE_h_serviceId = 20
    RULE_h_clauseId = 21
    RULE_h_attribute = 22
    RULE_h_comment = 23
    RULE_h_duration = 24
    RULE_h_parameters = 25
    RULE_h_constant = 26
    RULE_h_type = 27
    RULE_h_variable = 28
    RULE_h_predicate = 29
    RULE_main = 30
    RULE_aalprog = 31
    RULE_declaration = 32
    RULE_agentDec = 33
    RULE_dataDec = 34
    RULE_rsService = 35
    RULE_psService = 36
    RULE_serviceDec = 37
    RULE_varDec = 38
    RULE_attrValue = 39
    RULE_typeDec = 40
    RULE_type_super = 41
    RULE_type_attr = 42
    RULE_type_actions = 43
    RULE_agentType = 44
    RULE_serviceType = 45
    RULE_dataType = 46
    RULE_clause = 47
    RULE_usage = 48
    RULE_audit = 49
    RULE_rectification = 50
    RULE_actionExp = 51
    RULE_actionExp1Action = 52
    RULE_actionExp2notAction = 53
    RULE_actionExp3modalAction = 54
    RULE_actionExp4condition = 55
    RULE_actionExp6Author = 56
    RULE_actionExp7ifthen = 57
    RULE_actionExp8qvar = 58
    RULE_quant = 59
    RULE_qvar = 60
    RULE_booleanOp = 61
    RULE_author = 62
    RULE_ifthen = 63
    RULE_exp = 64
    RULE_condition = 65
    RULE_condition1notExp = 66
    RULE_condition2cmpExp = 67
    RULE_action = 68
    RULE_modal = 69
    RULE_time = 70
    RULE_macro = 71
    RULE_args = 72
    RULE_macroCall = 73
    RULE_exec = 74
    RULE_loadlib = 75
    RULE_ltlCheck = 76
    RULE_check = 77
    RULE_checkApply = 78
    RULE_atom = 79
    RULE_formula = 80

    ruleNames =  [ "h_lpar", "h_rpar", "h_lbar", "h_rbar", "h_lmar", "h_rmar", 
                   "h_dot", "h_colon", "h_equal", "h_inequal", "h_slash", 
                   "h_data", "h_value", "h_time", "h_agentId", "h_varTypeId", 
                   "h_varId", "h_dataId", "h_date", "h_purposeId", "h_serviceId", 
                   "h_clauseId", "h_attribute", "h_comment", "h_duration", 
                   "h_parameters", "h_constant", "h_type", "h_variable", 
                   "h_predicate", "main", "aalprog", "declaration", "agentDec", 
                   "dataDec", "rsService", "psService", "serviceDec", "varDec", 
                   "attrValue", "typeDec", "type_super", "type_attr", "type_actions", 
                   "agentType", "serviceType", "dataType", "clause", "usage", 
                   "audit", "rectification", "actionExp", "actionExp1Action", 
                   "actionExp2notAction", "actionExp3modalAction", "actionExp4condition", 
                   "actionExp6Author", "actionExp7ifthen", "actionExp8qvar", 
                   "quant", "qvar", "booleanOp", "author", "ifthen", "exp", 
                   "condition", "condition1notExp", "condition2cmpExp", 
                   "action", "modal", "time", "macro", "args", "macroCall", 
                   "exec", "loadlib", "ltlCheck", "check", "checkApply", 
                   "atom", "formula" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class H_lparContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AALParser.RULE_h_lpar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_lpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_lpar(self)




    def h_lpar(self):

        localctx = AALParser.H_lparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_h_lpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(self.T__6)
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
            return AALParser.RULE_h_rpar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_rpar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_rpar(self)




    def h_rpar(self):

        localctx = AALParser.H_rparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_h_rpar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(self.T__10)
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
            return AALParser.RULE_h_lbar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_lbar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_lbar(self)




    def h_lbar(self):

        localctx = AALParser.H_lbarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_h_lbar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(self.T__9)
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
            return AALParser.RULE_h_rbar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_rbar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_rbar(self)




    def h_rbar(self):

        localctx = AALParser.H_rbarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_h_rbar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(self.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_lmarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AALParser.RULE_h_lmar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_lmar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_lmar(self)




    def h_lmar(self):

        localctx = AALParser.H_lmarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_h_lmar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(self.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_rmarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AALParser.RULE_h_rmar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_rmar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_rmar(self)




    def h_rmar(self):

        localctx = AALParser.H_rmarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_h_rmar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(self.T__1)
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
            return AALParser.RULE_h_dot

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_dot(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_dot(self)




    def h_dot(self):

        localctx = AALParser.H_dotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_h_dot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(self.T__11)
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
            return AALParser.RULE_h_colon

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_colon(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_colon(self)




    def h_colon(self):

        localctx = AALParser.H_colonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_h_colon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(self.T__7)
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
            return AALParser.RULE_h_equal

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_equal(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_equal(self)




    def h_equal(self):

        localctx = AALParser.H_equalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_h_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(self.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_inequalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AALParser.RULE_h_inequal

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_inequal(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_inequal(self)




    def h_inequal(self):

        localctx = AALParser.H_inequalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_h_inequal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(self.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_slashContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AALParser.RULE_h_slash

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_slash(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_slash(self)




    def h_slash(self):

        localctx = AALParser.H_slashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_h_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(self.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_dataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_data

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_data(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_data(self)




    def h_data(self):

        localctx = AALParser.H_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_h_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_constant(self):
            return self.getTypedRuleContext(AALParser.H_constantContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_h_value

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_value(self)




    def h_value(self):

        localctx = AALParser.H_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_h_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186 
            self.h_constant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_date(self):
            return self.getTypedRuleContext(AALParser.H_dateContext,0)


        def h_duration(self):
            return self.getTypedRuleContext(AALParser.H_durationContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_h_time

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_time(self)




    def h_time(self):

        localctx = AALParser.H_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_h_time)
        try:
            self.state = 190
            token = self._input.LA(1)
            if token in [self.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188 
                self.h_date()

            elif token in [self.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189 
                self.h_duration()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_agentIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_agentId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_agentId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_agentId(self)




    def h_agentId(self):

        localctx = AALParser.H_agentIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_h_agentId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_varTypeIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_varTypeId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_varTypeId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_varTypeId(self)




    def h_varTypeId(self):

        localctx = AALParser.H_varTypeIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_h_varTypeId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_varIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_varId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_varId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_varId(self)




    def h_varId(self):

        localctx = AALParser.H_varIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_h_varId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_dataIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_dataId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_dataId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_dataId(self)




    def h_dataId(self):

        localctx = AALParser.H_dataIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_h_dataId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_dateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AALParser.STRING, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_date

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_date(self)




    def h_date(self):

        localctx = AALParser.H_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_h_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(self.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_purposeIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_purposeId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_purposeId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_purposeId(self)




    def h_purposeId(self):

        localctx = AALParser.H_purposeIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_h_purposeId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_serviceIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_serviceId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_serviceId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_serviceId(self)




    def h_serviceId(self):

        localctx = AALParser.H_serviceIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_h_serviceId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_clauseIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_clauseId

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_clauseId(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_clauseId(self)




    def h_clauseId(self):

        localctx = AALParser.H_clauseIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_h_clauseId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_attribute

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_attribute(self)




    def h_attribute(self):

        localctx = AALParser.H_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_h_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_commentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(AALParser.NEWLINE, 0)

        def MLCOMMENT(self):
            return self.getToken(AALParser.MLCOMMENT, 0)

        def COMMENT(self):
            return self.getToken(AALParser.COMMENT, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_comment

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_comment(self)




    def h_comment(self):

        localctx = AALParser.H_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_h_comment)
        try:
            self.state = 214
            token = self._input.LA(1)
            if token in [self.COMMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(self.COMMENT)
                self.state = 211
                self.match(self.NEWLINE)

            elif token in [self.MLCOMMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(self.MLCOMMENT)
                self.state = 213
                self.match(self.NEWLINE)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_durationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.INT)
            else:
                return self.getToken(AALParser.INT, i)

        def h_colon(self):
            return self.getTypedRuleContext(AALParser.H_colonContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_h_duration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_duration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_duration(self)




    def h_duration(self):

        localctx = AALParser.H_durationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_h_duration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(self.INT)
            self.state = 217
            self.match(self.INT)
            self.state = 218 
            self.h_colon()
            self.state = 219
            self.match(self.INT)
            self.state = 220
            self.match(self.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_variable(self):
            return self.getTypedRuleContext(AALParser.H_variableContext,0)


        def h_constant(self):
            return self.getTypedRuleContext(AALParser.H_constantContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_h_parameters

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_parameters(self)




    def h_parameters(self):

        localctx = AALParser.H_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_h_parameters)
        try:
            self.state = 224
            token = self._input.LA(1)
            if token in [self.T__0, self.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222 
                self.h_constant()

            elif token in [self.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223 
                self.h_variable()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_constantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(AALParser.INT, 0)

        def STRING(self):
            return self.getToken(AALParser.STRING, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_constant

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_constant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_constant(self)




    def h_constant(self):

        localctx = AALParser.H_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_h_constant)
        try:
            self.state = 230
            token = self._input.LA(1)
            if token in [self.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(self.INT)

            elif token in [self.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(self.T__0)
                self.state = 228
                self.match(self.STRING)
                self.state = 229
                self.match(self.T__0)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_h_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_type(self)




    def h_type(self):

        localctx = AALParser.H_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_h_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def h_colon(self):
            return self.getTypedRuleContext(AALParser.H_colonContext,0)


        def h_type(self):
            return self.getTypedRuleContext(AALParser.H_typeContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_h_variable

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_variable(self)




    def h_variable(self):

        localctx = AALParser.H_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_h_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(self.ID)
            self.state = 238
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 235 
                self.h_colon()
                self.state = 236 
                self.h_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class H_predicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.ID)
            else:
                return self.getToken(AALParser.ID, i)

        def getRuleIndex(self):
            return AALParser.RULE_h_predicate

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_predicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_predicate(self)




    def h_predicate(self):

        localctx = AALParser.H_predicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_h_predicate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(self.T__8)
            self.state = 241
            self.match(self.ID)
            self.state = 242 
            self.h_lpar()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 243
                self.match(self.ID)
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 249 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aalprog(self):
            return self.getTypedRuleContext(AALParser.AalprogContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitMain(self)




    def main(self):

        localctx = AALParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251 
            self.aalprog()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AalprogContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def checkApply(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.CheckApplyContext)
            else:
                return self.getTypedRuleContext(AALParser.CheckApplyContext,i)


        def exec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ExecContext)
            else:
                return self.getTypedRuleContext(AALParser.ExecContext,i)


        def h_comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_commentContext)
            else:
                return self.getTypedRuleContext(AALParser.H_commentContext,i)


        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ClauseContext)
            else:
                return self.getTypedRuleContext(AALParser.ClauseContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(AALParser.DeclarationContext,i)


        def loadlib(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.LoadlibContext)
            else:
                return self.getTypedRuleContext(AALParser.LoadlibContext,i)


        def macroCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.MacroCallContext)
            else:
                return self.getTypedRuleContext(AALParser.MacroCallContext,i)


        def ltlCheck(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.LtlCheckContext)
            else:
                return self.getTypedRuleContext(AALParser.LtlCheckContext,i)


        def macro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.MacroContext)
            else:
                return self.getTypedRuleContext(AALParser.MacroContext,i)


        def getRuleIndex(self):
            return AALParser.RULE_aalprog

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAalprog(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAalprog(self)




    def aalprog(self):

        localctx = AALParser.AalprogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_aalprog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 14)) & ~0x3f) == 0 and ((1 << (_la - 14)) & ((1 << (self.D_service - 14)) | (1 << (self.D_agent - 14)) | (1 << (self.D_data - 14)) | (1 << (self.D_clause - 14)) | (1 << (self.D_type - 14)) | (1 << (self.M_macro - 14)) | (1 << (self.M_call - 14)) | (1 << (self.M_load - 14)) | (1 << (self.M_check - 14)) | (1 << (self.M_apply - 14)) | (1 << (self.M_exec - 14)) | (1 << (self.ID - 14)) | (1 << (self.COMMENT - 14)) | (1 << (self.MLCOMMENT - 14)))) != 0):
                self.state = 262
                token = self._input.LA(1)
                if token in [self.D_clause]:
                    self.state = 253 
                    self.clause()

                elif token in [self.D_service, self.D_agent, self.D_data, self.D_type, self.ID]:
                    self.state = 254 
                    self.declaration()

                elif token in [self.COMMENT, self.MLCOMMENT]:
                    self.state = 255 
                    self.h_comment()

                elif token in [self.M_macro]:
                    self.state = 256 
                    self.macro()

                elif token in [self.M_call]:
                    self.state = 257 
                    self.macroCall()

                elif token in [self.M_load]:
                    self.state = 258 
                    self.loadlib()

                elif token in [self.M_check]:
                    self.state = 259 
                    self.ltlCheck()

                elif token in [self.M_apply]:
                    self.state = 260 
                    self.checkApply()

                elif token in [self.M_exec]:
                    self.state = 261 
                    self.exec()

                else:
                    raise NoViableAltException(self)

                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(AALParser.NEWLINE, 0)

        def dataDec(self):
            return self.getTypedRuleContext(AALParser.DataDecContext,0)


        def serviceDec(self):
            return self.getTypedRuleContext(AALParser.ServiceDecContext,0)


        def varDec(self):
            return self.getTypedRuleContext(AALParser.VarDecContext,0)


        def typeDec(self):
            return self.getTypedRuleContext(AALParser.TypeDecContext,0)


        def agentDec(self):
            return self.getTypedRuleContext(AALParser.AgentDecContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = AALParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            token = self._input.LA(1)
            if token in [self.D_agent]:
                self.state = 267 
                self.agentDec()

            elif token in [self.D_service]:
                self.state = 268 
                self.serviceDec()

            elif token in [self.D_data]:
                self.state = 269 
                self.dataDec()

            elif token in [self.D_type]:
                self.state = 270 
                self.typeDec()

            elif token in [self.ID]:
                self.state = 271 
                self.varDec()

            else:
                raise NoViableAltException(self)

            self.state = 275
            _la = self._input.LA(1)
            if _la==AALParser.NEWLINE:
                self.state = 274
                self.match(self.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AgentDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def D_types(self):
            return self.getToken(AALParser.D_types, 0)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def psService(self):
            return self.getTypedRuleContext(AALParser.PsServiceContext,0)


        def h_agentId(self):
            return self.getTypedRuleContext(AALParser.H_agentIdContext,0)


        def D_agent(self):
            return self.getToken(AALParser.D_agent, 0)

        def rsService(self):
            return self.getTypedRuleContext(AALParser.RsServiceContext,0)


        def agentType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.AgentTypeContext)
            else:
                return self.getTypedRuleContext(AALParser.AgentTypeContext,i)


        def getRuleIndex(self):
            return AALParser.RULE_agentDec

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAgentDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAgentDec(self)




    def agentDec(self):

        localctx = AALParser.AgentDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_agentDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(self.D_agent)
            self.state = 278 
            self.h_agentId()
            self.state = 296
            _la = self._input.LA(1)
            if _la==AALParser.D_types:
                self.state = 279
                self.match(self.D_types)
                self.state = 280 
                self.h_lpar()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 281 
                    self.agentType()
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 287 
                self.h_rpar()
                self.state = 294
                token = self._input.LA(1)
                if token in [self.M_rservice]:
                    self.state = 288 
                    self.rsService()
                    self.state = 289 
                    self.psService()

                elif token in [self.M_pservice]:
                    self.state = 291 
                    self.psService()
                    self.state = 292 
                    self.rsService()

                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def D_types(self):
            return self.getToken(AALParser.D_types, 0)

        def h_dataId(self):
            return self.getTypedRuleContext(AALParser.H_dataIdContext,0)


        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def psService(self):
            return self.getTypedRuleContext(AALParser.PsServiceContext,0)


        def h_agentId(self):
            return self.getTypedRuleContext(AALParser.H_agentIdContext,0)


        def dataType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.DataTypeContext)
            else:
                return self.getTypedRuleContext(AALParser.DataTypeContext,i)


        def rsService(self):
            return self.getTypedRuleContext(AALParser.RsServiceContext,0)


        def D_data(self):
            return self.getToken(AALParser.D_data, 0)

        def M_subject(self):
            return self.getToken(AALParser.M_subject, 0)

        def getRuleIndex(self):
            return AALParser.RULE_dataDec

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterDataDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitDataDec(self)




    def dataDec(self):

        localctx = AALParser.DataDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_dataDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(self.D_data)
            self.state = 299 
            self.h_dataId()
            self.state = 300
            self.match(self.D_types)
            self.state = 301 
            self.h_lpar()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 302 
                self.dataType()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 308 
            self.h_rpar()
            self.state = 315
            token = self._input.LA(1)
            if token in [self.M_rservice]:
                self.state = 309 
                self.rsService()
                self.state = 310 
                self.psService()
                pass
            elif token in [self.M_pservice]:
                self.state = 312 
                self.psService()
                self.state = 313 
                self.rsService()
                pass
            elif token in [self.EOF, self.D_service, self.D_agent, self.D_data, self.D_clause, self.D_type, self.M_subject, self.M_macro, self.M_call, self.M_load, self.M_check, self.M_apply, self.M_exec, self.ID, self.NEWLINE, self.COMMENT, self.MLCOMMENT]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 319
            _la = self._input.LA(1)
            if _la==AALParser.M_subject:
                self.state = 317
                self.match(self.M_subject)
                self.state = 318 
                self.h_agentId()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RsServiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_serviceId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_serviceIdContext)
            else:
                return self.getTypedRuleContext(AALParser.H_serviceIdContext,i)


        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def M_rservice(self):
            return self.getToken(AALParser.M_rservice, 0)

        def getRuleIndex(self):
            return AALParser.RULE_rsService

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterRsService(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitRsService(self)




    def rsService(self):

        localctx = AALParser.RsServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_rsService)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(self.M_rservice)
            self.state = 322 
            self.h_lpar()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 323 
                self.h_serviceId()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PsServiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_serviceId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_serviceIdContext)
            else:
                return self.getTypedRuleContext(AALParser.H_serviceIdContext,i)


        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def M_pservice(self):
            return self.getToken(AALParser.M_pservice, 0)

        def getRuleIndex(self):
            return AALParser.RULE_psService

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterPsService(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitPsService(self)




    def psService(self):

        localctx = AALParser.PsServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_psService)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(self.M_pservice)
            self.state = 332 
            self.h_lpar()
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 333 
                self.h_serviceId()
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ServiceDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def D_types(self):
            return self.getToken(AALParser.D_types, 0)

        def M_purpose(self):
            return self.getToken(AALParser.M_purpose, 0)

        def h_rpar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_rparContext)
            else:
                return self.getTypedRuleContext(AALParser.H_rparContext,i)


        def D_service(self):
            return self.getToken(AALParser.D_service, 0)

        def serviceType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ServiceTypeContext)
            else:
                return self.getTypedRuleContext(AALParser.ServiceTypeContext,i)


        def h_lpar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_lparContext)
            else:
                return self.getTypedRuleContext(AALParser.H_lparContext,i)


        def h_purposeId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_purposeIdContext)
            else:
                return self.getTypedRuleContext(AALParser.H_purposeIdContext,i)


        def h_serviceId(self):
            return self.getTypedRuleContext(AALParser.H_serviceIdContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_serviceDec

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterServiceDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitServiceDec(self)




    def serviceDec(self):

        localctx = AALParser.ServiceDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_serviceDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(self.D_service)
            self.state = 342 
            self.h_serviceId()
            self.state = 353
            _la = self._input.LA(1)
            if _la==AALParser.D_types:
                self.state = 343
                self.match(self.D_types)
                self.state = 344 
                self.h_lpar()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 345 
                    self.serviceType()
                    self.state = 350
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 351 
                self.h_rpar()


            self.state = 365
            _la = self._input.LA(1)
            if _la==AALParser.M_purpose:
                self.state = 355
                self.match(self.M_purpose)
                self.state = 356 
                self.h_lpar()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 357 
                    self.h_purposeId()
                    self.state = 362
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 363 
                self.h_rpar()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_varId(self):
            return self.getTypedRuleContext(AALParser.H_varIdContext,0)


        def attrValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.AttrValueContext)
            else:
                return self.getTypedRuleContext(AALParser.AttrValueContext,i)


        def h_varTypeId(self):
            return self.getTypedRuleContext(AALParser.H_varTypeIdContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_varDec

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterVarDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitVarDec(self)




    def varDec(self):

        localctx = AALParser.VarDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_varDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367 
            self.h_varTypeId()
            self.state = 368 
            self.h_varId()
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 369 
                    self.attrValue() 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttrValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def h_attribute(self):
            return self.getTypedRuleContext(AALParser.H_attributeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.ID)
            else:
                return self.getToken(AALParser.ID, i)

        def getRuleIndex(self):
            return AALParser.RULE_attrValue

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAttrValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAttrValue(self)




    def attrValue(self):

        localctx = AALParser.AttrValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_attrValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375 
            self.h_attribute()
            self.state = 376 
            self.h_lpar()
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 377
                self.match(self.ID)
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 383 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeDecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_actions(self):
            return self.getTypedRuleContext(AALParser.Type_actionsContext,0)


        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def type_super(self):
            return self.getTypedRuleContext(AALParser.Type_superContext,0)


        def type_attr(self):
            return self.getTypedRuleContext(AALParser.Type_attrContext,0)


        def D_type(self):
            return self.getToken(AALParser.D_type, 0)

        def getRuleIndex(self):
            return AALParser.RULE_typeDec

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterTypeDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitTypeDec(self)




    def typeDec(self):

        localctx = AALParser.TypeDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_typeDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(self.D_type)
            self.state = 386
            self.match(self.ID)
            self.state = 388
            _la = self._input.LA(1)
            if _la==AALParser.M_extends:
                self.state = 387 
                self.type_super()


            self.state = 391
            _la = self._input.LA(1)
            if _la==AALParser.M_attr:
                self.state = 390 
                self.type_attr()


            self.state = 394
            _la = self._input.LA(1)
            if _la==AALParser.M_actions:
                self.state = 393 
                self.type_actions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_superContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def M_extends(self):
            return self.getToken(AALParser.M_extends, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.ID)
            else:
                return self.getToken(AALParser.ID, i)

        def getRuleIndex(self):
            return AALParser.RULE_type_super

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterType_super(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitType_super(self)




    def type_super(self):

        localctx = AALParser.Type_superContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_type_super)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(self.M_extends)
            self.state = 397 
            self.h_lpar()
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 398
                self.match(self.ID)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 404 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_attrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def M_attr(self):
            return self.getToken(AALParser.M_attr, 0)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.ID)
            else:
                return self.getToken(AALParser.ID, i)

        def getRuleIndex(self):
            return AALParser.RULE_type_attr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterType_attr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitType_attr(self)




    def type_attr(self):

        localctx = AALParser.Type_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_type_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(self.M_attr)
            self.state = 407 
            self.h_lpar()
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 408
                self.match(self.ID)
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 414 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_actionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def M_actions(self):
            return self.getToken(AALParser.M_actions, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.ID)
            else:
                return self.getToken(AALParser.ID, i)

        def getRuleIndex(self):
            return AALParser.RULE_type_actions

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterType_actions(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitType_actions(self)




    def type_actions(self):

        localctx = AALParser.Type_actionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_type_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(self.M_actions)
            self.state = 417 
            self.h_lpar()
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 418
                self.match(self.ID)
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 424 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AgentTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_agentType

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAgentType(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAgentType(self)




    def agentType(self):

        localctx = AALParser.AgentTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_agentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ServiceTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_serviceType

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterServiceType(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitServiceType(self)




    def serviceType(self):

        localctx = AALParser.ServiceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_serviceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def getRuleIndex(self):
            return AALParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitDataType(self)




    def dataType(self):

        localctx = AALParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_dataType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(self.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.NEWLINE)
            else:
                return self.getToken(AALParser.NEWLINE, i)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def D_clause(self):
            return self.getToken(AALParser.D_clause, 0)

        def usage(self):
            return self.getTypedRuleContext(AALParser.UsageContext,0)


        def rectification(self):
            return self.getTypedRuleContext(AALParser.RectificationContext,0)


        def h_clauseId(self):
            return self.getTypedRuleContext(AALParser.H_clauseIdContext,0)


        def audit(self):
            return self.getTypedRuleContext(AALParser.AuditContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitClause(self)




    def clause(self):

        localctx = AALParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(self.D_clause)
            self.state = 433 
            self.h_clauseId()
            self.state = 434 
            self.h_lpar()

            self.state = 435 
            self.usage()
            self.state = 437
            _la = self._input.LA(1)
            if _la==AALParser.NEWLINE:
                self.state = 436
                self.match(self.NEWLINE)


            self.state = 443
            _la = self._input.LA(1)
            if _la==AALParser.C_auditing:
                self.state = 439 
                self.audit()
                self.state = 441
                _la = self._input.LA(1)
                if _la==AALParser.NEWLINE:
                    self.state = 440
                    self.match(self.NEWLINE)




            self.state = 449
            _la = self._input.LA(1)
            if _la==AALParser.C_ifviolated:
                self.state = 445 
                self.rectification()
                self.state = 447
                _la = self._input.LA(1)
                if _la==AALParser.NEWLINE:
                    self.state = 446
                    self.match(self.NEWLINE)




            self.state = 451 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UsageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actionExp(self):
            return self.getTypedRuleContext(AALParser.ActionExpContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_usage

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterUsage(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitUsage(self)




    def usage(self):

        localctx = AALParser.UsageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_usage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453 
            self.actionExp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AuditContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def usage(self):
            return self.getTypedRuleContext(AALParser.UsageContext,0)


        def C_auditing(self):
            return self.getToken(AALParser.C_auditing, 0)

        def getRuleIndex(self):
            return AALParser.RULE_audit

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAudit(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAudit(self)




    def audit(self):

        localctx = AALParser.AuditContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_audit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.match(self.C_auditing)
            self.state = 456 
            self.usage()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RectificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def usage(self):
            return self.getTypedRuleContext(AALParser.UsageContext,0)


        def C_ifviolated(self):
            return self.getToken(AALParser.C_ifviolated, 0)

        def getRuleIndex(self):
            return AALParser.RULE_rectification

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterRectification(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitRectification(self)




    def rectification(self):

        localctx = AALParser.RectificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_rectification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(self.C_ifviolated)
            self.state = 459 
            self.usage()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanOp(self):
            return self.getTypedRuleContext(AALParser.BooleanOpContext,0)


        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def actionExp8qvar(self):
            return self.getTypedRuleContext(AALParser.ActionExp8qvarContext,0)


        def actionExp7ifthen(self):
            return self.getTypedRuleContext(AALParser.ActionExp7ifthenContext,0)


        def actionExp3modalAction(self):
            return self.getTypedRuleContext(AALParser.ActionExp3modalActionContext,0)


        def actionExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ActionExpContext)
            else:
                return self.getTypedRuleContext(AALParser.ActionExpContext,i)


        def actionExp2notAction(self):
            return self.getTypedRuleContext(AALParser.ActionExp2notActionContext,0)


        def actionExp1Action(self):
            return self.getTypedRuleContext(AALParser.ActionExp1ActionContext,0)


        def actionExp6Author(self):
            return self.getTypedRuleContext(AALParser.ActionExp6AuthorContext,0)


        def actionExp4condition(self):
            return self.getTypedRuleContext(AALParser.ActionExp4conditionContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp(self)



    def actionExp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AALParser.ActionExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_actionExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 462 
                self.actionExp1Action()
                pass

            elif la_ == 2:
                self.state = 463 
                self.actionExp2notAction()
                pass

            elif la_ == 3:
                self.state = 464 
                self.actionExp3modalAction()
                pass

            elif la_ == 4:
                self.state = 465 
                self.actionExp4condition()
                pass

            elif la_ == 5:
                self.state = 466 
                self.actionExp6Author()
                pass

            elif la_ == 6:
                self.state = 467 
                self.actionExp7ifthen()
                pass

            elif la_ == 7:
                self.state = 468 
                self.actionExp8qvar()
                pass

            elif la_ == 8:
                self.state = 469 
                self.h_lpar()
                self.state = 470 
                self.actionExp(0)
                self.state = 471 
                self.h_rpar()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AALParser.ActionExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_actionExp)
                    self.state = 475
                    if not self.precpred(self._ctx, 5):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 476 
                    self.booleanOp()
                    self.state = 477 
                    self.actionExp(6) 
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ActionExp1ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(AALParser.ActionContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp1Action

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp1Action(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp1Action(self)




    def actionExp1Action(self):

        localctx = AALParser.ActionExp1ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_actionExp1Action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484 
            self.action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExp2notActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def O_not(self):
            return self.getToken(AALParser.O_not, 0)

        def actionExp(self):
            return self.getTypedRuleContext(AALParser.ActionExpContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp2notAction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp2notAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp2notAction(self)




    def actionExp2notAction(self):

        localctx = AALParser.ActionExp2notActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_actionExp2notAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(self.O_not)
            self.state = 487 
            self.actionExp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExp3modalActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def actionExp(self):
            return self.getTypedRuleContext(AALParser.ActionExpContext,0)


        def modal(self):
            return self.getTypedRuleContext(AALParser.ModalContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp3modalAction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp3modalAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp3modalAction(self)




    def actionExp3modalAction(self):

        localctx = AALParser.ActionExp3modalActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_actionExp3modalAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489 
            self.modal()
            self.state = 490 
            self.h_lpar()
            self.state = 491 
            self.actionExp(0)
            self.state = 492 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExp4conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AALParser.ConditionContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp4condition

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp4condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp4condition(self)




    def actionExp4condition(self):

        localctx = AALParser.ActionExp4conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_actionExp4condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494 
            self.condition(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExp6AuthorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def author(self):
            return self.getTypedRuleContext(AALParser.AuthorContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp6Author

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp6Author(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp6Author(self)




    def actionExp6Author(self):

        localctx = AALParser.ActionExp6AuthorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_actionExp6Author)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496 
            self.author()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExp7ifthenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifthen(self):
            return self.getTypedRuleContext(AALParser.IfthenContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp7ifthen

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp7ifthen(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp7ifthen(self)




    def actionExp7ifthen(self):

        localctx = AALParser.ActionExp7ifthenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_actionExp7ifthen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498 
            self.ifthen()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionExp8qvarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.QvarContext)
            else:
                return self.getTypedRuleContext(AALParser.QvarContext,i)


        def actionExp(self):
            return self.getTypedRuleContext(AALParser.ActionExpContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_actionExp8qvar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterActionExp8qvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitActionExp8qvar(self)




    def actionExp8qvar(self):

        localctx = AALParser.ActionExp8qvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_actionExp8qvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500 
            self.qvar()
            self.state = 504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 501 
                    self.qvar() 
                self.state = 506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 507 
            self.actionExp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Q_forall(self):
            return self.getToken(AALParser.Q_forall, 0)

        def Q_exists(self):
            return self.getToken(AALParser.Q_exists, 0)

        def getRuleIndex(self):
            return AALParser.RULE_quant

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterQuant(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitQuant(self)




    def quant(self):

        localctx = AALParser.QuantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_quant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            _la = self._input.LA(1)
            if not(_la==AALParser.Q_forall or _la==AALParser.Q_exists):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QvarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(AALParser.ConditionContext,0)


        def h_variable(self):
            return self.getTypedRuleContext(AALParser.H_variableContext,0)


        def O_where(self):
            return self.getToken(AALParser.O_where, 0)

        def quant(self):
            return self.getTypedRuleContext(AALParser.QuantContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_qvar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterQvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitQvar(self)




    def qvar(self):

        localctx = AALParser.QvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_qvar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511 
            self.quant()
            self.state = 512 
            self.h_variable()
            self.state = 515
            _la = self._input.LA(1)
            if _la==AALParser.O_where:
                self.state = 513
                self.match(self.O_where)
                self.state = 514 
                self.condition(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BooleanOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_unless(self):
            return self.getToken(AALParser.T_unless, 0)

        def T_until(self):
            return self.getToken(AALParser.T_until, 0)

        def O_and(self):
            return self.getToken(AALParser.O_and, 0)

        def O_or(self):
            return self.getToken(AALParser.O_or, 0)

        def O_onlywhen(self):
            return self.getToken(AALParser.O_onlywhen, 0)

        def getRuleIndex(self):
            return AALParser.RULE_booleanOp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterBooleanOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitBooleanOp(self)




    def booleanOp(self):

        localctx = AALParser.BooleanOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_booleanOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.O_or) | (1 << self.O_and) | (1 << self.O_onlywhen) | (1 << self.T_until) | (1 << self.T_unless))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AuthorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(AALParser.NEWLINE, 0)

        def A_deny(self):
            return self.getToken(AALParser.A_deny, 0)

        def action(self):
            return self.getTypedRuleContext(AALParser.ActionContext,0)


        def A_permit(self):
            return self.getToken(AALParser.A_permit, 0)

        def getRuleIndex(self):
            return AALParser.RULE_author

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAuthor(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAuthor(self)




    def author(self):

        localctx = AALParser.AuthorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_author)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            _la = self._input.LA(1)
            if not(_la==AALParser.A_permit or _la==AALParser.A_deny):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 520 
            self.action()
            self.state = 522
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 521
                self.match(self.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfthenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_rmar(self):
            return self.getTypedRuleContext(AALParser.H_rmarContext,0)


        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def O_if(self):
            return self.getToken(AALParser.O_if, 0)

        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def actionExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ActionExpContext)
            else:
                return self.getTypedRuleContext(AALParser.ActionExpContext,i)


        def h_lmar(self):
            return self.getTypedRuleContext(AALParser.H_lmarContext,0)


        def O_then(self):
            return self.getToken(AALParser.O_then, 0)

        def getRuleIndex(self):
            return AALParser.RULE_ifthen

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterIfthen(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitIfthen(self)




    def ifthen(self):

        localctx = AALParser.IfthenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_ifthen)
        try:
            self.state = 538
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(self.O_if)
                self.state = 525 
                self.h_lpar()
                self.state = 526 
                self.actionExp(0)
                self.state = 527 
                self.h_rpar()
                self.state = 528
                self.match(self.O_then)
                self.state = 529 
                self.h_lmar()
                self.state = 530 
                self.actionExp(0)
                self.state = 531 
                self.h_rmar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(self.O_if)
                self.state = 534 
                self.actionExp(0)
                self.state = 535
                self.match(self.O_then)
                self.state = 536 
                self.actionExp(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_dot(self):
            return self.getTypedRuleContext(AALParser.H_dotContext,0)


        def h_predicate(self):
            return self.getTypedRuleContext(AALParser.H_predicateContext,0)


        def h_variable(self):
            return self.getTypedRuleContext(AALParser.H_variableContext,0)


        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def h_constant(self):
            return self.getTypedRuleContext(AALParser.H_constantContext,0)


        def h_attribute(self):
            return self.getTypedRuleContext(AALParser.H_attributeContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitExp(self)




    def exp(self):

        localctx = AALParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_exp)
        try:
            self.state = 547
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540 
                self.h_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 541 
                self.h_constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 542 
                self.h_predicate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 543
                self.match(self.ID)
                self.state = 544 
                self.h_dot()
                self.state = 545 
                self.h_attribute()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def O_and(self):
            return self.getToken(AALParser.O_and, 0)

        def condition1notExp(self):
            return self.getTypedRuleContext(AALParser.Condition1notExpContext,0)


        def O_or(self):
            return self.getToken(AALParser.O_or, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ConditionContext)
            else:
                return self.getTypedRuleContext(AALParser.ConditionContext,i)


        def condition2cmpExp(self):
            return self.getTypedRuleContext(AALParser.Condition2cmpExpContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitCondition(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AALParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 550 
                self.condition1notExp()
                pass

            elif la_ == 2:
                self.state = 551 
                self.condition2cmpExp()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 559
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AALParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 554
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 555
                    _la = self._input.LA(1)
                    if not(_la==AALParser.O_or or _la==AALParser.O_and):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 556 
                    self.condition(2) 
                self.state = 561
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Condition1notExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def O_not(self):
            return self.getToken(AALParser.O_not, 0)

        def exp(self):
            return self.getTypedRuleContext(AALParser.ExpContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_condition1notExp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterCondition1notExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitCondition1notExp(self)




    def condition1notExp(self):

        localctx = AALParser.Condition1notExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_condition1notExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            _la = self._input.LA(1)
            if _la==AALParser.O_not:
                self.state = 562
                self.match(self.O_not)


            self.state = 565 
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Condition2cmpExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_inequal(self):
            return self.getTypedRuleContext(AALParser.H_inequalContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ExpContext)
            else:
                return self.getTypedRuleContext(AALParser.ExpContext,i)


        def h_equal(self):
            return self.getTypedRuleContext(AALParser.H_equalContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_condition2cmpExp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterCondition2cmpExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitCondition2cmpExp(self)




    def condition2cmpExp(self):

        localctx = AALParser.Condition2cmpExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_condition2cmpExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567 
            self.exp()
            self.state = 570
            token = self._input.LA(1)
            if token in [self.T__2]:
                self.state = 568 
                self.h_equal()

            elif token in [self.T__5]:
                self.state = 569 
                self.h_inequal()

            else:
                raise NoViableAltException(self)

            self.state = 572 
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_dot(self):
            return self.getTypedRuleContext(AALParser.H_dotContext,0)


        def h_rbar(self):
            return self.getTypedRuleContext(AALParser.H_rbarContext,0)


        def h_lbar(self):
            return self.getTypedRuleContext(AALParser.H_lbarContext,0)


        def M_purpose(self):
            return self.getToken(AALParser.M_purpose, 0)

        def h_rpar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_rparContext)
            else:
                return self.getTypedRuleContext(AALParser.H_rparContext,i)


        def time(self):
            return self.getTypedRuleContext(AALParser.TimeContext,0)


        def exp(self):
            return self.getTypedRuleContext(AALParser.ExpContext,0)


        def h_agentId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_agentIdContext)
            else:
                return self.getTypedRuleContext(AALParser.H_agentIdContext,i)


        def h_lpar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_lparContext)
            else:
                return self.getTypedRuleContext(AALParser.H_lparContext,i)


        def h_purposeId(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_purposeIdContext)
            else:
                return self.getTypedRuleContext(AALParser.H_purposeIdContext,i)


        def h_serviceId(self):
            return self.getTypedRuleContext(AALParser.H_serviceIdContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAction(self)




    def action(self):

        localctx = AALParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574 
            self.h_agentId()
            self.state = 575 
            self.h_dot()

            self.state = 576 
            self.h_serviceId()
            self.state = 583
            _la = self._input.LA(1)
            if _la==AALParser.T__9:
                self.state = 577 
                self.h_lbar()
                self.state = 579
                _la = self._input.LA(1)
                if _la==AALParser.ID:
                    self.state = 578 
                    self.h_agentId()


                self.state = 581 
                self.h_rbar()


            self.state = 585 
            self.h_lpar()
            self.state = 587
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__8) | (1 << self.T__0) | (1 << self.ID) | (1 << self.INT))) != 0):
                self.state = 586 
                self.exp()


            self.state = 589 
            self.h_rpar()
            self.state = 591
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 590 
                self.time(0)


            self.state = 603
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 593
                self.match(self.M_purpose)
                self.state = 594 
                self.h_lpar()
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 595 
                    self.h_purposeId()
                    self.state = 600
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 601 
                self.h_rpar()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def T_mustnot(self):
            return self.getToken(AALParser.T_mustnot, 0)

        def T_sometime(self):
            return self.getToken(AALParser.T_sometime, 0)

        def T_never(self):
            return self.getToken(AALParser.T_never, 0)

        def T_always(self):
            return self.getToken(AALParser.T_always, 0)

        def T_must(self):
            return self.getToken(AALParser.T_must, 0)

        def getRuleIndex(self):
            return AALParser.RULE_modal

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterModal(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitModal(self)




    def modal(self):

        localctx = AALParser.ModalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_modal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T_must) | (1 << self.T_mustnot) | (1 << self.T_always) | (1 << self.T_never) | (1 << self.T_sometime))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def O_and(self):
            return self.getToken(AALParser.O_and, 0)

        def h_date(self):
            return self.getTypedRuleContext(AALParser.H_dateContext,0)


        def O_or(self):
            return self.getToken(AALParser.O_or, 0)

        def time(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.TimeContext)
            else:
                return self.getTypedRuleContext(AALParser.TimeContext,i)


        def O_after(self):
            return self.getToken(AALParser.O_after, 0)

        def O_before(self):
            return self.getToken(AALParser.O_before, 0)

        def getRuleIndex(self):
            return AALParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitTime(self)



    def time(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AALParser.TimeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_time, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            _la = self._input.LA(1)
            if not(_la==AALParser.O_after or _la==AALParser.O_before):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 609 
            self.h_date()
            self._ctx.stop = self._input.LT(-1)
            self.state = 616
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AALParser.TimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_time)
                    self.state = 611
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 612
                    _la = self._input.LA(1)
                    if not(_la==AALParser.O_or or _la==AALParser.O_and):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 613 
                    self.time(2) 
                self.state = 618
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MacroContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def M_macro(self):
            return self.getToken(AALParser.M_macro, 0)

        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(AALParser.ArgsContext,0)


        def MCODE(self):
            return self.getToken(AALParser.MCODE, 0)

        def getRuleIndex(self):
            return AALParser.RULE_macro

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterMacro(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitMacro(self)




    def macro(self):

        localctx = AALParser.MacroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(self.M_macro)
            self.state = 620
            self.match(self.ID)
            self.state = 622
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.state = 621 
                self.args()


            self.state = 624 
            self.h_lpar()
            self.state = 625
            self.match(self.MCODE)
            self.state = 626 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.ID)
            else:
                return self.getToken(AALParser.ID, i)

        def getRuleIndex(self):
            return AALParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitArgs(self)




    def args(self):

        localctx = AALParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628 
            self.h_lpar()
            self.state = 632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 629
                self.match(self.ID)
                self.state = 634
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 635 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MacroCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.STRING)
            else:
                return self.getToken(AALParser.STRING, i)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def M_call(self):
            return self.getToken(AALParser.M_call, 0)

        def getRuleIndex(self):
            return AALParser.RULE_macroCall

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterMacroCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitMacroCall(self)




    def macroCall(self):

        localctx = AALParser.MacroCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_macroCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.match(self.M_call)
            self.state = 638
            self.match(self.ID)
            self.state = 639 
            self.h_lpar()
            self.state = 643
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.STRING:
                self.state = 640
                self.match(self.STRING)
                self.state = 645
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 646 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def M_exec(self):
            return self.getToken(AALParser.M_exec, 0)

        def MCODE(self):
            return self.getToken(AALParser.MCODE, 0)

        def getRuleIndex(self):
            return AALParser.RULE_exec

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterExec(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitExec(self)




    def exec(self):

        localctx = AALParser.ExecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_exec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self.match(self.M_exec)
            self.state = 649
            self.match(self.MCODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoadlibContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AALParser.STRING, 0)

        def M_load(self):
            return self.getToken(AALParser.M_load, 0)

        def getRuleIndex(self):
            return AALParser.RULE_loadlib

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterLoadlib(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitLoadlib(self)




    def loadlib(self):

        localctx = AALParser.LoadlibContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_loadlib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.match(self.M_load)
            self.state = 652
            self.match(self.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LtlCheckContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def M_check(self):
            return self.getToken(AALParser.M_check, 0)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def check(self):
            return self.getTypedRuleContext(AALParser.CheckContext,0)


        def args(self):
            return self.getTypedRuleContext(AALParser.ArgsContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_ltlCheck

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterLtlCheck(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitLtlCheck(self)




    def ltlCheck(self):

        localctx = AALParser.LtlCheckContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_ltlCheck)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(self.M_check)
            self.state = 655
            self.match(self.ID)
            self.state = 657
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 656 
                self.args()


            self.state = 659 
            self.h_lpar()
            self.state = 660 
            self.check()
            self.state = 661 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CheckContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formula(self):
            return self.getTypedRuleContext(AALParser.FormulaContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_check

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterCheck(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitCheck(self)




    def check(self):

        localctx = AALParser.CheckContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_check)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 663 
            self.formula(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CheckApplyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.STRING)
            else:
                return self.getToken(AALParser.STRING, i)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def ID(self):
            return self.getToken(AALParser.ID, 0)

        def M_apply(self):
            return self.getToken(AALParser.M_apply, 0)

        def getRuleIndex(self):
            return AALParser.RULE_checkApply

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterCheckApply(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitCheckApply(self)




    def checkApply(self):

        localctx = AALParser.CheckApplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_checkApply)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.match(self.M_apply)
            self.state = 666
            self.match(self.ID)
            self.state = 667 
            self.h_lpar()
            self.state = 671
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.STRING:
                self.state = 668
                self.match(self.STRING)
                self.state = 673
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 674 
            self.h_rpar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def h_dot(self):
            return self.getTypedRuleContext(AALParser.H_dotContext,0)


        def PREDICATE(self):
            return self.getToken(AALParser.PREDICATE, 0)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def C_rectification(self):
            return self.getToken(AALParser.C_rectification, 0)

        def h_clauseId(self):
            return self.getTypedRuleContext(AALParser.H_clauseIdContext,0)


        def C_audit(self):
            return self.getToken(AALParser.C_audit, 0)

        def C_usage(self):
            return self.getToken(AALParser.C_usage, 0)

        def C_clause(self):
            return self.getToken(AALParser.C_clause, 0)

        def getRuleIndex(self):
            return AALParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitAtom(self)




    def atom(self):

        localctx = AALParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 686
            token = self._input.LA(1)
            if token in [self.C_clause]:
                self.enterOuterAlt(localctx, 1)
                self.state = 676
                self.match(self.C_clause)
                self.state = 677 
                self.h_lpar()
                self.state = 678 
                self.h_clauseId()
                self.state = 679 
                self.h_rpar()
                self.state = 683
                la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                if la_ == 1:
                    self.state = 680 
                    self.h_dot()
                    self.state = 681
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.C_usage) | (1 << self.C_audit) | (1 << self.C_rectification))) != 0)):
                        self._errHandler.recoverInline(self)
                    self.consume()



            elif token in [self.PREDICATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 685
                self.match(self.PREDICATE)

            else:
                raise NoViableAltException(self)

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

        def NEGATION(self):
            return self.getToken(AALParser.NEGATION, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AALParser.NEWLINE)
            else:
                return self.getToken(AALParser.NEWLINE, i)

        def h_lpar(self):
            return self.getTypedRuleContext(AALParser.H_lparContext,0)


        def h_rpar(self):
            return self.getTypedRuleContext(AALParser.H_rparContext,0)


        def EQUIVALENCE(self):
            return self.getToken(AALParser.EQUIVALENCE, 0)

        def IMPLICATION(self):
            return self.getToken(AALParser.IMPLICATION, 0)

        def CONJUNCTION(self):
            return self.getToken(AALParser.CONJUNCTION, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.FormulaContext)
            else:
                return self.getTypedRuleContext(AALParser.FormulaContext,i)


        def DISJUNCTION(self):
            return self.getToken(AALParser.DISJUNCTION, 0)

        def CONSTANTS(self):
            return self.getToken(AALParser.CONSTANTS, 0)

        def atom(self):
            return self.getTypedRuleContext(AALParser.AtomContext,0)


        def getRuleIndex(self):
            return AALParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitFormula(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AALParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 160
        self.enterRecursionRule(localctx, 160, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            token = self._input.LA(1)
            if token in [self.CONSTANTS]:
                self.state = 689
                self.match(self.CONSTANTS)
                self.state = 693
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 690
                        self.match(self.NEWLINE) 
                    self.state = 695
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,60,self._ctx)


            elif token in [self.C_clause, self.PREDICATE]:
                self.state = 696 
                self.atom()
                self.state = 700
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 697
                        self.match(self.NEWLINE) 
                    self.state = 702
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)


            elif token in [self.NEGATION]:
                self.state = 703
                self.match(self.NEGATION)
                self.state = 704 
                self.formula(0)
                self.state = 708
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 705
                        self.match(self.NEWLINE) 
                    self.state = 710
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,62,self._ctx)


            elif token in [self.T__6]:
                self.state = 711 
                self.h_lpar()
                self.state = 712 
                self.formula(0)
                self.state = 713 
                self.h_rpar()
                self.state = 717
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 714
                        self.match(self.NEWLINE) 
                    self.state = 719
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,63,self._ctx)


            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 753
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 751
                    la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                    if la_ == 1:
                        localctx = AALParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 722
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 726
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==AALParser.NEWLINE:
                            self.state = 723
                            self.match(self.NEWLINE)
                            self.state = 728
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 729 
                        self.formula(2)
                        pass

                    elif la_ == 2:
                        localctx = AALParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 730
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 734
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==AALParser.NEWLINE:
                            self.state = 731
                            self.match(self.NEWLINE)
                            self.state = 736
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 737
                        _la = self._input.LA(1)
                        if not(((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & ((1 << (self.CONJUNCTION - 71)) | (1 << (self.DISJUNCTION - 71)) | (1 << (self.IMPLICATION - 71)) | (1 << (self.EQUIVALENCE - 71)))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 741
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==AALParser.NEWLINE:
                            self.state = 738
                            self.match(self.NEWLINE)
                            self.state = 743
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 744 
                        self.formula(0)
                        self.state = 748
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,68,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 745
                                self.match(self.NEWLINE) 
                            self.state = 750
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,68,self._ctx)

                        pass

             
                self.state = 755
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[51] = self.actionExp_sempred
        self._predicates[65] = self.condition_sempred
        self._predicates[70] = self.time_sempred
        self._predicates[80] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def time_sempred(self, localctx:TimeContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def actionExp_sempred(self, localctx:ActionExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         



