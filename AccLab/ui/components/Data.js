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
		this.cmp_data = $('<div class="btn-components fa fa-database fa-2x"></div>')
		this.cmp_data.click(this.addElement);
		this.parent.componentsPanel.append(this.cmp_data);
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
	},
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
     * @method
     * Generate the AAL declaration
     */
    getAALDeclaration: function() {
        return this._super();
    },
});