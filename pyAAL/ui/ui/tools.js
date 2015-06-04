//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : tools.js
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

		$('#clear-graph').toolbar({
			content: '#user-toolbar-options', 
			position: 'top',
			hideOnClick: true
		});

		this.toolsRegistrator();
		this.view(this);
		this.control(this);
	},


	/**
	 * @method
	 * Register tools
	 */
	toolsRegistrator: function() {
		this.tools.push(new visualEditor.ui.tools.selectTool());
		this.tools.push(new visualEditor.ui.tools.panneTool());
		this.tools.push(new visualEditor.ui.tools.mselectTool());
		this.tools.push(new visualEditor.ui.tools.copyTool());
		this.tools.push(new visualEditor.ui.tools.deleteTool());
		this.tools.push(new visualEditor.ui.tools.lockTool());
		this.tools.push(new visualEditor.ui.tools.zoomInTool());
		this.tools.push(new visualEditor.ui.tools.zoomOutTool());
		this.tools.push(new visualEditor.ui.tools.zoomOriginTool());
		this.tools.push(new visualEditor.ui.tools.undoTool());
		this.tools.push(new visualEditor.ui.tools.redoTool());
		this.tools.push(new visualEditor.ui.tools.saveTool());
		this.tools.push(new visualEditor.ui.tools.groupTool());
		this.tools.push(new visualEditor.ui.tools.ungroupTool());
		this.tools.push(new visualEditor.ui.tools.fullScreenTool());
		this.tools.push(new visualEditor.ui.tools.clearTool());
		this.tools.push(new visualEditor.ui.tools.separatorTool());
		this.tools.push(new visualEditor.ui.tools.genAALTool());
		this.tools.push(new visualEditor.ui.tools.genTSPASSTool());
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
			var p = visualEditor.ui.canvas.getCurrentSelection().clone();
			console.log(p)
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
				new draw2d.command.CommandDelete(visualEditor.ui.canvas.getCurrentSelection())
			);
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

	control: function(parent) {

		var fx = function(e) {
			var file = visualEditor.ui.activeTab.container.title;
			var fileType = file.split('.').pop().toLowerCase();
			switch (fileType) {
				case "aal":
					var editor = ace.edit(visualEditor.ui.activeTab.container.elementContent.id);
					visualEditor.ui.fileManager.saveFile(file, editor.getValue());
					break;

				case "acd":
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
					break;
			}
		}
		this.button.click(fx);
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
			var reader = new draw2d.io.json.Reader();
			visualEditor.ui.canvas.clear();
 			reader.unmarshal(visualEditor.ui.canvas , visualEditor.ui.savedCanvas );
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
		this.button = $('<div title="Generate AAL file (ctrl+G)" id="genAALBtn" class="btn-action fa fa-file-text-o fa-lg"/>');
		parent.actionsPanel.append(this.button);
	},

	control: function(parent) {
		var fx = function(e){
			var active = visualEditor.ui.activeTab.container.title;
			visualEditor.ui.fileManager.showGeneratedAAL(active);
		};
		this.button.click(fx);
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

	control: function(parent) {
		var fx = function(e){
			//var active = visualEditor.ui.activeTab.container.title;
			//visualEditor.ui.fileManager.showGeneratedTSPASS(active);
            var file = visualEditor.ui.activeTab.container.title;
            var dType = "text";
			var action = "compileAAL";
			var fileType = file.split('.').pop().toLowerCase();
			if(fileType == "tspass")
				action = "compileFOTL";

			$.ajax({
				dataType: dType,
				type:'POST',
				url: visualEditor.backend,
				data: {action: action, file: file},
				success: function(response){
					$("#output_window").empty().append(response);
					toastr.info('Compiling...');
				}
			});
		};

		this.button.click(fx);
		shortcut.add("Ctrl+Enter", fx);
	}
});
