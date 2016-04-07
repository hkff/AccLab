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
    oldTreeState    : [],
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
          '<div id="fmm-new-vfodtl" data-options="iconCls:\'fa fa-calendar-o\'" class="menu-item cmenuBtn" >New VFODTL file</div>'+
		  '<div id="fmm-open"  data-options="iconCls:\'fa fa-folder-open\'" class="menu-item cmenuBtn">Open</div>'+
		  '<div id="fmm-rename" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >Rename</div>'+
		  //'<div class="menu-sep"></div>'+
		  '<div id="fmm-delete" data-options="iconCls:\'fa fa-times\'" class="menu-item cmenuBtn">Delete</div>'+
		  '<div id="fmm-refresh" data-options="iconCls:\'fa fa-refresh\'" class="menu-item cmenuBtn">Refresh</div>'+
		  '<div id="fmm-compile" data-options="iconCls:\'fa fa-cog\'" class="menu-item cmenuBtn">Compile</div>'+
          '<div id="fmm-run" data-options="iconCls:\'fa fa-flash\'" class="menu-item cmenuBtn">Run</div>'+ '</div>';
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
				var path = _this.getAbsPath(node, $("#explorer"));
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
                var ex = $("#explorer");
                ex.tree("collapseAll");
                for(var i=0; i<visualEditor.ui.fileManager.oldTreeState.length; i++) {
                    var e = ex.tree('find', visualEditor.ui.fileManager.oldTreeState[i]);
                    if(e != null && e!= undefined) {
                        ex.tree("expand", e.target);
                    }
                }
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

			var path = _this.getAbsPath(node, $("#explorer"));
			file = path.replace(node.text, "") + file;

			_this.createFolder(file);
		});

        $('#fmm-new-vfodtl').click({"type": ".vfodtl"}, visualEditor.ui.fileManager.createFileMenu);

		$('#fmm-new-diagram').click({"type": ".acd"}, visualEditor.ui.fileManager.createFileMenu);

		$('#fmm-new-aal').click({"type": ".aal"}, visualEditor.ui.fileManager.createFileMenu);

		$('#fmm-rename').click(function(e){
			var node = $("#explorer").tree('getSelected');
            var path = _this.getAbsPath(node, $("#explorer"));
			var file;
			do {
				file=prompt("Enter file name", path);
			}
			while(file.length <= 0);

			$.ajax({
				dataType: 'text',
				type:'POST',
				url: visualEditor.backend,
				data: {action: "rename", file: path, new_name: file},
				success: function(response){
					visualEditor.ui.fileManager.reloadWithState();
				}
			});
		});

		$('#fmm-open').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var path = _this.getAbsPath(node, $("#explorer"));
			_this.openFile(path);
		});		

		$('#fmm-delete').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var path = _this.getAbsPath(node, $("#explorer"));
			_this.deleteFile(path);
		});

		$('#fmm-refresh').click(function(e){
			// Update explorer
			$("#explorer").tree("reload");
		});

		$('#fmm-compile').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file = _this.getAbsPath(node, $("#explorer"));
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

        $('#fmm-run').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var file = _this.getAbsPath(node, $("#explorer"));
            var dType = "text";
			var action = "runDjango";
			var fileType = file.split('.').pop().toLowerCase();
            if(node.text == "manage.py") {
                $.ajax({
                    dataType: dType,
                    type:'POST',
                    url: visualEditor.backend,
                    data: {action: action, file: file},
                    success: function(response){
						//visualEditor.log(response);
                        $("#output_window").empty().append(response);
                        toastr.info('Running...');
                    }
                });
            } else {
                toastr.error('Not a runnable file !');
            }
		});
	},

    /**
     * Create a file from menu btn
     * @param e
     */
    createFileMenu: function(e){
        var node = $("#explorer").tree('getSelected');
        var file;
        do {
            file=prompt("Enter file name");
        }
        while(file.length <= 0);
        file = file + e.data.type;
        var path = visualEditor.ui.fileManager.getAbsPath(node, $("#explorer"));
        if(visualEditor.ui.fileManager.isDir(path))
            file = path + "/" + file;
        else
            file = path.replace(node.text, "") + file;

        visualEditor.ui.fileManager.createFile(file, true);
    },

	/**
	 * Get absolute path
	 */
	getAbsPath: function(node, root) {
		var parent = root.tree('getParent', node.target);
		if(parent != undefined || parent != null)
			return (visualEditor.ui.fileManager.getAbsPath(parent, root) + "/" + node.text);
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
		if(fileType === "acd" || fileType === "vfodtl" )
			dType = "json";
        var i = this.isOpened(file);
		if(i != -1) {
            window.documentNode.container.setActiveChild(documentNode.children[i].container);
			return;
		}

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

                // Add file in recent files
                visualEditor.ui.fileManager.addToRecentFiles(file);

				switch(fileType) {
					case "acd":
						// Load ACD diagram
						editor4.canvas = new visualEditor.ui.gridEditor(id, "toolbox_window", "componentbox_window", "properties_window", "acd");
						visualEditor.ui.canvas = editor4.canvas;
						var reader = new draw2d.io.json.Reader();
						visualEditor.ui.canvas.clear();
			 			reader.unmarshal(visualEditor.ui.canvas, response);
						visualEditor.ui.outline.canvasToTree();

                        // Switch to acd mode
                        visualEditor.acdMode();
			 			break;

					case "vfodtl":
						// Load Fodtl diagram
						editor4.canvas = new visualEditor.ui.gridEditor(id, "toolbox_window", "componentbox_window", "properties_window", "vfodtl");
						visualEditor.ui.canvas = editor4.canvas;
						var reader = new draw2d.io.json.Reader();
						visualEditor.ui.canvas.clear();
			 			reader.unmarshal(visualEditor.ui.canvas, response);

                        // Switch to acd mode
                        visualEditor.vfodtlMode();
			 			break;

					default:
					    // Set the source
					    var inPlaceAALEditor = visualEditor.ui.fileManager.openAceEditor(id, fileType.toUpperCase());
					    inPlaceAALEditor.setValue(response);
					    inPlaceAALEditor.clearSelection();
                        inPlaceAALEditor.first = true;
                        inPlaceAALEditor.session.getUndoManager().markClean();
                        inPlaceAALEditor.on("input", function() {
                            if(inPlaceAALEditor.first) {
                                inPlaceAALEditor.first = false;
                                inPlaceAALEditor.session.getUndoManager().markClean();
                                inPlaceAALEditor.on("input", function () {
                                    visualEditor.markPanelEdited();
                                });
                            }
                        });

                        visualEditor.activeEditor = inPlaceAALEditor;
                        visualEditor.ui.openedEditors[visualEditor.ui.activeTab.panel.title] = inPlaceAALEditor;

                        // Add context menu handler
                        $(inPlaceAALEditor.container).bind("contextmenu", function(e) {
                            visualEditor.ui.toggleAceWheelContextMenu(e);
                            return false;
                        });

						// Switch to aal mode
						if(fileType === "aal")
                        	visualEditor.aalMode();

						break;
				}
			}
		});
	},

	/**
	 * Reload the current opened file
	 */
	reloadFile: function() {
        var file = visualEditor.ui.activeTab.container.title;
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "text";
		if(fileType === "acd" || fileType === "vfodtl" )
			dType = "json";
		// Ajax request
        $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend,
			data: {action: "read", file: file},
			success: function(response){
                // Add file in recent files
                visualEditor.ui.fileManager.addToRecentFiles(file);

				switch(fileType) {
					case "acd":case "vfodtl":
						// Load ACD diagram
						var reader = new draw2d.io.json.Reader();
						visualEditor.ui.canvas.clear();
			 			reader.unmarshal(visualEditor.ui.canvas, response);
						visualEditor.ui.outline.canvasToTree();

                        // Switch to acd mode
                        visualEditor.acdMode();
			 			break;
                    case "aal":
					    // Set the source
					    visualEditor.activeEditor.setValue(response);
                        visualEditor.activeEditor.selection.clearSelection();
                        visualEditor.activeEditor.session.getUndoManager().markClean();

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
	 * Check file is a dir
	 * @param file
	 */
	isDir: function(file) {
		return file.split('.').length <= 1;
	},

    /**
     * Get file extension
     * @param file
     * @returns {string}
     */
    getFileType: function (file) {
        return file.split('.').pop().toLowerCase();
    },

    /**
     * Reload file tree and restore state
     */
    reloadWithState: function() {
        var ex = $("#explorer");
        visualEditor.ui.fileManager.oldTreeState = [];
        var oldState = ex.tree('getChildren', ex.tree('getRoot'));

        for(var i=0; i<oldState.length; i++) {
            if(oldState[i].state === "open" && this.isDir(oldState[i].id))
                visualEditor.ui.fileManager.oldTreeState.push(oldState[i].id);
        }
        ex.tree("reload");
    },

	/**
	 * Create a file
	 * @param file
     * @param open
	 */
	createFile: function(file, open) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "text";
		var data = " ";
		if(fileType === "acd" || fileType === "vfodtl"){
			dType = "json";
			data = "[]";
		}
        $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend,
			data: {action: "write", file: file, data: data},
			success: function(response){
                if(open == true)
                    visualEditor.ui.fileManager.openFile(file);
            }
		});

		// Update explorer
		visualEditor.ui.fileManager.reloadWithState();
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
			success: function(response){}
		});

		// Update explorer
		visualEditor.ui.fileManager.reloadWithState();
	},

    /**
     * Create file of a given type
     * @param fileType
     */
    createFileType: function(fileType) {
        var file;
        do {
            file=prompt("Enter file name");
        }
        while(file.length <= 0);
        file = file + "." + fileType;
        this.createFile(file, true);
    },

    /**
     * Add a file to recent opened files
     * @param file
     */
    addToRecentFiles: function(file) {
        var exists = visualEditor.userPrefs["recentFiles"].indexOf(file);
        if (exists > -1)
            visualEditor.userPrefs["recentFiles"].splice(exists, 1);

        visualEditor.userPrefs["recentFiles"].unshift(file);
        if(visualEditor.userPrefs["recentFiles"].length > 15)
            visualEditor.userPrefs["recentFiles"].pop();
        visualEditor.savePrefs();
    },

	/**
	 * Show generated aal file
	 * @param file
	 * @param target
	 */
	showGeneratedAAL: function(file, target) {
		var aal = visualEditor.ui.generateAAL(file);
		this.saveFile(target, aal);
        this.openFile(target);
		toastr.success('AAL file generated !');

		// Update explorer
		visualEditor.ui.fileManager.reloadWithState();
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


        // create statusBar with command shell
        $(editor.container).append('<div id="statusBar">Command : <input id="cmd"></div>');
        var StatusBar = ace.require("ace/ext/statusbar").StatusBar;
        var jstatusbar = $("#statusBar");
        var statusBar = new StatusBar(editor, jstatusbar[0]);
		jstatusbar.on("mouseover", function(e) { $(e.target).css("opacity", 1.0) })
			.on("mouseout", function(e) { $(e.target).css("opacity", 0.2) });

        // Eval command on ENTER key
        $("#cmd").keypress(function(e) {
            if(e.which == 13) {
				visualEditor.ui.consoleLog.push($(this).val());
                visualEditor.ui.evalCmd($(this).val());
                $(this).val("");
                $(this).typeAhead({source: visualEditor.ui.consoleLog.concat(visualEditor.ui.consolePredefs)});
            }
        }).typeAhead({source: visualEditor.ui.consoleLog.concat(visualEditor.ui.consolePredefs)});

		$("#cmd").on("focus mouseover keydown", function(e) { $("#statusBar").css("opacity", 1.0) })
			.on("mouseout focusout", function(e) { $("#statusBar").css("opacity", 0.2) });

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
			success: function(response){}
		});

		// Update explorer
		visualEditor.ui.fileManager.reloadWithState();
	},

	/**
	 * Save file
	 * @param file
	 * @param data
     * @param callback
	 */
	saveFile: function(file, data, callback) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "";
		switch(fileType) {
            case "acd": case "vfodtl":
				dType = "json";
				var writer = new draw2d.io.json.Writer();
					writer.marshal(visualEditor.ui.canvas, function(json){
						$.ajax({
							dataType: dType,
							type:'POST',
							url: visualEditor.backend,
							data: {action: "write", file: file, data: data},
							success: function(response){
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
                        if(callback != undefined)
                            callback();
                        else
						    toastr.success('File saved !');
					}
				});
				break;
		}
	},

    /**
     * Sysmon template specific
     * @param textToWrite
     * @param fileNameToSaveAs
     */
    saveTextAsFile: function (textToWrite, fileNameToSaveAs) {
        var textFileAsBlob = new Blob([textToWrite], {type:'text/plain'});
        var downloadLink = document.createElement("a");
        downloadLink.download = fileNameToSaveAs;
        downloadLink.innerHTML = "Download File";
        if (window.webkitURL != null) {
            // Chrome allows the link to be clicked
            // without actually adding it to the DOM.
            downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
        }
        else {
            // Firefox requires the link to be added to the DOM
            // before it can be clicked.
            downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
            downloadLink.onclick = function (event) { document.body.removeChild(event.target); };
            downloadLink.style.display = "none";
            document.body.appendChild(downloadLink);
        }

        downloadLink.click();
    },

    /**
     * Sysmon template specific
     * @param fileToLoadId
     * @param inputToLoadId
     */
    loadFileAsList: function (fileToLoadId, inputToLoadId) {
        var fileToLoad = document.getElementById(fileToLoadId).files[0];

        var fileReader = new FileReader();
        fileReader.onload = function(fileLoadedEvent) {
            var textFromFileLoaded = fileLoadedEvent.target.result;
            var entries = textFromFileLoaded.split(";");
            var list = $('#'+inputToLoadId);
            entries.forEach(function(e, i, a){
                if (e != '')
                    list.append($('<option></option>').val(2).html(e+';'));
            });
            document.getElementById(inputToLoadId).value = textFromFileLoaded;
        };
        fileReader.readAsText(fileToLoad, "UTF-8");
    },

    /**
     * Generate django app template
     * @param aal_file
     * @param spec_file
     * @param output_file
     */
	django: function(aal_file, spec_file, output_folder) {
        $.ajax({
			dataType: "text",
			type:'POST',
			url: visualEditor.backend,
			data: {action: "django", aal_file: aal_file, spec_file: spec_file, output_folder: output_folder},
			success: function(response){
				// Update explorer
				visualEditor.ui.fileManager.reloadWithState();
				visualEditor.log(response)
            }
		});
	},

    filterTree: function(filterType) {
        var roots = $("#explorer").tree("getRoots");
        roots.forEach(function(e, i) {
            if(e.text.endsWith(".aal")) {
                console.log(e.text)
            }
            //var children = $("#explorer").tree("getChildren", e);

        });
    }
};
