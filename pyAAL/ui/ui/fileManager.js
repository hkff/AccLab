//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : fileManager.js
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

visualEditor.ui.fileManager = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	commandStack    : null,
	canvas          : null,
	selectedNode    : null,

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
		this.view(this);
		this.control(this);
	},

	/**
	 * View
	 * @param _this
	 */
	view: function(_this) {
		
		this.ctMenu =
		  '<div id="fmm" class="easyui-menu menu-top menu" style="width: 137px; display: none; left: 94px; top: 150px; z-index: 110009;">'+
		  '<div class="menu-line"></div>'+
		  '<div id="fmm-new-diagram" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >New Diagram</div>'+
		  '<div id="fmm-new-aal" data-options="iconCls:\'fa fa-file-code-o\'" class="menu-item cmenuBtn" >New AAL file</div>'+
		  '<div id="fmm-open"  data-options="iconCls:\'fa fa-folder-open\'" class="menu-item cmenuBtn">Open</div>'+
		  '<div id="fmm-rename" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >Rename</div>'+
		  //'<div class="menu-sep"></div>'+
		  '<div id="fmm-delete" data-options="iconCls:\'fa fa-times\'" class="menu-item cmenuBtn">Delete</div>'+ '</div>' +
		  '<div id="fmm-refresh" data-options="iconCls:\'fa fa-refresh\'" class="menu-item cmenuBtn">Refresh</div>'+ '</div>';
		$('body').append(this.ctMenu);

		$("#explorer").tree({
			animate: true,
			checkbox:false,
			url: visualEditor.backend + "?action=list",

			onContextMenu: function(e,node){
				e.preventDefault();
				$(this).tree('select', node.target);
				$('#fmm').menu('show',{
					left: e.pageX,
					top: e.pageY
				});
			},

			onDblClick: function(node){
				var path = _this.getAbsPath(node);
				_this.openFile(path);
			},

			formatter:function(node){
				var s = node.text;
				if(node.children){
					s += ' <span style=\'color:gray\'>(' + node.children.length + ')</span>';
				}
				return s;
			},

			onLoadSuccess: function(node, data){
				$("#explorer").tree("collapseAll");
			}
		});
	},

	/**
	 * Controller
	 * @param _this
	 */
	control: function(_this) {
		// Context menu actions
		$('#fmm-new-diagram').click(function(e){
			var node = $("#explorer").tree('getSelected');
			//var path = _this.getAbsPath(node);
			var file = "toto.acd";
			_this.createFile(file);
			_this.openFile(file);
		});

		$('#fmm-new-aal').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file = "newFile.aal";
			_this.createFile(file);
			_this.openFile(file);
		});

		$('#fmm-open').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var path = _this.getAbsPath(node);
			_this.openFile(path);
		});		

		$('#fmm-delete').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var path = _this.getAbsPath(node);
			_this.deleteFile(path);
		});

		$('#fmm-refresh').click(function(e){
			// Update explorer
			$("#explorer").tree("reload");
		});
	},

	/**
	 * Get absolute path
	 */
	getAbsPath: function(node) {
		var parent = $("#explorer").tree('getParent', node.target);
		if(parent != undefined || parent != null)
			return (visualEditor.ui.fileManager.getAbsPath(parent) + "/" + node.text);
		else
			return node.text;
	},

	/**
	 * Open file
	 * @param file
	 */
	openFile: function(file) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "text";
		if(fileType == "acd")
			dType = "json";

		// Ajax request
        $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend,
			data: {action: "read", file: file},
			success: function(response){
				// Create a new editor window
		  		var id = visualEditor.guid();
				var editor = $('<div id="'+id+'" caption="' + file + '" class="editor1-window editor-host"></div>');
				$(document.body).append(editor);
				var editor4 = new dockspawn.PanelContainer($("#"+id)[0], dockManager);
				var editor4Node  = dockManager.dockFill(documentNode, editor4);
		
				console.log(file + "  "+fileType)
				switch(fileType) {
					case "acd":
						// Load ACD diagram
						editor4.canvas = new visualEditor.ui.gridEditor(id, "toolbox_window", "componentbox_window", "properties_window");
						visualEditor.ui.canvas = editor4.canvas;
						var reader = new draw2d.io.json.Reader();
						visualEditor.ui.canvas.clear();
			 			reader.unmarshal(visualEditor.ui.canvas, response);
						visualEditor.ui.outline.canvasToTree();
			 			break;

					default:
					    // Set the source
					    var inPlaceAALEditor = visualEditor.ui.fileManager.openAceEditor(id, fileType.toUpperCase());
					    inPlaceAALEditor.setValue(response);
					    inPlaceAALEditor.clearSelection();
						break;
				}
			}
		});
	},

	/**
	 * Create file
	 * @param file
	 */
	createFile: function(file) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "text";
		var data = "";
		if(fileType == "acd"){
			dType = "json";
			data = "[]";
		}
        $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend,
			data: {action: "write", file: file, data: data},
			success: function(response){
				// Notify
				console.log(response)
			}
		});

		// Update explorer
		$("#explorer").tree("reload");
	},

	/**
	 * Show generated aal file
	 * @param file
	 */
	showGeneratedAAL: function(file) {
		var aal = visualEditor.ui.generateAAL();
		var f = file.replace(".acd", ".aal");
        this.saveFile(f, aal);
        this.openFile(f);

		// Update explorer
		$("#explorer").tree("reload");
	},

	/**
	 * Open ace editor
	 * @param id
	 * @param type
	 * @returns {*}
	 */
	openAceEditor: function(id, type) {
		var inPlaceAALEditor = ace.edit(id);
		// monokai
	    inPlaceAALEditor.setTheme("ace/theme/monokai");
		if(type == "AAL" || type == "TSPASS")
			inPlaceAALEditor.getSession().setMode("ace/mode/" + type);
		else
			inPlaceAALEditor.getSession().setMode("ace/mode/plain_text");
	    inPlaceAALEditor.setFontSize(14);
	    return inPlaceAALEditor;
	},

	/**
	 * Delete file
	 * @param file
	 */
	deleteFile: function(file) {
		console.log("deleting " + file)
        $.ajax({
			dataType: "text",
			type:'POST',
			url: visualEditor.backend,
			data: {action: "delete", file: file},
			success: function(response){
				// Notify
				console.log(response)
			}
		});
		// Update explorer
		$("#explorer").tree("reload");
	},

	/**
	 * Save file
	 * @param file
	 * @param data
	 */
	saveFile: function(file, data) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "";
		switch(fileType) {
			case "acd": 
				dType = "json";
				var writer = new draw2d.io.json.Writer();
					writer.marshal(visualEditor.ui.canvas, function(json){
						$.ajax({
							dataType: dType,
							type:'POST',
							url: visualEditor.backend,
							data: {action: "write", file: file, data: data},
							success: function(response){
						  		console.log(response)
							}
						});
					});
				break;
			default:
				dType = "text";
				$.ajax({
					dataType: dType,
					type:'POST',
					url: visualEditor.backend,
					data: {action: "write", file: file, data: data},
					success: function(response){
				  		console.log(response)
					}
				});
				break;
		}
	}
};
