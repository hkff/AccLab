visualEditor.ui.outline = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	commandStack    : null,
	canvas          : null,
	selectedNode    : null,
	tree : null,

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
		this.tree = $("<ul id='outlineTree' class='easyui-tree'>");
		$("#outline_window").append(this.tree);
		this.tree.tree({
			animate: true,
			checkbox:false,

			onContextMenu: function(e,node){
				e.preventDefault();
				$(this).tree('select',node.target);
				$('#mm').menu('show',{
					left: e.pageX,
					top: e.pageY
				});},

			formatter:function(node){
				//console.log(node)
				var s = node.text;
				if(node.children){
					s += ' <span style=\'color:gray\'>(' + node.children.length + ')</span>';
				}
				return s;
			},
		});


		this.ctMenu = '<div id="mm" class="easyui-menu menu-top menu" style="width: 137px; display: none; left: 94px; top: 150px; z-index: 110009;">'+
						'<div class="menu-line"></div>'+
						'<div onclick="visualEditor.ui.outline.expandAll()" class="menu-item" style="height: 20px;">Expand</div>'+
						'<div onclick="visualEditor.ui.outline.collapseAll()" class="menu-item" style="height: 20px;">Collapse</div>'+
					'</div>';
		$('body').append(this.ctMenu);

	},


	/**
	 *
	 */
	control: function(_this) {
		this.tree.tree({
			onSelect: function(node) {
				var figs = visualEditor.ui.canvas.getFigures();
				for (var i=0; i<figs.getSize(); i++) {
					if(figs.get(i).id == node.id && figs.get(i).type == node.type) {
						visualEditor.ui.canvas.setCurrentSelection(figs.get(i));
						//visualEditor.ui.selectedNode = figs.get(i);
        				//$(visualEditor.ui).trigger('nodeSelected');
					}
				};
			},

			onAfterEdit: function(node) {
				var figs = visualEditor.ui.canvas.getFigures();
				for (var i=0; i<figs.getSize(); i++) {
					if(figs.get(i).id == node.id && figs.get(i).type == node.type) {
						figs.get(i).updateName(node.text);
					}
				};
			},

			onDblClick: function(node) {
				_this.expand();
				//$(this).tree('beginEdit', node.target);
			},		

		});
	},



	canvasToTree: function() {
		var fig = visualEditor.ui.canvas.getFigures();
		var nodes = this.tree.tree('getRoots');
		var lng = nodes.length;
		for (var i=0; i<lng; i++) {
			this.tree.tree('remove', nodes[0].target);
		}

		for (var i=0; i<fig.getSize(); i++) {
			console.log(fig.get(i).toJSONtree())
			console.log(JSON.parse(fig.get(i).toJSONtree()))

			// Get the JSON tree representation of the node and insert it
			this.tree.tree('insert',{
		    		after:this.tree.tree('getRoot'),
		    		data:[JSON.parse(fig.get(i).toJSONtree())]});
		};
	},


	collapse: function() {
		var node = this.tree.tree('getSelected');
		$('#outlineTree').tree('collapse',node.target);
	},

	expand: function() {
		var node = this.tree.tree('getSelected');
		$('#outlineTree').tree('expand',node.target);
	},

	collapseAll: function() {
		$('#outlineTree').tree('collapseAll');
	},

	expandAll: function() {
		$('#outlineTree').tree('expandAll');
	},

	select: function(nodeId) {
		var node = $('#outlineTree').tree('find', nodeId);
		$('#outlineTree').tree('select', node.target);
		$('#outline_window').stop().scrollTo(node.target, 500)
		
	},

};

