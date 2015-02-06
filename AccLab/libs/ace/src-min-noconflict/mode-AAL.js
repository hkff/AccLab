/**
 * AAL Mode
 */
ace.define('ace/mode/AAL', function(require, exports, module) {
    var oop = require("../lib/oop");
    var TextMode = require("./text").Mode;
    var Tokenizer = require("../tokenizer").Tokenizer;
    var aalHighlightRules = require("./aal_highlight_rules").aalHighlightRules;

    var Mode = function() {
        this.$tokenizer = new Tokenizer(new aalHighlightRules().getRules());
    };
    oop.inherits(Mode, TextMode);


    (function() {
        // Extra logic goes here. (see below)
    }).call(Mode.prototype);

    exports.Mode = Mode;
});


/**
 * AAL syntax highlighter
 */
ace.define('ace/mode/aal_highlight_rules', function(require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

       var aalHighlightRules = function() {
        this.$rules = new TextHighlightRules().getRules();

        // Keywords
        var keywords = (
                " CLAUSE AGENT SERVICE DATA TYPE TYPES SUBJECT RS REQUIRED PS PROVIDED PURPOSE MACRO CALL LOAD"+
                " Clause Agent Service Data Type Types SUBJECT Rs Required Ps Provided Purpose Macro Call Load"+
                " clause Agent service data type types SUBJECT rs required ps provided purpose macro call load"+
                
                " AUDITING IF_VIOLATED_THEN AUDIT"+
                " Auditing if_violated_then Audit"+
                " auditing if_violated_then audit"+
                /*
                " OR AND NOT THEN ONLYWHEN FORALL EXISTS IF"+
                " or and not then onlywhen forall exists if"+
                " Or And Not Then Onlywhen Forall Exists If"+
                */
                " AFTER BEFORE"+

                " PERMIT DENY"+
                " Permit Deny"+
                " permit deny"+

                " MAY MUST MUSTNOT ALWAYS"+
                " may must mustnot always"+
                " May Must Mustnot Always");
        
        // Predifined Types
        var types = ("Subject Controller Processor Auditor");
        
        // Operators
        var operators = ("OR AND NOT THEN ONLYWHEN FORALL EXISTS IF WHERE");

        // Reflexion api functions
        var langFunctions = ("getClauses getDeclarations");

        // Compound keywords        
        var compoundKeywords = "foo";


        // Keyword mapper
        var keywordMapper = this.createKeywordMapper({
          //  "keyword.clause" : "Clause",
            "variable.language": "this AGENT BEFORE",
            "keyword": keywords,
            "constant.language": "TRUE FALSE NULL SPACE",
            "support.type": types,
            "support.reflexion.functions": langFunctions,
            "constant.library": langFunctions,
            //"keyword.operator": operators,
            //"variable.language": operators
            "variable.parameter": operators,
        }, "text", false, " ");
        

        this.$rules = {
            
            "start" : [
                {token : "string", regex : "`", next  : "string"},
                {token : "string", regex : "'|\"", next  : "qstring"},
                {token : "comment", regex : "\\/\\/.*$"},
                {token : "comment", regex : "\\/\\*", next : "comment"},
                //{token : "invalid", regex: "\\.{2,}"},
                //{token : "keyword.operator", regex: /\W[\-+\%=<>*]\W|\*\*|[~:,\.&$]|->*?|=>/},
                
                // Helper
                {token : "paren.lparen", regex : "[\\[({]"},
                {token : "paren.rparen", regex : "[\\])}]"},
                {token : "constant.numeric", regex: "[+-]?\\d+\\b"},
                
                //{token : "variable.parameter", regex : /sy|pa?\d\d\d\d\|t\d\d\d\.|innnn/}, 
                {token : "keyword", regex : compoundKeywords}, 
                //{token : "variable.parameter", regex : /\w+-\w+(?:-\w+)*/}, 
                //{token : keywordMapper, regex : "\\b\\w+\\b"},
                {token : keywordMapper, regex : "[a-zA-Z_$][a-zA-Z0-9_$]*\\b"},
                {caseInsensitive: true},
                {token : "d", regex: "dz"}
            ],
            "qstring" : [
                {token : "constant.language.escape",   regex : "''"},
                {token : "string", regex : "'|\"",     next  : "start"},
                {defaultToken : "string"}
            ],
            "string" : [
                {token : "constant.language.escape",   regex : "``"},
                {token : "string", regex : "`",     next  : "start"},
                {defaultToken : "string"}
            ],
            "comment" : [
                // Closing comment
                {token : "comment", regex : ".*?\\*\\/", next : "start"},
                // comment spanning whole line
                {token : "comment", regex : ".+"}
            ]
        };
    }

    oop.inherits(aalHighlightRules, TextHighlightRules);
    exports.aalHighlightRules = aalHighlightRules;


});