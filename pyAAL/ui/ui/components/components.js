//////////////////////////////////////////////////////////
//
//  AccLab UI : components.js
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

visualEditor.ui.components = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	components      : [],

	/**
	 * init function
	 * @param grid
	 * @param actionsPanel
	 * @param componentsPanel
	 * @param propertiesPanel
	 */
	init: function(grid, actionsPanel, componentsPanel, propertiesPanel) {
		
		// Get view elements
		this.grid            = $('#'+ grid);
		this.actionsPanel    = $('#'+ actionsPanel);
		this.componentsPanel = $('#'+ componentsPanel);
		this.propertiesPanel = $('#'+ propertiesPanel);

		this.componentsRegistrator();

		// Load components
		this.components.forEach(function(e){
			e.view(e);
		});
	},

	/**
	 * Register components
	 */
	componentsRegistrator: function() {
		// ACD
		//this.components.push(new agent());
		//this.components.push(new data());
		//this.components.push(new policy());
		this.components.push(new Actor());

		this.components.push(new this.Separator());
        this.components.push(new this.Note());
        this.components.push(new this.Picture());

		// FODTL
		this.components.push(new this.Separator());
		this.components.push(new Fodtl_formula());
        this.components.push(new Fodtl_formula_inline());

		this.components.push(new this.Separator());
		this.components.push(new Fodtl_value());
		this.components.push(new Fodtl_true());
		this.components.push(new Fodtl_false());
		this.components.push(new Fodtl_constant());
		this.components.push(new Fodtl_variable());
		this.components.push(new Fodtl_regexp());
		this.components.push(new Fodtl_predicate());

		this.components.push(new this.Separator());
		this.components.push(new Fodtl_and());
		this.components.push(new Fodtl_or());
		this.components.push(new Fodtl_not());
		this.components.push(new Fodtl_imply());

		this.components.push(new this.Separator());
		this.components.push(new Fodtl_always());
		this.components.push(new Fodtl_future());
		this.components.push(new Fodtl_next());
		this.components.push(new Fodtl_until());
		this.components.push(new Fodtl_release());

		this.components.push(new this.Separator());
		this.components.push(new Fodtl_forall());
		this.components.push(new Fodtl_exists());

		this.components.push(new this.Separator());
		this.components.push(new Fodtl_at());
	},

	/**
	 * Separator component
	 */
	Separator: Class.extend({
		init: function() {
			this.parent = visualEditor.ui.components;
		},

		view: function () {
			this.parent.componentsPanel.append("<div class='separators'><br><hr></div>");
		}
	}),

    /**
	 * Note component
	 */
	Note: Class.extend({
		init: function() {
			this.parent = visualEditor.ui.components;
		},

        view: function(_this) {
            this.cmp_data = $('<div title="Note" class="btn-components fa fa-sticky-note"></div>');
            this.cmp_data.click(_this, this.addElement);
            this.parent.componentsPanel.append(this.cmp_data);
        },

        addElement: function(event, position) {
            var element =  new draw2d.shape.note.PostIt({
               text:"Click to edit this note",
               color:"#000000",
               padding:20
            });
            element.installEditor(new draw2d.ui.LabelInplaceEditor());
            if(position == undefined) position = {x:100, y:100};
            visualEditor.ui.canvas.add(element, position.x, position.y);
            return element;
        }
	}),

    /**
	 * Picture component
	 */
	Picture: Class.extend({
		init: function() {
			this.parent = visualEditor.ui.components;
		},

        view: function(_this) {
            this.cmp_data = $('<div title="Note" class="btn-components fa fa-file-image-o"></div>');
            this.cmp_data.click(_this, this.addElement);
            this.parent.componentsPanel.append(this.cmp_data);
        },

        addElement: function(event, position) {
            var file;
			do {
				file=prompt("Select an image file");
			}
			while(file.length < 0);

            var element =  new draw2d.shape.basic.Image({
               path: '../examples/'+file
            });
            if(position == undefined) position = {x:100, y:100};
            visualEditor.ui.canvas.add(element, position.x, position.y);
            return element;
        }
	}),

	hideAcdCompnents: function(){
        $('#componentbox_window .btn-components').show().first().hide();
        $('.separators').show();
	},

	hideVfodtlCompnents: function(){
        var elements = $('#componentbox_window .btn-components');
        elements.hide();
        for(var i=0; i<3; i++)
            $(elements.get(i)).show();
        $('.separators').hide();
	}

};
