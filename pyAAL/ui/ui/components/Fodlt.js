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

Fodtl_OpUI = function() {
	return {
        NAME: "Fodtl_OpUI",
        type : "Fodtl_OpUI",
        tlabel : null,
        outlineIcon : "outlineIcons-data fa fa-database",
        name : "",
        BG_COLOR : "#000000",
        width: 80,
        height: 30,
        resizeable: false,
        label_editable: false,
        _type : "",

        init : function(args) {
            this._super();
            var _this = this;
            if(args != undefined) {
                if (args.color != undefined) this.BG_COLOR = args.color;
                if (args.label_editable != undefined) this.label_editable = args.label_editable;
                if (args.size != undefined) {
                    this.width = args.size.width;
                    this.height = args.size.height;
                }
                if (args.name != undefined) this.name = args.name;
                if (args._type != undefined) this._type = args._type;
            }


            this.setBackgroundColor(this.BG_COLOR);
            this.tlabel = new draw2d.shape.basic.Label({
                text: _this.name,
                color:"#0d0d0d",
                fontColor: "#ffffff",
                fontSize: '15px',
                bold: true,
                stroke:0
            });

            if(this.label_editable) {
                //this.tlabel.installEditor(new draw2d.ui.LabelInplaceEditor());
            } else {
                this.installEditPolicy(new draw2d.policy.figure.AntSelectionFeedbackPolicy());
            }

            this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
        },

        getPersistentAttributes : function() {
            var memento = this._super();
            // add all decorations to the memento
            memento.tlabeltxt = this.tlabel.text;
            memento.label_editable = this.label_editable;
            memento._type = this._type;
            return memento;
        },

        setPersistentAttributes : function(memento) {
            this._super(memento);
            // remove all decorations created in the constructor of this element
            this.resetChildren();
            this.label_editable = memento.label_editable;

            this.tlabel = new draw2d.shape.basic.Label({
                text:memento.tlabeltxt,
                color:"#0d0d0d",
                fontColor: "#ffffff",
                fontSize: '15px',
                bold: true,
                stroke:0
            });
            if(this.label_editable) {
                this.tlabel.installEditor(new draw2d.ui.LabelInplaceEditor());
            } else {
                this.installEditPolicy(new draw2d.policy.figure.AntSelectionFeedbackPolicy());
            }
            this._type = memento._type;

            // add the new decoration to the connection with a position locator.
            this.add(this.tlabel, new draw2d.layout.locator.CenterLocator(this));
        },

        createPort: function(type, locator){
            var newPort = null;
            var count =0;

            switch(type){
            case "input":
                newPort= draw2d.Configuration.factory.createInputPort(this);
                count = this.inputPorts.getSize();
                break;
            case "output":
                newPort= draw2d.Configuration.factory.createOutputPort(this);
                count = this.outputPorts.getSize();
                // On connect
                newPort.on("connect", function(emitterPort, connection){
                    console.log( connection);
                    console.log(emitterPort)
                });

                break;
            case "hybrid":
                newPort= draw2d.Configuration.factory.createHybridPort(this);
                count = this.hybridPorts.getSize();
                break;
            default:
                throw "Unknown type ["+type+"] of port requested";
            }

            newPort.setName(type+count);

            this.addPort(newPort, locator);
            // relayout the ports
            this.setDimension(this.width,this.height);

            this.layoutPorts();

            return newPort;
        }
    }
};


Fodtl_rectOpUI = draw2d.shape.basic.Rectangle.extend(
    jQuery.extend(Fodtl_OpUI(),
    {
        NAME: "Fodtl_rectOpUI",
        type: "Fodtl_rectOpUI"
    })
);


Fodtl_circleOpUI = draw2d.shape.basic.Circle.extend(
	jQuery.extend(Fodtl_OpUI(),
    {
        NAME: "Fodtl_circleOpUI",
        type: "Fodtl_circleOpUI"
    })
);

Fodtl_diamondOpUI = draw2d.shape.basic.Diamond.extend(
	jQuery.extend(Fodtl_OpUI(),
    {
        NAME: "Fodtl_diamondOpUI",
        type: "Fodtl_diamondOpUI"
    })
);

/***************************************
 * Atom in operators model
 **************************************/
