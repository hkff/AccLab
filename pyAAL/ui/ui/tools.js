//////////////////////////////////////////////////////////
//
//  AccLab UI : tools.js
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

visualEditor.ui.tools = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	tools           : [],

	/**
	 * init function
	 * @param grid
	 * @param actionsPanel
	 * @param componentsPanel
	 * @param propertiesPanel
	 */
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel) {
		
		// Get view elements
		this.grid            = $('#'+ grid);
		this.actionsPanel    = $('#'+ actionsPanel);
		this.componentsPanel = $('#'+ componentsPanel);
		this.propertiesPanel = $('#'+ propertiesPanel);

		//$('#clear-graph').toolbar({
		//	content: '#user-toolbar-options',
		//	position: 'top',
		//	hideOnClick: true
		//});

		this.toolsRegistrator();
		this.view(this);
		this.control(this);
	},

	/**
	 * @method
	 * Register tools
	 */
	toolsRegistrator: function() {
		this.tools.push(new visualEditor.ui.tools.selectTool());               // 0
		this.tools.push(new visualEditor.ui.tools.panneTool());                // 1
		this.tools.push(new visualEditor.ui.tools.mselectTool());              // 2
		this.tools.push(new visualEditor.ui.tools.copyTool());                 // 3
		this.tools.push(new visualEditor.ui.tools.deleteTool());               // 4
		this.tools.push(new visualEditor.ui.tools.lockTool());                 // 5
		this.tools.push(new visualEditor.ui.tools.zoomInTool());               // 6
		this.tools.push(new visualEditor.ui.tools.zoomOutTool());              // 7
		this.tools.push(new visualEditor.ui.tools.zoomOriginTool());           // 8
		this.tools.push(new visualEditor.ui.tools.undoTool());                 // 9
		this.tools.push(new visualEditor.ui.tools.redoTool());                 // 10
		this.tools.push(new visualEditor.ui.tools.saveTool());                 // 11
		this.tools.push(new visualEditor.ui.tools.groupTool());                // 12
		this.tools.push(new visualEditor.ui.tools.ungroupTool());              // 13
		this.tools.push(new visualEditor.ui.tools.fullScreenTool());           // 14
		this.tools.push(new visualEditor.ui.tools.clearTool());                // 15
		this.tools.push(new visualEditor.ui.tools.separatorTool());            // 16
		this.tools.push(new visualEditor.ui.tools.genAALTool());               // 17
		this.tools.push(new visualEditor.ui.tools.genTSPASSTool());            // 18
		this.tools.push(new visualEditor.ui.tools.keyboardShortcutsTool());    // 19
		this.tools.push(new visualEditor.ui.tools.AALSyntaxTool());            // 20
		this.tools.push(new visualEditor.ui.tools.templatesTool());            // 21
		this.tools.push(new visualEditor.ui.tools.acethemeTool());             // 22
		this.tools.push(new visualEditor.ui.tools.clearOutputTool());          // 23
		this.tools.push(new visualEditor.ui.tools.simulationTool());           // 24
	},

	/**
	 * View
	 */
	view: function(_this) {
		// Render all tools
		for (var i=0; i<this.tools.length; i++) {
			this.tools[i].view(this);
		}
	},

	/**
	 * Controller
	 */
	control: function(_this) {
		for (var i=0; i<this.tools.length; i++) {
			this.tools[i].control(this);
		}
	}
};


//////////////////////////////////////////////////////////
//
//  Tool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tool = Class.extend({
	NAME : "visualEditor.ui.tool",
	
	view: function(parent) {
	},

	control: function(parent) {
	}
});


//////////////////////////////////////////////////////////
//
//  separatorTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.separatorTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.separatorTool",
	
	view: function(parent) {
		parent.actionsPanel.append("<br><hr>");
	},

	control: function(parent) {
	}
});


//////////////////////////////////////////////////////////
//
//  selectTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.selectTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.selectTool",
	
	view: function(parent) {
		this.button = $('<div title="Selection mode" id="selectBtn" class="btn-action fa fa-hand-o-up fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.installEditPolicy(new CopyInterceptorPolicy());
		});
	}
});

//////////////////////////////////////////////////////////
//
//  panneTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.panneTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.panneTool",

	view: function(parent) {
		this.button = $('<div title="Move mode" id="panneBtn" class="btn-action fa fa-arrows fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.installEditPolicy(new draw2d.policy.canvas.PanningSelectionPolicy());
		});
	}
});

//////////////////////////////////////////////////////////
//
//  mselectTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.mselectTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.mselectTool",

	view: function(parent) {
		this.button = $('<div title="Multiple Selection Mode" id="mselectBtn" class="btn-action fa fa-square fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.installEditPolicy(new draw2d.policy.canvas.BoundingboxSelectionPolicy());
		});
	}
});


