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

policy = Class.extend({
	NAME : "policy",
    name : "policy",
    uiElement : null,
    leftLocator  : new draw2d.layout.locator.InputPortLocator(),
    rightLocator : new draw2d.layout.locator.OutputPortLocator(),

	init: function() {
		this.parent = visualEditor.ui.components;
        this.uiElement = "PolicyUI2";
	},

	view: function() {
		// Agent
		this.cmp_data = $('<div title="Policy (Ctrl+Shift+E)" class="btn-components fa fa-file-powerpoint-o fa-2x"></div>');
		this.cmp_data.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
        shortcut.add("Ctrl+Shift+E", this.addElement);
	},

	addElement: function(e, name) {
		var element = new PolicyUI2();
        if(name != undefined) element.setName(name);
		visualEditor.ui.canvas.add(element, 100, 100);
	}
});

/*
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
*/


var CollapsibleLocator =  {
    checkDelegate: function(port) {

        // install delegate if required
        if(port.visible === false && typeof port.__restoreData === "undefined") {
            port.__restoreData =
            {
                getAbsoluteX : port.getAbsoluteX,
                getAbsoluteY : port.getAbsoluteY,
                getConnectionDirection : port.getConnectionDirection
            };

            port.getAbsoluteX = function() {
                if(this.parent===null) {
                    return this.getX();
                }
                return this.getX() + this.parent.parent.getAbsoluteX();
            }.bind(port);

            port.getAbsoluteY = function() {
                if(this.parent===null) {
                    return this.getY();
                }
                return this.getY() + this.parent.parent.getAbsoluteY();
            }.bind(port);

            port.getConnectionDirection=function() {
                return this.parent.parent.getBoundingBox().getDirection(this.getAbsolutePosition());
            };
        }
        else if(port.isVisible()===true && typeof port.__restoreData!=="undefined") {
            port.getAbsoluteX = port.__restoreData.getAbsoluteX;
            port.getAbsoluteY = port.__restoreData.getAbsoluteY;
            port.getConnectionDirection = port.__restoreData.getConnectionDirection;
            delete port.__restoreData;
        }
    }
};

var CollapsibleInputLocator = draw2d.layout.locator.InputPortLocator.extend({

    init: function( ) {
        this._super();
    },

    relocate:function(index, port){
        CollapsibleLocator.checkDelegate(port);
        var node = port.getParent();
        if(!port.visible)
            this.applyConsiderRotation( port, 0, (node.getParent().getHeight()/2));
        else
            this._super(index, port);
    }
});

var CollapsibleOutputLocator = draw2d.layout.locator.OutputPortLocator.extend({

    init: function() {
        this._super();
    },

    relocate:function(index, port) {
        CollapsibleLocator.checkDelegate(port);
        var node = port.getParent();
        if(!port.visible)
            this.applyConsiderRotation( port, node.getParent().getWidth(), (node.getParent().getHeight()/2));
        else
            this._super(index, port);
    }
});


