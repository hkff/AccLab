/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

grammar TSPASS;

//-------------------------------------------------------//
//----------------- Lexer rules ------------------------//
//------------------------------------------------------//
ID        : (('a'..'z')|('A'..'Z')) (('a'..'z')|('A'..'Z')| INT | '_')*;
INT       : '0'..'9'+;
NEWLINE   : '\r'?'\n' -> channel(HIDDEN);
WS        : (' '|'\t'|'\n'|'\r')+ -> skip;
BLANK     : (' ')+;
STRING    : '"' (.)*? '"';
COMMENT   : '%' (.)*? '\n' -> channel(HIDDEN);

x : 'x';
y : 'y';
h_lpar    : '(';
h_rpar    : ')';
h_lbar    : '[';
h_rbar    : ']';
h_dot     : '.';
h_colon   : ':';
h_equal   : '=';

// % Comments are written like this
// % Formulae written on separate lines without any logical operation linking them together
// % are treated as conjuncts.
// % Brackets '(', ')' can be used for grouping.
// % Input formulae are *not* negated before being transformed into the normal form.

formula : //variable NEWLINE* | constants NEWLINE* | atom NEWLINE*
        atom NEWLINE*
        | formula NEWLINE* (conjunction | disjunction | implication | equivalence) NEWLINE* formula NEWLINE*
        | negation formula NEWLINE*
        | uQuant formula NEWLINE* | eQuant formula NEWLINE*
        | formula btOperators formula NEWLINE* | utOperators formula NEWLINE*
        | h_lpar formula h_rpar NEWLINE*
        | formula NEWLINE* formula;

atom        : predicate (h_lpar (variable | constants) (',' (variable | constants))* h_rpar)?;
predicate   : ID;
variable    : ID;
constants   : 'true' | 'false';
negation    : '~' | 'not';
conjunction : '&';
disjunction : '|';
implication : '->' |'=>';
equivalence :'<->' | '<=>';

uQuant : '!' '[' ID (',' ID)* ']';
eQuant : '?' '[' ID (',' ID)* ']';

utOperators : always | snext | sometime;
btOperators : until | unless;

always   : 'always';
snext    : 'next';
sometime : 'sometime';
until    : 'until';
unless   : 'unless';