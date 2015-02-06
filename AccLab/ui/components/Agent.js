//////////////////////////////////////////////////////////
//
//  Agent
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
	},
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
     * @method
     * Generate the AAL declaration
     */
    getAALDeclaration: function() {
        return this._super();
    },

});