//////////////////////////////////////////////////////////
//
//  copyTool
//
//////////////////////////////////////////////////////////

visualEditor.ui.tools.copyTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.copyTool",

	view: function(parent) {
		this.button = $('<div title="Duplicate" id="copyBtn" class="btn-action fa fa-copy fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		this.button.click(function(e) {
			var p = visualEditor.ui.canvas.getSelection().primary.clone();
			visualEditor.ui.canvas.add(p, 100, 100);
		});
	}
});


//////////////////////////////////////////////////////////
//
//  deleteTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.deleteTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.deleteTool",

	view: function(parent) {
		this.button = $('<div title="Delete" id="deleteBtn" class="btn-action fa fa-trash-o fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
            visualEditor.ui.canvas.getCommandStack().execute(
                new draw2d.command.CommandDelete(visualEditor.ui.canvas.getSelection().primary));
		});
	}
});

//////////////////////////////////////////////////////////
//
//  lockTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.lockTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.lockTool",

	view: function(parent) {
		this.button = $('<div title="Lock diagram" id="lockBtn" class="btn-action fa fa-lock fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.installEditPolicy(new draw2d.policy.canvas.ReadOnlySelectionPolicy());
		});
	}
});

//////////////////////////////////////////////////////////
//
//  zoomInTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.zoomInTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.zoomInTool",

	view: function(parent) {
		this.button = $('<div title="Zoom in (Page_up)" id="zoomInBtn" class="btn-action fa fa-search-plus fa-lg"/>');
		parent.actionsPanel.append(this.button);
		
	},

	control: function(parent) {
		var fx = function(e){
			visualEditor.ui.canvas.setZoom(visualEditor.ui.canvas.getZoom()*0.7, true);	
		};

		this.button.click(fx);
		shortcut.add("Page_up", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  zoomOutTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.zoomOutTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.zoomOutTool",

	view: function(parent) {
		this.button = $('<div title="Zoom out (Page_down)" id="zoomOutBtn" class="btn-action fa fa-search-minus fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		var fx = function(e){
			visualEditor.ui.canvas.setZoom(visualEditor.ui.canvas.getZoom()*1.3, true);	
		};
		this.button.click(fx);
		shortcut.add("Page_down", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  zoomOriginTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.zoomOriginTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.zoomOriginTool",

	view: function(parent) {
		this.button = $('<div title="Original size" id="zoomOriginBtn" class="btn-action fa fa-search fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.setZoom(1.0, true);	
		});
	}
});

//////////////////////////////////////////////////////////
//
//  undoTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.undoTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.undoTool",

	view: function(parent) {
		this.button = $('<div title="Undo" id="undoBtn" class="btn-action fa fa-undo fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.getCommandStack().undo();
		});
	}
});

//////////////////////////////////////////////////////////
//
//  redoTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.redoTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.redoTool",

	view: function(parent) {
		this.button = $('<div title="Redo" id="redoBtn" class="btn-action fa fa-repeat fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.getCommandStack().redo();
		});
	}
});

//////////////////////////////////////////////////////////
//
//  saveTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.saveTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.saveTool",

	view: function(parent) {
		this.button = $('<div title="Save (ctrl+S)" id="saveBtn" class="btn-action fa fa-save fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {

		var fx = function(e) {
			var file = visualEditor.ui.activeTab.container.title;
			var fileType = file.split('.').pop().toLowerCase();
			switch (fileType) {
				case "aal":
					var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
					visualEditor.ui.fileManager.saveFile(file, editor.getValue());
                    if(visualEditor.activeEditor != null)
                        visualEditor.activeEditor.session.getUndoManager().markClean();
                    // Remove save marker
					visualEditor.markPanelClear();
					break;

				case "acd": case "vfodtl":
					var writer = new draw2d.io.json.Writer();
					writer.marshal(visualEditor.ui.canvas, function (json) {
						// convert the json object into string representation
						var jsonTxt = JSON.stringify(json, null, 2);
						// insert the json string into a DIV for preview or post
						visualEditor.ui.savedCanvas = jsonTxt;

						var file = visualEditor.ui.activeTab.container.title;
						visualEditor.ui.fileManager.saveFile(file, jsonTxt);
					});
					break;

				default:
					var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
					visualEditor.ui.fileManager.saveFile(file, editor.getValue());
					if(visualEditor.activeEditor != null)
                        visualEditor.activeEditor.session.getUndoManager().markClean();
                    // Remove save marker
                    visualEditor.markPanelClear();
					break;
			}
		};
		this.button.click(fx);
		if(disableShortcut != null) return;
		shortcut.add("Ctrl+S", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  groupTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.groupTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.groupTool",

	view: function(parent) {
		this.button = $('<div title="Group" id="groupBtn" class="btn-action fa fa-link fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.getCommandStack().execute(
				new draw2d.command.CommandGroup(visualEditor.ui.canvas, visualEditor.ui.canvas.getSelection())
			);
		});
	}
});

