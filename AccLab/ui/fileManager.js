visualEditor.ui.fileManager = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	commandStack    : null,
	canvas          : null,
	selectedNode    : null,

	/**
	 * @method
	 * init function
	 *
	 **/
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel) {
		
		// Get view elements
		this.grid            = $('#'+ grid);
		this.actionsPanel    = $('#'+ actionsPanel);
		this.componentsPanel = $('#'+ componentsPanel);
		this.propertiesPanel = $('#'+ propertiesPanel);
		this.view(this);
		this.control(this);
	},


	view: function(_this) {
		
		this.ctMenu = '<div id="fmm" class="easyui-menu menu-top menu" style="width: 137px; display: none; left: 94px; top: 150px; z-index: 110009;">'+
						'<div class="menu-line"></div>'+
						'<div id="fmm-new-diagram" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >New Diagram</div>'+
						'<div id="fmm-open"  data-options="iconCls:\'fa fa-folder-open\'" class="menu-item cmenuBtn">Open</div>'+
						'<div id="fmm-rename" data-options="iconCls:\'fa fa-edit\'" class="menu-item cmenuBtn" >Rename</div>'+
						//'<div class="menu-sep"></div>'+
						'<div id="fmm-delete" data-options="iconCls:\'fa fa-times\'" class="menu-item cmenuBtn">Delete</div>'+

					'</div>';
		$('body').append(this.ctMenu);

		$("#explorer").tree({
			animate: true,
			checkbox:false,
			url: visualEditor.backend + "files.php?action=list",

			onContextMenu: function(e,node){
				e.preventDefault();
				$(this).tree('select', node.target);
				_this.fmmShow(node);
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
				//console.log(node)
				var s = node.text;
				if(node.children){
					s += ' <span style=\'color:gray\'>(' + node.children.length + ')</span>';
				}
				return s;
			},
		});

	},



	/**
	 * Control
	 */
	control: function(_this) {
		$('#fmm-new-diagram').click(function(e){
			var node = $("#explorer").tree('getSelected');
			//var path = _this.getAbsPath(node);
			var file = "toto.acd";
			_this.createFile(file);
			_this.openFile(file);
		});
		

		$('#fmm-open').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var path = _this.getAbsPath(node);
			console.log(path)
			_this.openFile(path);
		});		

		$('#fmm-delete').click(function(e){
			var node = $("#explorer").tree('getSelected');
			var path = _this.getAbsPath(node);
			_this.deleteFile(path);
		});	

		//_this.getFilesList();
	},

	/**
	 * Get absolute path
	 */
	getAbsPath: function(node) {
		if(!str) var str = "";
		var parent = $("#explorer").tree('getParent', node.target);

		if(parent != undefined || parent != null){
			//var str2 = parent.text + "/" + node.text;
			return (visualEditor.ui.fileManager.getAbsPath(parent) + "/"+node.text );
		}else{
			return node.text;
		}
	},


	/**
	 * File explorer context menu
	 */
	fmmShow: function(node) {
		console.log(node.children)
		if(node.children){
		}else{
		}
	},

	/**
	 * Files API
	 */ 
	getFilesList: function() {
		

		return;
	},


	openFile: function(file) {

		var fileType = file.split('.').pop().toLowerCase();
		var dType = "";
		switch(fileType) {
			case "aal": dType = "text"; break;
			case "acd": dType = "json"; break;
		}

        var req = $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend + "files.php",//?action=read&file="+file,
			data: {action: "read", file: file},
			success: function(response){
				// Create a new editor window
		  		var id = visualEditor.guid();
				var editor = $('<div id="'+id+'" caption="'+file+'" class="editor1-window editor-host"></div>');
				$(document.body).append(editor);
				var editor4 = new dockspawn.PanelContainer($("#"+id)[0], dockManager);
				var editor4Node  = dockManager.dockFill(documentNode, editor4);
		
				console.log(file + "  "+fileType)
				switch(fileType) {
					case "aal":
					console.log("kkk")
					    // Set the AAL source
					    var inPlaceAALEditor = visualEditor.ui.fileManager.openAALEditor(id);
					    inPlaceAALEditor.setValue(response);
					    inPlaceAALEditor.clearSelection();
					break;

					case "acd":
					console.log("acccccccc")
						// Load ACD diagram
						editor4.canvas = new visualEditor.ui.gridEditor(id, "toolbox_window", "componentbox_window", "properties_window");
						visualEditor.ui.canvas = editor4.canvas;
						var reader = new draw2d.io.json.Reader();
						visualEditor.ui.canvas.clear();
			 			reader.unmarshal(visualEditor.ui.canvas, response);
			 		break;
				}
			}
		});
		console.log(req)
	},

	createFile: function(file) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "";
		var data = "";
		switch(fileType) {
			case "aal": 
				dType = "text"; 
				data = "";
				break;
			case "acd": 
				dType = "json"; 
				data = "[]";
				break;
		}

        var req = $.ajax({
			dataType: dType,
			type:'POST',
			url: visualEditor.backend + "files.php",//?action=write&file="+file+"&data="+data,
			data: {action: "write", file: file, data: data},
			success: function(response){
				// Notify
				console.log(response)
			}
		});
		console.log(req)
		$("#explorer").tree("reload");
	},

	showGeneratedAAL: function(file) {
		var aal = visualEditor.ui.generateAAL();
		/*
		// Create a new editor window
  		var id = visualEditor.guid();
		var editor = $('<div id="'+id+'" caption="'+file+"(Generated AAL)"+'" class="editor1-window editor-host"></div>');
		$(document.body).append(editor);
		var editor4 = new dockspawn.PanelContainer($("#"+id)[0], dockManager);
		var editor4Node  = dockManager.dockFill(documentNode, editor4);

	    // Set generated AAL
	    var inPlaceAALEditor = visualEditor.ui.fileManager.openAALEditor(id);
	    inPlaceAALEditor.setValue(aal);
	    inPlaceAALEditor.clearSelection();
	    inPlaceAALEditor.setReadOnly(true);
        */
        this.saveFile(file.replace("acd", "aal"), aal);
        this.openFile(file.replace("acd", "aal"));
	},

	openAALEditor: function(id) {
		var inPlaceAALEditor = ace.edit(id);
		// monokai
	    inPlaceAALEditor.setTheme("ace/theme/monokai");
	    inPlaceAALEditor.getSession().setMode("ace/mode/AAL");
	    inPlaceAALEditor.setFontSize(14);
	    return inPlaceAALEditor;
	},

	closeFile: function(file) {


	},


	deleteFile: function(file) {
		console.log(file)
        var req = $.ajax({
			dataType: "text",
			type:'POST',
			url: visualEditor.backend + "files.php",//?action=delete&file="+file,
			data: {action: "delete", file: file},
			success: function(response){
				// Notify
				console.log(response)
			}
		});
		console.log(req)
		$("#explorer").tree("reload");
	},


	saveFile: function(file, data) {
		var fileType = file.split('.').pop().toLowerCase();
		var dType = "";
        console.log(data)
		switch(fileType) {
			case "aal": 
				dType = "text";
				var req = $.ajax({
					dataType: dType,
					type:'POST',
					url: visualEditor.backend + "files.php?",//action=write&file="+file+"&data="+data,
					data: {action: "write", file: file, data: data},
					success: function(response){
				  		console.log(response)
					}
				}); 
			break;

			case "acd": 
				dType = "json";
				var writer = new draw2d.io.json.Writer();
					writer.marshal(visualEditor.ui.canvas, function(json){
						var req = $.ajax({
							dataType: dType,
							type:'POST',
							url: visualEditor.backend + "files.php",//?action=write&file="+file+"&data="+data,
							data: {action: "write", file: file, data: data},
							success: function(response){
						  		console.log(response)
							}
						});
					});
			break;
		}
	},


    //////////////////////////////////////////////////////////
    //
    //  Get selectedFile
    //
    //////////////////////////////////////////////////////////        
    compile: function() {
      
    },

	//////////////////////////////////////////////////////////
    //
    //  Get selectedFile
    //
    //////////////////////////////////////////////////////////
    /* @depcreted
    createRequest: function() {
        var result = null;
        if (window.XMLHttpRequest) {
            // FireFox, Safari, etc.
            result = new XMLHttpRequest();
            if (typeof xmlhttp.overrideMimeType != 'undefined') {
              result.overrideMimeType('text/xml'); // Or anything else
            }
          }
          else if (window.ActiveXObject) {
            // MSIE
            result = new ActiveXObject("Microsoft.XMLHTTP");
          } 
          else {
            // No known mechanism -- consider aborting the application
          }
          return result;
    },
    */

};

