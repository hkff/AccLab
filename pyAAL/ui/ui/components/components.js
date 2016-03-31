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
		this.components.push(new Actor());
        this.components.push(new Policy());

		this.components.push(new this.Separator());
        this.components.push(new this.Note());
        this.components.push(new this.Picture());
        this.components.push(new this.Slide());

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
            this.cmp_data = $('<div title="Picture" class="btn-components fa fa-file-image-o"></div>');
            this.cmp_data.click(_this, this.addElement);
            this.parent.componentsPanel.append(this.cmp_data);
        },

        addElement: function(event, position) {
            var file;
			do {
				file=prompt("Select an image file");
			}
			while(file.length <= 0);

            var element =  new draw2d.shape.basic.Image({
               path: '../examples/'+file
            });
            if(position == undefined) position = {x:100, y:100};
            visualEditor.ui.canvas.add(element, position.x, position.y);
            return element;
        }
	}),

    /**
     * Hide Acd components (1)
     */
	hideAcdCompnents: function(){
        var elements = $('#componentbox_window .btn-components');
        elements.show();
        for(var i=0; i<2; i++)
            $(elements.get(i)).hide();
        $('.separators').show();
	},

    /**
     * Hide Vfodtl components (4-n)
     */
	hideVfodtlCompnents: function(){
        var elements = $('#componentbox_window .btn-components');
        elements.hide();
        for(var i=0; i<5; i++)
            $(elements.get(i)).show();
        $('.separators').hide().first().show();
	},

	/**
	 * Slide component
	 */
    Slide: Class.extend({
        init: function() {
			this.parent = visualEditor.ui.components;
		},

        view: function(_this) {
            this.cmp_data = $('<div title="Slide" class="btn-components fa fa-outdent"></div>');
            this.cmp_data.click(_this, this.addElement);
            this.parent.componentsPanel.append(this.cmp_data);
        },

        addElement: function(event, position) {
            var a = new visualEditor.ui.components.ZoomFigure({width:100, height:60}, true);
            if(position == undefined) position = {x:100, y:100};
            visualEditor.ui.canvas.add(a, position.x, position.y);
            return a;
        }
	}),

	ZoomFigure: draw2d.shape.layout.StackLayout.extend({

        Picture: draw2d.SetFigure.extend({
            init: function(path) {
                this._super();
                this.strokeScale = false;
                this.setKeepAspectRatio(false);
                this.img_path = path;
            },

            createSet: function() {
                this.canvas.paper.setStart();
                this.canvas.paper.image('../examples/'+ this.img_path, 0, 0, 100, 60);
                return this.canvas.paper.setFinish();
            }
        }),

        addPicture: function(msg) {
            var file;
			do { file=prompt(msg); } while(file.length <= 0);
            this.pictures.push(file);
            return new this.Picture(file);
        },

        init: function (attr, ui) {
            this._super(attr);
            this.pictures = [];
            if(ui) {
                var pic2 = this.addPicture("Select the first image file");
                var pic1 = this.addPicture("Select the second image file");
                this.add(pic1);
                this.add(pic2);
            }
            this.setKeepAspectRatio(true);
            this.lastZoom = 1;
            this.installEditPolicy(new draw2d.policy.figure.FigureEditPolicy());
            //this.createPort("input");
            //this.createPort("output");

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
                //var zoomer = new draw2d.policy.canvas.WheelZoomPolicy();
                //zoomer.canvas = visualEditor.ui.canvas;
                //zoomer.onMouseWheel(10, event.x, event.y, true, false);
                //visualEditor.ui.canvas.setZoom(0.3, true);
                //visualEditor.ui.canvas.scrollTo(emitter.x*3, emitter.y*3);
                // FIXME
            });
        },

         getPersistentAttributes: function() {
            var memento = this._super();
            memento.pic2 = this.pictures[1];
            memento.pic1 = this.pictures[0];
            memento.type = "visualEditor.ui.components.ZoomFigure";
            return memento;
         },

        setPersistentAttributes: function(memento) {
            this._super(memento);
            this.pictures.push(memento.pic1);
            this.pictures.push(memento.pic2);
            this.add(new this.Picture(memento.pic2));
            this.add(new this.Picture(memento.pic1));
            return this;
        }
    })
};


var originalRaphaelImageFn = Raphael.fn.image;
Raphael.fn.image = function(url, x, y, w, h) {
    // fix the image dimensions to match original scale unless otherwise provided
    if( !w || !h ) {
        var img = new Image();
        img.src = url;
        if( !w ) w = img.width;
        if( !h ) h = img.height;
    }
    return originalRaphaelImageFn.call(this, url, x, y, w, h);
};
