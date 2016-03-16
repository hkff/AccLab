//////////////////////////////////////////////////////////
//
//  AccLab UI : grid.js
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

visualEditor.ui.gridEditor = draw2d.Canvas.extend({

	NAME : "visualEditor.ui.gridEditor",
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	_this           : this,
	labelColor      : null,
	editPolicies    : [],
    mode            : "acd",

	/**
	 * init function
	 * @param grid
	 * @param actionsPanel
	 * @param componentsPanel
	 * @param propertiesPanel
     * @param mode
	 */
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel, mode) {

		// Get view elements
		this.grid            = $('#'+ grid);
		this.actionsPanel    = $('#'+ actionsPanel);
		this.componentsPanel = $('#'+ componentsPanel);
		this.propertiesPanel = $('#'+ propertiesPanel);
        this.mode = mode;

		// init graph
        this.makeWheelContextMenu("acdPops");

		this._super(grid, 2000, 2000);
		this.setScrollArea("#"+grid);

		this.handleEvents();

        switch (mode) {
            // ------------------ ACD mode ------------------- //
            case "acd":
                this.installEditPolicy(new CopyInterceptorPolicy());
                this.installEditPolicy(new draw2d.policy.canvas.CoronaDecorationPolicy());
                this.installEditPolicy(new draw2d.policy.canvas.SnapToGeometryEditPolicy());
                this.installEditPolicy(new draw2d.policy.canvas.ShowDotEditPolicy()); // SnapToGridEditPolicy


                draw2d.Connection.createConnection = function (sourcePort, targetPort) {
                    var c = new MyConnection({
                        //targetDecorator : new draw2d.decoration.connection.CircleDecorator(10,10),
                        //sourceDecorator : new draw2d.decoration.connection.RequiredDecorator(0, 200)
                        sourceDecorator: new draw2d.decoration.connection.BarDecorator(),
                        targetDecorator: new draw2d.decoration.connection.DiamondDecorator()
                    });
                    //c.setRouter(draw2d.Connection.DEFAULT_ROUTER);
                    //c.setRouter(new draw2d.layout.connection.SplineConnectionRouter());
                    return c;
                };

                // Connection override
                draw2d.Configuration.factory.createConnection = function (sourcePort, targetPort) {
                    var c = new MyConnection({
                        //targetDecorator : new draw2d.decoration.connection.CircleDecorator(10,10),
                        //sourceDecorator : new draw2d.decoration.connection.RequiredDecorator(0, 200)
                        sourceDecorator: new draw2d.decoration.connection.BarDecorator(),
                        targetDecorator: new draw2d.decoration.connection.DiamondDecorator()
                    });
                    //c.setRouter(draw2d.Connection.DEFAULT_ROUTER);
                    //c.setRouter(new draw2d.layout.connection.SplineConnectionRouter());
                    return c;
                };

                this.on("select", function (emitter, figure) {
                    if (figure !== null) {
                        // Update panel prop
                        visualEditor.ui.selectedNode = figure;
                        $(visualEditor.ui).trigger('nodeSelected');

                        $(visualEditor.ui.propertiesPanel.children()).css("opacity", 1);
                        visualEditor.ui.propertiesPanel[0].removeEventListener("click", visualEditor.ui.stoper, true);
                    }
                    else {
                        // Hide panel prop
                        visualEditor.ui.selectedNode = null;
                        $(visualEditor.ui.propertiesPanel.children()).css("opacity", 0.15);
                        visualEditor.ui.propertiesPanel[0].addEventListener("click", visualEditor.ui.stoper, true);
                    }
                });

                // add an event listener to the Canvas for change notifications.
                var _this = this;
                this.getCommandStack().addEventListener(function (e) {
                    if (e.isPostChangeEvent())
                        _this.updatePreview();
                });
                break;

            // ------------------ VFODTL mode ------------------- //
            case "vfodtl":
                break;
        }
	},

    handleEvents: function() {
    	$(this.grid).bind("mousewheel", this.zoom);
    	$(this.grid).bind("onDrop", this.onDrop);

        // Handle context menu
        //$(this.grid).bind("contextmenu", this.toggleWheelContextMenu);
    },

    zoom: function(event) {
    	if(event.altKey){
    		if(event.originalEvent.wheelDelta < 0) delta = 1.3;
			else delta = 0.7;
			visualEditor.ui.canvas.setZoom(visualEditor.ui.canvas.getZoom()*delta, true);	
    	}
    },

    /**
     * Create the wheel context menu
     */
    makeWheelContextMenu: function(target_id) {
        var pops = $("#" + target_id);

        var btn = new visualEditor.ui.tools.saveTool();
        btn.button = $('<li><div title="Save (ctrl+S)" id="saveBtn" class="btn-action fa fa-save fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        btn = new visualEditor.ui.tools.genAALTool();
        btn.button = $('<li><div title="Generate AAL file (ctrl+G)" id="genAALBtn" class="btn-action fa fa-file-text-o fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops, true);

        btn = new visualEditor.ui.tools.AALSyntaxTool();
        btn.button = $('<li><div title="Agent (Ctrl+Shift+A)" class="btn-components fa fa-user fa-2x"></div></li>');
        $(btn.button).on("click", function(e){ console.log("koko"); var a = new agent(); a.addElement() })
        pops.append(btn.button);
        //btn.control(pops, true);

        btn = new visualEditor.ui.tools.mselectTool();
        btn.button = $('<li><div title="Multiple Selection Mode" id="mselectBtn" class="btn-action fa fa-square fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops);

        btn = new visualEditor.ui.tools.clearOutputTool();
        btn.button = $('<li><div title="Clear output" id="clearOutputBtn" class="btn-action fa fa-square-o  fa-lg"/></li>');
        pops.append(btn.button);
        btn.control(pops);

        // Bind the event listener to the trigger
        $("#acdTrigger").bind("mousedown", this.toggleWheelContextMenu);

        // Make the wheel draggable
        $("#acdWheelContextMenu").draggable();
    },

    toggleWheelContextMenu: function(e) {
        if(visualEditor.ui.selectedNode != null)
            return;

        var wcm = $("#acdWheelContextMenu");
        wcm.toggle("display");
        wcm.css("top", e.clientY - 75);
        wcm.css("left", e.clientX - 75);

        e.preventDefault();
        $.popcircle('#acdPops', {
            spacing:'-5px',
            type:'full',        // full, half, quad
            offset:0,	        // 0, 1, 2, 3, 4, 5, 6, 7 or 5.1
            ease:'easeOutQuad', // jquery ease effects,
            time:'fast'         // slow, fast, 1000
        });
    },

    updatePreview: function() {
        // convert the canvas into a PNG image source string
        //
        var xCoords = [];
        var yCoords = [];
        this.getFigures().each(function(i,f) {
            var b = f.getBoundingBox();
            xCoords.push(b.x, b.x+b.w);
            yCoords.push(b.y, b.y+b.h);
        });
        var minX   = Math.min.apply(Math, xCoords);
        var minY   = Math.min.apply(Math, yCoords);
        var width  = Math.max.apply(Math, xCoords)-minX;
        var height = Math.max.apply(Math, yCoords)-minY;

        var writer = new draw2d.io.png.Writer();
        writer.marshal(this,function(png){
           $("#preview").attr("src", png);
        }, new draw2d.geo.Rectangle(minX,minY,width,height));
    }
});


/**
 * Custom connection
 */
var MyConnection= draw2d.Connection.extend({
    init:function(attr) {
        this._super(attr);
        //this.setRouter(new draw2d.layout.connection.InteractiveManhattanConnectionRouter());
        this.setRouter(new draw2d.layout.connection.MazeConnectionRouter());
        this.installEditPolicy(new draw2d.policy.line.VertexSelectionFeedbackPolicy());
        this.setOutlineStroke(0);
        this.setOutlineColor("#303030");
        this.setStroke(4);
        this.setColor('#00A8F0');
        this.setRadius(20);
    },

	onContextMenu:function(x,y){
        $.contextMenu({
            selector: 'body',
            events:
            {
                hide:function(){ $.contextMenu( 'destroy' ); }
            },
            callback: $.proxy(function(key, options)
            {
               switch(key){
               case "red":
                   this.setColor('#f3546a');
                   break;
               case "green":
                   this.setColor('#b9dd69');
                   break;
               case "blue":
                   this.setColor('#00A8F0');
                   break;
               case "delete":
                   // without undo/redo support
              //     this.getCanvas().remove(this);

                   // with undo/redo support
                   var cmd = new draw2d.command.CommandDelete(this);
                   this.getCanvas().getCommandStack().execute(cmd);
               default:
                   break;
               }

            },this),
            x:x,
            y:y,
            items:
            {
                "red":    {name: "Red", icon: "edit"},
                "green":  {name: "Green", icon: "cut"},
                "blue":   {name: "Blue", icon: "copy"},
                "sep1":   "---------",
                "delete": {name: "Delete", icon: "delete"}
            }
        });
    }
});


//////////////////////////////////////////////////////////
//
//  CopyInterceptorPolicy
//
//////////////////////////////////////////////////////////
var CopyInterceptorPolicy = draw2d.policy.canvas.SingleSelectionPolicy.extend({

	init : function() {
	    this._super();
	    this.cloneOnDrag = false;
	},

	/**
	 * @method
	 * 
	 * @param {draw2d.Canvas} canvas
	 * @param {Number} x the x-coordinate of the mouse down event
	 * @param {Number} y the y-coordinate of the mouse down event
	 * @param {Boolean} shiftKey true if the shift key has been pressed during this event
	 * @param {Boolean} ctrlKey true if the ctrl key has been pressed during the event
	 */
	onMouseDown:function(canvas, x, y, shiftKey, ctrlKey) {
		this.cloneOnDrag = shiftKey;
		this._super(canvas, x,y,shiftKey, ctrlKey);
	},

	/**
	 * Copy the selected figure if the user start dragging the selection.
	 * 
	 */
	onMouseDrag:function(canvas, dx, dy, dx2, dy2) {
		if( !((this.mouseDraggingElement instanceof draw2d.ResizeHandle) || (this.mouseDraggingElement instanceof draw2d.Port))){
	    	if(this.cloneOnDrag ===true && this.mouseDraggingElement !==null){
	    		// get the current position of the selecgted shape
	    		var pos = this.mouseDraggingElement.getPosition();
	    		
	    		// cancel the current drag&drop operation
	    		this.mouseDraggingElement.onDragEnd(pos.x, pos.y, false,false);
	    		
	    		// clone the selection
	    		this.mouseDraggingElement  = this.mouseDraggingElement.clone();
	    		
	    		// add the clone to the canvas and start dragging of the clone
	    		canvas.addFigure(this.mouseDraggingElement, pos);
	    		// select the clone
	    		this.select(canvas,this.mouseDraggingElement);

	    		// start dragging if the clone
	    		this.mouseDraggingElement.onDragStart(pos.x, pos.y, false,false);
	    	}
		}
		this.cloneOnDrag=false;
		this._super(canvas, dx,dy,dx2,dy2);
	}
});


draw2d.decoration.connection.RequiredDecorator = draw2d.decoration.connection.Decorator.extend({

	NAME : "draw2d.decoration.connection.RequiredDecorator",

	/**
	 * @constructor 
	 * 
	 * @param {Number} [width] the width of the arrow
	 * @param {Number} [height] the height of the arrow
	 */
    init : function(width, height)
   	{   
        this._super( width, height);
    },

	/**
	 * Draw a filled circle decoration.
     *
	 * @param {Raphael} paper the raphael paper object for the paint operation 
	 **/
	paint:function(paper)
	{
        var st = paper.set();
        
        var partial_circle = this.arcpath(paper, this.width/2, 0, this.width/2, 0.5 );
		st.push(partial_circle);
		//st.push(paper.circle(0, 0, this.width/2));
        st.attr({fill:this.backgroundColor.hash(),stroke:this.color.hash()});
		
		return st;
	},

	arcpath: function(canvas, x, y, r, ratio)
	{
	    if (ratio >= 1.0) return canvas.circle(x, y, r);
	    //  we use this to determine whether to use the large-sweep-flag or not
	    var degrees = 360 * ratio;
	    //  this is actually the angle of the terminal point on the circle's circumference -- up is Math.PI / 2, so we need to subtract that out.
	    var radians = (Math.PI * 2 * ratio) - Math.PI / 2;
	    var pathparts = 
	    [
	        "M" + x + "," + y,
	        "v" + (0 - r),
	        "A" + r + "," + r + " " + degrees + " " + (degrees >= 180 ? "1" : "0" ) + " 1 " + 
	              (x + (r * Math.cos(radians))) + "," + (y + (r * Math.sin(radians))),
	        "z"
	    ];

	    //canvas.animate({rotation: "360 65 25"}, 20);
	    return canvas.path(pathparts);
	}
});
