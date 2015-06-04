//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : Agent.js
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

agent = actor.extend({
	NAME : "agent",
    uiElement : null,
    parent    : null,

	init: function() {
		this._super();
		this.uiElement = "AgentUI";
	},

	view: function() {
		// Agent
		this.cmp_agent = $('<div class="btn-components fa fa-user fa-2x"></div>')
		this.cmp_agent.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_agent);
	},

	addElement: function() {
		var leftLocator  = new draw2d.layout.locator.InputPortLocator();
    	var rightLocator = new draw2d.layout.locator.OutputPortLocator();
		var element = new AgentUI();
        element.addPservice("provided1");
        element.addRservice("required1");
        visualEditor.ui.canvas.add(element, 100, 100);
        visualEditor.ui.outline.canvasToTree();
	}
});


AgentUI = ActorUI.extend({
	NAME : "AgentUI",
	type : "Agent",
	outlineIcon : "outlineIcons-agent fa fa-user",
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
