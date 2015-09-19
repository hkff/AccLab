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
    currentAAL      : null,

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
		}
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

	stoper: function(e) {
		e.stopPropagation();
		e.preventDefault()
	},

	updateToastSize: function(type, size) {
        var l = $(".toast-" + type);
        if(l[l.length - 1] != undefined)
            $(l[l.length - 1] ).css("width", size + "px");
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
		if(fileType != "acd") {
			this.disableNode(this.propertiesPanel);
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
			}
			if(fileType == "aal") {
				$(visualEditor.ui.tools.tools[20].button).show();
				$(visualEditor.ui.tools.tools[21].button).show();
				$(visualEditor.ui.tools.tools[22].button).show();
			}

		} else {
			// Enable them
			this.enableNode(this.propertiesPanel);
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
			var tmp_policy = tmp.getPolicy();
			if(tmp_policy != "")
				aal += tmp_policy + "\n\n";
		}
		return aal;
	},

    /**
     * Analyse opened AAL file and update info
     */
	analyseAAL: function (aalFile) {
        $.ajax({
            dataType: 'text',
            type:'POST',
            url: visualEditor.backend,
            data: {action: "getAALdec", file: aalFile},
            success: function(response) {
                var obj = jQuery.parseJSON(response);
                visualEditor.ui.currentAAL = obj;
            }
	    });
    }

};
