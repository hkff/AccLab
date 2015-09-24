ace.define('ace/snippets/AAL', function(require, exports, module) {
    exports.snippetText =
        [
            '## Clause \n',
            'snippet clause\n	CLAUSE ${1:name} (\n	  ${2:usage}\n	  AUDITING true\n	  IF_VIOLATED_THEN true\n	) \n',
            '## Declarations \n',
            'snippet agent\n	AGENT ${1:id} TYPES(${2}) REQUIRED(${3}) PROVIDED(${4}) \n'
        ]
        .join('');
    exports.scope = "AAL";

});

/*
    snippet po\n	protected\n
    ## Comment
    snippet name
    Content  ${1:args} \n	(tab after \n)
 */