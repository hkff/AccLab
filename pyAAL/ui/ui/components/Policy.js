//////////////////////////////////////////////////////////
//
//  AccLab UI : Policy.js
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

Policy = Class.extend({
    NAME: "Policy",
    type: "Policy",

    init: function() {
        this.parent = visualEditor.ui.components;
    },

    view: function(_this) {
        this.cmp_data = $('<div title="Policy" class="btn-components fa fa-file-powerpoint-o"></div>');
        this.cmp_data.click(_this, this.addElement);
        this.parent.componentsPanel.append(this.cmp_data);
    },

    addElement: function(event, position) {
        var a = new PolicyUI({width:100, height:60}, true);
        if(position == undefined) position = {x:100, y:100};
        visualEditor.ui.canvas.add(a, position.x, position.y);
        return a;
    }
});


PolicyUI = draw2d.shape.basic.Rectangle.extend({
	NAME   : "PolicyUI",
	tlabel : null,
	type   : "Policy",
	policy : " ",
	DEFAULT_bgColor : "#0d0d0d",
    DEFAULT_labelColor : "#0d0d0d",

    init: function(attr) {
        this._super(attr);
        var _this = this;
        this.tlabel = new draw2d.shape.basic.Text({text:"clause name", stroke:0});
        this.tlabel.installEditor(new draw2d.ui.LabelInplaceEditor());
        this.tlabel.on("change", function(e) {
            // Update name in the policy FIXME
            //var re = /CLAUSE \w+/;
            //var m = re.exec(_this.policy);
            //if (m !== null)
            //    _this.policy = _this.policy.replace(m[0], "CLAUSE " + this.text);
            //visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(this.policy);
        });
        this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
        this.createPort("output");
        this.createPort("input");
    },

    onMouseEnter: function() {
        visualEditor.ui.selectedNode = this;
    },

    onClick: function() {
        visualEditor.ui.selectedNode = this;
        visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(this.policy);
    },

    onDoubleClick: function(e) {
        visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(this.policy);
        $("#inPlaceAALEditor").fadeIn(600);
    },

    getPersistentAttributes: function() {
        var memento = this._super();
        memento.policy = this.policy;
        memento.tlabeltxt = this.tlabel.text;
        memento.type = "PolicyUI";
        return memento;
     },

    setPersistentAttributes: function(memento) {
        this._super(memento);
        this.policy = memento.policy;
        this.tlabel.text = memento.tlabeltxt;
        return this;
    },

    refresh: function() {
        this.setBackgroundColor(this.DEFAULT_bgColor);
        this.repaint();
    }
});
