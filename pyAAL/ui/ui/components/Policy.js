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

PolicyUI = draw2d.shape.layout.StackLayout.extend({
    NAME   : "PolicyUI",
	type   : "Policy",

    init: function (attr, ui) {
        this._super(attr);
        this.policy = "CLAUSE";
        this.name = "Policy name";

        if(ui) {
            this.policyUI = new draw2d.shape.basic.Text({text:this.policy, stroke:0});
            this.nameUI = new draw2d.shape.basic.Text({text:this.name, stroke:0});
            this.add(this.policyUI);
            this.add(this.nameUI);
        }

        this.setKeepAspectRatio(true);
        this.lastZoom = 1;
        this.installEditPolicy(new draw2d.policy.figure.AntSelectionFeedbackPolicy());
        this.createPort("input");
        this.createPort("output");

        var _this = this;
        var zoomHandler = function (emitter, event) {
            var border = 0.7;

            if (_this.lastZoom >= border && event.value < border) {
                _this.setVisibleLayer(0, 500);
            }
            else if (_this.lastZoom <= border && event.value > border) {
                _this.setVisibleLayer(1, 700);
            }
            _this.lastZoom = event.value;
        };

        this.on("added", function (emitter, event) {
            event.canvas.on("zoom", zoomHandler);
        });

        this.on("removed", function (emitter, event) {
            event.canvas.off("zoom", zoomHandler);
        });

        this.on("dblclick", function(emitter, event) {
            visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(_this.policy);
            $("#inPlaceAALEditor").fadeIn(600);
        });

        this.on("click", function(e) {
            visualEditor.ui.selectedNode = _this;
            visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(_this.policy);
        });

        this.on("mouseenter", function(e) {
            visualEditor.ui.selectedNode = _this;
        });
    },

     getPersistentAttributes: function() {
        var memento = this._super();
        memento.policy = this.policy;
        memento.type = "PolicyUI";
        return memento;
     },

    setPersistentAttributes: function(memento) {
        this._super(memento);
        this.policy = memento.policy;
        return this;
    },

    updatePolicy: function(policy) {
        this.policy = policy;
        this.name = this.getPolicyName();
        this.policyUI.text = this.policy;
        this.nameUI.text = this.name;
        this.refresh();
    },

    refresh: function () {
        this.remove(this.getChildren().get(0));
        this.remove(this.getChildren().get(0));
        this.add(this.policyUI);
        this.add(this.nameUI);
        console.log(this.policyUI.width + " " + this.policyUI.height)
        this.setDimension(this.policyUI.width, this.policyUI.height);
        this.repaint();
    },

    getPolicyName: function() {
        var re = /CLAUSE \w+/;
        var m = re.exec(this.policy);
        if (m !== null) {
            if (m.index === re.lastIndex)
                re.lastIndex++;
            return m[0];
        }
        return "Policy name";
    }
});
/*
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
		// Policy
		this.cmp_data = $('<div title="Policy (Ctrl+Shift+E)" class="btn-components fa fa-file-powerpoint-o fa-2x"></div>');
		this.cmp_data.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
        shortcut.add("Ctrl+Shift+E", this.addElement);
	},

	addElement: function(e, name) {
		var element = new PolicyUI();
        if(name != undefined) element.setName(name);
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

    init:function(attr) {
      this._super(attr);
      // Create any Draw2D figure as decoration for the connection
      this.tlabel = new draw2d.shape.basic.Text({text:"this.typeqssssdddddd5f4s6rgrgg\nfergrzgz", stroke:1});
      // add the new decoration to the connection with a position locator.
      this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
    },

    onMouseEnter: function() {
        visualEditor.ui.selectedNode = this;
    },

    onClick: function() {
        visualEditor.ui.selectedNode = this;
        //visualEditor.ui.properties.updateProps();
    },

    refresh: function() {
		console.log("inside "+this.DEFAULT_bgColor)
        this.setBackgroundColor(this.DEFAULT_bgColor);
        this.repaint();
    }
});
*/