/**
 * AAL Mode
 */
ace.define('ace/mode/AAL', function(require, exports, module) {
    var oop = require("../lib/oop");
    var TextMode = require("./text").Mode;
    //var Tokenizer = require("../tokenizer").Tokenizer;
    var aalHighlightRules = require("./aal_highlight_rules").aalHighlightRules;
    var aalFoldMode = require("./aalFolding").FoldMode;
    var WorkerClient = require("../worker/worker_client").WorkerClient;

    var Mode = function() {
        //this.$tokenizer = new Tokenizer(new aalHighlightRules().getRules());
        //this.$keywordList = aalHighlightRules.$keywordList;
        this.HighlightRules = aalHighlightRules;
        this.foldingRules = new aalFoldMode("\\:");
    };
    oop.inherits(Mode, TextMode);


    (function() {
        this.lineCommentStart = "//";
        this.blockComment = {start: "/*", end: "*/"};

        // Creating AAL worker
        this.createWorker = function(session) {
            this.$worker = new WorkerClient(["ace"], "ace/worker/aal_worker", "AALWorker");
            this.$worker.attachToDocument(session.getDocument());

            this.$worker.on("errors", function(e) {
                session.setAnnotations(e.data);
            });

            this.$worker.on("annotate", function(e) {
                session.setAnnotations(e.data);
            });

            this.$worker.on("terminate", function() {
                session.clearAnnotations();
            });

            this.$worker.on("log", function(e) {
                visualEditor.log(e.data);
            });

            this.$worker.on("callback", function(e) {
                visualEditor.ui.workerCallback(e.data.result, e.data.cmd);
            });

            return this.$worker;
        };

        this.$id = "ace/mode/AAL";

    }).call(Mode.prototype);

    exports.Mode = Mode;
});

/**
 * AAL Folding mode
 */
ace.define('ace/mode/aalFolding', function(require, exports, module) {
    var oop = require("../lib/oop");
    var BaseFoldMode = require("./folding/fold_mode").FoldMode;

    var FoldMode = exports.FoldMode = function(markers) {
        this.foldingStartMarker = new RegExp("([\\[{\(])(?:\\s*)$|(" + markers + ")(?:\\s*)(?:#.*)?$");
    };
    oop.inherits(FoldMode, BaseFoldMode);

    (function() {

        this.getFoldWidgetRange = function(session, foldStyle, row) {
            var line = session.getLine(row);
            var match = line.match(this.foldingStartMarker);
            if (match) {
                if (match[1])
                    return this.openingBracketBlock(session, match[1], row, match.index);
                if (match[2])
                    return this.indentationBlock(session, row, match.index + match[2].length);
                return this.indentationBlock(session, row);
            }
        }

    }).call(FoldMode.prototype);
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
            ", AFTER AND BEFORE EXISTS FORALL IF NOT ONLYWHEN OR THEN WHERE " +
            "APPLY AUDITING BEHAVIOR TEMPLATE CALL CHECK CLAUSE EXEC IF_VIOLATED_THEN LOAD MACRO OF TYPES PROVIDED PS PURPOSE REQUIRED RS ENV " +
            "ae ACTIONS ATTRIBUTES DENY EXTENDS UNION SUM INTERSEC GET_AUDIT GET_RECTIFICATION GET_USAGE PERMIT re SUBJECT ue "
        );

        //this.$keywordList = keywords;

        // Predefined Types
        var types = ("Behavior Template Clause Usage Rectification Audit Actor DataSubject DataController DataProcessor DwDataController Auditor CloudProvider CloudCustomer EndUser User Data");
        
        // Operators
        var operators = ("OR AND NOT THEN ONLYWHEN FORALL EXISTS IF WHERE");

        // Reflexion api functions
        var langFunctions = ("getClauses getDeclarations clause");

        // Keyword mapper
        var keywordMapper = this.createKeywordMapper({
            "variable.language": "this AGENT SERVICE DATA TYPE ref arg template",
            "keyword": keywords,
            "constant.language": "true false TRUE FALSE NULL SPACE",
            "support.type": types,
            "support.reflexion.functions": langFunctions,
            "constant.library": langFunctions,
            "keyword.operator": "ALWAYS MUST MUSTNOT NEVER SOMETIME UNTIL UNLESS NEXT",
            "variable.parameter": operators
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
                //{token : "keyword", regex : compoundKeywords},
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
