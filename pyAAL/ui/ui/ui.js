//////////////////////////////////////////////////////////
//
//  AccLab UI : ui.js
//
// Copyright (C) 2014 Walid Benghabrit
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//////////////////////////////////////////////////////////

visualEditor.ui = {
	grid             : null,
	actionsPanel     : null,
	componentsPanel  : null,
	propertiesPanel  : null,
	outlinePanel     : null,
	inplacePanel     : null,
	commandStack     : null,
	canvas           : null,
	selectedNode     : null,
	activeTab        : null,
    currentAAL       : null,
    interval         : null,
	psUpdateInterval : 10000,
	openedEditors    : {},
    consoleLog       : [],
    consolePredefs   : ['call', 'clear', 'agents', 'services', 'clauses'],

	/**
	 * init function
	 * @param grid
	 * @param actionsPanel
	 * @param componentsPanel
	 * @param propertiesPanel
	 */
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel, outlinePanel, inplacePanel) {
		// Get view elements
		this.grid            = $('#' + grid);
		this.actionsPanel    = $('#' + actionsPanel);
		this.componentsPanel = $('#' + componentsPanel);
		this.propertiesPanel = $('#' + propertiesPanel);
		this.outlinePanel    = $('#' + outlinePanel);
		this.inplacePanel    = $('#' + inplacePanel);

		//visualEditor.ui.canvas = new visualEditor.ui.gridEditor(grid, actionsPanel, componentsPanel, propertiesPanel);
		//visualEditor.ui.properties.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.tools.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.outline.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.fileManager.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.components.init(grid, actionsPanel, componentsPanel, propertiesPanel);

		toastr.options = {
			"closeButton": false,
			"debug": false,
			"newestOnTop": false,
			"progressBar": false,
			"positionClass": "toast-top-center",
			"preventDuplicates": false,
			"onclick": null,
			"showDuration": "200",
			"hideDuration": "700",
			"timeOut": "2000",
			"extendedTimeOut": "1000",
			"showEasing": "swing",
			"hideEasing": "linear",
			"showMethod": "fadeIn",
			"hideMethod": "fadeOut"
		};

		// Init ace editor wheelContextMenu
    	this.makeAceWheelContextMenu("acePops");

        // Hide ACD preview
        $("#preview").draggable().hide();
	},

	// Events
	handleEvents: function() {
		$(this).bind('nodeSelected', this.nodeSelected);
		$(this).bind('nodeUpdated', this.nodeUpdated);

	},

	nodeSelected: function() {
		//visualEditor.ui.properties.updateProps();
		//visualEditor.ui.outline.select(visualEditor.ui.selectedNode.id);
	},

	nodeUpdated: function() {
		visualEditor.ui.outline.canvasToTree();
	},

	stoper: function(e) {
		e.stopPropagation();
		e.preventDefault()
	},

	updateToastSize: function(type, size, dragable, icon) {
        var l = $(".toast-" + type);
        if(l[l.length - 1] != undefined) {
            if(size.width != undefined) $(l[l.length - 1]).css("width", size.width + "px");
            if(size.height != undefined) $(l[l.length - 1]).css("height", size.height + "px");
            if(dragable) $(l[l.length - 1]).draggable();
			if(icon != undefined || icon != null) {
                var p =  $(l[l.length - 1]).attr("style");
				 $(l[l.length - 1]).attr("style", p + "background-image: " + icon + " !IMPORTANT;");
            }
        }
    },

	/**
	 * Update all panels states
	 */
	updatePanel: function() {
		var file = "";
		if(visualEditor.ui.activeTab != null)
			file = visualEditor.ui.activeTab.container.title;

		var fileType = file.split('.').pop().toLowerCase();
		var tt = visualEditor.ui.tools.tools;
		// If it is not a diagram, disable gui elements
		if(fileType != "acd" && fileType != "vfodtl") {
            $("#preview").hide();
			//this.disableNode(this.propertiesPanel);
			//this.disableNode(this.actionsPanel);
			for(var i=0; i<tt.length; i++) {
				$(tt[i].button).hide();
			}
			this.disableNode(this.componentsPanel);
			this.disableNode(this.outlinePanel);
			this.disableNode(this.inplacePanel);

			if(file != "") {
				$(visualEditor.ui.tools.tools[11].button).show();
				$(visualEditor.ui.tools.tools[14].button).show();
				$(visualEditor.ui.tools.tools[18].button).show();
				$(visualEditor.ui.tools.tools[19].button).show();
				$(visualEditor.ui.tools.tools[23].button).show();
			}
			if(fileType == "aal") {
				$(visualEditor.ui.tools.tools[20].button).show();
				$(visualEditor.ui.tools.tools[21].button).show();
				$(visualEditor.ui.tools.tools[22].button).show();
			}

		} else {
            $("#preview").show();
			// Enable them
			//this.enableNode(this.propertiesPanel);
			//this.enableNode(this.actionsPanel);
			for(var i=0; i<tt.length; i++) {
				$(tt[i].button).show();
			}
			this.enableNode(this.componentsPanel);
			this.enableNode(this.outlinePanel);
			this.enableNode(this.inplacePanel);
			$(visualEditor.ui.tools.tools[18].button).hide();
			$(visualEditor.ui.tools.tools[20].button).hide();
			$(visualEditor.ui.tools.tools[21].button).hide();
		}
	},

    /**
     * Get current opened file name
     * @returns {*}
     */
    getOpenedFile: function() {
        return visualEditor.ui.activeTab.container.title;
    },

	/**
	 * Enable a node
	 * @param node
	 */
	enableNode: function(node) {
        node.children().fadeTo('slow', 1.0);
        node[0].removeEventListener("click", this.stoper, true);
	},

	/**
	 * Disable a node
	 * @param node
	 */
	disableNode: function(node) {
        node.children().fadeTo('slow', .15);
        node[0].addEventListener("click", this.stoper, true);
	},

	/**
	 * Generate AAL code
	 */
	generateAAL: function(file_name) {
		var date = new Date(Date.now()).toUTCString();
		var aal = "/**\n * Generated AAL file \n * @diagram source : " + file_name +
            "\n * @author : " + visualEditor.getUserName() + "\n * @on : " + date + "\n */\n\n" +
            "\n// Loading types & macros libraries\nLOAD \"core.types\"\nLOAD \"core.macros\"\n\n";
		var figs = visualEditor.ui.canvas.getFigures();
		var tmp = null;
		
		// Handle declarations
		aal += "/***************************\n *       Declarations\n ****************************/\n";
		aal += "// Actors\n";
		for(var i=0; i<figs.getSize(); i++) {
			tmp = figs.get(i);
			aal += tmp.getAALDeclaration()+"\n";
		}

		aal += "\n// Services\n";
		var services = "";
		for(var i=0; i<figs.getSize(); i++) {
			tmp = figs.get(i);
			services += tmp.getRservices().data + ",";
			services += tmp.getPservices().data + ",";
		}

		var servicesTmp = services.split(",");
		var servicesTmp2 = [];
		$.each(servicesTmp, function(i, el){
    		if($.inArray(el, servicesTmp2) === -1 && el != "") servicesTmp2.push(el);
		});

		for(var i=0; i<servicesTmp2.length; i++) {
			aal += "SERVICE " + servicesTmp2[i] + "\n";
		}

		// Handle clauses
		aal += "\n/***************************\n *       Clauses\n ****************************/\n";
		for(var i=0; i<figs.getSize(); i++) {
			tmp = figs.get(i);
			var tmp_policy = tmp.policy;
			if(tmp_policy != "")
				aal += tmp_policy + "\n\n";
		}
		return aal;
	},

    /**
     * Analyse opened AAL file and update info
     */
	analyseAAL: function (aalFile, callback) {
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.backend,
            data: {action: "getAALdec", file: aalFile},
            success: function(response) {
                visualEditor.ui.currentAAL = jQuery.parseJSON(response);
				if(callback != null || callback != undefined)
					callback(response)
            }
	    });
    },

    /**
     * Convert fodtl formula to diagram
     */
    fodtlToDiagram: function(formula, callback) {
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.backend,
            data: {action: "fodtlToDiagram", formula: formula},
            success: function(response) {
                visualEditor.fodtl_to_vfodtl(response);
				if(callback != null || callback != undefined)
					callback(response)
            }
	    });
    },

    /**
     * Highligh line
     */
    clearHighlight: function() {
        if(visualEditor.activeEditor != null) {
            var markers = visualEditor.activeEditor.session.$backMarkers;
            for(var key in markers){
                if(markers[key].clazz.startsWith("aceHighlight"))
                    visualEditor.activeEditor.session.removeMarker(markers[key].id);
            }
        }
    },

    /**
     * Highlight selected text / current line
     */
    highlight: function(theme) {
        if(visualEditor.activeEditor != null) {
            var sr = visualEditor.activeEditor.getSelectionRange();
            // Select one line
             var range = null;
            if(sr.start.column ==  sr.end.column)
                range = new Range(sr.start.row, 0, sr.end.row, Number.MAX_VALUE);
            else
                range = new Range(sr.start.row, sr.start.column, sr.end.row, sr.end.column);
            visualEditor.activeEditor.session.addMarker(range, theme, "line");
        }
    },

    highlightRed: function() {
        visualEditor.ui.highlight("aceHighlightRed");
    },

    highlightGreen: function() {
        visualEditor.ui.highlight("aceHighlightGreen");
    },


    /**
     * Create the ace editor wheel context menu
     */
    makeAceWheelContextMenu: function(target_id) {
        var pops = $("#" + target_id);

        var btn = new visualEditor.ui.tools.saveTool();
        btn.button = $('<li><div title="Save (ctrl+S)" id="saveBtn" class="btn-action fa fa-save fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        btn = new visualEditor.ui.tools.genTSPASSTool();
        btn.button = $('<li><div title="Compile (ctrl+Enter)" id="genTSPASSBtn" class="btn-action fa fa-cog fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        btn = new visualEditor.ui.tools.AALSyntaxTool();
        btn.button = $('<li><div title="AAL Syntax (ctrl+M)" id="aalSyntaxBtn" class="btn-action fa fa-file-code-o fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        btn = new visualEditor.ui.tools.templatesTool();
        btn.button = $('<li><div title="AAL policy wizard (ctrl+e)" id="tmpBtn" class="btn-action fa fa-magic fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        btn = new visualEditor.ui.tools.clearOutputTool();
        btn.button = $('<li><div title="Clear output" id="clearOutputBtn" class="btn-action fa fa-square-o  fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        // Bind the event listener to the trigger
        $("#aceTrigger").bind("mousedown", visualEditor.ui.toggleAceWheelContextMenu);

        // Make the wheel draggable
        $("#aceWheelContextMenu").draggable()
    },

    /**
     * Toggle Ace Wheel Context Menu
     */
    toggleAceWheelContextMenu: function(e) {
        var wcm = $("#aceWheelContextMenu");
        wcm.toggle("display");
        wcm.css("top", e.clientY - 75);
        wcm.css("left", e.clientX - 75);

        $.popcircle('#acePops', {
                spacing:'-5px',
                type:'full',        // full, half, quad
                offset:0,	        // 0, 1, 2, 3, 4, 5, 6, 7 or 5.1
                ease:'easeOutQuad', // jquery ease effects,
                time:'fast'         // slow, fast, 1000
            });
    },

    /**
     * Eval command
     * @param input
     */
	evalCmd: function(input) {
        var tmp = input.split(" ");
        var cmd = tmp[0];
        var args = tmp[1];

        switch(cmd.toLowerCase()) {
            case "clear": $("#output_window").empty(); break;

            // Calling Macros
            case "call":
                var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
                var file = visualEditor.ui.activeTab.container.title;
                var macro_name = input.substring(cmd.length + 1, input.indexOf('(')).trim();
                var macro_args = "[" + input.substring(input.indexOf('(') + 1, input.indexOf(')')).replace(/\s\s+/g, ' ')
                    .split(" ").toString() + "]";
                visualEditor.ui.fileManager.saveFile(file, editor.getValue(), function() {
                    var file = visualEditor.ui.activeTab.container.title;
                    $.ajax({
                        dataType: "text",
                        type: "POST",
                        url: visualEditor.backend,
                        data: {action: "macroCallAPI", file: file, macro: macro_name, args: macro_args},
                        success: function (response) {
                            toastr.clear($(".toast-error"));
                            $("#output_window").empty().append(response).scrollTop(0);
                            $(".aceLine").click(function (e) {
                                var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
                                if (editor != undefined && editor != null)
                                    editor.gotoLine(parseInt(e.target.innerHTML.replace("at line ", "")));
                            });
                        }
                    });
                });
                break;

            // Get AAL nodes
            case "agents"  : visualEditor.activeEditor.postMsgWorker("getAgents"); break;
            case "services": visualEditor.activeEditor.postMsgWorker("getServices"); break;
            case "clauses" : visualEditor.activeEditor.postMsgWorker("getClauses"); break;

            // Miscellaneous
            case "visu" : visualEditor.ui.createVisualAAL(); break;

            default:
                // Should print help
                visualEditor.log("HELP : (note : commands are not case sensitive)" +
                    "\n- CLEAR : clean the output console" +
                    "\n- CALL macro_name(macro_args) : Call a macro" +
                    "\n- AGENTS : Print all declared agents in the current AAL file" +
                    "\n- SERVICES: Print all declared services in the current AAL file" +
                    "\n- CLAUSES : Print all declared clauses in the current AAL file" +
                    "\n- VISU : Generate diagram for the current AAL file"
                );
                break;
        }
    },


    /**
     * Worker Callback
     * @param res
     * @param cmd
     */
    workerCallback: function(res, cmd) {
        switch (cmd) {
            case "getAgents":
                // TODO improve
                visualEditor.log(res.agents);
                break;
            case "getServices":
                visualEditor.log(res.services);
                break;
            case "getClauses":
                visualEditor.log(res.clauses);
                break;
            case "analyseAALtreeForAcd":
                var agentGenerator = new Actor();
                for(var i=0; i<res.agents.length; i++) {
                    var e = agentGenerator.addElement(null, res.agents[i].name);
                    res.agents[i].rs.forEach(function(v) {e.addEntity(v, "RS");});
                    res.agents[i].ps.forEach(function(v) {e.addEntity(v, "PS");});
                }
                break;
        }
    },


    /**
     *
     * @param file
     */
    createVisualAAL: function(file) {
        if(visualEditor.activeEditor != null) {
            // Create a new editor window
            var id = visualEditor.guid();
            var editor = $('<div id="'+id+'" caption="' + file + '" class="editor1-window editor-host"></div>');
            $(document.body).append(editor);
            var editor4 = new dockspawn.PanelContainer($("#"+id)[0], dockManager);
            var editor4Node  = dockManager.dockRight(documentNode, editor4, 0.5);
            editor4.canvas = new visualEditor.ui.gridEditor(id, "toolbox_window", "componentbox_window", "properties_window", "acd");
            visualEditor.ui.canvas = editor4.canvas;

            // AAL to nodes
            visualEditor.activeEditor.postMsgWorker("analyseAALtreeForAcd");
        }
    },

    /**
     * Generate Accmon spec
     */
    generateAccmon: function(spec) {
        spec = (spec === "")?" ": spec;
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.backend,
            data: {action: "genAccmon", spec: spec, file: visualEditor.ui.activeTab.container.title},
            success: function(response){
                if(response != 'Error') {
                    $("#explorer").tree("reload");
                    visualEditor.ui.fileManager.openFile(response);
                }
            }
	    });
    },

    /**
     * Register the current opened vfodtl file in AccMon
     */
    registerVfodtlToAccMon: function(url, name) {
        var formula = visualEditor.vFodtl_to_fodtl(visualEditor.ui.canvas);
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.backend,
            data: {action: "registerAccMonMonitor", formula: formula, name: name, accmon_url: url},
            success: function(response){
                console.log(response);
            }
	    });
    }
};
