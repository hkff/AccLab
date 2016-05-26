grammar AAL;
/*
    // AAL CORE
    AALprogram    ::= (Declaration | Clause | Comment | Macro | MacroCall | Loadlib | LtlCheck | CheckApply | Exec | Behavior | Env)
    Declaration   ::= AgentDec | ServiceDec | DataDec | TypesDec | varDec
    AgentDec      ::= AGENT Id [TYPES '(' Type *')' REQUIRED'('service*')' PROVIDED'('service*')']
    ServiceDec    ::= SERVICE Id [TYPES '(' Type* ')'] [PURPOSE '(' Id* ')']
    DataDec       ::= DATA Id TYPES '(' Type* ')' [REQUIRED'('service*')' PROVIDED'('service*')'] SUBJECT agent
    VarDec        ::= Type_Id Id [attr_Id '(' value* ')']*
    Clause        ::= CLAUSE Id '(' [Usage] [Audit Rectification] ')'
    Usage         ::= ActionExp
    Audit         ::= AUDITING Usage
    Rectification ::= IF_VIOLATED_THEN Usage

    ActionExp     ::= Action
                    | NOT ActionExp
                    | Modality ActionExp
                    | Condition
                    | ActionExp (AND|OR|ONLYWHEN|UNTIL|UNLESS) ActionExp
                    | Author
                    | Quant*
                    | IF '(' ActionExp ')' THEN '{' ActionExp '}'

    Exp           ::= Variable | Constant | Variable.Attribute
    Condition     ::= [NOT] Exp | Exp ['==' | '!='] Exp | Condition (AND|OR) Condition
    Author        ::= (PERMIT | DENY) Action
    Action        ::= agent.service ['['[agent]']'] '('Exp')' [Time] [Purpose]
    Quant         ::= (FORALL | EXISTS) Var [WHERE Condition]
    Variable      ::= Var ':' Type
    Modality      ::= MUST | MUSTNOT | ALWAYS | NEVER | SOMETIME
    Time          ::= (AFTER | BEFORE) Date | Time (AND | OR) Time
    Date          ::= STRING
    Type, var, val, attr Id, agent, Constant, Purpose ::= literal


    // AAL Type extension
    TypesDec      ::= TYPE Id [EXTENDS '(' Type* ')'] ATTRIBUTES '(' AttributeDec* ')' ACTIONS '(' ActionDec* ')'
    AttributeDec  ::= Id ':' Type
    ActionDec     ::= Id
    Type, Id      ::= litteral


    // Reflexion extension
    Macro         ::= MACRO Id '(' param* ')' '(' mcode ')'
    MCode         ::= """ Meta model api + Python3 code (subset) """
    MCall         ::= CALL Id '(' param* ')'
    LoadLib       ::= LOAD STRING;
    Exec          ::= EXEC MCode

    // LTL checking extension
    LtlCheck     ::= CHECK Id '(' param* ')' '(' check ')'
    check        ::= FOTL_formula + clause(Id) [.ue | .ae | .re]
    CheckApply   ::= APPLY Id '(' param* ')'
    Env          ::= check

    // Behavior extension
    Behavior    ::= BEHAVIOR Id '(' ActionExp ')'
*/


//-------------------------------------------------------//
//------------------- Keywords -------------------------//
//------------------------------------------------------//

/** Declarable **/
D_service : 'SERVICE'; // | 'Service';
D_agent	  : 'AGENT';   // | 'Agent';
D_data    : 'DATA';    // | 'Data';
D_clause  : 'CLAUSE';  // | 'Clause';
D_type    : 'TYPE';    // | 'Type';
D_types   : 'TYPES';   // | 'Types';

/** Clause **/
C_auditing   : 'AUDITING';         // | 'Auditing';
C_ifviolated : 'IF_VIOLATED_THEN'; // | 'If_Violated_Then';

/** Logical Operators **/
O_or       : 'OR';       // | 'or';
O_and      : 'AND';      // | 'and' | ',';
O_onlywhen : 'ONLYWHEN'; // | 'onlywhen';
O_then     : 'THEN';     // | 'then';
O_if       : 'IF';       // | 'if';
O_not      : 'NOT';      // | 'not';
O_where    : 'WHERE';    // | 'where';
O_after    : 'AFTER';    // | 'after';
O_before   : 'BEFORE';   // | 'before';

/** Temporal operators **/
T_must     : 'MUST';     // | 'must';
T_mustnot  : 'MUSTNOT';  // | 'mustnot';
T_always   : 'ALWAYS';   // | 'always';
T_never    : 'NEVER';    // | 'never';
T_sometime : 'SOMETIME'; // | 'sometime';
T_until    : 'UNTIL';    // | 'until';
T_unless   : 'UNLESS';   // | 'unless';
T_next     : 'NEXT';     // | 'next';

