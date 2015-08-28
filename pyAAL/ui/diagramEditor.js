//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : diagramEditor.js
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
    
var visualEditor = {
    path          : "curpath",
	/*currentCanvas : null,
	activeTab     : null,
    canvas        : [],*/
    activeEditor    : null,
    visualEditor  : false,
    activeCloseBtn: null,
    backend       : "http://127.0.0.1:8000/",

    /**
     * Initialize function
     */
    init: function(grid, actionsPanel, componentsPanel, propertiesPanel, outlinePanel, inplacePanel) {
    	this.backend = window.location.origin;
    	// init workspace
        visualEditor.ui.init(grid, actionsPanel, componentsPanel, propertiesPanel, outlinePanel, inplacePanel);
    },

    /**
     * Generate unique id
     * @returns {*}
     */
    guid: function() {
        function _p8(s) {
            var p = (Math.random().toString(16)+"000000000").substr(2,8);
            return s ? "-" + p.substr(0,4) + "-" + p.substr(4,4) : p ;
        }
       return _p8() + _p8(true) + _p8(true) + _p8();
    },

    closeFile: function() {
        // If the page contains a panel element, undock it and destroy it
        if (visualEditor.activeCloseBtn.parent.container.containerType == "panel")
        {
            visualEditor.activeCloseBtn.undockInitiator.enabled = false;
            var panel = visualEditor.activeCloseBtn.parent.container;
            panel.performUndock();
        }
    }
};


/**
 * On load
 */
window.onload = function() {
    // Override close btn
    dockspawn.TabHandle.prototype.onCloseButtonClicked = function() {
        visualEditor.activeCloseBtn = this;
        var p = '<button type="button" class="btn" onclick="visualEditor.closeFile()">YES</button> <button type="button" class="btn">NO</button>';
        toastr.error(p, "Close file without Saving ?", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": true,
  				"showDuration": "2000",
			  	"hideDuration": "500",
			  	"timeOut": 0,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-center"
			});
    };

    // Convert a div to the dock manager.  Panels can then be docked on to it
    this.divDockManager = document.getElementById("my_dock_manager");
    this.dockManager = new dockspawn.DockManager(divDockManager);
    this.dockManager.initialize();
    // Let the dock manager element fill in the entire screen
    var onResized = function (e) {
        dockManager.resize(window.innerWidth - (divDockManager.clientLeft + divDockManager.offsetLeft),
            window.innerHeight - (divDockManager.clientTop + divDockManager.offsetTop));
    }
    window.onresize = onResized;
    onResized(null);

    // Convert existing elements on the page into "Panels".
    // They can then be docked on to the dock manager
    // Panels get a titlebar and a close button, and can also be
    // converted to a floating dialog box which can be dragged / resized
    this.solution = new dockspawn.PanelContainer($("#solution_window")[0], dockManager);
    this.solution.elementButtonClose.innerHTML = "";
    this.outline = new dockspawn.PanelContainer($("#outline_window")[0], dockManager);
    this.outline.elementButtonClose.innerHTML = "";
    this.components = new dockspawn.PanelContainer($("#componentbox_window")[0], dockManager);
    this.components.elementButtonClose.innerHTML = "";
    this.toolbox = new dockspawn.PanelContainer($("#toolbox_window")[0], dockManager);
    this.toolbox.elementButtonClose.innerHTML = "";
    this.properties = new dockspawn.PanelContainer($("#properties_window")[0], dockManager);
    this.properties.elementButtonClose.innerHTML = "";
    this.inplaceAAL = new dockspawn.PanelContainer($("#inPlaceAALEditor")[0], dockManager);
    this.inplaceAAL.elementButtonClose.innerHTML = "";
    this.output = new dockspawn.PanelContainer($("#output_window")[0], dockManager);
    this.output.elementButtonClose.innerHTML = "";
//            this.editor1 = new dockspawn.PanelContainer($("#editor1_window")[0], dockManager);

    // Dock the panels on the dock manager
    this.documentNode = dockManager.context.model.documentManagerNode;
    var prop = 200 / $(document).width();
    this.solutionNode = dockManager.dockLeft(documentNode, solution, prop);
    this.outlineNode = dockManager.dockDown(solutionNode, outline, 0.50);

    prop = 250 / $(document).width();
    this.propertiesNode = dockManager.dockRight(documentNode, properties, prop);

    prop = 500 / $(document).height();
    this.outputNode = dockManager.dockDown(documentNode, output, prop);
    this.problemsNode = dockManager.dockDown(this.propertiesNode, inplaceAAL, 0.40);

    prop = 145 / $(document).width();
    this.componentsNode = dockManager.dockLeft(documentNode, components, prop);
    this.toolboxNode = dockManager.dockDown(componentsNode, toolbox, 0.80);

    // Tabhost
    dockspawn.TabHost.prototype.onTabChanged = function (page) {
        visualEditor.ui.canvas = page.activeTab.container.canvas;
        visualEditor.ui.activeTab = page.activeTab;
        visualEditor.ui.updatePanel();
    };

    // TODO REMOVE
    //visualEditor.ui.fileManager.openFile("tuto2.aal");
}

/**
 * Replace ALL
 * @param find
 * @param replace
 * @param str
 * @returns {XML|string|*|void}
 */
function replaceAll(find, replace, str) {
  return str.replace(new RegExp(find, 'g'), replace);
}
