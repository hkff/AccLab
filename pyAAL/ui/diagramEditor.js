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
    aceTheme      : (sessionStorage.getItem("theme") != null)?sessionStorage.getItem("theme"):"monokai",
    aceThemesList : ["monokai", "chrome", "tomorrow", "kuroir", "eclipse", "chaos"],
    backend       : "http://127.0.0.1:8000/",
    username      : "",

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

    /**
     * Close file
     */
    closeFile: function() {
        // If the page contains a panel element, undock it and destroy it
        if (visualEditor.activeCloseBtn.parent.container.containerType == "panel")
        {
            visualEditor.activeCloseBtn.undockInitiator.enabled = false;
            var panel = visualEditor.activeCloseBtn.parent.container;
            panel.performUndock();
            visualEditor.activeCloseBtn = null;
        }
    },

    /**
     * Get username
     */
    getUserName: function() {
        if(sessionStorage.getItem("username") != null) {
            return sessionStorage.getItem("username");
        }
        else {
            var username = "";
            do {
                username =prompt("Enter a user name : ");
            }
            while(username.length < 0);
            // Save and return the username
            sessionStorage.setItem("username", username);
            return username;
        }
    },

    /**
     * Clear Preferences
     */
    clearPrefs: function() {
        sessionStorage.clear();
            toastr.info("Cache cleared !", "", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": true,
  				"showDuration": "500",
			  	"hideDuration": "500",
			  	"timeOut": 1300,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-center"
			});
    },

    /**
     * Update Ace editor Theme
     * @param theme
     */
    updateAceTheme: function(theme) {

        visualEditor.aceTheme = $(theme).val();
        // Save theme in local storage
        sessionStorage.setItem("theme", visualEditor.aceTheme);
        this.updateEditorsTheme();
    },

    updateEditorsTheme: function() {
        // Update Editors
        if (visualEditor.activeEditor != null)
            visualEditor.activeEditor.setTheme("ace/theme/" + visualEditor.aceTheme);

        if (visualEditor.ui.properties.aalEditor.inPlaceAALEditor != null)
            visualEditor.ui.properties.aalEditor.inPlaceAALEditor.setTheme("ace/theme/" + visualEditor.aceTheme);
    },

    /**
     * Unlock all panels
     */
    clearPanels: function() {
     for(var i=0; i<window.panelNodes.length; i++) {
            try {
                window.panelNodes[i].performUndock();
            } catch (e) {
            }
        }
    },

    /**
     * Adding edited marker " *" to current file
     */
    markPanelEdited: function() {
        var tt = $(".tab-handle-selected .tab-handle-text");
        if(tt.length > 0 && !tt[0].innerHTML.endsWith(" *"))
            tt[0].innerHTML += " *";
    },

    /**
     * Remove edited marker " *" from current file
     */
    markPanelClear: function() {
        var tt = $(".tab-handle-selected .tab-handle-text");
        if(tt.length > 0)
            tt[0].innerHTML = tt[0].innerHTML.replace(" *", "");
    },

    /**
     * AAL view mode
     */
    aalMode: function() {
        visualEditor.clearPanels();
        var prop = 200 / $(document).width();

        window.solutionNode = dockManager.dockLeft(window.documentNode, window.solution, 0.20);
        window.outputNode = dockManager.dockRight(window.documentNode, window.output, 0.4);
        window.toolboxNode = dockManager.dockUp(window.solutionNode, window.toolbox, 0.2);

        //window.outlineNode = dockManager.dockFill(solutionNode, outline);
        /*
        window.problemsNode = dockManager.dockDown(window.propertiesNode, inplaceAAL, 0.40);
        window.propertiesNode = dockManager.dockRight(documentNode, properties, 0.20);
        window.inplaceAALNode = dockManager.dockFill(window.propertiesNode, window.inplaceAAL);
        window.componentsNode = dockManager.dockFill(window.propertiesNode, components);
        */
    },

    /**
     * Design view mode
     */
    acdMode: function() {
        visualEditor.clearPanels();

        // Dock the panels on the dock manager
        var prop = 200 / $(document).width();
        window.solutionNode = dockManager.dockLeft(window.documentNode, window.solution, prop);
        window.outlineNode = dockManager.dockDown(window.solutionNode, window.outline, 0.50);

        prop = 145 / $(document).width();
        window.componentsNode = dockManager.dockLeft(window.documentNode, window.components, prop);
        window.toolboxNode = dockManager.dockDown(window.componentsNode, window.toolbox, 0.80);

        prop = 250 / $(document).width();
        window.propertiesNode = dockManager.dockRight(window.documentNode, window.properties, prop);
        //window.inplaceAALNode = dockManager.dockRight(window.documentNode, window.inplaceAAL, prop);
        //window.propertiesNode = dockManager.dockFill(window.inplaceAALNode, window.properties);

        //prop = 500 / $(document).height();
        //window.outputNode = dockManager.dockDown(window.documentNode, window.output, prop);
    },

    /**
     * Default mode
     */
    defaultMode: function() {
        visualEditor.clearPanels();

        window.documentNode = dockManager.context.model.documentManagerNode;
        var prop = 200 / $(document).width();
        window.solutionNode = dockManager.dockLeft(documentNode, solution, prop);
        window.outlineNode = dockManager.dockDown(solutionNode, outline, 0.50);

        prop = 250 / $(document).width();
        window.propertiesNode = dockManager.dockRight(documentNode, properties, prop);

        prop = 500 / $(document).height();
        window.outputNode = dockManager.dockDown(documentNode, output, prop);
        window.inplaceAALNode = dockManager.dockDown(this.propertiesNode, inplaceAAL, 0.40);

        prop = 145 / $(document).width();
        window.componentsNode = dockManager.dockLeft(documentNode, components, prop);
        window.toolboxNode = dockManager.dockDown(componentsNode, toolbox, 0.80);
    },
    
    about: function () {
        var abt = "" +
            "<img src='assets/icon_128.png' class='logoAbout' alt='AccLab logo'>" +
            "<div class='versionAbout'>AccLab Version 1.0.2</div>" +
            "<div class='aboutCore'>AccLab is a web based accountability framework designed in the context of A4CLOUD project. " +
            "The main goal is to observe ”accountability in action” by simulating a software system with several" +
            " agents exchanging data and requiring different privacy policy." +
            "</div></br><a href='http://www.emn.fr/z-info/acclab/' target='_blank'>http://www.emn.fr/z-info/acclab/</a> " +

            "<div class='membersAbout'>* Developers : - Walid Benghabrit * Contributors :" +
            " - Pr.Jean-Claude Royer (Kernel/Theory/UI)" +
            " - Dr. Hervé Grall (Theory)" +
            " - Dr. Mohamed Sellami (Theory)" +
            " - Pierre Teilhard (Kernel)" +
            " - Anqi Tong (UI)" +
            " - Julie Spens (UI)</div>" +

            "<div class='footerAbout'>Copyright (C) 2014-2015 Walid Benghabrit - Ecole des Mines de Nantes - ARMINES</br>" +
            "ASCOLA Research Group - A4CLOUD Project http://www.a4cloud.eu/ </div>";
       toastr.info(abt, "About", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": true,
  				"showDuration": "1000",
			  	"hideDuration": "1000",
			  	"timeOut": 0,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-center"
			});
        visualEditor.ui.updateToastSize("info", 800);
    }
};


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


