ace.define("ace/snippets/AAL", ["require", "exports", "module"], function(e, t, n) {
    "use strict";
    t.snippetText = '## Access Modifiers\nsnippet po\n	protected\nsnippet pu\n	public\nsnippet pr\n' +
    '	private\n##\n## Annotations\nsnippet before\n	@Before\n	static void ${1:intercept}(${2:args}) { ${3} }' +
    '\nsnippet mm\n	@ManyToMany\n	${1}\nsnippet mo\n	@ManyToOne\n	${1}\nsnippet om\n	' +
    '@OneToMany${1:(cascade=CascadeType.ALL)}\n	${2}\nsnippet oo\n	'
    , t.scope = "java"
})
