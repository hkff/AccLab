//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : Actor.js
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

actor = Class.extend({
    NAME     : "actor",
    name      : null,
    uiElement : null,
    parent    : null,
    id        : 0,

    /**
     * Constructor
     */
    init: function() {
    	this.parent = visualEditor.ui.components;
        this.uiElement = "ActorUI";
    },

    addElement: function() {
        var leftLocator  = new draw2d.layout.locator.InputPortLocator();
        var rightLocator = new draw2d.layout.locator.OutputPortLocator();

        var element = new ActorUI();
       /* element.createPort("ps", this.leftLocator);
        element.createPort("rs", this.rightLocator);
        element.createPort("ps", this.leftLocator);
        element.createPort("rs", this.rightLocator);*/
        visualEditor.ui.canvas.add(element, 100, 100);
    }
});


draw2d.shape.basic.Label2 = draw2d.shape.basic.Label.extend({

    onMouseDown: function() {
        visualEditor.ui.selectedNode = this.parent;
        $(visualEditor.ui).trigger('nodeSelected');
    },

    onMouseEnter: function() {
        //visualEditor.ui.selectedNode = this.parent;
    },

    onClick: function() {
        visualEditor.ui.selectedNode = this.parent;
        $(visualEditor.ui).trigger('nodeSelected');
    }
});

