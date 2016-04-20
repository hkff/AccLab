//////////////////////////////////////////////////////////
//
//  AccLab UI : Actor.js
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

Actor = Class.extend({
	NAME : "actor",
    uiElement : null,
    leftLocator  : new draw2d.layout.locator.InputPortLocator(),
    rightLocator : new draw2d.layout.locator.OutputPortLocator(),

	init: function() {
		this.parent = visualEditor.ui.components;
        this.uiElement = "ActorUI2";
	},

	view: function() {
		// Agent
		this.cmp_data = $('<div title="Actor (Ctrl+Shift+E)" class="btn-components fa fa-user fa-2x"></div>');
		this.cmp_data.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
        shortcut.add("Ctrl+Shift+E", this.addElement);
	},

	addElement: function(e, name) {
		var element = new ActorUI2();
        if(name != undefined) element.setName(name);
		visualEditor.ui.canvas.add(element, 100, 100);
        return element;
	}
});


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


ActorUI2 = draw2d.shape.layout.VerticalLayout.extend({
    NAME: "ActorUI2",
    type: "Actor",
    policy: "",
    types: new draw2d.util.ArrayList(),
    PSO: new draw2d.util.ArrayList(),
    RSO: new draw2d.util.ArrayList(),
    classLabel: null,
    inputLocator: null,
    outputLocator: null,
    header: null,
    toggler: null,
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
            text: "ActorName",
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
                        case "newRS": setTimeout(function() { _table.addEntity("ServiceName", "RS").onDoubleClick(); }, 10);
                            break;
                        case "newPS": setTimeout(function() {_table.addEntity("ServiceName", "PS").onDoubleClick(); }, 10);
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
        this.toggler = new draw2d.shape.basic.Label({ text:"X", padding:{right:10} });
        var toggle = function() {
            this.RSO.data.forEach(function(e){ e.portRelayoutRequired = true; });
            this.PSO.data.forEach(function(e){ e.portRelayoutRequired = true; });
            this.RSO.data.forEach(function(e){ e.setVisible(!e.isVisible()); });
            this.PSO.data.forEach(function(e){ e.setVisible(!e.isVisible()); });
            this.RSO.data.forEach(function(e){ e.portRelayoutRequired = true; e.layoutPorts();});
            this.PSO.data.forEach(function(e){ e.portRelayoutRequired = true; e.layoutPorts();});
        }.bind(this);

        this.toggler.on("click", toggle);
        this.toggler.addCssClass("pointer");
        this.header.add(this.toggler);
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
                    case "newRS": setTimeout(function(){ _table.addEntity("ServiceName", "RS").onDoubleClick(); },10);
                        break;
                    case "newPS": setTimeout(function(){ _table.addEntity("ServiceName", "PS").onDoubleClick(); },10);
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
        memento.ports = [];
        memento.name = this.classLabel.getText();
        memento.entities   = [];
        this.children.each(function(i,e) {
            if(i > 0) { // skip the header of the figure
                memento.entities.push({
                    text: e.figure.getText(),
                    id: e.figure.id,
                    userData: {
                        "type": e.figure.userData,
                        "RSPortID": (e.figure.getOutputPorts().getSize() > 0)? e.figure.getOutputPort(0).id:"",
                        "PSPortID": (e.figure.getInputPorts().getSize() > 0)? e.figure.getInputPort(0).id:""
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
        this.policy             = memento.policy;
        //var PSO                 = memento.PSO;
        //var RSO                 = memento.RSO;
        this.types              = this.toArrayList(memento.types);
        this.DEFAULT_bgColor    = memento.DEFAULT_bgColor;
        this.DEFAULT_rsColor    = memento.DEFAULT_rsColor;
        this.DEFAULT_psColor    = memento.DEFAULT_psColor;
        this.DEFAULT_labelColor = memento.DEFAULT_labelColor;
        this.setName(memento.name);
        this.ports = [];

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
                    entity.getOutputPort(0).setId(e.userData.RSPortID);
                }
            }, this));
        }
        this._super(memento);
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
        var dec = "AGENT "+this.getName();
        var lng = this.types.getSize();
        var i;
        dec += " TYPES(";
        for (i = 0; i < lng; i++) {
            dec += this.types.get(i)+" ";
        }
        dec += ")";

        lng = this.RSO.getSize();
        dec += " REQUIRED(";
        for (i = 0; i < lng; i++) {
            dec += this.RSO.get(i).text+" ";
        }
        dec += ")";

        lng = this.PSO.getSize();
        dec += " PROVIDED(";
        for (i = 0; i < lng; i++) {
            dec += this.PSO.get(i).text+" ";
        }
        dec += ")";

        return dec;
    },

    /**
     * return a tree in JSON format of the actor
     * @return{Object}
     */
    toJSONtree: function() {
        var json = '{"id":"'+ this.id +'", "text":"'+this.getName()+'", "iconCls":"'+this.outlineIcon+'", "type":"'+this.type+'",';
        json += '"children":[';

        // Add required services
        json += '{"id":"'+ this.getName()+'-rs", "text":"Required", "iconCls":"outlineIcons-rs fa fa-chevron-down",';
        json += '"children":[';
        var oupt = this.getRservices();
        oupt.forEach(function(e) {
            json += '{"id":"'+'rs-'+e+'","text":"'+e+'","iconCls":"outlineIcons-rs-s fa fa-cog","type":"OutputPort" },';
        });
        if(oupt.length > 0)
            json = json.substring(0,json.length-1);
        json += ']},';

        // Add provided services
        json += '{"id":"'+ this.getName()+'-ps", "text":"Provided", "iconCls":"outlineIcons-ps fa fa-circle",';
        json += '"children":[';
        var inpt = this.getPservices();
        inpt.forEach(function(e) {
            json += '{"id":"'+'ps-'+e+'","text":"'+e+'"'+ ',"iconCls":"outlineIcons-ps-s fa fa-cog ","type":"OutputPort" },';
        });
        if(inpt.length > 0)
            json = json.substring(0,json.length-1);

        json += ']}';
        json += ']}';
        return json;
    }
});