/** Authorizations **/
A_permit   : 'PERMIT'; // | 'permit';
A_deny     : 'DENY';   // | 'deny';


/** Quantifications **/
Q_forall   : 'FORALL'; // | 'forall';
Q_exists   : 'EXISTS'; // | 'exists';


/** Misc **/
M_subject  : 'SUBJECT';
M_rservice : 'REQUIRED'; // | 'RS' | 'required';
M_pservice : 'PROVIDED'; // | 'PS' | 'provided';
M_purpose  : 'PURPOSE';  // | 'purpose';
//M_audit    : 'AUDIT' | 'audit';
M_extends  : 'EXTENDS';    // | 'extends';
M_attr     : 'ATTRIBUTES'; // | 'attributes';
M_actions  : 'ACTIONS';    // | 'actions';
M_macro    : 'MACRO';      // | 'macro';
M_call     : 'CALL';       // | 'call';
M_load     : 'LOAD';       // | 'load';
M_check    : 'CHECK';      // | 'check';
M_apply    : 'APPLY';      // | 'apply';
M_exec     : 'EXEC';       // | 'exec';
M_behavior : 'BEHAVIOR';   // | 'behavior';
M_env      : 'ENV';        // | 'env';

/** Check **/
C_clause        : 'clause'           | 'cl';
C_usage         : 'get_usage'        | 'ue';
C_audit         : 'get_audit'        | 'ae';
C_rectification : 'get_rectification'| 're';
C_violation     : 'get_violation'    | 'vl';


/** Helpers **/
h_lpar    : '(';
h_rpar    : ')';
h_lbar    : '[';
h_rbar    : ']';
h_lmar    : '{';
h_rmar    : '}';
h_dot     : '.';
h_colon   : ':';
h_equal   : '==';
h_inequal : '!=';
h_slash   : '/';
h_data    : ID;
h_value   : h_constant;
h_time    : h_date | h_duration;
h_agentId    : ID;
h_varTypeId  : ID;
h_varId      : ID;
h_dataId     : ID;
h_date       : STRING; // INT INT h_slash INT INT h_slash INT INT INT INT;
h_purposeId  : ID;
h_serviceId  : ID;
h_clauseId   : ID;
h_attribute  : ID;
h_comment    : COMMENT NEWLINE | MLCOMMENT NEWLINE;
h_duration   : INT INT h_colon INT INT;
h_parameters : h_constant | h_variable;
h_constant   : INT |  STRING;
h_type       : ID;
h_variable   : ID (h_colon h_type)?;
h_predicate  : '@' ID h_lpar (h_pArgs)* h_rpar;
h_pArgs      : ID | STRING;

//-------------------------------------------------------//
//----------------- Lexer rules ------------------------//
//------------------------------------------------------//
ID        : (('a'..'z')|('A'..'Z')) (('a'..'z')|('A'..'Z')| INT | '_')*;
INT       : '0'..'9'+;
NEWLINE   : '\r'?'\n' -> channel(HIDDEN);
WS        : (' '|'\t'|'\n'|'\r')+ -> skip;
BLANK     : (' ')+;
STRING    : '"' (.)*? '"';
COMMENT   : '//' (.)*? '\n' -> channel(HIDDEN);
MLCOMMENT : '/*' (.)*? '*/' -> channel(HIDDEN);


//-------------------------------------------------------//
//---------------- Parser rules ------------------------//
//------------------------------------------------------//

main        : aalprog;
aalprog     : (clause | declaration | h_comment | macro | macroCall | loadlib | ltlCheck | checkApply | exec | behavior | env)*;
declaration : (agentDec | serviceDec | dataDec | typeDec | varDec) NEWLINE?;


//****   Declarations ****//
agentDec   : D_agent h_agentId ( D_types h_lpar agentType*  h_rpar ( (rsService psService) | (psService rsService) ) )?;
dataDec    : D_data h_dataId D_types h_lpar dataType* h_rpar ((rsService psService) | (psService rsService))? (M_subject h_agentId)?;
rsService  : M_rservice h_lpar h_serviceId* h_rpar;
psService  : M_pservice h_lpar h_serviceId* h_rpar;
serviceDec : D_service h_serviceId ( D_types h_lpar serviceType* h_rpar)? (M_purpose h_lpar h_purposeId* h_rpar )?;

varDec       : h_varTypeId h_varId attrValue*;
attrValue    : h_attribute h_lpar ID* h_rpar;

