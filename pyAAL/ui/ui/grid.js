//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : grid.js
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

	/**
	 * init function
	 * @param grid
	 * @param actionsPanel
	 * @param componentsPanel
	 * @param propertiesPanel
	 */
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel) {
		
		// Get view elements
		this.grid            = $('#'+ grid);
		this.actionsPanel    = $('#'+ actionsPanel);
		this.componentsPanel = $('#'+ componentsPanel);
		this.propertiesPanel = $('#'+ propertiesPanel);

		// init graph
		//this.canvas = new draw2d.Canvas(grid);

		this._super(grid, 2000, 2000);
		this.setScrollArea("#"+grid);

		this.handleEvents();
		
		this.installEditPolicy(new CopyInterceptorPolicy());
		this.installEditPolicy(new draw2d.policy.canvas.CoronaDecorationPolicy());
		this.installEditPolicy(new draw2d.policy.canvas.SnapToGeometryEditPolicy());
		this.installEditPolicy(new draw2d.policy.canvas.ShowDotEditPolicy());

		// override the default method for connection create. 
		// Now we create always the kind of connection which the user has been selected in the
		// menubar. 
		draw2d.Connection.createConnection=function(sourcePort, targetPort){
		    var c = new MyConnection({
	    	   		targetDecorator : new draw2d.decoration.connection.CircleDecorator(10,10),
					sourceDecorator : new draw2d.decoration.connection.RequiredDecorator(0, 200)
		    });
		    //c.setRouter(draw2d.Connection.DEFAULT_ROUTER);
		    c.setRouter(new draw2d.layout.connection.SplineConnectionRouter());
		    return c;
		};

		this.on("select", function(emitter,figure){
	    	if(figure!==null){
	        	//visualEditor.ui.selectedNode = figure;
	        	//$(visualEditor.ui).trigger('nodeSelected');
	        	//console.log("changed ")
	     	}
	     	else{
     		}
     	});
	},

    handleEvents: function() {
    	 $(this.grid).bind("mousewheel", this.zoom);
    	 $(this.grid).bind("onDrop", this.onDrop);
    },

    zoom: function(event) {
    	if(event.altKey){
    		if(event.originalEvent.wheelDelta < 0) delta = 1.3;
			else delta = 0.7;
			visualEditor.ui.canvas.setZoom(visualEditor.ui.canvas.getZoom()*delta, true);	
    	}
    }
});



var MyConnection= draw2d.Connection.extend({
    init:function(attr) {
	this._super(attr);
	this.setRouter(new draw2d.layout.connection.InteractiveManhattanConnectionRouter());
	this.setOutlineStroke(0);
	this.setOutlineColor("#303030");
	this.setStroke(3);
	this.setColor('#00A8F0');
	this.setRadius(0);
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