//////////////////////////////////////////////////////////
//
//  ungroupTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.ungroupTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.ungroupTool",

	view: function(parent) {
		this.button = $('<div title="Ungroup" id="ungroupBtn" class="btn-action fa fa-unlink fa-lg"/>');
		parent.actionsPanel.append(this.button);

	},

	control: function(parent) {
		this.button.click(function(e){
			visualEditor.ui.canvas.getCommandStack().execute(
				new draw2d.command.CommandUngroup(visualEditor.ui.canvas, visualEditor.ui.canvas.getSelection())
				);
		});
	}
});

//////////////////////////////////////////////////////////
//
//  fullScreenTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.fullScreenTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.fullScreenTool",

	view: function(parent) {
		this.button = $('<div title="Fullscreen (F11)" id="fullScreenBtn" class="btn-action fa fa-arrows-alt fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		var fx = function(e){
			if (screenfull.enabled){
				if(screenfull.isFullscreen)
					screenfull.exit();
				else
					screenfull.request();
			}
		};

		this.button.click(fx);
		shortcut.add("F11", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  clearTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.clearTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.clearTool",

	view: function(parent) {
		this.button = $('<div title="Clear diagram" id="clearBtn" class="btn-action fa fa-eraser fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		this.button.click(function(e){
			//var reader = new draw2d.io.json.Reader();
			//visualEditor.ui.canvas.clear();
 			//reader.unmarshal(visualEditor.ui.canvas , visualEditor.ui.savedCanvas );
			var clauses = visualEditor.ui.canvas.getFigures().data.filter(function(e){return e.type === "Policy"});
			for(var i=0; i<clauses.length; i++) {
				clauses[i].refresh();
				var cons = clauses[i].getConnections();
				for(var j=0; j<cons.getSize(); j++)
					cons.get(j).setColor("#00A8F0");
			}
		});
	}
});


