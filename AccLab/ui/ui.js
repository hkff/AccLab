//////////////////////////////////////////////////////////
//
//  AccDesigner V 0.2
//
//////////////////////////////////////////////////////////
visualEditor.ui = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	commandStack    : null,
	canvas          : null,
	selectedNode    : null,
	activeTab       : null,

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

		//visualEditor.ui.canvas = new visualEditor.ui.gridEditor(grid, actionsPanel, componentsPanel, propertiesPanel);
		//visualEditor.ui.fileManager.openFile("File1");
		visualEditor.ui.properties.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.tools.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.outline.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.fileManager.init(grid, actionsPanel, componentsPanel, propertiesPanel);
		visualEditor.ui.components.init(grid, actionsPanel, componentsPanel, propertiesPanel);
	},

	// Events
	handleEvents: function() {
		$(this).bind('nodeSelected', this.nodeSelected)
		$(this).bind('nodeUpdated', this.nodeUpdated)

	},


	nodeSelected: function() {
		visualEditor.ui.properties.updateProps();
		visualEditor.ui.outline.select(visualEditor.ui.selectedNode.id);
	},

	nodeUpdated: function() {
		visualEditor.ui.outline.canvasToTree();
	},

//visualEditor.ui.selectedNode = this.parent;
        //$(visualEditor.ui).trigger('nodeSelected');



	/**
	 * Generate AAL code
	 */
	generateAAL: function() {
		var aal = "";
		var figs = visualEditor.ui.canvas.getFigures();
		var tmp = null;
		
		// Handle declarations
		aal += "/***************************\n *       Declarations\n ****************************/\n";
		for (var i=0; i<figs.getSize(); i++) {
			tmp = figs.get(i);
			aal += tmp.getAALDeclaration()+"\n";
		};

		// Handle clauses
		aal += "\n/***************************\n *       Clauses\n ****************************/\n";
		for (var i=0; i<figs.getSize(); i++) {
			tmp = figs.get(i);
			aal += tmp.getPolicy() + "\n\n";
		};
		console.log(aal)
		return aal;
	},
};
