//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : Policy.js
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

policy = Class.extend({
	NAME : "policy",
    name : "policy",
    uiElement : null,
    leftLocator  : new draw2d.layout.locator.InputPortLocator(),
    rightLocator : new draw2d.layout.locator.OutputPortLocator(),

	init: function() {
		this.parent = visualEditor.ui.components;
        this.uiElement = "PolicyUI";
	},

	view: function() {
		// Agent
		this.cmp_data = $('<div class="btn-components fa fa-file-powerpoint-o fa-2x"></div>');
		this.cmp_data.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
	},

	addElement: function() {
		var element = new PolicyUI();
		//element.createPort("input", this.leftLocator);
		visualEditor.ui.canvas.add(element, 100, 100);
	}
});


PolicyUI = draw2d.shape.basic.Text.extend({
	NAME   : "PolicyUI",
	tlabel : null,
	type   : "Policy",
	policy : "",
	DEFAULT_bgColor : "#0d0d0d",
    DEFAULT_labelColor : "#0d0d0d",

	/**
	 * @method
	 * init
	 */
    init:function(attr) {
      this._super(attr);
      // Create any Draw2D figure as decoration for the connection
      //this.tlabel = new draw2d.shape.basic.Text({text:"this.typeqssssdddddd5f4s6rgrgg\nfergrzgz", stroke:1});
      // add the new decoration to the connection with a position locator.
      //this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
    },

    onMouseEnter: function() {
        visualEditor.ui.selectedNode = this;
    },

    onClick: function() {
        visualEditor.ui.selectedNode = this;
        visualEditor.ui.properties.updateProps();
    },

    refresh: function() {
		console.log("inside "+this.DEFAULT_bgColor)
        this.setBackgroundColor(this.DEFAULT_bgColor);
        this.repaint();
    }
});