PolicyUI2 = draw2d.shape.layout.VerticalLayout.extend({
    NAME: "PolicyUI2",
    type: "Policy",
    policy: "",
    types: new draw2d.util.ArrayList(),
    PSO: new draw2d.util.ArrayList(),
    RSO: new draw2d.util.ArrayList(),
    classLabel: null,
    inputLocator: null,
    outputLocator: null,
    header: null,
    DEFAULT_bgColor: "#93d7f3",
    DEFAULT_rsColor: "#0d0d0d",
    DEFAULT_psColor: "#0d0d0d",
    DEFAULT_labelColor: "#0d0d0d",
    outlineIcon: "outlineIcons-agent fa fa-user",

    /**
     * Init
     * @param attr
     */
    init : function(attr) {
        this.inputLocator  = new CollapsibleInputLocator();
        this.outputLocator = new CollapsibleOutputLocator();
        this.types = new draw2d.util.ArrayList();
        this.PSO = new draw2d.util.ArrayList();
        this.RSO = new draw2d.util.ArrayList();

        this._super($.extend({bgColor: this.DEFAULT_bgColor, color:"#39b2e5", stroke:1, radius:2, gap:5}, attr));

        this.header = new draw2d.shape.layout.HorizontalLayout({stroke: 0, radius: 0, bgColor: "#1daeef"});

        this.classLabel = new draw2d.shape.basic.Label({
            text: "Actor Name",
            stroke:0,
            fontColor:"#ffffff",
            radius: this.getRadius(),
            resizeable:true,
            fontSize:16,
            fontFamily:"Verdana",
            padding:{left:20, right:20}
        });
        this.classLabel.installEditor(new draw2d.ui.LabelInplaceEditor());

        var _table = this;
        this.classLabel.on("contextmenu", function(emitter, event) {
            $.contextMenu({
                selector: 'body',
                events: {
                    hide: function () { $.contextMenu('destroy'); }
                },
                callback: $.proxy(function (key, options) {
                    switch (key) {
                        case "rename": setTimeout(function() { emitter.onDoubleClick(); }, 10);
                            break;
                        case "newRS": setTimeout(function() { _table.addEntity("_new_", "RS").onDoubleClick(); }, 10);
                            break;
                        case "newPS": setTimeout(function() {_table.addEntity("_new_", "PS").onDoubleClick(); }, 10);
                            break;
                        case "delete": _table.getCanvas().getCommandStack().execute(new draw2d.command.CommandDelete(_table));
                            break;
                        default:
                            break;
                    }
                }, this),
                x: event.x,
                y: event.y,
                items: {
                    "rename": {name: "Rename"},
                    "newPS": {name: "New Provided service"},
                    "newRS": {name: "New Required service"},
                    "sep1": "---------",
                    "delete": {name: "Delete"}
                }
            });
        });

        this.header.add(this.classLabel);

        // Collapsible image
        var img1 = new draw2d.shape.basic.Label({ text:"X", padding:{right:10} });

        var toggle=function() {
            this.RSO.data.forEach(function(e){ e.portRelayoutRequired = true; });
            this.PSO.data.forEach(function(e){ e.portRelayoutRequired = true; });
            this.RSO.data.forEach(function(e){ e.setVisible(!e.isVisible()); });
            this.PSO.data.forEach(function(e){ e.setVisible(!e.isVisible()); });
            this.RSO.data.forEach(function(e){ e.portRelayoutRequired = true; e.layoutPorts();});
            this.PSO.data.forEach(function(e){ e.portRelayoutRequired = true; e.layoutPorts();});
        }.bind(this);

        img1.on("click", toggle);
        img1.addCssClass("pointer");
        this.header.add(img1);
        this.add(this.header);
    },

    /**
     * @method
     * Add an entity to the db shape
     *
     * @param {String} txt the label to show
     * @param {String} kind the type of entity RS/PS
     * @param {Number} [optionalIndex] index where to insert the entity
     */
    addEntity: function(txt, kind, optionalIndex) {
        var label = new draw2d.shape.basic.Label({
            text: txt,
            stroke: 0,
            radius: 0,
            padding: {left:20},
            fontColor: "#303030",
            resizeable: true
        });

        label.installEditor(new draw2d.ui.LabelInplaceEditor());

        if(kind != null && kind != undefined) {
            if(kind === "PS") {
                var input = label.createPort("input", this.inputLocator);
                input.setName(label.id);
                this.PSO.add(label);
                label.userData = "PS";
            }
            else if(kind === "RS") {
                var output = label.createPort("output", this.outputLocator);
                output.setName(label.id);
                this.RSO.add(label);
                label.userData = "RS";
            }
        }

        var _table = this;
        label.on("contextmenu", function(emitter, event) {
            $.contextMenu({
                selector: 'body',
                events: {
                    hide:function(){ $.contextMenu('destroy'); }
                },
                callback: $.proxy(function(key, options)
                {
                    switch(key){
                    case "rename": setTimeout(function(){ emitter.onDoubleClick(); },10);
                        break;
                    case "newRS": setTimeout(function(){ _table.addEntity("_new_", "RS").onDoubleClick(); },10);
                        break;
                    case "newPS": setTimeout(function(){ _table.addEntity("_new_", "PS").onDoubleClick(); },10);
                        break;
                    case "delete": emitter.getCanvas().getCommandStack().execute(new draw2d.command.CommandDelete(emitter));
                        break;
                    default:
                        break;
                    }
                },this),
                x:event.x,
                y:event.y,
                items: {
                    "rename": {name: "Rename"},
                    "newPS":  {name: "New Provided service"},
                    "newRS":  {name: "New Required service"},
                    "sep1":   "---------",
                    "delete": {name: "Delete"}
                }
            });
        });

        if($.isNumeric(optionalIndex))
            this.add(label, null, optionalIndex+1);
        else
            this.add(label);

        return label;
    },

    /**
     * @method
     * Remove the entity with the given index from the DB table shape.<br>
     * This method removes the entity without care of existing connections. Use
     * a draw2d.command.CommandDelete command if you want to delete the connections to this entity too
     *
     * @param {Number} index the index of the entity to remove
     */
    removeEntity: function(index) {
        this.remove(this.children.get(index+1).figure);
    },

    /**
     * @method
     * Returns the entity figure with the given index
     *
     * @param {Number} index the index of the entity to return
     */
    getEntity: function(index) {
        return this.children.get(index+1).figure;
    },

    /**
     * Set/get Name
     * @param name
     * @returns {PolicyUI2}
     */
    setName: function(name) {
         this.classLabel.setText(name);
         return this;
     },

    getName: function() {
        return this.classLabel.text;
    },

     /**
      * @method
      * Return an objects with all important attributes for XML or JSON serialization
      *
      * @returns {Object}
      */
     getPersistentAttributes : function()
     {
        var memento= this._super();
        // add all decorations to the memento
        memento.policy             = this.policy;
        memento.RSO                = this.getPservices();
        memento.PSO                = this.getRservices();
        memento.types              = this.types;
        memento.DEFAULT_bgColor    = this.DEFAULT_bgColor;
        memento.DEFAULT_rsColor    = this.DEFAULT_rsColor;
        memento.DEFAULT_psColor    = this.DEFAULT_psColor;
        memento.DEFAULT_labelColor = this.DEFAULT_labelColor;

        memento.name = this.classLabel.getText();
        memento.entities   = [];
        this.children.each(function(i,e) {
            if(i > 0) { // skip the header of the figure
                console.log(e)
                memento.entities.push({
                    text: e.figure.getText(),
                    id: e.figure.id,
                    userData: {
                        "type": e.figure.userData,
                        "RSPortID": (e.figure.getOutputPort(0) != null)? e.figure.getOutputPorts(0).id:"",
                        "PSPortID": (e.figure.getInputPort(0) != null)? e.figure.getInputPorts(0).id:""
                    }
                });
            }
        });

        return memento;
     },

    /**
     * @method
     * Read all attributes from the serialized properties and transfer them into the shape.
     *
     * @param {Object} memento
     * @return
     */
    setPersistentAttributes : function(memento)
    {
        this._super(memento);
        this.policy             = memento.policy;
        //var PSO                 = memento.PSO;
        //var RSO                 = memento.RSO;
        this.types              = this.toArrayList(memento.types);
        this.DEFAULT_bgColor    = memento.DEFAULT_bgColor;
        this.DEFAULT_rsColor    = memento.DEFAULT_rsColor;
        this.DEFAULT_psColor    = memento.DEFAULT_psColor;
        this.DEFAULT_labelColor = memento.DEFAULT_labelColor;

        this.setName(memento.name);
        if(typeof memento.entities !== "undefined"){
            $.each(memento.entities, $.proxy(function(i,e) {
                var entity = this.addEntity(e.text, e.userData.type);
                entity.id = e.id;
                if(entity.getInputPort(0) != null) {
                    entity.getInputPort(0).setName(e.id);
                    entity.getInputPort(0).setId(e.userData.PSPortID);
                }
                if(entity.getOutputPort(0) != null) {
                    entity.getOutputPort(0).setName(e.id);
                    entity.getOutputPorts(0).setId(e.userData.RSPortID);
                }
            }, this));
        }

         return this;
    },

    toArrayList: function(list) {
        var l = new draw2d.util.ArrayList();
        list.data.forEach(function(e){
            l.push(e);
        });
        return l;
    },

     /**
     * Get required services
     * @returns {*}
     */
    getRservices: function() {
        var res = [];
        this.RSO.data.forEach(function(e){
            res.push(e.text);
        });
        return res;
    },

    /**
     * Get provided services
     * @returns {*}
     */
    getPservices: function() {
        var res = [];
        this.PSO.data.forEach(function(e){
            res.push(e.text);
        });
        return res;
    },

    /**
     * Generate the AAL declaration
     * @returns {string}
     */
    getAALDeclaration: function() {
        var dec = this.type.toUpperCase()+" "+this.getName();
        var lng = this.types.getSize();
        var i;
        dec += " TYPES(";
        for (i = 0; i < lng; i++) {
            dec += this.types.get(i)+" ";
        }
        dec += ")";

        lng = this.rservices.getSize();
        dec += " REQUIRED(";
        for (i = 0; i < lng; i++) {
            dec += this.rservices.get(i).getName()+" ";
        }
        dec += ")";

        lng = this.pservices.getSize();
        dec += " PROVIDED(";
        for (i = 0; i < lng; i++) {
            dec += this.pservices.get(i).getName()+" ";
        }
        dec += ")";

        return dec;
    }
});