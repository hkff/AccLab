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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3L")
        buf.write("\u02ea\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\5\r\u00b9\n\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\5\27\u00d1\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\5\31\u00db\n\31\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u00e1\n\32\3\33\3\33\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u00e9\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u00fc\n\37\f\37\16\37\u00ff\13\37\3 \3 \3 \3 \3 \5 \u0106")
        buf.write("\n \3 \5 \u0109\n \3!\3!\3!\3!\3!\7!\u0110\n!\f!\16!\u0113")
        buf.write("\13!\3!\3!\3!\3!\3!\3!\3!\5!\u011c\n!\5!\u011e\n!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\7\"\u0125\n\"\f\"\16\"\u0128\13\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0131\n\"\3\"\3\"\5\"\u0135")
        buf.write("\n\"\3#\3#\3#\7#\u013a\n#\f#\16#\u013d\13#\3#\3#\3$\3")
        buf.write("$\3$\7$\u0144\n$\f$\16$\u0147\13$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\7%\u0150\n%\f%\16%\u0153\13%\3%\3%\5%\u0157\n%\3%\3")
        buf.write("%\3%\7%\u015c\n%\f%\16%\u015f\13%\3%\3%\5%\u0163\n%\3")
        buf.write("&\3&\3&\7&\u0168\n&\f&\16&\u016b\13&\3\'\3\'\3\'\7\'\u0170")
        buf.write("\n\'\f\'\16\'\u0173\13\'\3\'\3\'\3(\3(\3(\5(\u017a\n(")
        buf.write("\3(\5(\u017d\n(\3(\5(\u0180\n(\3)\3)\3)\7)\u0185\n)\f")
        buf.write(")\16)\u0188\13)\3)\3)\3*\3*\3*\7*\u018f\n*\f*\16*\u0192")
        buf.write("\13*\3*\3*\3+\3+\3+\7+\u0199\n+\f+\16+\u019c\13+\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3/\3/\5/\u01ab\n/\3/\3/\5")
        buf.write("/\u01af\n/\5/\u01b1\n/\3/\3/\5/\u01b5\n/\5/\u01b7\n/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01cf\n\63\3\63\3\63\3\63\3\63\7\63\u01d5\n\63\f\63\16")
        buf.write("\63\u01d8\13\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\7:\u01ec\n:\f:")
        buf.write("\16:\u01ef\13:\3:\3:\3;\3;\3<\3<\3<\3<\5<\u01f9\n<\3=")
        buf.write("\3=\3>\3>\3>\5>\u0200\n>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\5?\u0210\n?\3@\3@\3@\3@\3@\3@\3@\5@\u0219")
        buf.write("\n@\3A\3A\3A\5A\u021e\nA\3A\3A\3A\7A\u0223\nA\fA\16A\u0226")
        buf.write("\13A\3B\5B\u0229\nB\3B\3B\3C\3C\3C\5C\u0230\nC\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\5D\u0239\nD\3D\3D\5D\u023d\nD\3D\3D\5D\u0241")
        buf.write("\nD\3D\3D\5D\u0245\nD\3D\3D\3D\7D\u024a\nD\fD\16D\u024d")
        buf.write("\13D\3D\3D\5D\u0251\nD\3E\3E\3F\3F\3F\3F\3F\3F\3F\7F\u025c")
        buf.write("\nF\fF\16F\u025f\13F\3G\3G\3G\5G\u0264\nG\3G\3G\3G\3G")
        buf.write("\3H\3H\7H\u026c\nH\fH\16H\u026f\13H\3H\3H\3I\3I\3I\3I")
        buf.write("\7I\u0277\nI\fI\16I\u027a\13I\3I\3I\3J\3J\3J\3K\3K\3K")
        buf.write("\3L\3L\3L\5L\u0287\nL\3L\3L\3L\3L\3M\3M\3N\3N\3N\3N\7")
        buf.write("N\u0293\nN\fN\16N\u0296\13N\3N\3N\3O\3O\3O\3O\3O\3O\3")
        buf.write("O\5O\u02a1\nO\3O\5O\u02a4\nO\3P\3P\3P\7P\u02a9\nP\fP\16")
        buf.write("P\u02ac\13P\3P\3P\7P\u02b0\nP\fP\16P\u02b3\13P\3P\3P\3")
        buf.write("P\7P\u02b8\nP\fP\16P\u02bb\13P\3P\3P\3P\3P\7P\u02c1\n")
        buf.write("P\fP\16P\u02c4\13P\5P\u02c6\nP\3P\3P\7P\u02ca\nP\fP\16")
        buf.write("P\u02cd\13P\3P\3P\3P\7P\u02d2\nP\fP\16P\u02d5\13P\3P\3")
        buf.write("P\7P\u02d9\nP\fP\16P\u02dc\13P\3P\3P\7P\u02e0\nP\fP\16")
        buf.write("P\u02e3\13P\7P\u02e5\nP\fP\16P\u02e8\13P\3P\2\6d\u0080")
        buf.write("\u008a\u009eQ\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtv")
        buf.write("xz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\u0098\u009a\u009c\u009e\2\n\3\2)*\4")
        buf.write("\2\26\30$%\3\2\'(\3\2\26\27\3\2\37#\3\2\35\36\3\29;\3")
        buf.write("\2GJ\u02f5\2\u00a0\3\2\2\2\4\u00a2\3\2\2\2\6\u00a4\3\2")
        buf.write("\2\2\b\u00a6\3\2\2\2\n\u00a8\3\2\2\2\f\u00aa\3\2\2\2\16")
        buf.write("\u00ac\3\2\2\2\20\u00ae\3\2\2\2\22\u00b0\3\2\2\2\24\u00b2")
        buf.write("\3\2\2\2\26\u00b4\3\2\2\2\30\u00b8\3\2\2\2\32\u00ba\3")
        buf.write("\2\2\2\34\u00bc\3\2\2\2\36\u00be\3\2\2\2 \u00c0\3\2\2")
        buf.write("\2\"\u00c2\3\2\2\2$\u00c4\3\2\2\2&\u00c6\3\2\2\2(\u00c8")
        buf.write("\3\2\2\2*\u00ca\3\2\2\2,\u00d0\3\2\2\2.\u00d2\3\2\2\2")
        buf.write("\60\u00da\3\2\2\2\62\u00e0\3\2\2\2\64\u00e2\3\2\2\2\66")
        buf.write("\u00e4\3\2\2\28\u00ea\3\2\2\2:\u00f0\3\2\2\2<\u00fd\3")
        buf.write("\2\2\2>\u0105\3\2\2\2@\u010a\3\2\2\2B\u011f\3\2\2\2D\u0136")
        buf.write("\3\2\2\2F\u0140\3\2\2\2H\u014a\3\2\2\2J\u0164\3\2\2\2")
        buf.write("L\u016c\3\2\2\2N\u0176\3\2\2\2P\u0181\3\2\2\2R\u018b\3")
        buf.write("\2\2\2T\u0195\3\2\2\2V\u019f\3\2\2\2X\u01a1\3\2\2\2Z\u01a3")
        buf.write("\3\2\2\2\\\u01a5\3\2\2\2^\u01ba\3\2\2\2`\u01bc\3\2\2\2")
        buf.write("b\u01bf\3\2\2\2d\u01ce\3\2\2\2f\u01d9\3\2\2\2h\u01db\3")
        buf.write("\2\2\2j\u01de\3\2\2\2l\u01e3\3\2\2\2n\u01e5\3\2\2\2p\u01e7")
        buf.write("\3\2\2\2r\u01e9\3\2\2\2t\u01f2\3\2\2\2v\u01f4\3\2\2\2")
        buf.write("x\u01fa\3\2\2\2z\u01fc\3\2\2\2|\u020f\3\2\2\2~\u0218\3")
        buf.write("\2\2\2\u0080\u021d\3\2\2\2\u0082\u0228\3\2\2\2\u0084\u022c")
        buf.write("\3\2\2\2\u0086\u0233\3\2\2\2\u0088\u0252\3\2\2\2\u008a")
        buf.write("\u0254\3\2\2\2\u008c\u0260\3\2\2\2\u008e\u0269\3\2\2\2")
        buf.write("\u0090\u0272\3\2\2\2\u0092\u027d\3\2\2\2\u0094\u0280\3")
        buf.write("\2\2\2\u0096\u0283\3\2\2\2\u0098\u028c\3\2\2\2\u009a\u028e")
        buf.write("\3\2\2\2\u009c\u02a3\3\2\2\2\u009e\u02c5\3\2\2\2\u00a0")
        buf.write("\u00a1\7\7\2\2\u00a1\3\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3")
        buf.write("\5\3\2\2\2\u00a4\u00a5\7\6\2\2\u00a5\7\3\2\2\2\u00a6\u00a7")
        buf.write("\7\3\2\2\u00a7\t\3\2\2\2\u00a8\u00a9\7\5\2\2\u00a9\13")
        buf.write("\3\2\2\2\u00aa\u00ab\7\b\2\2\u00ab\r\3\2\2\2\u00ac\u00ad")
        buf.write("\7\n\2\2\u00ad\17\3\2\2\2\u00ae\u00af\7\f\2\2\u00af\21")
        buf.write("\3\2\2\2\u00b0\u00b1\7\13\2\2\u00b1\23\3\2\2\2\u00b2\u00b3")
        buf.write("\7=\2\2\u00b3\25\3\2\2\2\u00b4\u00b5\5\62\32\2\u00b5\27")
        buf.write("\3\2\2\2\u00b6\u00b9\5\"\22\2\u00b7\u00b9\5.\30\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\31\3\2\2\2\u00ba")
        buf.write("\u00bb\7=\2\2\u00bb\33\3\2\2\2\u00bc\u00bd\7=\2\2\u00bd")
        buf.write("\35\3\2\2\2\u00be\u00bf\7=\2\2\u00bf\37\3\2\2\2\u00c0")
        buf.write("\u00c1\7=\2\2\u00c1!\3\2\2\2\u00c2\u00c3\7B\2\2\u00c3")
        buf.write("#\3\2\2\2\u00c4\u00c5\7=\2\2\u00c5%\3\2\2\2\u00c6\u00c7")
        buf.write("\7=\2\2\u00c7\'\3\2\2\2\u00c8\u00c9\7=\2\2\u00c9)\3\2")
        buf.write("\2\2\u00ca\u00cb\7=\2\2\u00cb+\3\2\2\2\u00cc\u00cd\7C")
        buf.write("\2\2\u00cd\u00d1\7?\2\2\u00ce\u00cf\7D\2\2\u00cf\u00d1")
        buf.write("\7?\2\2\u00d0\u00cc\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("-\3\2\2\2\u00d2\u00d3\7>\2\2\u00d3\u00d4\7>\2\2\u00d4")
        buf.write("\u00d5\5\f\7\2\u00d5\u00d6\7>\2\2\u00d6\u00d7\7>\2\2\u00d7")
        buf.write("/\3\2\2\2\u00d8\u00db\5\62\32\2\u00d9\u00db\5\66\34\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\61\3\2")
        buf.write("\2\2\u00dc\u00e1\7>\2\2\u00dd\u00de\7\r\2\2\u00de\u00df")
        buf.write("\7B\2\2\u00df\u00e1\7\r\2\2\u00e0\u00dc\3\2\2\2\u00e0")
        buf.write("\u00dd\3\2\2\2\u00e1\63\3\2\2\2\u00e2\u00e3\7=\2\2\u00e3")
        buf.write("\65\3\2\2\2\u00e4\u00e8\7=\2\2\u00e5\u00e6\5\f\7\2\u00e6")
        buf.write("\u00e7\5\64\33\2\u00e7\u00e9\3\2\2\2\u00e8\u00e5\3\2\2")
        buf.write("\2\u00e8\u00e9\3\2\2\2\u00e9\67\3\2\2\2\u00ea\u00eb\7")
        buf.write("\t\2\2\u00eb\u00ec\7=\2\2\u00ec\u00ed\5\2\2\2\u00ed\u00ee")
        buf.write("\7=\2\2\u00ee\u00ef\5\4\3\2\u00ef9\3\2\2\2\u00f0\u00f1")
        buf.write("\5<\37\2\u00f1;\3\2\2\2\u00f2\u00fc\5\\/\2\u00f3\u00fc")
        buf.write("\5> \2\u00f4\u00fc\5,\27\2\u00f5\u00fc\5\u008cG\2\u00f6")
        buf.write("\u00fc\5\u0090I\2\u00f7\u00fc\5\u0094K\2\u00f8\u00fc\5")
        buf.write("\u0096L\2\u00f9\u00fc\5\u009aN\2\u00fa\u00fc\5\u0092J")
        buf.write("\2\u00fb\u00f2\3\2\2\2\u00fb\u00f3\3\2\2\2\u00fb\u00f4")
        buf.write("\3\2\2\2\u00fb\u00f5\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fb")
        buf.write("\u00f7\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3")
        buf.write("\2\2\2\u00fd\u00fe\3\2\2\2\u00fe=\3\2\2\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u0100\u0106\5@!\2\u0101\u0106\5H%\2\u0102\u0106")
        buf.write("\5B\"\2\u0103\u0106\5N(\2\u0104\u0106\5J&\2\u0105\u0100")
        buf.write("\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0102\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106\u0108\3\2\2\2")
        buf.write("\u0107\u0109\7?\2\2\u0108\u0107\3\2\2\2\u0108\u0109\3")
        buf.write("\2\2\2\u0109?\3\2\2\2\u010a\u010b\7\17\2\2\u010b\u011d")
        buf.write("\5\32\16\2\u010c\u010d\7\23\2\2\u010d\u0111\5\2\2\2\u010e")
        buf.write("\u0110\5V,\2\u010f\u010e\3\2\2\2\u0110\u0113\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0114\u011b\5\4\3\2\u0115\u0116\5")
        buf.write("D#\2\u0116\u0117\5F$\2\u0117\u011c\3\2\2\2\u0118\u0119")
        buf.write("\5F$\2\u0119\u011a\5D#\2\u011a\u011c\3\2\2\2\u011b\u0115")
        buf.write("\3\2\2\2\u011b\u0118\3\2\2\2\u011c\u011e\3\2\2\2\u011d")
        buf.write("\u010c\3\2\2\2\u011d\u011e\3\2\2\2\u011eA\3\2\2\2\u011f")
        buf.write("\u0120\7\20\2\2\u0120\u0121\5 \21\2\u0121\u0122\7\23\2")
        buf.write("\2\u0122\u0126\5\2\2\2\u0123\u0125\5Z.\2\u0124\u0123\3")
        buf.write("\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127")
        buf.write("\3\2\2\2\u0127\u0129\3\2\2\2\u0128\u0126\3\2\2\2\u0129")
        buf.write("\u0130\5\4\3\2\u012a\u012b\5D#\2\u012b\u012c\5F$\2\u012c")
        buf.write("\u0131\3\2\2\2\u012d\u012e\5F$\2\u012e\u012f\5D#\2\u012f")
        buf.write("\u0131\3\2\2\2\u0130\u012a\3\2\2\2\u0130\u012d\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0133\7")
        buf.write("+\2\2\u0133\u0135\5\32\16\2\u0134\u0132\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135C\3\2\2\2\u0136\u0137\7,\2\2\u0137")
        buf.write("\u013b\5\2\2\2\u0138\u013a\5&\24\2\u0139\u0138\3\2\2\2")
        buf.write("\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3")
        buf.write("\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f")
        buf.write("\5\4\3\2\u013fE\3\2\2\2\u0140\u0141\7-\2\2\u0141\u0145")
        buf.write("\5\2\2\2\u0142\u0144\5&\24\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149\5")
        buf.write("\4\3\2\u0149G\3\2\2\2\u014a\u014b\7\16\2\2\u014b\u0156")
        buf.write("\5&\24\2\u014c\u014d\7\23\2\2\u014d\u0151\5\2\2\2\u014e")
        buf.write("\u0150\5X-\2\u014f\u014e\3\2\2\2\u0150\u0153\3\2\2\2\u0151")
        buf.write("\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0154\3\2\2\2")
        buf.write("\u0153\u0151\3\2\2\2\u0154\u0155\5\4\3\2\u0155\u0157\3")
        buf.write("\2\2\2\u0156\u014c\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0162")
        buf.write("\3\2\2\2\u0158\u0159\7.\2\2\u0159\u015d\5\2\2\2\u015a")
        buf.write("\u015c\5$\23\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3")
        buf.write("\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\5\4\3\2\u0161\u0163")
        buf.write("\3\2\2\2\u0162\u0158\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("I\3\2\2\2\u0164\u0165\5\34\17\2\u0165\u0169\5\36\20\2")
        buf.write("\u0166\u0168\5L\'\2\u0167\u0166\3\2\2\2\u0168\u016b\3")
        buf.write("\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016aK")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\5*\26\2\u016d")
        buf.write("\u0171\5\2\2\2\u016e\u0170\7=\2\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175")
        buf.write("\5\4\3\2\u0175M\3\2\2\2\u0176\u0177\7\22\2\2\u0177\u0179")
        buf.write("\7=\2\2\u0178\u017a\5P)\2\u0179\u0178\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u017d\5R*\2\u017c\u017b")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3\2\2\2\u017e")
        buf.write("\u0180\5T+\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("O\3\2\2\2\u0181\u0182\7/\2\2\u0182\u0186\5\2\2\2\u0183")
        buf.write("\u0185\7=\2\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\5\4\3\2\u018aQ")
        buf.write("\3\2\2\2\u018b\u018c\7\60\2\2\u018c\u0190\5\2\2\2\u018d")
        buf.write("\u018f\7=\2\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\3")
        buf.write("\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\5\4\3\2\u0194S")
        buf.write("\3\2\2\2\u0195\u0196\7\61\2\2\u0196\u019a\5\2\2\2\u0197")
        buf.write("\u0199\7=\2\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d\3")
        buf.write("\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\5\4\3\2\u019eU")
        buf.write("\3\2\2\2\u019f\u01a0\7=\2\2\u01a0W\3\2\2\2\u01a1\u01a2")
        buf.write("\7=\2\2\u01a2Y\3\2\2\2\u01a3\u01a4\7=\2\2\u01a4[\3\2\2")
        buf.write("\2\u01a5\u01a6\7\21\2\2\u01a6\u01a7\5(\25\2\u01a7\u01a8")
        buf.write("\5\2\2\2\u01a8\u01aa\5^\60\2\u01a9\u01ab\7?\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01b0\3\2\2\2")
        buf.write("\u01ac\u01ae\5`\61\2\u01ad\u01af\7?\2\2\u01ae\u01ad\3")
        buf.write("\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ac")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b6\3\2\2\2\u01b2")
        buf.write("\u01b4\5b\62\2\u01b3\u01b5\7?\2\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b4\u01b5\3\2\2\2\u01b5\u01b7\3\2\2\2\u01b6\u01b2\3")
        buf.write("\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9")
        buf.write("\5\4\3\2\u01b9]\3\2\2\2\u01ba\u01bb\5d\63\2\u01bb_\3\2")
        buf.write("\2\2\u01bc\u01bd\7\24\2\2\u01bd\u01be\5^\60\2\u01bea\3")
        buf.write("\2\2\2\u01bf\u01c0\7\25\2\2\u01c0\u01c1\5^\60\2\u01c1")
        buf.write("c\3\2\2\2\u01c2\u01c3\b\63\1\2\u01c3\u01cf\5f\64\2\u01c4")
        buf.write("\u01cf\5h\65\2\u01c5\u01cf\5j\66\2\u01c6\u01cf\5l\67\2")
        buf.write("\u01c7\u01cf\5n8\2\u01c8\u01cf\5p9\2\u01c9\u01cf\5r:\2")
        buf.write("\u01ca\u01cb\5\2\2\2\u01cb\u01cc\5d\63\2\u01cc\u01cd\5")
        buf.write("\4\3\2\u01cd\u01cf\3\2\2\2\u01ce\u01c2\3\2\2\2\u01ce\u01c4")
        buf.write("\3\2\2\2\u01ce\u01c5\3\2\2\2\u01ce\u01c6\3\2\2\2\u01ce")
        buf.write("\u01c7\3\2\2\2\u01ce\u01c8\3\2\2\2\u01ce\u01c9\3\2\2\2")
        buf.write("\u01ce\u01ca\3\2\2\2\u01cf\u01d6\3\2\2\2\u01d0\u01d1\f")
        buf.write("\7\2\2\u01d1\u01d2\5x=\2\u01d2\u01d3\5d\63\b\u01d3\u01d5")
        buf.write("\3\2\2\2\u01d4\u01d0\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7e\3\2\2\2\u01d8")
        buf.write("\u01d6\3\2\2\2\u01d9\u01da\5\u0086D\2\u01dag\3\2\2\2\u01db")
        buf.write("\u01dc\7\33\2\2\u01dc\u01dd\5d\63\2\u01ddi\3\2\2\2\u01de")
        buf.write("\u01df\5\u0088E\2\u01df\u01e0\5\2\2\2\u01e0\u01e1\5d\63")
        buf.write("\2\u01e1\u01e2\5\4\3\2\u01e2k\3\2\2\2\u01e3\u01e4\5\u0080")
        buf.write("A\2\u01e4m\3\2\2\2\u01e5\u01e6\5z>\2\u01e6o\3\2\2\2\u01e7")
        buf.write("\u01e8\5|?\2\u01e8q\3\2\2\2\u01e9\u01ed\5v<\2\u01ea\u01ec")
        buf.write("\5v<\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f1\5d\63\2\u01f1s\3\2\2\2\u01f2")
        buf.write("\u01f3\t\2\2\2\u01f3u\3\2\2\2\u01f4\u01f5\5t;\2\u01f5")
        buf.write("\u01f8\5\66\34\2\u01f6\u01f7\7\34\2\2\u01f7\u01f9\5\u0080")
        buf.write("A\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9w\3\2")
        buf.write("\2\2\u01fa\u01fb\t\3\2\2\u01fby\3\2\2\2\u01fc\u01fd\t")
        buf.write("\4\2\2\u01fd\u01ff\5\u0086D\2\u01fe\u0200\7?\2\2\u01ff")
        buf.write("\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200{\3\2\2\2\u0201")
        buf.write("\u0202\7\32\2\2\u0202\u0203\5\2\2\2\u0203\u0204\5d\63")
        buf.write("\2\u0204\u0205\5\4\3\2\u0205\u0206\7\31\2\2\u0206\u0207")
        buf.write("\5\2\2\2\u0207\u0208\5d\63\2\u0208\u0209\5\4\3\2\u0209")
        buf.write("\u0210\3\2\2\2\u020a\u020b\7\32\2\2\u020b\u020c\5d\63")
        buf.write("\2\u020c\u020d\7\31\2\2\u020d\u020e\5d\63\2\u020e\u0210")
        buf.write("\3\2\2\2\u020f\u0201\3\2\2\2\u020f\u020a\3\2\2\2\u0210")
        buf.write("}\3\2\2\2\u0211\u0219\5\66\34\2\u0212\u0219\5\62\32\2")
        buf.write("\u0213\u0219\58\35\2\u0214\u0215\7=\2\2\u0215\u0216\5")
        buf.write("\n\6\2\u0216\u0217\5*\26\2\u0217\u0219\3\2\2\2\u0218\u0211")
        buf.write("\3\2\2\2\u0218\u0212\3\2\2\2\u0218\u0213\3\2\2\2\u0218")
        buf.write("\u0214\3\2\2\2\u0219\177\3\2\2\2\u021a\u021b\bA\1\2\u021b")
        buf.write("\u021e\5\u0082B\2\u021c\u021e\5\u0084C\2\u021d\u021a\3")
        buf.write("\2\2\2\u021d\u021c\3\2\2\2\u021e\u0224\3\2\2\2\u021f\u0220")
        buf.write("\f\3\2\2\u0220\u0221\t\5\2\2\u0221\u0223\5\u0080A\4\u0222")
        buf.write("\u021f\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0081\3\2\2\2\u0226\u0224\3")
        buf.write("\2\2\2\u0227\u0229\7\33\2\2\u0228\u0227\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\5~@\2\u022b")
        buf.write("\u0083\3\2\2\2\u022c\u022f\5~@\2\u022d\u0230\5\16\b\2")
        buf.write("\u022e\u0230\5\20\t\2\u022f\u022d\3\2\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\5~@\2\u0232\u0085")
        buf.write("\3\2\2\2\u0233\u0234\5\32\16\2\u0234\u0235\5\n\6\2\u0235")
        buf.write("\u023c\5&\24\2\u0236\u0238\5\6\4\2\u0237\u0239\5\32\16")
        buf.write("\2\u0238\u0237\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a")
        buf.write("\3\2\2\2\u023a\u023b\5\b\5\2\u023b\u023d\3\2\2\2\u023c")
        buf.write("\u0236\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2")
        buf.write("\u023e\u0240\5\2\2\2\u023f\u0241\5~@\2\u0240\u023f\3\2")
        buf.write("\2\2\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0244")
        buf.write("\5\4\3\2\u0243\u0245\5\u008aF\2\u0244\u0243\3\2\2\2\u0244")
        buf.write("\u0245\3\2\2\2\u0245\u0250\3\2\2\2\u0246\u0247\7.\2\2")
        buf.write("\u0247\u024b\5\2\2\2\u0248\u024a\5$\23\2\u0249\u0248\3")
        buf.write("\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\u024e\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write("\u024f\5\4\3\2\u024f\u0251\3\2\2\2\u0250\u0246\3\2\2\2")
        buf.write("\u0250\u0251\3\2\2\2\u0251\u0087\3\2\2\2\u0252\u0253\t")
        buf.write("\6\2\2\u0253\u0089\3\2\2\2\u0254\u0255\bF\1\2\u0255\u0256")
        buf.write("\t\7\2\2\u0256\u0257\5\"\22\2\u0257\u025d\3\2\2\2\u0258")
        buf.write("\u0259\f\3\2\2\u0259\u025a\t\5\2\2\u025a\u025c\5\u008a")
        buf.write("F\4\u025b\u0258\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b")
        buf.write("\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u008b\3\2\2\2\u025f")
        buf.write("\u025d\3\2\2\2\u0260\u0261\7\62\2\2\u0261\u0263\7=\2\2")
        buf.write("\u0262\u0264\5\u008eH\2\u0263\u0262\3\2\2\2\u0263\u0264")
        buf.write("\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0266\5\2\2\2\u0266")
        buf.write("\u0267\7E\2\2\u0267\u0268\5\4\3\2\u0268\u008d\3\2\2\2")
        buf.write("\u0269\u026d\5\2\2\2\u026a\u026c\7=\2\2\u026b\u026a\3")
        buf.write("\2\2\2\u026c\u026f\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e")
        buf.write("\3\2\2\2\u026e\u0270\3\2\2\2\u026f\u026d\3\2\2\2\u0270")
        buf.write("\u0271\5\4\3\2\u0271\u008f\3\2\2\2\u0272\u0273\7\63\2")
        buf.write("\2\u0273\u0274\7=\2\2\u0274\u0278\5\2\2\2\u0275\u0277")
        buf.write("\7B\2\2\u0276\u0275\3\2\2\2\u0277\u027a\3\2\2\2\u0278")
        buf.write("\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027b\3\2\2\2")
        buf.write("\u027a\u0278\3\2\2\2\u027b\u027c\5\4\3\2\u027c\u0091\3")
        buf.write("\2\2\2\u027d\u027e\7\67\2\2\u027e\u027f\7E\2\2\u027f\u0093")
        buf.write("\3\2\2\2\u0280\u0281\7\64\2\2\u0281\u0282\7B\2\2\u0282")
        buf.write("\u0095\3\2\2\2\u0283\u0284\7\65\2\2\u0284\u0286\7=\2\2")
        buf.write("\u0285\u0287\5\u008eH\2\u0286\u0285\3\2\2\2\u0286\u0287")
        buf.write("\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u0289\5\2\2\2\u0289")
        buf.write("\u028a\5\u0098M\2\u028a\u028b\5\4\3\2\u028b\u0097\3\2")
        buf.write("\2\2\u028c\u028d\5\u009eP\2\u028d\u0099\3\2\2\2\u028e")
        buf.write("\u028f\7\66\2\2\u028f\u0290\7=\2\2\u0290\u0294\5\2\2\2")
        buf.write("\u0291\u0293\7B\2\2\u0292\u0291\3\2\2\2\u0293\u0296\3")
        buf.write("\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2\2\2\u0295\u0297")
        buf.write("\3\2\2\2\u0296\u0294\3\2\2\2\u0297\u0298\5\4\3\2\u0298")
        buf.write("\u009b\3\2\2\2\u0299\u029a\78\2\2\u029a\u029b\5\2\2\2")
        buf.write("\u029b\u029c\5(\25\2\u029c\u02a0\5\4\3\2\u029d\u029e\5")
        buf.write("\n\6\2\u029e\u029f\t\b\2\2\u029f\u02a1\3\2\2\2\u02a0\u029d")
        buf.write("\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1\u02a4\3\2\2\2\u02a2")
        buf.write("\u02a4\7L\2\2\u02a3\u0299\3\2\2\2\u02a3\u02a2\3\2\2\2")
        buf.write("\u02a4\u009d\3\2\2\2\u02a5\u02a6\bP\1\2\u02a6\u02aa\7")
        buf.write("K\2\2\u02a7\u02a9\7?\2\2\u02a8\u02a7\3\2\2\2\u02a9\u02ac")
        buf.write("\3\2\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab")
        buf.write("\u02c6\3\2\2\2\u02ac\u02aa\3\2\2\2\u02ad\u02b1\5\u009c")
        buf.write("O\2\u02ae\u02b0\7?\2\2\u02af\u02ae\3\2\2\2\u02b0\u02b3")
        buf.write("\3\2\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2\3\2\2\2\u02b2")
        buf.write("\u02c6\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b4\u02b5\7F\2\2")
        buf.write("\u02b5\u02b9\5\u009eP\2\u02b6\u02b8\7?\2\2\u02b7\u02b6")
        buf.write("\3\2\2\2\u02b8\u02bb\3\2\2\2\u02b9\u02b7\3\2\2\2\u02b9")
        buf.write("\u02ba\3\2\2\2\u02ba\u02c6\3\2\2\2\u02bb\u02b9\3\2\2\2")
        buf.write("\u02bc\u02bd\5\2\2\2\u02bd\u02be\5\u009eP\2\u02be\u02c2")
        buf.write("\5\4\3\2\u02bf\u02c1\7?\2\2\u02c0\u02bf\3\2\2\2\u02c1")
        buf.write("\u02c4\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2")
        buf.write("\u02c3\u02c6\3\2\2\2\u02c4\u02c2\3\2\2\2\u02c5\u02a5\3")
        buf.write("\2\2\2\u02c5\u02ad\3\2\2\2\u02c5\u02b4\3\2\2\2\u02c5\u02bc")
        buf.write("\3\2\2\2\u02c6\u02e6\3\2\2\2\u02c7\u02cb\f\3\2\2\u02c8")
        buf.write("\u02ca\7?\2\2\u02c9\u02c8\3\2\2\2\u02ca\u02cd\3\2\2\2")
        buf.write("\u02cb\u02c9\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02ce\3")
        buf.write("\2\2\2\u02cd\u02cb\3\2\2\2\u02ce\u02e5\5\u009eP\4\u02cf")
        buf.write("\u02d3\f\6\2\2\u02d0\u02d2\7?\2\2\u02d1\u02d0\3\2\2\2")
        buf.write("\u02d2\u02d5\3\2\2\2\u02d3\u02d1\3\2\2\2\u02d3\u02d4\3")
        buf.write("\2\2\2\u02d4\u02d6\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d6\u02da")
        buf.write("\t\t\2\2\u02d7\u02d9\7?\2\2\u02d8\u02d7\3\2\2\2\u02d9")
        buf.write("\u02dc\3\2\2\2\u02da\u02d8\3\2\2\2\u02da\u02db\3\2\2\2")
        buf.write("\u02db\u02dd\3\2\2\2\u02dc\u02da\3\2\2\2\u02dd\u02e1\5")
        buf.write("\u009eP\2\u02de\u02e0\7?\2\2\u02df\u02de\3\2\2\2\u02e0")
        buf.write("\u02e3\3\2\2\2\u02e1\u02df\3\2\2\2\u02e1\u02e2\3\2\2\2")
        buf.write("\u02e2\u02e5\3\2\2\2\u02e3\u02e1\3\2\2\2\u02e4\u02c7\3")
        buf.write("\2\2\2\u02e4\u02cf\3\2\2\2\u02e5\u02e8\3\2\2\2\u02e6\u02e4")
        buf.write("\3\2\2\2\u02e6\u02e7\3\2\2\2\u02e7\u009f\3\2\2\2\u02e8")
        buf.write("\u02e6\3\2\2\2H\u00b8\u00d0\u00da\u00e0\u00e8\u00fb\u00fd")
        buf.write("\u0105\u0108\u0111\u011b\u011d\u0126\u0130\u0134\u013b")
        buf.write("\u0145\u0151\u0156\u015d\u0162\u0169\u0171\u0179\u017c")
        buf.write("\u017f\u0186\u0190\u019a\u01aa\u01ae\u01b0\u01b4\u01b6")
        buf.write("\u01ce\u01d6\u01ed\u01f8\u01ff\u020f\u0218\u021d\u0224")
        buf.write("\u0228\u022f\u0238\u023c\u0240\u0244\u024b\u0250\u025d")
        buf.write("\u0263\u026d\u0278\u0286\u0294\u02a0\u02a3\u02aa\u02b1")
        buf.write("\u02b9\u02c2\u02c5\u02cb\u02d3\u02da\u02e1\u02e4\u02e6")
        return buf.getvalue()
		

class AALParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    T__10=1
    T__9=2
    T__8=3
    T__7=4
    T__6=5
    T__5=6
    T__4=7
    T__3=8
    T__2=9
    T__1=10
    T__0=11
    D_service=12
    D_agent=13
    D_data=14
    D_clause=15
    D_type=16
    D_types=17
    C_auditing=18
    C_ifviolated=19
    O_or=20
    O_and=21
    O_onlywhen=22
    O_then=23
    O_if=24
    O_not=25
    O_where=26
    O_after=27
    O_before=28
    T_must=29
    T_mustnot=30
    T_always=31
    T_never=32
    T_sometime=33
    T_until=34
    T_unless=35
    T_next=36
    A_permit=37
    A_deny=38
    Q_forall=39
    Q_exists=40
    M_subject=41
    M_rservice=42
    M_pservice=43
    M_purpose=44
    M_extends=45
    M_attr=46
    M_actions=47
    M_macro=48
    M_call=49
    M_load=50
    M_check=51
    M_apply=52
    M_exec=53
    C_clause=54
    C_usage=55
    C_audit=56
    C_rectification=57
    C_violation=58
    ID=59
    INT=60
    NEWLINE=61
    WS=62
    BLANK=63
    STRING=64
    COMMENT=65
    MLCOMMENT=66
    MCODE=67
    NEGATION=68
    CONJUNCTION=69
    DISJUNCTION=70
    IMPLICATION=71
    EQUIVALENCE=72
    CONSTANTS=73
    PREDICATE=74

    tokenNames = [ "<INVALID>", "']'", "')'", "'.'", "'['", "'('", "':'", 
                   "'@'", "'=='", "'/'", "'!='", "'\"'", "D_service", "D_agent", 
                   "D_data", "D_clause", "D_type", "D_types", "C_auditing", 
                   "C_ifviolated", "O_or", "O_and", "O_onlywhen", "O_then", 
                   "O_if", "O_not", "O_where", "O_after", "O_before", "T_must", 
                   "T_mustnot", "T_always", "T_never", "T_sometime", "T_until", 
                   "T_unless", "T_next", "A_permit", "A_deny", "Q_forall", 
                   "Q_exists", "M_subject", "M_rservice", "M_pservice", 
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
    RULE_h_dot = 4
    RULE_h_colon = 5
    RULE_h_equal = 6
    RULE_h_inequal = 7
    RULE_h_slash = 8
    RULE_h_data = 9
    RULE_h_value = 10
    RULE_h_time = 11
    RULE_h_agentId = 12
    RULE_h_varTypeId = 13
    RULE_h_varId = 14
    RULE_h_dataId = 15
    RULE_h_date = 16
    RULE_h_purposeId = 17
    RULE_h_serviceId = 18
    RULE_h_clauseId = 19
    RULE_h_attribute = 20
    RULE_h_comment = 21
    RULE_h_duration = 22
    RULE_h_parameters = 23
    RULE_h_constant = 24
    RULE_h_type = 25
    RULE_h_variable = 26
    RULE_h_predicate = 27
    RULE_main = 28
    RULE_aalprog = 29
    RULE_declaration = 30
    RULE_agentDec = 31
    RULE_dataDec = 32
    RULE_rsService = 33
    RULE_psService = 34
    RULE_serviceDec = 35
    RULE_varDec = 36
    RULE_attrValue = 37
    RULE_typeDec = 38
    RULE_type_super = 39
    RULE_type_attr = 40
    RULE_type_actions = 41
    RULE_agentType = 42
    RULE_serviceType = 43
    RULE_dataType = 44
    RULE_clause = 45
    RULE_usage = 46
    RULE_audit = 47
    RULE_rectification = 48
    RULE_actionExp = 49
    RULE_actionExp1Action = 50
    RULE_actionExp2notAction = 51
    RULE_actionExp3modalAction = 52
    RULE_actionExp4condition = 53
    RULE_actionExp6Author = 54
    RULE_actionExp7ifthen = 55
    RULE_actionExp8qvar = 56
    RULE_quant = 57
    RULE_qvar = 58
    RULE_booleanOp = 59
    RULE_author = 60
    RULE_ifthen = 61
    RULE_exp = 62
    RULE_condition = 63
    RULE_condition1notExp = 64
    RULE_condition2cmpExp = 65
    RULE_action = 66
    RULE_modal = 67
    RULE_time = 68
    RULE_macro = 69
    RULE_args = 70
    RULE_macroCall = 71
    RULE_exec = 72
    RULE_loadlib = 73
    RULE_ltlCheck = 74
    RULE_check = 75
    RULE_checkApply = 76
    RULE_atom = 77
    RULE_formula = 78

    ruleNames =  [ "h_lpar", "h_rpar", "h_lbar", "h_rbar", "h_dot", "h_colon", 
                   "h_equal", "h_inequal", "h_slash", "h_data", "h_value", 
                   "h_time", "h_agentId", "h_varTypeId", "h_varId", "h_dataId", 
                   "h_date", "h_purposeId", "h_serviceId", "h_clauseId", 
                   "h_attribute", "h_comment", "h_duration", "h_parameters", 
                   "h_constant", "h_type", "h_variable", "h_predicate", 
                   "main", "aalprog", "declaration", "agentDec", "dataDec", 
                   "rsService", "psService", "serviceDec", "varDec", "attrValue", 
                   "typeDec", "type_super", "type_attr", "type_actions", 
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
            self.state = 158
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
            self.state = 160
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
            self.state = 162
            self.match(self.T__7)
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
            self.state = 164
            self.match(self.T__10)
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
        self.enterRule(localctx, 8, self.RULE_h_dot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
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
            return AALParser.RULE_h_colon

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.enterH_colon(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, AALListener ):
                listener.exitH_colon(self)




    def h_colon(self):

        localctx = AALParser.H_colonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_h_colon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(self.T__5)
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
        self.enterRule(localctx, 12, self.RULE_h_equal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(self.T__3)
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
        self.enterRule(localctx, 14, self.RULE_h_inequal)
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
        self.enterRule(localctx, 16, self.RULE_h_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(self.T__2)
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
        self.enterRule(localctx, 18, self.RULE_h_data)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self.enterRule(localctx, 20, self.RULE_h_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178 
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
        self.enterRule(localctx, 22, self.RULE_h_time)
        try:
            self.state = 182
            token = self._input.LA(1)
            if token in [self.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180 
                self.h_date()

            elif token in [self.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181 
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
        self.enterRule(localctx, 24, self.RULE_h_agentId)
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
        self.enterRule(localctx, 26, self.RULE_h_varTypeId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
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
        self.enterRule(localctx, 28, self.RULE_h_varId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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
        self.enterRule(localctx, 30, self.RULE_h_dataId)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
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
        self.enterRule(localctx, 32, self.RULE_h_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
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
        self.enterRule(localctx, 34, self.RULE_h_purposeId)
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
        self.enterRule(localctx, 36, self.RULE_h_serviceId)
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
        self.enterRule(localctx, 38, self.RULE_h_clauseId)
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
        self.enterRule(localctx, 40, self.RULE_h_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
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
        self.enterRule(localctx, 42, self.RULE_h_comment)
        try:
            self.state = 206
            token = self._input.LA(1)
            if token in [self.COMMENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(self.COMMENT)
                self.state = 203
                self.match(self.NEWLINE)

            elif token in [self.MLCOMMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(self.MLCOMMENT)
                self.state = 205
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
        self.enterRule(localctx, 44, self.RULE_h_duration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(self.INT)
            self.state = 209
            self.match(self.INT)
            self.state = 210 
            self.h_colon()
            self.state = 211
            self.match(self.INT)
            self.state = 212
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
        self.enterRule(localctx, 46, self.RULE_h_parameters)
        try:
            self.state = 216
            token = self._input.LA(1)
            if token in [self.T__0, self.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214 
                self.h_constant()

            elif token in [self.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215 
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
        self.enterRule(localctx, 48, self.RULE_h_constant)
        try:
            self.state = 222
            token = self._input.LA(1)
            if token in [self.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(self.INT)

            elif token in [self.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(self.T__0)
                self.state = 220
                self.match(self.STRING)
                self.state = 221
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
        self.enterRule(localctx, 50, self.RULE_h_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
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
        self.enterRule(localctx, 52, self.RULE_h_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(self.ID)
            self.state = 230
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 227 
                self.h_colon()
                self.state = 228 
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
        self.enterRule(localctx, 54, self.RULE_h_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(self.T__4)
            self.state = 233
            self.match(self.ID)
            self.state = 234 
            self.h_lpar()
            self.state = 235
            self.match(self.ID)
            self.state = 236 
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
        self.enterRule(localctx, 56, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238 
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
        self.enterRule(localctx, 58, self.RULE_aalprog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 12)) & ~0x3f) == 0 and ((1 << (_la - 12)) & ((1 << (self.D_service - 12)) | (1 << (self.D_agent - 12)) | (1 << (self.D_data - 12)) | (1 << (self.D_clause - 12)) | (1 << (self.D_type - 12)) | (1 << (self.M_macro - 12)) | (1 << (self.M_call - 12)) | (1 << (self.M_load - 12)) | (1 << (self.M_check - 12)) | (1 << (self.M_apply - 12)) | (1 << (self.M_exec - 12)) | (1 << (self.ID - 12)) | (1 << (self.COMMENT - 12)) | (1 << (self.MLCOMMENT - 12)))) != 0):
                self.state = 249
                token = self._input.LA(1)
                if token in [self.D_clause]:
                    self.state = 240 
                    self.clause()

                elif token in [self.D_service, self.D_agent, self.D_data, self.D_type, self.ID]:
                    self.state = 241 
                    self.declaration()

                elif token in [self.COMMENT, self.MLCOMMENT]:
                    self.state = 242 
                    self.h_comment()

                elif token in [self.M_macro]:
                    self.state = 243 
                    self.macro()

                elif token in [self.M_call]:
                    self.state = 244 
                    self.macroCall()

                elif token in [self.M_load]:
                    self.state = 245 
                    self.loadlib()

                elif token in [self.M_check]:
                    self.state = 246 
                    self.ltlCheck()

                elif token in [self.M_apply]:
                    self.state = 247 
                    self.checkApply()

                elif token in [self.M_exec]:
                    self.state = 248 
                    self.exec()

                else:
                    raise NoViableAltException(self)

                self.state = 253
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
        self.enterRule(localctx, 60, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            token = self._input.LA(1)
            if token in [self.D_agent]:
                self.state = 254 
                self.agentDec()

            elif token in [self.D_service]:
                self.state = 255 
                self.serviceDec()

            elif token in [self.D_data]:
                self.state = 256 
                self.dataDec()

            elif token in [self.D_type]:
                self.state = 257 
                self.typeDec()

            elif token in [self.ID]:
                self.state = 258 
                self.varDec()

            else:
                raise NoViableAltException(self)

            self.state = 262
            _la = self._input.LA(1)
            if _la==AALParser.NEWLINE:
                self.state = 261
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
        self.enterRule(localctx, 62, self.RULE_agentDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(self.D_agent)
            self.state = 265 
            self.h_agentId()
            self.state = 283
            _la = self._input.LA(1)
            if _la==AALParser.D_types:
                self.state = 266
                self.match(self.D_types)
                self.state = 267 
                self.h_lpar()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 268 
                    self.agentType()
                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 274 
                self.h_rpar()
                self.state = 281
                token = self._input.LA(1)
                if token in [self.M_rservice]:
                    self.state = 275 
                    self.rsService()
                    self.state = 276 
                    self.psService()

                elif token in [self.M_pservice]:
                    self.state = 278 
                    self.psService()
                    self.state = 279 
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
        self.enterRule(localctx, 64, self.RULE_dataDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(self.D_data)
            self.state = 286 
            self.h_dataId()
            self.state = 287
            self.match(self.D_types)
            self.state = 288 
            self.h_lpar()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 289 
                self.dataType()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295 
            self.h_rpar()
            self.state = 302
            token = self._input.LA(1)
            if token in [self.M_rservice]:
                self.state = 296 
                self.rsService()
                self.state = 297 
                self.psService()
                pass
            elif token in [self.M_pservice]:
                self.state = 299 
                self.psService()
                self.state = 300 
                self.rsService()
                pass
            elif token in [self.EOF, self.D_service, self.D_agent, self.D_data, self.D_clause, self.D_type, self.M_subject, self.M_macro, self.M_call, self.M_load, self.M_check, self.M_apply, self.M_exec, self.ID, self.NEWLINE, self.COMMENT, self.MLCOMMENT]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 306
            _la = self._input.LA(1)
            if _la==AALParser.M_subject:
                self.state = 304
                self.match(self.M_subject)
                self.state = 305 
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
        self.enterRule(localctx, 66, self.RULE_rsService)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(self.M_rservice)
            self.state = 309 
            self.h_lpar()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 310 
                self.h_serviceId()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 316 
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
        self.enterRule(localctx, 68, self.RULE_psService)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(self.M_pservice)
            self.state = 319 
            self.h_lpar()
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 320 
                self.h_serviceId()
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 326 
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
        self.enterRule(localctx, 70, self.RULE_serviceDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(self.D_service)
            self.state = 329 
            self.h_serviceId()
            self.state = 340
            _la = self._input.LA(1)
            if _la==AALParser.D_types:
                self.state = 330
                self.match(self.D_types)
                self.state = 331 
                self.h_lpar()
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 332 
                    self.serviceType()
                    self.state = 337
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 338 
                self.h_rpar()


            self.state = 352
            _la = self._input.LA(1)
            if _la==AALParser.M_purpose:
                self.state = 342
                self.match(self.M_purpose)
                self.state = 343 
                self.h_lpar()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 344 
                    self.h_purposeId()
                    self.state = 349
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 350 
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
        self.enterRule(localctx, 72, self.RULE_varDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354 
            self.h_varTypeId()
            self.state = 355 
            self.h_varId()
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 356 
                    self.attrValue() 
                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 74, self.RULE_attrValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362 
            self.h_attribute()
            self.state = 363 
            self.h_lpar()
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 364
                self.match(self.ID)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370 
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
        self.enterRule(localctx, 76, self.RULE_typeDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(self.D_type)
            self.state = 373
            self.match(self.ID)
            self.state = 375
            _la = self._input.LA(1)
            if _la==AALParser.M_extends:
                self.state = 374 
                self.type_super()


            self.state = 378
            _la = self._input.LA(1)
            if _la==AALParser.M_attr:
                self.state = 377 
                self.type_attr()


            self.state = 381
            _la = self._input.LA(1)
            if _la==AALParser.M_actions:
                self.state = 380 
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
        self.enterRule(localctx, 78, self.RULE_type_super)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(self.M_extends)
            self.state = 384 
            self.h_lpar()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 385
                self.match(self.ID)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391 
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
        self.enterRule(localctx, 80, self.RULE_type_attr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(self.M_attr)
            self.state = 394 
            self.h_lpar()
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 395
                self.match(self.ID)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 401 
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
        self.enterRule(localctx, 82, self.RULE_type_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(self.M_actions)
            self.state = 404 
            self.h_lpar()
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 405
                self.match(self.ID)
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411 
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
        self.enterRule(localctx, 84, self.RULE_agentType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
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
        self.enterRule(localctx, 86, self.RULE_serviceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
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
        self.enterRule(localctx, 88, self.RULE_dataType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
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
        self.enterRule(localctx, 90, self.RULE_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(self.D_clause)
            self.state = 420 
            self.h_clauseId()
            self.state = 421 
            self.h_lpar()

            self.state = 422 
            self.usage()
            self.state = 424
            _la = self._input.LA(1)
            if _la==AALParser.NEWLINE:
                self.state = 423
                self.match(self.NEWLINE)


            self.state = 430
            _la = self._input.LA(1)
            if _la==AALParser.C_auditing:
                self.state = 426 
                self.audit()
                self.state = 428
                _la = self._input.LA(1)
                if _la==AALParser.NEWLINE:
                    self.state = 427
                    self.match(self.NEWLINE)




            self.state = 436
            _la = self._input.LA(1)
            if _la==AALParser.C_ifviolated:
                self.state = 432 
                self.rectification()
                self.state = 434
                _la = self._input.LA(1)
                if _la==AALParser.NEWLINE:
                    self.state = 433
                    self.match(self.NEWLINE)




            self.state = 438 
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
        self.enterRule(localctx, 92, self.RULE_usage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440 
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
        self.enterRule(localctx, 94, self.RULE_audit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(self.C_auditing)
            self.state = 443 
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
        self.enterRule(localctx, 96, self.RULE_rectification)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(self.C_ifviolated)
            self.state = 446 
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
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_actionExp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 449 
                self.actionExp1Action()
                pass

            elif la_ == 2:
                self.state = 450 
                self.actionExp2notAction()
                pass

            elif la_ == 3:
                self.state = 451 
                self.actionExp3modalAction()
                pass

            elif la_ == 4:
                self.state = 452 
                self.actionExp4condition()
                pass

            elif la_ == 5:
                self.state = 453 
                self.actionExp6Author()
                pass

            elif la_ == 6:
                self.state = 454 
                self.actionExp7ifthen()
                pass

            elif la_ == 7:
                self.state = 455 
                self.actionExp8qvar()
                pass

            elif la_ == 8:
                self.state = 456 
                self.h_lpar()
                self.state = 457 
                self.actionExp(0)
                self.state = 458 
                self.h_rpar()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AALParser.ActionExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_actionExp)
                    self.state = 462
                    if not self.precpred(self._ctx, 5):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 463 
                    self.booleanOp()
                    self.state = 464 
                    self.actionExp(6) 
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 100, self.RULE_actionExp1Action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471 
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
        self.enterRule(localctx, 102, self.RULE_actionExp2notAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(self.O_not)
            self.state = 474 
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
        self.enterRule(localctx, 104, self.RULE_actionExp3modalAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476 
            self.modal()
            self.state = 477 
            self.h_lpar()
            self.state = 478 
            self.actionExp(0)
            self.state = 479 
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
        self.enterRule(localctx, 106, self.RULE_actionExp4condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481 
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
        self.enterRule(localctx, 108, self.RULE_actionExp6Author)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483 
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
        self.enterRule(localctx, 110, self.RULE_actionExp7ifthen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485 
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
        self.enterRule(localctx, 112, self.RULE_actionExp8qvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487 
            self.qvar()
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 488 
                    self.qvar() 
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 494 
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
        self.enterRule(localctx, 114, self.RULE_quant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
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
        self.enterRule(localctx, 116, self.RULE_qvar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498 
            self.quant()
            self.state = 499 
            self.h_variable()
            self.state = 502
            _la = self._input.LA(1)
            if _la==AALParser.O_where:
                self.state = 500
                self.match(self.O_where)
                self.state = 501 
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
        self.enterRule(localctx, 118, self.RULE_booleanOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
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
        self.enterRule(localctx, 120, self.RULE_author)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not(_la==AALParser.A_permit or _la==AALParser.A_deny):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 507 
            self.action()
            self.state = 509
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 508
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

        def O_if(self):
            return self.getToken(AALParser.O_if, 0)

        def h_rpar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_rparContext)
            else:
                return self.getTypedRuleContext(AALParser.H_rparContext,i)


        def actionExp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.ActionExpContext)
            else:
                return self.getTypedRuleContext(AALParser.ActionExpContext,i)


        def O_then(self):
            return self.getToken(AALParser.O_then, 0)

        def h_lpar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AALParser.H_lparContext)
            else:
                return self.getTypedRuleContext(AALParser.H_lparContext,i)


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
        self.enterRule(localctx, 122, self.RULE_ifthen)
        try:
            self.state = 525
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(self.O_if)
                self.state = 512 
                self.h_lpar()
                self.state = 513 
                self.actionExp(0)
                self.state = 514 
                self.h_rpar()
                self.state = 515
                self.match(self.O_then)
                self.state = 516 
                self.h_lpar()
                self.state = 517 
                self.actionExp(0)
                self.state = 518 
                self.h_rpar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 520
                self.match(self.O_if)
                self.state = 521 
                self.actionExp(0)
                self.state = 522
                self.match(self.O_then)
                self.state = 523 
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
        self.enterRule(localctx, 124, self.RULE_exp)
        try:
            self.state = 534
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527 
                self.h_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 528 
                self.h_constant()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 529 
                self.h_predicate()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 530
                self.match(self.ID)
                self.state = 531 
                self.h_dot()
                self.state = 532 
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
        _startState = 126
        self.enterRecursionRule(localctx, 126, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 537 
                self.condition1notExp()
                pass

            elif la_ == 2:
                self.state = 538 
                self.condition2cmpExp()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 546
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AALParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 541
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 542
                    _la = self._input.LA(1)
                    if not(_la==AALParser.O_or or _la==AALParser.O_and):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 543 
                    self.condition(2) 
                self.state = 548
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 128, self.RULE_condition1notExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            _la = self._input.LA(1)
            if _la==AALParser.O_not:
                self.state = 549
                self.match(self.O_not)


            self.state = 552 
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
        self.enterRule(localctx, 130, self.RULE_condition2cmpExp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554 
            self.exp()
            self.state = 557
            token = self._input.LA(1)
            if token in [self.T__3]:
                self.state = 555 
                self.h_equal()

            elif token in [self.T__1]:
                self.state = 556 
                self.h_inequal()

            else:
                raise NoViableAltException(self)

            self.state = 559 
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
        self.enterRule(localctx, 132, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561 
            self.h_agentId()
            self.state = 562 
            self.h_dot()

            self.state = 563 
            self.h_serviceId()
            self.state = 570
            _la = self._input.LA(1)
            if _la==AALParser.T__7:
                self.state = 564 
                self.h_lbar()
                self.state = 566
                _la = self._input.LA(1)
                if _la==AALParser.ID:
                    self.state = 565 
                    self.h_agentId()


                self.state = 568 
                self.h_rbar()


            self.state = 572 
            self.h_lpar()
            self.state = 574
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.T__4) | (1 << self.T__0) | (1 << self.ID) | (1 << self.INT))) != 0):
                self.state = 573 
                self.exp()


            self.state = 576 
            self.h_rpar()
            self.state = 578
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 577 
                self.time(0)


            self.state = 590
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 580
                self.match(self.M_purpose)
                self.state = 581 
                self.h_lpar()
                self.state = 585
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==AALParser.ID:
                    self.state = 582 
                    self.h_purposeId()
                    self.state = 587
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 588 
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
        self.enterRule(localctx, 134, self.RULE_modal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
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
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_time, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            _la = self._input.LA(1)
            if not(_la==AALParser.O_after or _la==AALParser.O_before):
                self._errHandler.recoverInline(self)
            self.consume()
            self.state = 596 
            self.h_date()
            self._ctx.stop = self._input.LT(-1)
            self.state = 603
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AALParser.TimeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_time)
                    self.state = 598
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 599
                    _la = self._input.LA(1)
                    if not(_la==AALParser.O_or or _la==AALParser.O_and):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 600 
                    self.time(2) 
                self.state = 605
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        self.enterRule(localctx, 138, self.RULE_macro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(self.M_macro)
            self.state = 607
            self.match(self.ID)
            self.state = 609
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 608 
                self.args()


            self.state = 611 
            self.h_lpar()
            self.state = 612
            self.match(self.MCODE)
            self.state = 613 
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
        self.enterRule(localctx, 140, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615 
            self.h_lpar()
            self.state = 619
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.ID:
                self.state = 616
                self.match(self.ID)
                self.state = 621
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 622 
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
        self.enterRule(localctx, 142, self.RULE_macroCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(self.M_call)
            self.state = 625
            self.match(self.ID)
            self.state = 626 
            self.h_lpar()
            self.state = 630
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.STRING:
                self.state = 627
                self.match(self.STRING)
                self.state = 632
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 633 
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
        self.enterRule(localctx, 144, self.RULE_exec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(self.M_exec)
            self.state = 636
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
        self.enterRule(localctx, 146, self.RULE_loadlib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(self.M_load)
            self.state = 639
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
        self.enterRule(localctx, 148, self.RULE_ltlCheck)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(self.M_check)
            self.state = 642
            self.match(self.ID)
            self.state = 644
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.state = 643 
                self.args()


            self.state = 646 
            self.h_lpar()
            self.state = 647 
            self.check()
            self.state = 648 
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
        self.enterRule(localctx, 150, self.RULE_check)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650 
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
        self.enterRule(localctx, 152, self.RULE_checkApply)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(self.M_apply)
            self.state = 653
            self.match(self.ID)
            self.state = 654 
            self.h_lpar()
            self.state = 658
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AALParser.STRING:
                self.state = 655
                self.match(self.STRING)
                self.state = 660
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 661 
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
        self.enterRule(localctx, 154, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 673
            token = self._input.LA(1)
            if token in [self.C_clause]:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.match(self.C_clause)
                self.state = 664 
                self.h_lpar()
                self.state = 665 
                self.h_clauseId()
                self.state = 666 
                self.h_rpar()
                self.state = 670
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 667 
                    self.h_dot()
                    self.state = 668
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.C_usage) | (1 << self.C_audit) | (1 << self.C_rectification))) != 0)):
                        self._errHandler.recoverInline(self)
                    self.consume()



            elif token in [self.PREDICATE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
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
        _startState = 156
        self.enterRecursionRule(localctx, 156, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            token = self._input.LA(1)
            if token in [self.CONSTANTS]:
                self.state = 676
                self.match(self.CONSTANTS)
                self.state = 680
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 677
                        self.match(self.NEWLINE) 
                    self.state = 682
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,59,self._ctx)


            elif token in [self.C_clause, self.PREDICATE]:
                self.state = 683 
                self.atom()
                self.state = 687
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 684
                        self.match(self.NEWLINE) 
                    self.state = 689
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,60,self._ctx)


            elif token in [self.NEGATION]:
                self.state = 690
                self.match(self.NEGATION)
                self.state = 691 
                self.formula(0)
                self.state = 695
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 692
                        self.match(self.NEWLINE) 
                    self.state = 697
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)


            elif token in [self.T__6]:
                self.state = 698 
                self.h_lpar()
                self.state = 699 
                self.formula(0)
                self.state = 700 
                self.h_rpar()
                self.state = 704
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 701
                        self.match(self.NEWLINE) 
                    self.state = 706
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,62,self._ctx)


            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 740
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,69,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 738
                    la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                    if la_ == 1:
                        localctx = AALParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 709
                        if not self.precpred(self._ctx, 1):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 713
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==AALParser.NEWLINE:
                            self.state = 710
                            self.match(self.NEWLINE)
                            self.state = 715
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 716 
                        self.formula(2)
                        pass

                    elif la_ == 2:
                        localctx = AALParser.FormulaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 717
                        if not self.precpred(self._ctx, 4):
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 721
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==AALParser.NEWLINE:
                            self.state = 718
                            self.match(self.NEWLINE)
                            self.state = 723
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 724
                        _la = self._input.LA(1)
                        if not(((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (self.CONJUNCTION - 69)) | (1 << (self.DISJUNCTION - 69)) | (1 << (self.IMPLICATION - 69)) | (1 << (self.EQUIVALENCE - 69)))) != 0)):
                            self._errHandler.recoverInline(self)
                        self.consume()
                        self.state = 728
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==AALParser.NEWLINE:
                            self.state = 725
                            self.match(self.NEWLINE)
                            self.state = 730
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 731 
                        self.formula(0)
                        self.state = 735
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,67,self._ctx)
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt==1:
                                self.state = 732
                                self.match(self.NEWLINE) 
                            self.state = 737
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,67,self._ctx)

                        pass

             
                self.state = 742
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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
        self._predicates[49] = self.actionExp_sempred
        self._predicates[63] = self.condition_sempred
        self._predicates[68] = self.time_sempred
        self._predicates[78] = self.formula_sempred
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
         