Fodtl_atomOp = Class.extend({
	NAME      : "Fodtl_atomOp",
	uiElement : null,
    parent    : null,
    name      : "",
    color     : "#000000",
    figure    : Fodtl_rectOpUI,
    size      : {width: 80, height: 80},
    label_editable : false,
    _type : '',

	init: function() {
        this.parent = visualEditor.ui.components;
		this.uiElement = this.figure.prototype.NAME;
        this._type = this.NAME;
	},

	view: function(_this) {
        this.cmp_data = $('<div title="'+this.name+'" class="btn-components"><p style="font-size: 15px">'+this.name+'</p></div>');
		var args = {
            name: this.name,
            figure: this.figure,
            color: _this.color,
            size: _this.size,
            label_editable: _this.label_editable,
            _type: _this._type
        };
        this.cmp_data.click(args, this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
	},

	addElement: function(event) {
    	var element = new event.data.figure(event.data);
        element.createPort("input", this.leftLocator);
        visualEditor.ui.canvas.add(element, 100, 100);
	}
});

/***************************************
 * Atom out operators model
 **************************************/
Fodtl_atom2Op = Fodtl_atomOp.extend({
	NAME      : "Fodtl_atom2Op",

	addElement: function(event) {
    	var element = new event.data.figure(event.data);
        element.createPort("output", this.leftLocator);
        visualEditor.ui.canvas.add(element, 100, 100);
	}
});

/***************************************
 * Unary operators model
 **************************************/
Fodtl_unaryOp = Fodtl_atomOp.extend({
	NAME      : "Fodtl_unaryOp",
	//uiElement : null,
    //parent    : null,
    //name      : "",
    //color     : "#000000",
    //figure    : Fodtl_rectOpUI,
    //size      : {width: 80, height: 80},

	addElement: function(event) {
    	var element = new event.data.figure(event.data);
        element.createPort("input", this.leftLocator);
        element.createPort("output", this.leftLocator);
        visualEditor.ui.canvas.add(element, 100, 100);
	}
});



/***************************************
 * Binary operators model
 **************************************/
Fodtl_binaryOp = Fodtl_unaryOp.extend({
	NAME      : "Fodtl_binaryOp",
	//uiElement : null,
    //parent    : null,
    //name      : "",
    //color     : "#000000",
    //figure    : Fodtl_rectOpUI,
    //size      : {width: 80, height: 80},

	addElement: function(event) {
    	var element = new event.data.figure(event.data);
        element.createPort("input", this.leftLocator);
        element.createPort("output", this.leftLocator);
        element.createPort("output", this.leftLocator);
        visualEditor.ui.canvas.add(element, 100, 100);
	}
});


/***************************************
 * Fodtl operators
 **************************************/
Fodtl_formula = Fodtl_atom2Op.extend({NAME: "fodtl_formula", name: "Formula", figure: Fodtl_rectOpUI, color: "#3B3B3B", size: {width: 85, height: 40}});

// Predicates and constants
Fodtl_true  = Fodtl_atomOp.extend({NAME: "fodtl_true", name: "True", figure: Fodtl_rectOpUI, color: "#F0BC00", size: {width: 80, height: 30} });
Fodtl_false = Fodtl_atomOp.extend({NAME: "fodtl_false", name: "False", figure: Fodtl_rectOpUI, color: "#F0BC00", size: {width: 80, height: 30}});
Fodtl_constant = Fodtl_unaryOp.extend({NAME: "fodtl_constant", name: "Constant", figure: Fodtl_circleOpUI, color: "#F0BC00", size: {width: 80, height: 40}});
Fodtl_variable = Fodtl_unaryOp.extend({NAME: "fodtl_variable", name: "Variable", figure: Fodtl_circleOpUI, color: "#F0BC00", size: {width: 80, height: 40}});
Fodtl_regexp = Fodtl_unaryOp.extend({NAME: "fodtl_regexp", name: "Regexp", figure: Fodtl_circleOpUI, color: "#F0BC00", size: {width: 80, height: 40}});
Fodtl_predicate = Fodtl_unaryOp.extend({NAME: "fodtl_predicate", name: "Predicate", figure: Fodtl_rectOpUI, color: "#F0BC00", size: {width: 80, height: 40}});
Fodtl_value = Fodtl_atomOp.extend({NAME: "fodtl_value", name: "Value", figure: Fodtl_rectOpUI, color: "#F0BC00", size: {width: 80, height: 30}, label_editable: true});

// Boolean operators
Fodtl_and   = Fodtl_binaryOp.extend({NAME: "fodtl_and", name: "And", figure: Fodtl_rectOpUI, color: "#25BB1E", size: {width: 60, height: 60}});
Fodtl_or    = Fodtl_binaryOp.extend({NAME: "fodtl_or", name: "Or", figure: Fodtl_rectOpUI, color: "#25BB1E", size: {width: 60, height: 60}});
Fodtl_imply = Fodtl_binaryOp.extend({NAME: "fodtl_imply", name: "Imply", figure: Fodtl_rectOpUI, color: "#25BB1E", size: {width: 60, height: 60}});
Fodtl_not   = Fodtl_unaryOp.extend({NAME: "fodtl_not", name: "Not", figure: Fodtl_diamondOpUI, color: "#25BB1E", size: {width: 80, height: 80}});

// Temporal operators
Fodtl_always  = Fodtl_unaryOp.extend({NAME: "fodtl_always",  name: "Always", figure: Fodtl_circleOpUI, color: "#0058F0", size: {width: 65, height: 65}});
Fodtl_future  = Fodtl_unaryOp.extend({NAME: "fodtl_future",  name: "Future", figure: Fodtl_circleOpUI, color: "#0058F0", size: {width: 65, height: 65}});
Fodtl_next    = Fodtl_unaryOp.extend({NAME: "fodtl_next",    name: "Next", figure: Fodtl_circleOpUI, color: "#0058F0", size: {width: 60, height: 60}});
Fodtl_until   = Fodtl_binaryOp.extend({NAME: "fodtl_until",  name: "Until", figure: Fodtl_rectOpUI, color: "#0058F0", size: {width: 70, height: 70}});
Fodtl_release = Fodtl_binaryOp.extend({NAME: "fodtl_release",  name: "Release", figure: Fodtl_rectOpUI, color: "#0058F0", size: {width: 70, height: 70}});

// Quantifiers
Fodtl_forall  = Fodtl_unaryOp.extend({NAME: "fodtl_forall",  name: "Forall", figure: Fodtl_circleOpUI, color: "#941EBB", size: {width: 60, height: 60}});
Fodtl_exists  = Fodtl_unaryOp.extend({NAME: "fodtl_exists",  name: "Exists", figure: Fodtl_circleOpUI, color: "#941EBB", size: {width: 60, height: 60}});

// Distributed operators
Fodtl_at = Fodtl_unaryOp.extend({NAME: "fodtl_at",    name: "At", figure: Fodtl_circleOpUI, color: "#AD6217", size: {width: 60, height: 60}});



/**
 * Convert VFodtl diagram to Fodtl formula
 */
visualEditor.vFodtl_to_fodtl = function(diag) {
    var dic = {fodtl_always: "G", fodtl_future: "F", fodtl_next: "X", fodtl_until: "U", fodtl_release: "R",
                fodtl_and: "&", fodtl_or: "|", fodtl_imply: "=>", fodtl_not: "~", fodtl_forall: "!",
                fodtl_exists: "?", fodtl_at:"@", fodtl_true:"ture", fodtl_false: "false"};


    // Internal eval fx
    var _eval = function(node) {
        var port = null;
        switch (node._type) {
            case "fodtl_formula":
                port = node.outputPorts.get(0);
                if (port.connections.getSize() > 0)
                    return  _eval(port.connections.get(0).targetPort.parent);
                else
                    return "Error";
                break;

            // Unary operators
            case "fodtl_always": case "fodtl_future": case "fodtl_next": case "fodtl_not":
                port = node.outputPorts.get(0);
                if (port.connections.getSize() > 0)
                    return dic[node._type] + "(" + _eval(port.connections.get(0).targetPort.parent) + ")";
                else
                    return dic[node._type] + "( Error )";
                break;

            // Binary operators
            case "fodtl_and": case "fodtl_or": case "fodtl_imply": case "fodtl_until": case "fodtl_release":
                port1 = node.outputPorts.get(0);
                port2 = node.outputPorts.get(1);
                if (port1.connections.getSize() > 0 && port2.connections.getSize() > 0)
                    return _eval(port1.connections.get(0).targetPort.parent) + " " + dic[node._type] + " " +
                        _eval(port2.connections.get(0).targetPort.parent);
                else
                    return dic[node._type] + "( Error )";
                break;

            // Constant
            case "fodtl_constant":
                port = node.outputPorts.get(0);
                if (port.connections.getSize() > 0)
                    return "'" + _eval(port.connections.get(0).targetPort.parent) + "'";
                else
                    return dic[node._type] + "( Error )";
                break;

            // Variable
            case "fodtl_variable":
                port = node.outputPorts.get(0);
                if (port.connections.getSize() > 0)
                    return _eval(port.connections.get(0).targetPort.parent);
                else
                    return dic[node._type] + "( Error )";
                break;

            // Regexp
            case "fodtl_regexp":
                port = node.outputPorts.get(0);
                if (port.connections.getSize() > 0)
                    return 'r\"' + _eval(port.connections.get(0).targetPort.parent) + '\"';
                else
                    return dic[node._type] + "( Error )";
                break;

            // Value
            case "fodtl_value":
                return node.tlabel.text;
                break;

            // True / False
            case "fodtl_true": case "fodtl_false":
                return dic[node._type];
                break;

            // Predicate
            case "fodtl_predicate":
                port = node.outputPorts.get(0);
                if (port.connections.getSize() > 0)
                    return  _eval(port.connections.get(0).targetPort.parent);
                else
                    return dic[node._type] + "( Error )";
                break;
        }
    };

    var figs = visualEditor.ui.canvas.getFigures();
    for(var i=0; i<figs.getSize(); i++) {
        var tmp = figs.get(i);
        // Handle formulas only
        if(tmp._type === "fodtl_formula") {
            var res = _eval(tmp);
            console.log(res);
        }
    }
};