//////////////////////////////////////////////////////////
//
//  GenerateAALTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.genAALTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.genAALTool",
	
	view: function(parent) {
		this.button = $('<div title="Generate (ctrl+G)" id="genAALBtn" class="btn-action fa fa-file-text-o fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {
		var fx = function(e){
			var active = visualEditor.ui.activeTab.container.title;
			var activeFileType = visualEditor.ui.fileManager.getFileType(active);
            if(activeFileType === "acd"){
				//visualEditor.log(visualEditor.ui.generateAAL(active), true);
				// TODO test if file exists
				visualEditor.ui.fileManager.showGeneratedAAL(active, active.replace(".acd", ".aal"));
            } else if(activeFileType === "vfodtl"){
                if(visualEditor.vFodtl_check(visualEditor.ui.canvas) == true)
                    var formulas = visualEditor.vFodtl_to_fodtl(visualEditor.ui.canvas);
                    for(var i=0; i<formulas.length; i++)
                        visualEditor.log(formulas[i]);
            }
		};
		this.button.click(fx);
		if(disableShortcut != null) return;
		shortcut.add("Ctrl+G", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  GenerateTSPASSTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.genTSPASSTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.genTSPASSTool",
	
	view: function(parent) {
		this.button = $('<div title="Compile (ctrl+Enter)" id="genTSPASSBtn" class="btn-action fa fa-cog fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {
		var fx = function(e){
            var file = visualEditor.ui.activeTab.container.title;
			var fileType = file.split('.').pop().toLowerCase();

			if(fileType == "acd") {
				// ------------------------ Compile ACD
				toastr.error("<i class='fa fa-cog fa-spin'></i>", "Compiling...", {
						"closeButton": true,
						"preventDuplicates": true,
						"tapToDismiss": false,
						"showDuration": "2000",
						"hideDuration": "1000",
						"timeOut": 0,
						"extendedTimeOut": 0,
						"positionClass": "toast-top-center"
				});
				var action = "compileACD";
				var data = visualEditor.ui.checkPolicies();
				$.ajax({
					dataType: "json",
					type:'POST',
					url: visualEditor.backend,
					data: {action: action, aal: data.aal, spec: data.spec},
					success: function(response){
						$("#output_window").empty().append(response).scrollTop(0);
						var clauses = visualEditor.ui.canvas.getFigures().data.filter(function(e){return e.type === "Policy"});
						// Handle sat
						for(var i=0; i<clauses.length; i++) {
							for(var x in response.sat) {
								if(response.sat[x].hasOwnProperty(clauses[i].tlabel.text)) {
									if(response.sat[x][clauses[i].tlabel.text] === "Unsatisfiable")
										clauses[i].setBackgroundColor('#f3546a');
									else if(response.sat[x][clauses[i].tlabel.text] === "Satisfiable")
										clauses[i].setBackgroundColor('#b9dd69');
									break;
								}
							}
						}

						// Handle Compliance
						for(var i=0; i<clauses.length; i++) {
							var op = clauses[i].getOutputPorts();
							for(var j=0; j<op.getSize(); j++) {
								var con = op.get(j).getConnections();
								for(var k=0; k<con.getSize(); k++) {
									var tmp = clauses[i].tlabel.text + "->" + con.get(k).targetPort.parent.tlabel.text;
									for(var p=0; p<response.compliance.length; p++) {
										if (response.compliance[p].hasOwnProperty(tmp)) {
											if (response.compliance[p][tmp] === "false")
												con.get(k).setColor('#f3546a');
											else if(response.compliance[p][tmp] === "true")
												con.get(k).setColor('#b9dd69');
										}
									}
								}
							}
						}
						if(response.error != "")
							visualEditor.log(response.error, true);

						toastr.clear( $(".toast-error"));
					}
				});

			} else {
				// ------------------------ Compile AAL / TSPASS
				var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
				visualEditor.ui.fileManager.saveFile(file, editor.getValue(), function(){
					var file = visualEditor.ui.activeTab.container.title;
					var dType = "text";
					var action = "compileAAL";
					var fileType = file.split('.').pop().toLowerCase();
					if(fileType == "tspass")
						action = "compileFOTL";

					toastr.error("<i class='fa fa-cog fa-spin'></i>", "Compiling...", {
						"closeButton": true,
						"preventDuplicates": true,
						"tapToDismiss": false,
						"showDuration": "2000",
						"hideDuration": "1000",
						"timeOut": 0,
						"extendedTimeOut": 0,
						"positionClass": "toast-top-center",
						"onHidden": function() {
							$.ajax({
								dataType: 'text',
								type: 'POST',
								url: visualEditor.backend,
								data: {action: "cancelCurrentPS"},
								success: function (response) {
									$("#output_window").empty().append(response).scrollTop(0);
								}
							});
						}
					});
					$.ajax({
						dataType: dType,
						type:'POST',
						url: visualEditor.backend,
						data: {action: action, file: file},
						success: function(response){
							$("#output_window").empty().append(response).scrollTop(0);
							// Clear toastr
							toastr.clear( $(".toast-error"));
                            // Reload the file
                            visualEditor.ui.fileManager.reloadFile(false);
							// Setup lines
							$(".aceLine").click(function(e) {
								var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
								if (editor != undefined && editor != null)
									editor.gotoLine(parseInt(e.target.innerHTML.replace("at line ", "")));
							});
						}
					});
            	});
			}

            if(visualEditor.activeEditor != null)
				visualEditor.activeEditor.session.getUndoManager().markClean();
			// Remove save marker
			visualEditor.markPanelClear();
		};

		this.button.click(fx);
		if(disableShortcut != null) return;
		shortcut.add("Ctrl+Enter", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  keyboardShortcutsTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.keyboardShortcutsTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.keyboardShortcutsTool",

	view: function(parent) {
		this.button = $('<div title="Keyboard Shortcuts (ctrl+k)" id="ksBtn" class="btn-action fa fa-keyboard-o fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		var fx = function(e){
			var p = "<div id='keyboardShortcuts'>" +
			"<style>.keyword{color:orange;}</style>" +
			"<div style='width:500px; overflow: hidden;'>" +
			"	<b>Shortcuts</b><br>" +
			"	<ul style='list-style: disc inside; list-style-type: disc;list-style-position: inside;" +
			"list-style-image: initial;padding-left: 0px;margin-bottom: 0px;line-height: normal;}'>" +
					"<li><b class='keyword'>CTRL+S -</b> Save current file</li>" +
					"<li><b class='keyword'>CTRL+F -</b> Find in current editor</li>" +
					"<li><b class='keyword'>CTRL+H -</b> Advanced Search / Search &amp; Replace</li>" +
					"<li><b class='keyword'>CTRL+A -</b> Select all</li>" +
					"<li><b class='keyword'>CTRL+D -</b> Delete current line(s)</li>" +
					"<li><b class='keyword'>CTRL+P -</b> Find matching element [{()}]</li>" +
					"<li><b class='keyword'>CTRL+L -</b> Go To Line</li>" +
					"<li><b class='keyword'>CTRL+ENTER -</b> Compile</li>" +
					"<li><b class='keyword'>CTRL+G -</b> Generate AAL file from diagram</li>" +
					"<li><b class='keyword'>CTRL+M -</b> AAL Syntax</li>" +
					"<li><b class='keyword'>CTRL+K -</b> Keyboard shortcuts</li>" +
                    "<li><b class='keyword'>ALT+C -</b> Toggle comment</li>" +
					"<li><b class='keyword'>ALT+SHIFT+C -</b> Toggle multi-line comment</li>" +
                    "<li><b class='keyword'>ALT+0 -</b> Fold all</li>" +
                    "<li><b class='keyword'>ALT+SHIFT+0 -</b> Unfold all</li>" +
					"<li><b class='keyword'>F11 -</b> Full screen</li>" +
					"<li><b class='keyword'>ALT+Up -</b>Arrow - Move current line(s) up</li>" +
					"<li><b class='keyword'>ALT+Down -</b>Arrow - Move current line(s) down</li>" +
					"<li><b class='keyword'>ALT+Shift+Up -</b>Arrow - Copy current line(s) above current</li>" +
					"<li><b class='keyword'>ALT+Shift+Down -</b>Arrow - Copy current line(s) below current</li>" +
					"<li><b class='keyword'>CTRL+Space bar -</b> Autocomplete</li>" +
					"<li><b class='keyword'>CTRL+Click -</b> Multiedit</li>" +
					"<li><b class='keyword'>ALT+A -</b> Highlight green</li>" +
                    "<li><b class='keyword'>ALT+Z -</b> Highlight red</li>" +
                    "<li><b class='keyword'>ALT+H -</b> Clear all highlights</li>" +
					"<a href='https://github.com/ajaxorg/ace/wiki/Default-Keyboard-Shortcuts'" +
					" target='_blank'>Click here for more ace editor shortcuts </a>" +
			"</ul>" +
			"</div></div>";

			toastr.info(p, "", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": true,
  				"showDuration": "3000",
			  	"hideDuration": "1000",
			  	"timeOut": 0,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-right"
			});
            visualEditor.ui.updateToastSize("info", {"width": 500}, true);
		};
		this.button.click(fx);
		shortcut.add("Ctrl+K", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  AALSyntaxTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.AALSyntaxTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.AALSyntaxTool",

	view: function(parent) {
		this.button = $('<div title="AAL Syntax (ctrl+M)" id="aalSyntaxBtn" class="btn-action fa fa-file-code-o fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {
		var fx = function(e){
			var p =
			"<div id='modal-content'>" +
            "<div style='width:950px'>" +
            "<style>" +
                ".keyword{color:orange; padding-right: 5px;} " +
                ".rule {padding-bottom: 0px;} " +
                ".coms {color: green;} " +
                ".ref {color: yellow;}" +
                ".select {width: 60px; height: 18px; float: left; border: none;" +
                         "margin-right: 5px; margin-left: 5px; margin-top: 0px;" +
                         "font-size: 12px; padding-left: 3px; padding: 0px 0px;}" +
            "</style>" +
            "<b>AAL syntax</b>" +
            "<pre>" +
				"<b class='coms'>// AAL core</b>" +
				"\nAALprogram    ::= (Declaration | Clause | Comment | Macro | MacroCall | Loadlib" +
                    "| LtlCheck | CheckApply | Exec)" +
				"\nDeclaration   ::= AgentDec | ServiceDec | DataDec | TypesDec | varDec" +
				"\nAgentDec      ::= AGENT Id [TYPES '(' Type *')' REQUIRED'('service*')' PROVIDED'('service*')']" +
				"\nServiceDec    ::= SERVICE Id [TYPES '(' Type* ')'] [PURPOSE '(' Id* ')']" +
				"\nDataDec       ::= DATA Id TYPES '(' Type* ')' [REQUIRED'('service*')' PROVIDED'('service*')'] SUBJECT agent" +
				"\nVarDec        ::= Type_Id Id [attr_Id '(' value* ')']*" +
				"\nClause        ::= CLAUSE Id '(' [Usage] [Audit Rectification] ')'" +
				"\nUsage         ::= ActionExp" +
				"\nAudit         ::= AUDITING Usage" +
				"\nRectification ::= IF_VIOLATED_THEN Usage" +
				"\nActionExp     ::= Action | NOT ActionExp | Modality ActionExp | Condition" +
			    "\n               | ActionExp (AND|OR|ONLYWHEN|UNTIL|UNLESS) ActionExp" +
			    "\n               | Author | Quant* | IF '(' ActionExp ')' THEN '{' ActionExp '}'" +
				"\nExp           ::= Variable | Constant | Variable.Attribute" +
				"\nCondition     ::= [NOT] Exp | Exp ['==' | '!='] Exp | Condition (AND|OR) Condition" +
				"\nAuthor        ::= (PERMIT | DENY) Action" +
				"\nAction        ::= agent.service ['['[agent]']'] '('Exp')' [Time] [Purpose]" +
				"\nQuant         ::= (FORALL | EXISTS) Var [WHERE Condition]" +
				"\nVariable      ::= Var ':' Type" +
				"\nModality      ::= MUST | MUSTNOT | ALWAYS | NEVER | SOMETIME" +
				"\nTime          ::= (AFTER | BEFORE) Date | Time (AND | OR) Time" +
				"\nDate          ::= STRING" +
				"\nType, var, val, attr Id, agent, Constant, Purpose ::= literal" +
				"\n<b class='coms'>// AAL Type extension</b>" +
				"\nTypesDec      ::= TYPE Id [EXTENDS '(' Type* ')'] ATTRIBUTES '(' AttributeDec* ')' ACTIONS '(' ActionDec* ')'" +
				"\nAttributeDec  ::= Id ':' Type" +
				"\nActionDec     ::= Id" +
				"\nType, Id      ::= litteral" +
				"\n<b class='coms'>// Reflexion extension</b>" +
				"\nMacro         ::= MACRO Id '(' param* ')' '(' mcode ')'" +
				"\nMCode         ::= '\"\"\"' Meta model api + Python3 code (subset) '\"\"\"'" +
				"\nMCall         ::= CALL Id '(' param* ')'" +
				"\nLoadLib       ::= LOAD STRING;" +
				"\nExec          ::= EXEC MCode" +
				"\n<b class='coms'>// FOTL checking extension</b>" +
				"\nLtlCheck     ::= CHECK Id '(' param* ')' '(' check ')'" +
				"\ncheck        ::= FOTL_formula + clause(Id) [.ue | .ae | .re]" +
				"\nCheckApply   ::= APPLY Id '(' param* ')'" +
			"</pre></div>" ;

				toastr.info(p, "", {
					"closeButton": true,
					"preventDuplicates": true,
					"tapToDismiss": true,
					"showDuration": "3000",
					"hideDuration": "1000",
					"timeOut": 0,
					"extendedTimeOut": 0,
					"positionClass": "toast-top-right"
				});
                $("#toast-container>.toast-info").attr("style","background-image: none !IMPORTANT;")
                visualEditor.ui.updateToastSize("info", {"width": 950}, true);
			};
			this.button.click(fx);
		    if(disableShortcut != null) return;
			shortcut.add("Ctrl+M", fx);
	}
});

/**
 * Insert text in current ace editor
 * @param s
 */
function insertSnippet(s) {
	if(visualEditor.ui.activeTab != null) {
		var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
		editor.insert(s, editor.selection.getCursor());
	}
}


//////////////////////////////////////////////////////////
//
//  templatesTool
//
//////////////////////////////////////////////////////////

visualEditor.ui.Template = {
	/**
	 * Template scheme
	 **/
    "name": "Name",
    "desc": "",
    "vars": [
      {"name": "Field1", "id": "Filed1", "type": "input", "pre": "Text before", "post": "Text after"},
      {"name": "Field2", "id": "Filed2", "type": "select", "pre": "Text before", "post": "Text after"},
      {"name": "Field3", "id": "Filed3", "type": "button", "pre": "Text before", "post": "Text after", "onclick": "js"}
    ],
    "aal": "",
    "html": "Template test {vars}",
    "xacml": "",

    // Helpers
    generateBtn: "<div style='text-align: center;'><button onclick='visualEditor.activeEditor.insert(visualEditor.ui.Template.genAAL" +
    "(visualEditor.ui.Template.current))' style='height: 25px;' class='fa fa-magic'>Generate</button></div>",
    current: null,

    /**
     * Returns the generated html for the given var
     * @param varObj
	 * @param counter
     */
    renderVar: function(varObj, counter) {
        // Generating options for select
        if(varObj.type === "select"){
            var options = "";
            var src = varObj.src;
            var agents = false;
            var data = false;

            if(src.indexOf("{aal.agents}") > -1)
                agents = true;

            if(src.indexOf("{aal.data}") > -1)
                data = true;

            // Replacing agents/services/clauses #NOTE : do not try to optimize
            src = src.replace("{aal.agents}",  JSON.stringify(visualEditor.ui.currentAAL.agents));
            src = src.replace("{aal.services}",  JSON.stringify(visualEditor.ui.currentAAL.services));
            src = src.replace("{aal.clauses}",  JSON.stringify(visualEditor.ui.currentAAL.clauses));
            src = src.replace("{aal.data}",  JSON.stringify(visualEditor.ui.currentAAL.data));
            src = src.replace("{aal.types}",  JSON.stringify(visualEditor.ui.currentAAL.types));
			src = src.replace("{aal.actorTypes}",  JSON.stringify(visualEditor.ui.currentAAL.actorTypes));
			src = src.replace("{aal.dataTypes}",  JSON.stringify(visualEditor.ui.currentAAL.dataTypes));
            src = JSON.parse(src);

            for(var i=0; i<src.length; i++)
                options += "<option value='" + src[i] + "'>" + src[i] + "</option>";

            // Add empty option
            options += "<option value=''></option>";

            // Adding quantifiers
            if(agents || data){
                var foralls = "";
                var exists = "";

                var tt = [];
                if(agents) tt = tt.concat(visualEditor.ui.currentAAL.actorTypes);
                if(data) tt = tt.concat(visualEditor.ui.currentAAL.dataTypes);

                for(var i=0; i<tt.length; i++) {
                    counter++;
                    foralls += "<option value='" + ((data)?'d':'x') + counter + "'>FORALL " + tt[i] + "</option>";
                    counter++;
                    exists += "<option value='" + ((data)?'d':'x') + counter + "'>EXISTS " + tt[i] + "</option>";
                }
                options += foralls + exists;
            }
        }

        return {
            view: "<div class='templateVar'>" + //<div class='templateVarName'>" + varObj.name + "</div>" +
                varObj.pre +
                ((varObj.type != "select")?
                    ("<input type='" + varObj.type + "' id='" + varObj.id + "' name='" + varObj.name + "'" +
                    ((varObj.onclick != undefined)? " onclick=\"" + varObj.onclick + "\" ":"") +
                    ((varObj.type === "button")? " value='" + varObj.name + "' ":"") +
                    ((varObj.checked != undefined)?" checked />":"/>")):
                ("<select id='" + varObj.id + "'>" + options +" </select>"))+
                varObj.post + "</div>",
            counter: counter};
    },

    /**
     * Render the template (using the html field
     * @param template
     * @param target
     */
	render: function(template, target) {
        // Set current template
        this.current = template;

        // handling vars
        var vars = {};
        var counter = 0;
        var res;
        for(var i=0; i<template.vars.length; i++){
            res = this.renderVar(template.vars[i], counter);
            vars[template.vars[i].id] = res.view;
            counter = res.counter;
        }

        //
        // Generating html
        //
        var tmp = "";
        Object.keys(vars).forEach(function(e){ tmp += "<div class='varGroupe'>" + vars[e] + "</div>";});

        var html =
            "<div class='templateName'>" + template.name + "</div>" +
            "<div class='templateDesc'>" + template.desc +"</div>" +
            ((typeof(template.html) == "string")?template.html:template.html.join(""));

        // Handle vars
        html = replaceAll("{vars}", tmp, html);
        // Handle genBtn
        html = replaceAll("{genBtn}", "<div class='varGroupe'>" + visualEditor.ui.Template.generateBtn + "</div>", html);
        // Handle vars one by one
        for(var i=0; i<template.vars.length; i++)
            html = replaceAll("{"+template.vars[i].id+"}", vars[template.vars[i].id], html);

        // Rendering
        $("#" + target).html(html);
	},

    /**
     * Generate AAL
     * @param template
     */
    genAAL: function(template) {
        var aal = (typeof(template.aal) == "string")?template.aal:template.aal.join(" ");
        for(var i=0; i<template.vars.length; i++) {
            aal = replaceAll("{"+template.vars[i].id+"}.ctext", eval("$('#"+template.vars[i].id+" option:selected').text()" ), aal);
            aal = replaceAll("{"+template.vars[i].id+"}.cval", eval("$('#"+template.vars[i].id+" option:selected').val()" ), aal);
            aal = replaceAll("{"+template.vars[i].id+"}.val", eval("$('#"+template.vars[i].id+"').val()" ), aal);
            aal = replaceAll("{"+template.vars[i].id+"}.checked", ("$('#"+template.vars[i].id+"').is(':checked')" ), aal);
        }

        // Handle evals
        var evals = aal.match(/{{(.*?)}}/g);

        if (evals != null) {
            for(var i=0; i<evals.length; i++) {
                var e = replaceAll("}}", "", replaceAll("{{", "", evals[i]));
                aal = aal.replace(evals[i], eval(e));
            }
        }
        return aal;
    }
}

/**
 * Get absolute path
 */
function getAbsPath(node) {
    var parent = $("#tt").tree('getParent', node.target);
    if(parent != undefined || parent != null)
        return (getAbsPath(parent) + "/" + node.text);
    else
        return node.text;
}

visualEditor.ui.tools.templatesTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.templatesTool",

	view: function(parent) {
		this.button = $('<div title="AAL policy wizard (ctrl+e)" id="tmpBtn" class="btn-action fa fa-magic fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {
		var fx = function(e){
            // Get AAL info
            visualEditor.ui.analyseAAL(visualEditor.ui.activeTab.panel.title, function(e) {

				var p = "<div id='aalwizard'>" +
					"<div style='width:17%; float: left;'>" +
					"	<b>Wizards</b>" +
					"<ul id='tt' class='easyui-tree unselectable'>" +
					"</div>" +
					"<div id='templateContent' style=''> </div>" +
					"</div>";
                /*
				toastr.info(p, "", {
					"closeButton": true,
					"preventDuplicates": true,
					"tapToDismiss": false,
					"showDuration": "3000",
					"hideDuration": "1000",
					"timeOut": 0,
					"extendedTimeOut": 0,
					"positionClass": "toast-top-right"
				});
				visualEditor.ui.updateToastSize("info", {"width": 800}, false, "none");

                // Minimazing on dbl click
                $(".toast-info").dblclick(function() {
                    if($(this).height() >= 20)
                        $(this).animate({width: "250px", height: "30px"});
                    else
                        $(this).animate({width: "800px", height: "453"});
                });
                */
                $("body").append(p);
                visualEditor.wm.createWindow.fromQuery("#aalwizard", {
                    title: "AAL wizard",
					x: 60,
					y: 50,
					width: 800,
					height: 490,
					widget: true,
					titlebar: true,
                    resizable: false,
					events: {
						closed: function() {
							this.destroy();
						}
					}
				}).open();

				$("#tt").tree({
					animate: true,
					checkbox: false,
					url: visualEditor.backend + "?action=listTemplates",

					onDblClick: function (node) {
						if (node.children == undefined)
							loadTemplate(getAbsPath(node) + ".json");
					},

					onClick: function (node) {
						if (node.children == undefined)
							loadTemplate(getAbsPath(node) + ".json");
					},

					formatter: function (node) {
						var s = node.text;
						if (node.children) {
							s += ' <span style=\'color:gray\'>(' + node.children.length + ')</span>';
						}
						return s;
					},

					onLoadSuccess: function (node, data) {
						$("#tt").tree("collapseAll");
					}
				});
			});
		};
		this.button.click(fx);
		if(disableShortcut != null) return;
		shortcut.add("Ctrl+e", fx);
	}
});

/**
 * Load a template from the backend
 * @param template
 */
function loadTemplate(template) {
	$.ajax({
		dataType: 'text',
		type:'POST',
		url: visualEditor.backend,
		data: {action: "getTemplate", file: template},
		success: function(response){
            var obj = jQuery.parseJSON(response);
            visualEditor.ui.Template.render(obj, "templateContent");
		}
	});
}

//////////////////////////////////////////////////////////
//
//  AceThemeTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.acethemeTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.acethemeTool",

	view: function(parent) {
		this.button = $('<div title="Editor Theme (ctrl+G)" id="aceThemeBtn" class="btn-action fa fa-file-image-o  fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		var fx = function(e){
            var options = "";
            for(var i=0; i<visualEditor.aceThemesList.length; i++)
                options += "<option value='" + visualEditor.aceThemesList[i] + "' " +
                    ((visualEditor.aceTheme == visualEditor.aceThemesList[i])?'selected':'')  + ">" +
                    visualEditor.aceThemesList[i] + "</option>";
			var p = "<select id='themes' onchange='visualEditor.updateAceTheme(this);'>" + options + "</select>";

            toastr.info(p, "Themes List", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": false,
  				"showDuration": "1000",
			  	"hideDuration": "1000",
			  	"timeOut": 0,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-center"
			});
		};
		this.button.click(fx);
		//shortcut.add("Ctrl+G", fx);
	}
});


//////////////////////////////////////////////////////////
//
//  clearOutputTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.clearOutputTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.clearOutputTool",

	view: function(parent) {
		this.button = $('<div title="Clear output" id="clearOutputBtn" class="btn-action fa fa-square-o  fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {
		var fx = function(e){
            $("#output_window").empty();
		};
		this.button.click(fx);
		if(disableShortcut != null) return;
		//shortcut.add("Ctrl+G", fx);
	}
});

//////////////////////////////////////////////////////////
//
//  simulationTool
//
//////////////////////////////////////////////////////////
visualEditor.ui.tools.simulationTool = visualEditor.ui.tool.extend({
	NAME : "visualEditor.ui.tools.simulationTool",

	view: function(parent) {
		this.button = $('<div title="Start simulation" id="simulationBtn" class="btn-action fa fa-cubes fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent, disableShortcut) {
		var fx = function(e){
            if(visualEditor.ui.simul.simulation == null) {
                visualEditor.ui.simul.startSimulation(9999);
                toastr.success('Simulation started !');
                $("#simulationBtn").attr("title", "Stop simulation").css("color", "green").addClass("fa-spin");
            } else {
                visualEditor.ui.simul.stopSimulation();
                toastr.error('Simulation stopped !');
                $("#simulationBtn").attr("title", "Start simulation").css("color", "").removeClass("fa-spin");
            }
		};
		this.button.click(fx);
		if(disableShortcut != null) return;
		//shortcut.add("Ctrl+G", fx);
	}
});
