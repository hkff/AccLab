/**
 * tspass Mode
 */
ace.define('ace/mode/TSPASS', function(require, exports, module) {
    var oop = require("../lib/oop");
    var TextMode = require("./text").Mode;
    var Tokenizer = require("../tokenizer").Tokenizer;
    var tspassHighlightRules = require("./tspass_highlight_rules").tspassHighlightRules;

    var Mode = function() {
        this.$tokenizer = new Tokenizer(new tspassHighlightRules().getRules());
    };
    oop.inherits(Mode, TextMode);


    (function() {
        // Extra logic goes here. (see below)
    }).call(Mode.prototype);

    exports.Mode = Mode;
});


/**
 * tspass syntax highlighter
 */
ace.define('ace/mode/tspass_highlight_rules', function(require, exports, module) {
    "use strict";

    var oop = require("../lib/oop");
    var TextHighlightRules = require("./text_highlight_rules").TextHighlightRules;

       var tspassHighlightRules = function() {
        this.$rules = new TextHighlightRules().getRules();

        // Keywords
        var keywords = ("true false ~ not & | -> => <-> <=> ! ?");

        // Temporal Operators
        var operators = ("always next sometime until unless");

        // Keyword mapper
        var keywordMapper = this.createKeywordMapper({
            //"keyword": keywords,
            "keyword.operator": operators,
            "variable.parameter": keywords
        }, "text", false, " ");

        this.$rules = {
            
            "start" : [
                {token : "string", regex : "`", next  : "string"},
                {token : "string", regex : "'|\"", next  : "qstring"},
                {token : "comment", regex : "\\%.*$"},

                // Helper
                {token : "paren.lparen", regex : "[\\[({]"},
                {token : "paren.rparen", regex : "[\\])}]"},
                {token : "constant.numeric", regex: "[+-]?\\d+\\b"},
                {token : keywordMapper, regex : "[a-zA-Z_$_&][a-zA-Z0-9_$_&]*\\b"},
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

    oop.inherits(tspassHighlightRules, TextHighlightRules);
    exports.tspassHighlightRules = tspassHighlightRules;
});
