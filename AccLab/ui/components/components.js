//////////////////////////////////////////////////////////
//
//  AccDesigner V 0.2
//
//////////////////////////////////////////////////////////
visualEditor.ui.components = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	components      : [],

	/**
	 * @method
	 * init function
	 *
	 **/
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel) {
		
		// Get view elements
		this.grid            = $('#'+ grid);
		this.actionsPanel    = $('#'+ actionsPanel);
		this.componentsPanel = $('#'+ componentsPanel);
		this.propertiesPanel = $('#'+ propertiesPanel);

		this.componentsRegistrator();

		// Load components
		this.components.forEach(function(e){
			e.view();
		});
	},

	/**
	 * Register components
	 */
	componentsRegistrator: function() {
		this.components.push(new agent());
		this.components.push(new data());
		this.components.push(new policy());

		//this.components[0].addElement();
		//this.components[1].addElement();
		//this.components[2].addElement();
	},

};