// TypesDec      ::= TYPE Id [EXTENDS '(' Type* ')'] ATTRIBUTES '(' AttributeDec* ')' ACTIONS '(' ActionDec* ')'
typeDec      : D_type ID  type_super? type_attr? type_actions?;
type_super   : M_extends h_lpar ID* h_rpar;
type_attr    : M_attr h_lpar ID* h_rpar;
type_actions : M_actions h_lpar ID* h_rpar;


//**** Types and Attributes ****//
agentType   : ID;
serviceType : ID;
dataType    : ID;


//**** Program core ****//

//Clause        ::= CLAUSE Id '(' [Usage] [Audit Rectification] ')'
clause        : D_clause h_clauseId h_lpar (usage NEWLINE?) (audit NEWLINE?)? (rectification NEWLINE?)? h_rpar ;
usage         : actionExp;
audit         : C_auditing usage;
rectification : C_ifviolated usage;


// We use this separation to handle contexts in the compiler
actionExp  : actionExp1Action
           | actionExp2notAction
           | actionExp3modalAction
           | actionExp4condition
           | actionExp booleanOp actionExp // use inline because antrl4 doesn't supports mutually left-recursive rules
           | actionExp6Author
           | actionExp7ifthen
           | actionExp8qvar
           | h_lpar actionExp h_rpar
           | h_predicate;

actionExp1Action      : action;
actionExp2notAction   : O_not actionExp;
actionExp3modalAction : modal h_lpar actionExp h_rpar;
actionExp4condition   : condition;
//actionExp5boolAction  : actionExp booleanOp actionExp;
actionExp6Author      : author;
actionExp7ifthen      : ifthen;
actionExp8qvar        : qvar actionExp; // Force the first qvar



quant       : Q_forall | Q_exists;
qvar        : quant h_variable (O_where condition)?;
booleanOp   : O_and | O_or | O_onlywhen | T_until | T_unless;
author      : (A_permit | A_deny) action NEWLINE?;
ifthen      : O_if h_lpar actionExp h_rpar O_then h_lmar actionExp h_rmar
            | O_if actionExp O_then actionExp
            | O_if actionExp IMPLICATION actionExp;


exp : h_variable
    | h_constant
    | h_predicate
    | ID h_dot h_attribute;

condition              : condition1notExp
                       | condition2cmpExp
                       | condition (O_and|O_or) condition;  // mutually left-recursive
condition1notExp       : (O_not)? exp;
condition2cmpExp       : exp (h_equal | h_inequal) exp;


action                 : h_agentId h_dot (h_serviceId) (h_lbar h_agentId? h_rbar)?  h_lpar exp? h_rpar (time)? (M_purpose h_lpar h_purposeId* h_rpar)?;

modal                  : T_must | T_mustnot | T_always | T_never | T_sometime | T_next;
time                   : (O_after | O_before) h_date | time (O_and | O_or) time;
    


//****  Reflexion extension ****//
macro  : M_macro ID args? h_lpar MCODE h_rpar;
args   : h_lpar ID* h_rpar;
MCODE : '"""' (.)*? '"""';
macroCall : M_call ID h_lpar STRING* h_rpar;
exec   : M_exec MCODE;
loadlib : M_load STRING;


//****  Behavior extension ****//
behavior :  M_behavior ID h_lpar actionExp h_rpar;


//****  LTL checking extension ****//
ltlCheck : M_check ID args? h_lpar check h_rpar;
check   : MCODE; //formula;
checkApply : M_apply ID h_lpar STRING* h_rpar;
env     : M_env MCODE; //formula;


NEGATION    : '~' | 'not';
CONJUNCTION : '&';
DISJUNCTION : '|';
IMPLICATION : '->' |'=>';
EQUIVALENCE :'<->' | '<=>';
CONSTANTS   : 'true' | 'false';
PREDICATE   : ID;

/*
atom : C_clause h_lpar h_clauseId h_rpar (h_dot (C_usage | C_audit | C_rectification))?
     | PREDICATE | CONSTANTS;

formula  : atom NEWLINE*
         //CONSTANTS NEWLINE* | atom NEWLINE*
         | formula NEWLINE* (CONJUNCTION | DISJUNCTION | IMPLICATION | EQUIVALENCE) NEWLINE* formula NEWLINE*
         | NEGATION formula NEWLINE*
         //| uQuant formula NEWLINE* | eQuant formula NEWLINE*
         //| formula btOperators formula NEWLINE* | utOperators formula NEWLINE*
         | h_lpar formula h_rpar NEWLINE*
         | formula NEWLINE* formula;
*/
