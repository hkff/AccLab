//////////////////////////////////////////////////////////
//
//  AccLab UI : fileManager.js
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
    supportedTypes  : ["AAL", "TSPASS", "PY", "JSON", "XML", "HTML", "JS"],
    typesMode       : {"AAL":"AAL", "TSPASS": "TSPASS", "PY": "python",
                        "JSON": "json", "XML": "xml", "HTML": "html", "JS": "javascript"},

	/**
	 * init function
	 * @param grid
	 * @param actionsPanel
	 * @param componentsPanel
	 * @param propertiesPanel
	 */
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel) {

        // Get view elements
        this.grid = $('#' + grid);
        this.actionsPanel = $('#' + actionsPanel);
        this.componentsPanel = $('#' + componentsPanel);
        this.propertiesPanel = $('#' + propertiesPanel);
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
          '<div id="fmm-new-folder" data-options="iconCls:\'fa fa-folder\'" class="menu-item cmenuBtn" >New Folder</div>'+
		  '<div id="fmm-new-diagram" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >New Diagram</div>'+
		  '<div id="fmm-new-aal" data-options="iconCls:\'fa fa-file-code-o\'" class="menu-item cmenuBtn" >New AAL file</div>'+
		  '<div id="fmm-open"  data-options="iconCls:\'fa fa-folder-open\'" class="menu-item cmenuBtn">Open</div>'+
		  '<div id="fmm-rename" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >Rename</div>'+
		  //'<div class="menu-sep"></div>'+
		  '<div id="fmm-delete" data-options="iconCls:\'fa fa-times\'" class="menu-item cmenuBtn">Delete</div>'+
		  '<div id="fmm-refresh" data-options="iconCls:\'fa fa-refresh\'" class="menu-item cmenuBtn">Refresh</div>'+
		  '<div id="fmm-compile" data-options="iconCls:\'fa fa-cog\'" class="menu-item cmenuBtn">Compile</div>'+ '</div>';
		$('body').append(this.ctMenu);

		$("#explorer").tree({
			animate: true,
			checkbox:false,
			url: visualEditor.backend + "?action=list",

			onContextMenu: function(e, node){
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
        $('#fmm-new-folder').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file;
			do {
				file=prompt("Enter folder name");
			}
			while(file.length < 0);

			var path = _this.getAbsPath(node);
			file = path.replace(node.text, "") + file;

			_this.createFolder(file);
		});

		$('#fmm-new-diagram').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file;
			do {
				file=prompt("Enter file name");
			}
			while(file.length < 0);
			file = file + ".acd";
			var path = _this.getAbsPath(node);
			file = path.replace(node.text, "") + file;

			_this.createFile(file);
			_this.openFile(file);
		});

		$('#fmm-new-aal').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file;
			do {
				file=prompt("Enter file name");
			}
			while(file.length < 0);
			file = file + ".aal";
			var path = _this.getAbsPath(node);
			file = path.replace(node.text, "") + file;

			_this.createFile(file);
			_this.openFile(file);
		});

		$('#fmm-rename').click(function(e){
			var node = $("#explorer").tree('getSelected');
            var path = _this.getAbsPath(node);
			var file;
			do {
				file=prompt("Enter file name", path);
			}
			while(file.length < 0);

			$.ajax({
				dataType: 'text',
				type:'POST',
				url: visualEditor.backend,
				data: {action: "rename", file: path, new_name: file},
				success: function(response){
					$("#explorer").tree("reload");
				}
			});
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

		$('#fmm-compile').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file = _this.getAbsPath(node);
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

		if(this.isOpened(file) != -1)
			return;

		if(this.isDir(file))
			return;

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

				switch(fileType) {
					case "acd":
						// Load ACD diagram
						editor4.canvas = new visualEditor.ui.gridEditor(id, "toolbox_window", "componentbox_window", "properties_window");
						visualEditor.ui.canvas = editor4.canvas;
						var reader = new draw2d.io.json.Reader();
						visualEditor.ui.canvas.clear();
			 			reader.unmarshal(visualEditor.ui.canvas, response);
						visualEditor.ui.outline.canvasToTree();

                        // Switch to acd mode
                        visualEditor.acdMode();
			 			break;

					default:
					    // Set the source
					    var inPlaceAALEditor = visualEditor.ui.fileManager.openAceEditor(id, fileType.toUpperCase());
					    inPlaceAALEditor.setValue(response);
					    inPlaceAALEditor.clearSelection();

                        inPlaceAALEditor.on("input", function() {
							visualEditor.markPanelEdited();
                        });

                        visualEditor.activeEditor = inPlaceAALEditor;
                        visualEditor.ui.openedEditors[visualEditor.ui.activeTab.panel.title] = inPlaceAALEditor;

                        visualEditor.activeEditor.session.getUndoManager().markClean();
                        $(".tab-handle-text")[0].innerHTML += " *";

                        // Add context menu handler
                        $(inPlaceAALEditor.container).bind("contextmenu", visualEditor.ui.toggleAceWheelContextMenu);

						// Switch to aal mode
                        visualEditor.aalMode();
						break;
				}
			}
		});
	},

	/**
	 * Check is a file is opened
	 * @param file
	 */
	isOpened: function(file) {
		var lng = documentNode.children.length;
		for(var i=0; i<lng; i++) {
			if(file == documentNode.children[i].container.title)
				return i;
		}
		return -1;
	},

	/**
	 * Check it is a dir
	 * @param file
	 */
	isDir: function(file) {
		return file.split('.').length <= 1;
	},

	/**
	 * Create file
	 * @param file
	 */
	createFile: function(file) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "text";
		var data = " ";
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
	 * Create folder
	 * @param file
	 */
	createFolder: function(file) {
		var dType = "text";
        $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend,
			data: {action: "createDir", file: file},
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
		var aal = visualEditor.ui.generateAAL(file);
		var f = file.replace(".acd", ".aal");
        this.saveFile(f, aal);
        this.openFile(f);
		toastr.success('AAL file generated !');

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
		var config = ace.require("ace/config");
        var editor = ace.edit(id);

        // Setting options
		editor.setOptions({
        	enableBasicAutocompletion: true,
        	enableSnippets: true,
        	enableLiveAutocompletion: true,
            fontSize: visualEditor.getFontSize(),
            theme: "ace/theme/" + visualEditor.aceTheme
    	});

        // Set Mode
		if(this.supportedTypes.indexOf(type) != -1)
			editor.getSession().setMode("ace/mode/" + this.typesMode[type]);
		else
            editor.getSession().setMode("ace/mode/plain_text");


        // create a simple selection status indicator
        $(editor.container).append('<div id="statusBar">Command : <input id="cmd"></div>');
        var StatusBar = ace.require("ace/ext/statusbar").StatusBar;
        var jstatusbar = $("#statusBar");
        var statusBar = new StatusBar(editor, jstatusbar[0]);
        jstatusbar.mouseover(function(e){
            //jstatusbar.animate({"background-color": "rgba(247, 247, 247, 1)"});
            //jstatusbar.animate({"color": "rgba(128, 128, 128, 1)"});
            //$("#cmd").animate({"opacity": "1.0"});
        });

        $("#cmd").keypress(function(e) {
            if(e.which == 13) {
                visualEditor.ui.evalCmd($(this).val());
                $(this).val("");
            }
        });

        // Worker communication
        editor.postMsgWorker = function(cmd, args) {
            editor.session.$worker.$worker.postMessage({"command" : cmd, "args": args});
        };
        editor.session.setOption("useWorker", true);

        // Add custom shortcuts
        editor.commands.addCommand({name: "togglecomment", bindKey: {win: "Alt-c", mac: "Command-Option-c"},
                exec: function(e) {e.toggleCommentLines()}, multiSelectAction: "forEachLine", scrollIntoView: "selectionPart"});
        editor.commands.addCommand({name: "toggleBlockComment", bindKey: {win: "Alt-Shift-c", mac: "Command-Option-Shift-c"},
                exec: function(e) { e.toggleBlockComment()}, multiSelectAction: "forEach", scrollIntoView: "selectionPart" });


	    return editor;
	},

	/**
	 * Delete file
	 * @param file
	 */
	deleteFile: function(file) {
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
	saveFile: function(file, data, callback) {
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
						  		//console.log(response)
								if(callback != undefined)
									callback();
								else
									toastr.success('File saved !');
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
				  		//console.log(response)
                        if(callback != undefined)
                            callback();
                        else
						toastr.success('File saved !');
					}
				});
				break;
		}
	}
};