/**
 * On load
 */
window.onload = function() {

    // ===================================
    // Patching dockspawn lib
    // ===================================

    // Override dockspawn close btn
    dockspawn.TabHandle.prototype.onCloseButtonClicked = function()
    {
        // check if file has been modified
        visualEditor.activeCloseBtn = this;
        if(visualEditor.activeEditor != null &&
            visualEditor.activeEditor.session.getUndoManager().isClean())
            visualEditor.closeFile();
        else {
            var p = '<button type="button" class="btn" onclick="visualEditor.closeFile()">YES' +
                '</button> <button type="button" class="btn">NO</button>';
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
        }
    };

    function removeNode(node) {
        if (node.parentNode == null)
            return false;
        node.parentNode.removeChild(node);
        return true;
    }

    // PATCH : do not remove panel from dom when changing tabs
    dockspawn.TabPage.prototype.setSelected = function(flag)
    {
        this.selected = flag;
        this.handle.setSelected(flag);

        if ($(this.containerElement).hasClass("panel-base")) {
            if (!this._initContent)
                this.host.contentElement.appendChild(this.containerElement);
            this._initContent = true;
        }

        if (this.selected)
        {
             if (!$(this.containerElement).hasClass("panel-base"))
                this.host.contentElement.appendChild(this.containerElement);
             else
                this.containerElement.style.display = 'block';

            // force a resize again
            var width = this.host.contentElement.clientWidth;
            var height = this.host.contentElement.clientHeight;
            this.container.resize(width, height);
        }
        else {
            if (!$(this.containerElement).hasClass("panel-base"))
               removeNode(this.containerElement);
            else
                 this.containerElement.style.display = 'none';
        }

        // Update theme
        if(visualEditor.aceTheme != null)
            visualEditor.updateEditorsTheme();
    };


    dockspawn.PanelContainer.loadFromState = function(state, dockManager)
    {
        var elementName = state.element;
        var elementContent = document.getElementById(elementName);
        var ret = new dockspawn.PanelContainer(elementContent, dockManager);
        //ret.elementContent = elementContent;
        //ret._initialize();
        ret.loadState(state);
        return ret;
    };
    // =========================================== //

    //
    // Main UI
    //

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
    this.inplaceAALNode = dockManager.dockDown(this.propertiesNode, inplaceAAL, 0.40);

    prop = 145 / $(document).width();
    this.componentsNode = dockManager.dockLeft(documentNode, components, prop);
    this.toolboxNode = dockManager.dockDown(componentsNode, toolbox, 0.80);

    // Tabhost
    dockspawn.TabHost.prototype.onTabChanged = function (page) {
        visualEditor.ui.canvas = page.activeTab.container.canvas;
        visualEditor.ui.activeTab = page.activeTab;
        visualEditor.ui.updatePanel();
    };

    this.panelNodes = [window.solution, window.outline, window.components, window.toolbox,
        window.properties, window.inplaceAAL, window.output];

    // Load user name
    visualEditor.username = visualEditor.getUserName();
}