//////////////////////////////////////////////////////////
//
//  ActorUI Class
//
//////////////////////////////////////////////////////////
ActorUI = //draw2d.shape.node.Hub.extend({
draw2d.shape.basic.Rectangle.extend({
	NAME   : "ActorUI",
	tlabel : null,
	type   : "actor",
    policy  : "",
    leftLocator  : new draw2d.layout.locator.InputPortLocator(),
    rightLocator : new draw2d.layout.locator.OutputPortLocator(),
    pservices : new draw2d.util.ArrayList(),
    rservices : new draw2d.util.ArrayList(),
    types     : new draw2d.util.ArrayList(),
    DEFAULT_bgColor : "#0d0d0d",
    DEFAULT_rsColor : "#0d0d0d",
    DEFAULT_psColor : "#0d0d0d",
    DEFAULT_labelColor : "#0d0d0d",
    outlineIcon : "outlineIcons-agent fa fa-user",

	/**
	 * init
	 */
    init: function(attr) {
        this._super(attr);
        // Create any Draw2D figure as decoration for the connection
        this.tlabel = new draw2d.shape.basic.Label2({
            text:this.type.toLowerCase(), 
            color:"#0d0d0d", 
            fontColor: this.DEFAULT_labelColor, 
            stroke:0
        });

        this.leftLocator  = new draw2d.layout.locator.InputPortLocator();
        this.rightLocator = new draw2d.layout.locator.OutputPortLocator();
        this.pservices    = new draw2d.util.ArrayList();
        this.rservices    = new draw2d.util.ArrayList();
        this.types        = new draw2d.util.ArrayList();
        
        // add the new decoration to the connection with a position locator.
        this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
        this.id = visualEditor.guid();
    },


    /**
     * Return an objects with all important attributes for XML or JSON serialization
     * @returns {Object}
     */
    getPersistentAttributes : function() {
        var memento = this._super();
        // add all decorations to the memento
        memento.tlabeltxt          = this.tlabel.text;
        memento.policy             = this.policy;
        memento.pservices          = this.pservices;
        memento.rservices          = this.rservices;
        memento.types              = this.types;
        memento.DEFAULT_bgColor    = this.DEFAULT_bgColor;
        memento.DEFAULT_rsColor    = this.DEFAULT_rsColor;
        memento.DEFAULT_psColor    = this.DEFAULT_psColor;
        memento.DEFAULT_labelColor = this.DEFAULT_labelColor;

        return memento;
    },

    /**
     * Read all attributes from the serialized properties and transfer them into the shape.
     * @param {Object} memento
     * @returns 
     */
    setPersistentAttributes : function(memento) {
        this._super(memento);
        
        // remove all decorations created in the constructor of this element
        //
        this.resetChildren();
        
        this.policy             = memento.policy;
        this.pservices          = this.toArrayList(memento.pservices);
        this.rservices          = this.toArrayList(memento.rservices);
        this.types              = this.toArrayList(memento.types);
        this.DEFAULT_bgColor    = memento.DEFAULT_bgColor;
        this.DEFAULT_rsColor    = memento.DEFAULT_rsColor;
        this.DEFAULT_psColor    = memento.DEFAULT_psColor;
        this.DEFAULT_labelColor = memento.DEFAULT_labelColor;
        //this.tlabel             = memento.tlabel;

        this.tlabel = new draw2d.shape.basic.Label2({
            text:memento.tlabeltxt, 
            color:"#0d0d0d", 
            fontColor: this.DEFAULT_labelColor, 
            stroke:0
        });
        
        // add the new decoration to the connection with a position locator.
        this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));

        // Restore pservices
        var ip = this.getInputPorts();
        for(var i=0; i< ip.getSize(); i++){
            ip.get(i).updateLabel(memento.pservices.data[i]);
        }

        // Restore pservices
        var op = this.getOutputPorts();
        for(var i=0; i< op.getSize(); i++){
            op.get(i).updateLabel(memento.rservices.data[i]);
        }
    },

    onMouseEnter: function() {
    	//visualEditor.ui.selectedNode = this;
    },

    onClick: function() {
        visualEditor.ui.selectedNode = this;
        $(visualEditor.ui).trigger('nodeSelected');
    },

    onMouseLeave: function (e) {
    },

    onDrop: function(x, y, shiftKey, ctrlKey) {
        this._super(x, y, shiftKey, ctrlKey);
        visualEditor.ui.selectedNode = this;
        $(visualEditor.ui).trigger('nodeSelected');
    },

    onDragEnter: function(draggedFigure) {
        visualEditor.ui.selectedNode = this;
        $(visualEditor.ui).trigger('nodeSelected');
         // redirect the dragEnter handling to the hybrid port
         if(draggedFigure.NAME == "draw2d.PolicyPort")
  		 	return this.getHybridPort(0).onDragEnter(draggedFigure);
  		 else
  		 	return null;
     },

    createPort: function(type, locator, name) {
        var newPort = null;
        var count =0;

    	switch(type){
    	case "input":
    		newPort = new draw2d.InputPort();
    		count = this.inputPorts.getSize();
    		break;
    	case "ps":
    		if(name == undefined) name = "PService";
            newPort = new draw2d.ProvidedPort(new draw2d.layout.locator.LeftLocator(this), name);
            this.pservices.add(name);
    		count = this.inputPorts.getSize();
    		break;
        case "rs":
            if(name == undefined) name = "RService";
            newPort = new draw2d.RequiredPort(new draw2d.layout.locator.RightLocator(this), name);
            this.rservices.add(name);
            count = this.outputPorts.getSize();
            break;
    	case "output":
    		newPort = new draw2d.OutputPort();
            count = this.outputPorts.getSize();
    		break;
        case "hybrid":
            newPort = new draw2d.HybridPort();
            count = this.hybridPorts.getSize();
            break;
    	default:
            throw "Unknown type ["+type+"] of port requested";
    	}

    	// relayout the ports
        this.addPort(newPort, locator);
    	this.setDimension(this.width,this.height);
        this.layoutPorts();

        return newPort;
    },

    
    toArrayList: function(list) {
        var l = new draw2d.util.ArrayList();
        list.data.forEach(function(e){
            l.push(e);
        });
        return l;
    },

    getName: function() {
        return this.tlabel.text;
    },

    getPolicy: function() {
        return this.policy;
    },

    /**
     * Generate the AAL declaration
     * @returns {string}
     */
    getAALDeclaration: function() {
        var dec = this.type.toUpperCase()+" "+this.getName();
        var lng = this.types.getSize();
        var i = 0;
        dec += " TYPES("
        for (i = 0; i < lng; i++) {
            dec += this.types.get(i)+" ";
        }
        dec += ")";

        lng = this.rservices.getSize();
        dec += " REQUIRED("
        for (i = 0; i < lng; i++) {
            dec += this.rservices.get(i)+" ";
        }
        dec += ")";

        lng = this.pservices.getSize();
        dec += " PROVIDED("
        for (i = 0; i < lng; i++) {
            dec += this.pservices.get(i)+" ";
        }
        dec += ")";

        return dec;
    },

    /**
     * 
     *
     */
    getRservices: function() {
        return this.rservices;
        // TODO : remove
        res = [];
        this.getOutputPorts().data.forEach(function(e){
            if(e.plabel)
                res.push(e.plabel.text);
        });
        return res;
    },

    /**
     * 
     * 
     */
    getPservices: function() {
        return this.pservices;
        // TODO : remove
        res = [];
        this.getInputPorts().data.forEach(function(e){
            if(e.plabel)
                res.push(e.plabel.text);
        });
        return res;
    },

    /**
     * 
     * 
     */
    getTypes: function() {
        return this.types;
    },

    /**
     * 
     * Add provided service in leftLocator
     */
    addPservice: function(name) {
        this.createPort("ps", this.leftLocator, name);
    },

    /**
     * 
     * Add required service in rightLocator
     */
    addRservice: function(name) {
        this.createPort("rs", this.rightLocator, name);
    },


    /**
     * 
     * Add a type
     */
    addType: function(name) {
        this.types.add(name);
    },

    /**
     * 
     * Remove the required service "name"
     */
    removeRservice: function(name) {
        this.getOutputPorts().data.forEach(function(e){
            if(e.plabel && e.plabel.text == name){
                e.parent.removePort(e);
                e.parent.inputPorts.remove(e);
                e.parent.outputPorts.remove(e);
                e.parent.hybridPorts.remove(e);
                e.parent.rservices.remove(name);
                e.parent.repaint();
            }
        });
    },

    /**
     * 
     * Remove the provided service "name"
     */
    removePservice: function(name) {
        this.getInputPorts().data.forEach(function(e){
            if(e.plabel && e.plabel.text == name){
                e.parent.removePort(e);
                e.parent.inputPorts.remove(e);
                e.parent.outputPorts.remove(e);
                e.parent.hybridPorts.remove(e);
                e.parent.pservices.remove(name);
                e.parent.repaint();
            }
        });
    },

    /**
     * 
     * Remove the type "name"
     */
    removeType: function(name) {
        this.types.remove(name);
    },

    updatePservices: function(newServices) {
        this.updateServices(newServices, this.pservices, this.addPservice, this.removePservice);
    },

    updateRservices: function(newServices) {
        this.updateServices(newServices, this.rservices, this.addRservice, this.removeRservice);
    },

    updateTypes: function(newTypes) {
        this.updateServices(newTypes, this.types, this.addType, this.removeType);
    },

    updateName: function(name) {
        this.tlabel.text = name;
        this.tlabel.repaint();
        this.repaint();
        $(visualEditor.ui).trigger('nodeUpdated');
    },

    /**
     * 
     */
    updateServices: function(newServices, services, addFunction, removeFunction) {
        var cmd = newServices.getSize() - services.getSize();
        
        // Positions swap
        if(cmd ==  0){
            // Clear all services
            for (var i = 0; i < newServices.getSize(); i++) {
                removeFunction.call(this, newServices.get(i));
            }

            // Add new services list
            for (var i = 0; i < newServices.getSize(); i++) {
                addFunction.call(this, newServices.get(i));
            }
        }else 
        if(cmd == 1){
            // Add new service
            for (var i = 0; i < newServices.getSize(); i++) {
                e = newServices.get(i);
                if(!services.contains(e)){
                    addFunction.call(this, e);
                    i = newServices.getSize();
                }
            }
        }else{
            // Remove a service
            for (var i = 0; i < services.getSize(); i++) {
                e = services.get(i);
                if(!newServices.contains(e)){
                    removeFunction.call(this, e);
                }
            }
        }


        $(visualEditor.ui).trigger('nodeUpdated');

    },

    /**
     * TODO : Need to be optimized
     */
    refresh: function() {
        this.setBackgroundColor(this.DEFAULT_bgColor);
        this.getOutputPorts().data.forEach(function(e){ e.setBackgroundColor(e.parent.DEFAULT_rsColor); });
        this.getInputPorts().data.forEach(function(e){ e.setBackgroundColor(e.parent.DEFAULT_psColor); });

        this.tlabel.setFontColor(this.DEFAULT_labelColor);
        this.tlabel.repaint();
        this.repaint();

        $(visualEditor.ui).trigger('nodeUpdated');
    },


    /**
     * return a tree in JSON format of the actor
     * @return{Object}
     */
    toJSONtree: function() {

        var json = '{"id":"'+ this.id +'", "text":"'+this.tlabel.text+'", "iconCls":"'+this.outlineIcon+'", "type":"'+this.type+'",';
        json += '"children":[';

        // Add required services
        json += '{"id":"'+ this.tlabel.text+'-rs' +'", "text":"'+'Required'+'", "iconCls":"'+"outlineIcons-rs fa fa-chevron-down" +'",';
        json += '"children":[';        
        var oupt = this.getOutputPorts().data;
        oupt.forEach(function(e) { json += e.toJSONtree()+',';});
        if(oupt.length > 0) 
            json = json.substring(0,json.length-1);
        json += ']},';

        // Add provided services
        json += '{"id":"'+ this.tlabel.text+'-ps' +'", "text":"'+'Provided'+'", "iconCls":"'+"outlineIcons-ps fa fa-circle" +'",';
        json += '"children":[';
        var oupt = this.getInputPorts().data;
        
        oupt.forEach(function(e) { json += e.toJSONtree()+',';});
        if(oupt.length > 0) 
            json = json.substring(0,json.length-1);

        json += ']}';

        json += ']}'
        return json;
    },


    /**
     * @inheritdoc
     *
     */
    setRotationAngle: function(angle) {
        this._super(angle);
        // Rotate children
        this.getOutputPorts().data.forEach(function(e){ e.setRotationAngle(angle); });
        this.getInputPorts().data.forEach(function(e){ e.setRotationAngle(angle); });
    }

});