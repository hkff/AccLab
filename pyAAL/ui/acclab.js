//////////////////////////////////////////////////////////
//
//  AccLab UI V 2.0 : acclab.js
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
    activeEditor  : null,
    visualEditor  : false,
    activeCloseBtn: null,
    userPrefs     : {"theme": "monokai", "username": "", "fontSize": 14, "recentFiles": []},
    aceTheme      : "monokai",
    aceThemesList : ["monokai", "chrome", "tomorrow", "kuroir", "eclipse", "chaos"],
    backend       : "http://127.0.0.1:8000/",
    version       : "2.0 (beta)",


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
            delete visualEditor.ui.openedEditors[visualEditor.ui.activeTab.panel.title];

            var panel = visualEditor.activeCloseBtn.parent.container;
            panel.performUndock();
            visualEditor.activeCloseBtn = null;

            // Clean editor to avoid memory leaks
            if(visualEditor.activeEditor != null) {
                //visualEditor.activeEditor.destroy();
                //$(visualEditor.activeEditor.container).remove();
                visualEditor.activeEditor = null;
            }
        }
    },

    /**
     * Get username
     */
    getUserName: function() {
        if(visualEditor.userPrefs["username"] == "") {
            var username = "";
            do {
                username =prompt("Enter a user name : ");
            }
            while(username.length < 0);
            // Save the username
            visualEditor.userPrefs["username"] = username;
            visualEditor.savePrefs();
        }
        return visualEditor.userPrefs.username;
    },

    /**
     * Get Font size
     */
    getFontSize: function() {
        if(visualEditor.userPrefs["fontSize"] == null) {
            visualEditor.userPrefs["fontSize"] = 14;
            visualEditor.savePrefs();
        }
        return visualEditor.userPrefs.fontSize;
    },

    /**
     * Update Ace editor Theme
     * @param theme
     */
    updateAceTheme: function(theme) {
        visualEditor.aceTheme = $(theme).val();
        visualEditor.userPrefs["theme"] = visualEditor.aceTheme;
        visualEditor.savePrefs();
        this.updateEditorsTheme();
    },

    updateEditorsTheme: function() {
        // Update Editors
        if (visualEditor.activeEditor != null)
            visualEditor.activeEditor.setTheme("ace/theme/" + visualEditor.aceTheme);

        //if (visualEditor.ui.properties.aalEditor.inPlaceAALEditor != null)
        //    visualEditor.ui.properties.aalEditor.inPlaceAALEditor.setTheme("ace/theme/" + visualEditor.aceTheme);
    },

    /**
     * Load user preferences
     */
    loadPrefs: function() {
        $.ajax({
            dataType: 'text',
            type: 'POST',
            url: visualEditor.backend,
            data: {action: "loadPrefs"},
            success: function (response) {
                var obj = jQuery.parseJSON(response);
                visualEditor.userPrefs = obj;
                visualEditor.getUserName();
                visualEditor.aceTheme = visualEditor.userPrefs["theme"];
                visualEditor.startup();
            }
        });
    },

    /**
     * Save user preferences
     */
    savePrefs: function() {
        $.ajax({
            dataType: 'text',
            type: 'POST',
            url: visualEditor.backend,
            data: {action: "savePrefs", prefs: JSON.stringify(visualEditor.userPrefs)},
            success: function (response) {
                //console.log(response)
            }
        });
    },

    /**
     * Clear Preferences
     */
    clearPrefs: function() {
        // Restore default values
        visualEditor.userPrefs["username"] = "";
        visualEditor.userPrefs["theme"] = "monokai";
        visualEditor.userPrefs["fontSize"] = 14;

        $.ajax({
            dataType: 'text',
            type: 'POST',
            url: visualEditor.backend,
            data: {action: "savePrefs", prefs: JSON.stringify(visualEditor.userPrefs)},
            success: function (response) {
                 toastr.info("Preferences cleared !", "", {
                    "closeButton": true,
                    "preventDuplicates": true,
                    "tapToDismiss": true,
                    "showDuration": "500",
                    "hideDuration": "500",
                    "timeOut": 1300,
                    "extendedTimeOut": 0,
                    "positionClass": "toast-top-center"
                });
            }
        });
    },

    /**
     * Unlock all panels
     */
    clearPanels: function() {
        for(var i=0; i<window.panelNodes.length; i++) {
            try {
                window.panelNodes[i].performUndock();
            } catch (e) {}
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
    aalMode: function(flat) {
        visualEditor.clearPanels();
        if(flat != undefined) {
            window.solutionNode = dockManager.dockRight(window.documentNode, window.output, 0.40);
        } else {
            window.solutionNode = dockManager.dockLeft(window.documentNode, window.solution, 0.20);
            window.outputNode = dockManager.dockRight(window.documentNode, window.output, 0.4);
            window.toolboxNode = dockManager.dockUp(window.solutionNode, window.toolbox, 0.2);
        }
    },

    /**
     * Design view mode
     */
    acdMode: function() {
        visualEditor.clearPanels();

        // Dock the panels on the dock manager
        var prop = 200 / $(document).width();
        window.solutionNode = dockManager.dockLeft(window.documentNode, window.solution, prop);
        window.outlineNode = dockManager.dockDown(window.solutionNode, window.outline, 0.30);

        prop = 100 / $(document).width();
        window.componentsNode = dockManager.dockLeft(window.documentNode, window.components, prop);
        window.toolboxNode = dockManager.dockRight(window.documentNode, window.toolbox, prop/1.5);

        prop = 200 / $(document).height();
        window.outputNode = dockManager.dockDown(documentNode, output, prop);

        //prop = 250 / $(document).width();
        //window.propertiesNode = dockManager.dockRight(window.documentNode, window.properties, prop);
    },

    /**
     * vFodtl view mode
     */
    vfodtlMode: function() {
        visualEditor.clearPanels();

        var prop = 100 / $(document).width();
        window.componentsNode = dockManager.dockLeft(window.documentNode, window.components, prop);
        window.toolboxNode = dockManager.dockRight(window.documentNode, window.toolbox, prop);
        prop = 200 / $(document).height();
        window.outputNode = dockManager.dockDown(documentNode, output, prop);
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

        //prop = 250 / $(document).width();
        //window.propertiesNode = dockManager.dockRight(documentNode, properties, prop);

        prop = 500 / $(document).height();
        window.outputNode = dockManager.dockDown(documentNode, output, prop);
        window.inplaceAALNode = dockManager.dockDown(this.propertiesNode, inplaceAAL, 0.40);

        prop = 145 / $(document).width();
        window.componentsNode = dockManager.dockLeft(documentNode, components, prop);
        window.toolboxNode = dockManager.dockDown(componentsNode, toolbox, 0.80);
    },

    /**
     * About panel
     */
    about: function () {
        var abt = "" +
            "<img src='assets/icon_128.png' class='logoAbout' alt='AccLab logo'>" +
            "<div class='versionAbout'>AccLab Version 2.0 BETA</div>" +
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

            "<div class='footerAbout'>Copyright (C) 2014-2016 Walid Benghabrit - Ecole des Mines de Nantes - ARMINES</br>" +
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
        visualEditor.ui.updateToastSize("info", {"width": 800, height:350}, false, "none", (window.innerHeight - 600)/2 + "px");
    },

     /**
     * Startup panel
     */
    startup: function () {
        var recentFiles = "";
        var files = visualEditor.userPrefs["recentFiles"];
        var file = "";
        for(var i=0; i<files.length; i++) {
            if(files[i].length > 25)
                file = "..." + files[i].substr(files[i].length-25);
            else
                file = files[i];

            recentFiles += "<a class='catElement' onclick='visualEditor.ui.fileManager.openFile(\""+files[i]+"\")'>"+file+"</a></br>"
        }
        var abt = "" +
            "<div>"+
            "<div class='startedCat'> <div class='startedCatInner'> <h3 style='color: rgb(9, 9, 9);'>" +
            "<i class='fa fa-folder-open'></i> Recent files</h3>"+ recentFiles +"</div> </div>"+

            "<div class='startedCat'><div class='startedCatInner'> <h3 style='color: rgb(9, 9, 9);'>" +
            "<i class='fa fa-file'></i> Create new file</h3> " +
            "<a class='catElement' onclick='visualEditor.ui.fileManager.createFileType(\"acd\", true)'>" +
            "<i class='fa fa-edit'></i> New component diagram</a></br></br>"+
            "<a class='catElement' onclick='visualEditor.ui.fileManager.createFileType(\"aal\", true)'>" +
            "<i class='fa fa-file-code-o'></i> New AAL policy</a></br></br>"+
            "<a class='catElement' onclick='visualEditor.ui.fileManager.createFileType(\"vfodtl\", true)'>" +
            "<i class='fa fa-calendar-o'></i> New Fodtl diagram</a></br></br>"+
            "</div></div>"+

            "<div class='startedCat'><div class='startedCatInner'><h3 style='color: rgb(9, 9, 9); margin-top: 6px;'>" +
            "<i class='fa fa-question-circle'></i> Help</h3>"+

            "<a class='catElement' target='_blank' href='https://github.com/hkff/AccLab/raw/master/pyAAL/UserGuide/UserGuide.pdf'>" +
            "<i class='fa fa-file-text-o'></i> User guide</a></br></br>"+
            "<a class='catElement' target='_blank' href='https://github.com/hkff/AccLab'>" +
            "<i class='fa fa-github'></i> Github page</a></br></br>"+
            "<a class='catElement' onclick='visualEditor.about()'><i class='fa fa-question'></i> About</a></br></br>"+
            "</div></div>"+
            "</div>"+
            "<div style='padding-top: 130px; display: inline-block; padding-right: 60px;'>AccLab version 2.0 2014-2016</div>";

        toastr.info(abt, "Get started", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": true,
  				"showDuration": "1000",
			  	"hideDuration": "1000",
			  	"timeOut": 0,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-center"
			});
        visualEditor.ui.updateToastSize("info", {"width": 800, "height": 400}, false, "none", (window.innerHeight - 600)/2 + "px");
    },

    /**
     * Get sys info
     */
    getMonInfo: function() {
        $.ajax({
            dataType: 'text',
            type: 'POST',
            url: visualEditor.backend,
            data: {action: "monitor"},
            success: function (response) {
                var obj = jQuery.parseJSON(response);
                var dg = $('#monGrid');

                // Clear rows
               dg.datagrid('loadData', {"total":0,"rows":[]});

                // Add new rows
                for(var i=0; i<obj.ps.length; i++) {
                    dg.datagrid('appendRow',{
                        user: obj.ps[i].user,
                        pid : obj.ps[i].pid,
                        cpu : obj.ps[i].cpu,
                        mem : obj.ps[i].mem,
                        time: obj.ps[i].time,
                        cmd : obj.ps[i].cmd
                    });
                }
                // Update grid
                dg.datagrid('reload').datagrid('resize');
            }
        });
    },

    /**
     * Kill process
     */
    killProcess: function() {
        var selected = $('#monGrid').datagrid('getSelected');
        if(selected != null && selected != undefined) {
            var pid = selected.pid;
            $.ajax({
                dataType: 'text',
                type: 'POST',
                url: visualEditor.backend,
                data: {action: "killPs", pid: pid},
                success: function (response) {}
            });
        }
    },

    /**
     * Sys monitor
     */
    monitor: function() {
        var mon =
         "<table id='monGrid' class='easyui-datagrid'  style='overflow:auto;width:400px;height:200px'" +
            "data-options='singleSelect:true,collapsible:true'  toolbar='#toolbar'>" +
            "<thead>" +
                "<tr>" +
                "<th data-options=\"field:'user',width:50\">USER</th>" +
                "<th data-options=\"field:'pid' ,width:80\">PID</th>" +
                "<th data-options=\"field:'cpu' ,width:50\">CPU</th>" +
                "<th data-options=\"field:'mem' ,width:50\">MEM</th>" +
                "<th data-options=\"field:'time',width:80\">TIME</th>" +
                "<th data-options=\"field:'cmd' ,width:300\">CMD</th>" +
                "</tr>" +
            "</thead>" +
            "<tbody></tbody>" +
        "</table>" +
         "<div id='toolbar'>" +
            "<div title='Refresh' class='btn-action fa fa-refresh fa-lg' style='padding-top:0px;' onclick='visualEditor.getMonInfo()'></div>" +
            "<div title='Kill process' class='btn-action fa fa-remove fa-lg' style='padding-top:0px;' onclick='visualEditor.killProcess()'></div>" +
        "</div>";

        toastr.warning(mon, "System monitor", {
				"closeButton": true,
				"preventDuplicates": true,
				"tapToDismiss": false,
  				"showDuration": "1000",
			  	"hideDuration": "1000",
			  	"timeOut": 0,
			  	"extendedTimeOut": 0,
				"positionClass": "toast-top-left",
                "onHidden": function() { if(visualEditor.ui.interval != null) clearInterval(visualEditor.ui.interval); }
			});
        visualEditor.ui.updateToastSize("warning", {"width": 410, "height": 240}, true, "none");
        $(".toast-warning").css("padding-left", "5px");
        $("#monGrid").datagrid({fit:false});

        // Minimazing on dbl click
        $(".toast-warning").dblclick(function() {
            if($(this).height() >= 20)
                $(this).animate({width: "150px", height: "30px"});
            else
                $(this).animate({width: "410px", height: "240"});
        });

        // Update moninfo
        visualEditor.getMonInfo();
        visualEditor.ui.interval = setInterval(visualEditor.getMonInfo, visualEditor.ui.psUpdateInterval);
    },

    /**
     * Start together
     */
    startTogether: function() {
        TogetherJSConfig_siteName = "AccLab";
        //TogetherJSConfig_toolName = "";
        TogetherJSConfig_dontShowClicks = true;
        TogetherJSConfig_useMinimizedCode = true;
        TogetherJSConfig_findRoom = "AccLab";
        TogetherJSConfig_suppressJoinConfirmation = true;
        TogetherJSConfig_autoStart = true;
        TogetherJSConfig_inviteFromRoom = true;
        TogetherJS(this);
        return false;
    },

    /**
     * Log msg into output
     * @param msg
     */
    log: function(msg) {
        if(typeof(msg) == "string")
            $("#output_window").append(replaceAll("\n", "<br>", msg) + "<br>");
        else
            $("#output_window").append(msg + "<br>");
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
            var of = visualEditor.ui.getOpenedFile();
            if(of.endsWith(".acd") || of.endsWith(".vfodtl")) {
                visualEditor.closeFile();
                return;
            }

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
        if(visualEditor.aceTheme != null) {
            visualEditor.updateEditorsTheme();
        }
    };

    // Tabhost
    dockspawn.TabHost.prototype.onTabChanged = function (page) {
        visualEditor.ui.canvas = page.activeTab.container.canvas;
        visualEditor.ui.activeTab = page.activeTab;
        visualEditor.activeEditor = visualEditor.ui.openedEditors[page.activeTab.panel.title];
        visualEditor.ui.updatePanel();
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
    };
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
    //this.properties = new dockspawn.PanelContainer($("#properties_window")[0], dockManager);
    //this.properties.elementButtonClose.innerHTML = "";
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

    //prop = 250 / $(document).width();
    //this.propertiesNode = dockManager.dockRight(documentNode, properties, prop);

    prop = 500 / $(document).height();
    this.outputNode = dockManager.dockDown(documentNode, output, prop);
    //this.inplaceAALNode = dockManager.dockDown(this.propertiesNode, inplaceAAL, 0.40);

    prop = 145 / $(document).width();
    this.componentsNode = dockManager.dockLeft(documentNode, components, prop);
    this.toolboxNode = dockManager.dockDown(componentsNode, toolbox, 0.80);


    this.panelNodes = [window.solution, window.outline, window.components, window.toolbox,
        /*window.properties,*/ window.inplaceAAL, window.output];

    // Load prefs
    visualEditor.userPrefs = visualEditor.loadPrefs();

    // Add shortcuts
    shortcut.add("Alt+h", visualEditor.ui.clearHighlight);
    shortcut.add("Alt+z", visualEditor.ui.highlightRed);
    shortcut.add("Alt+a", visualEditor.ui.highlightGreen);

    // DEBUG mode
    //console.log = console.error = function(e) { $("#output_window").append("<br>Console : " + e);}

    // Hide loader
    $('#loading-image').hide();
};
