//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : ui.js
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
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	outlinePanel    : null,
	inplacePanel    : null,
	commandStack    : null,
	canvas          : null,
	selectedNode    : null,
	activeTab       : null,

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

	/**
	 * Update all panels states
	 */
	updatePanel: function() {
		if(visualEditor.ui.activeTab != null)
			var file = visualEditor.ui.activeTab.container.title;
		else
			var file = "";

		var fileType = file.split('.').pop().toLowerCase();
		// If it is not a diagram, disable gui elements
		if(fileType != "acd") {
			this.disableNode(this.propertiesPanel);
			this.disableNode(this.actionsPanel);
			this.disableNode(this.componentsPanel);
			this.disableNode(this.outlinePanel);
			this.disableNode(this.inplacePanel);
		} else {
			// Enable them
			this.enableNode(this.propertiesPanel);
			this.enableNode(this.actionsPanel);
			this.enableNode(this.componentsPanel);
			this.enableNode(this.outlinePanel);
			this.enableNode(this.inplacePanel);
		}
	},

	/**
	 * Enable a node
	 * @param node
	 */
	enableNode: function(node) {
		node.css("opacity", "1.0");
	},

	/**
	 * Disable a node
	 * @param node
	 */
	disableNode: function(node) {
		//var node = $("#toolbox_window");
		node.css("opacity", "0.2");
	   	/*node.append("<div id='overlay'></div>");
		$("#overlay")
		  .css({
			 'opacity' : 0.4,
			 'position': 'fixed',
			 'top': 0,
			 'left': 0,
			 'background-color': 'black',
			 'width': node.width(),
			 'height': node.height(),
			 'z-index': 5000
		  });
*/
	},

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
		}

		// Handle clauses
		aal += "\n/***************************\n *       Clauses\n ****************************/\n";
		for (var i=0; i<figs.getSize(); i++) {
			tmp = figs.get(i);
			var tmp_policy = tmp.getPolicy();
			if(tmp_policy != "")
				aal += tmp_policy + "\n\n";
		}
		return aal;
	}
};
