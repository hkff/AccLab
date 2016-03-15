//////////////////////////////////////////////////////////
//
//  Fodtl
//
// Copyright (C) 2016 Walid Benghabrit
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

Fodtl_rectOpUI = draw2d.shape.basic.Rectangle.extend({
	NAME : "Fodtl_rectOpUI",
	type : "Fodtl_rectOpUI",
    tlabel : null,
	outlineIcon : "outlineIcons-data fa fa-database",
    name : "",
    color: "#007386",

    init: function(name) {
        this._super();
        this.setBackgroundColor(this.color);
        this.tlabel = new draw2d.shape.basic.Label2({
            text: name,
            color:"#0d0d0d",
            fontColor: "#ffffff",
            stroke:0
        });
        this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
    }
});


/***************************************
 * Unary operators model
 **************************************/
Fodtl_uTemporal = Class.extend({
	NAME : "Fodtl_unaryOp",
	uiElement : null,
    parent    : null,
    name      : "",

	init: function() {
        this.parent = visualEditor.ui.components;
		this.uiElement = "Fodtl_rectOpUI";
	},

	view: function() {
		this.cmp_data = $('<div title="'+this.name+'" class="btn-components"><p>'+this.name+'</p></div>');
		this.cmp_data.click({name: this.name}, this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
	},

	addElement: function(event) {
    	var element = new Fodtl_rectOpUI(event.data.name);
        element.createPort("input", this.leftLocator);
        element.createPort("output", this.leftLocator);
        visualEditor.ui.canvas.add(element, 100, 100);
	}
});



/***************************************
 * Binary operators model
 **************************************/
Fodtl_bTemporal = Class.extend({
	NAME : "Fodtl_binaryOp",
	uiElement : null,
    parent    : null,
    name      : "",

	init: function() {
        this.parent = visualEditor.ui.components;
		this.uiElement = "Fodtl_rectOpUI";
	},

	view: function() {
		this.cmp_data = $('<div title="'+this.name+'" class="btn-components"><p>'+this.name+'</p></div>');
		this.cmp_data.click({name: this.name}, this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
	},

	addElement: function(event) {
    	var element = new Fodtl_rectOpUI(event.data.name);
        element.createPort("input", this.leftLocator);
        element.createPort("output", this.leftLocator);
        element.createPort("output", this.leftLocator);
        visualEditor.ui.canvas.add(element, 100, 100);
	}
});


/***************************************
 * Fodtl operators
 **************************************/
Fodtl_always = Fodtl_uTemporal.extend({NAME: "fodtl_always",  name: "Always"});
Fodtl_future = Fodtl_uTemporal.extend({NAME: "fodtl_future",  name: "Future"});
Fodtl_next   = Fodtl_uTemporal.extend({NAME: "fodtl_next",    name: "Next"});
Fodtl_until = Fodtl_bTemporal.extend({NAME: "fodtl_until",  name: "Until"});
Fodtl_release = Fodtl_bTemporal.extend({NAME: "fodtl_release",  name: "Release"});

Fodtl_and   = Fodtl_uTemporal.extend({NAME: "fodtl_and",  name: "And"});
Fodtl_or    = Fodtl_uTemporal.extend({NAME: "fodtl_or",  name: "Or"});
Fodtl_imply = Fodtl_uTemporal.extend({NAME: "fodtl_imply",    name: "Imply"});



