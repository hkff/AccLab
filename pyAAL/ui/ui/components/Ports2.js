//////////////////////////////////////////////////////////
//
//  AccLab UI BETA V 1.0 : Ports2.js
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

draw2d.RequiredPort = draw2d.OutputPort.extend({
    NAME : "draw2d.RequiredPort",
    plabel : null,
    plabelLocator : null,
    plabeltxt : null,
    /**
     * @constructor
     * Create a new OutputPort element
     */
    /*init: function(attr) {
        this.init(attr, "RService");
        console.log("init1")
    },*/
    init: function(attr, name) {
        this._super(attr);

        this.setName(name);

        this.setPersistPorts(true);

        // responsive for the arrangement of the port 
        // calculates the x/y coordinates in relation to the parent node
        this.locator = new draw2d.layout.locator.OutputPortLocator();
        
        if(attr != undefined)
          this.plabelLocator = attr;
        else
          this.plabelLocator = new draw2d.layout.locator.RightLocator();

/*
        if(fname != undefined) 
          this.plabeltxt = fname;
        else 
            this.plabeltxt = this.name;
*/
        this.plabel = new draw2d.shape.basic.Label({text:name, color:"#0d0d0d", fontColor:"#0d0d0d", stroke:0});
        // add the new decoration to the connection with a position locator.
        this.add(this.plabel, this.plabelLocator);
        //this.plabel.installEditor(new draw2d.ui.LabelInplaceEditor());

        //this.decoration = new MarkerFigure();
        //this.add(this.decoration, new draw2d.layout.locator.RightLocator(/*{margin:8}*/));
    },

    /**
     * @inheritdoc
     * 
     */
    onDragLeave: function(figure) {
      // Ports accepts only InputPorts as DropTarget
      //
      if(figure instanceof draw2d.InputPort){
        this._super( figure);
      }
      else if(figure instanceof draw2d.HybridPort){
        this._super( figure);
      }
    },

    /**
     *
     */
    toJSONtree: function() {

        var json = '{"id":"'+'rs-'+this.plabel.text+'","text":"'+this.plabel.text+'"'+ ',"iconCls":"'+'outlineIcons-rs-s fa fa-cog ","type":"OutputPort"';
        json += '}';
        return json;
    },

    /**
     * @inheritdoc
     *
     */
    setRotationAngle: function(angle) {
        this._super(angle);
        this.plabel.setRotationAngle(angle);
    },

    updateLabel: function(name) {
        this.name = name;
        this.plabel.text = this.name;
    }

});



draw2d.ProvidedPort = draw2d.InputPort.extend({
    NAME : "draw2d.ProvidedPort",
	plabel : null,
	plabelLocator : null,

  
    /**
     * @constructor
     */
    init: function(attr, name) {
        this._super(attr);

        this.setPersistPorts(true);
        this.setName(name);

        // responsive for the arrangement of the port 
        // calculates the x/y coordinates in relation to the parent node
        this.locator = new draw2d.layout.locator.InputPortLocator();
		
        if(attr != undefined) 
          this.plabelLocator = attr;
        else
          this.plabelLocator = new draw2d.layout.locator.LeftLocator();

		this.plabel = new draw2d.shape.basic.Label({text:name, color:"#0d0d0d", fontColor:"#0d0d0d", stroke:0});
      	// add the new decoration to the connection with a position locator.
      	this.add(this.plabel, this.plabelLocator);
      	//this.plabel.installEditor(new draw2d.ui.LabelInplaceEditor());

        //this.decoration = new MarkerFigure();
        //this.add(this.decoration, new draw2d.layout.locator.LeftLocator(/*{margin:8}*/));
    },

    /**
     *
     */
    toJSONtree: function() {

        var json = '{"id":"'+'ps-'+this.plabel.text+'","text":"'+this.plabel.text+'"'+ ',"iconCls":"'+'outlineIcons-ps-s fa fa-cog ","type":"OutputPort"';
        json += '}';
        return json;
    },

    /**
     * @inheritdoc
     *
     */
    setRotationAngle: function(angle) {
        this._super(angle);
        this.plabel.setRotationAngle(angle);
    },

    updateLabel: function(name) {
        this.name = name;
        this.plabel.text = this.name;
    }
});


draw2d.PolicyPort = draw2d.HybridPort.extend({
    NAME : "draw2d.PolicyPort",
    plabel : null,
    plabelLocator : null,

    /**
     * @constructor
     * Create a new OutputPort element
     */
    init: function(attr) {
        this.init(attr, "Policy");
    },

    init : function(attr, name) {
        this._super(attr);
        this.plabelLocator = attr;
        console.log(this.plabelLocator)
        // responsive for the arrangement of the port 
        // calculates the x/y coordinates in relation to the parent node
        this.locator = new draw2d.layout.locator.OutputPortLocator();
        
        this.plabel = new draw2d.shape.basic.Label({text:name, color:"#0d0d0d", fontColor:"#0d0d0d", stroke:0});
        // add the new decoration to the connection with a position locator.
        this.add(this.plabel, this.plabelLocator);
        this.plabel.installEditor(new draw2d.ui.LabelInplaceEditor());
    }
});
