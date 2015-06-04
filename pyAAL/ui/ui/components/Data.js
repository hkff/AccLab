//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : Data.js
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

data = actor.extend({
	NAME : "data",
	uiElement : null,
    parent    : null,

	init: function() {
		this._super();
		this.uiElement = "DataUI";
	},

	view: function() {
		// Agent
		this.cmp_data = $('<div title="Data (shift+D)" class="btn-components fa fa-database fa-2x"></div>')
		this.cmp_data.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
		shortcut.add("Shift+D", this.addElement);
	},

	addElement: function() {
		var leftLocator  = new draw2d.layout.locator.InputPortLocator();
    	var rightLocator = new draw2d.layout.locator.OutputPortLocator();

    	var element = new DataUI();
        element.addPservice("read");
        element.addPservice("write");
        element.addPservice("delete");
        visualEditor.ui.canvas.add(element, 100, 100);
        visualEditor.ui.outline.canvasToTree();
	}
});


DataUI = ActorUI.extend({
	NAME : "DataUI",
	type : "Data",
	outlineIcon : "outlineIcons-data fa fa-database",
	subject : "",
    /*leftLocator  : new draw2d.layout.locator.InputPortLocator(),
    rightLocator : new draw2d.layout.locator.OutputPortLocator(),
    pservices : new draw2d.util.ArrayList(),
    rservices : new draw2d.util.ArrayList(),
    types     : new draw2d.util.ArrayList(),*/
    init:function(attr) {
      this._super(attr);
    },

    /**
     * Generate the AAL declaration
	 * @returns {*}
     */
    getAALDeclaration: function() {
        return this._super();
    }
});
