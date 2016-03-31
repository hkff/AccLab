//////////////////////////////////////////////////////////
//
//  AccLab UI : properties.js
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

visualEditor.ui.properties = {
	
	grid            : null,
	actionsPanel    : null,
	componentsPanel : null,
	propertiesPanel : null,
	elements        : [],
	isUpdating      : false,
	propertiesMap   : {nameProp       : 0,
					   bgColorProp    : 1,
					   rsColorProp    : 2,
					   rsProp         : 3,
					   psColorProp    : 4,
					   psProp         : 5,
					   labelColorProp : 6,
					   labelSizeProp  : 7,
					   typesProp      : 8
					  },

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
		
		this.AALEditor = new visualEditor.ui.properties.aalEditor();
		this.view(this);
		this.control(this);
	},

	/**
	 * View
	 * @param _this
	 */
	view: function(_this) {
		// Render the AAL editor
		this.AALEditor.view(this);
		return;
		/**
		 * Extended text editor for propertygrid editor
		 */
		$.extend($.fn.datagrid.defaults.editors, {
		    etext: {
		        init: function(container, options){
		        	var input =$('<input type="text" class="datagrid-editable-input">').appendTo(container);
		        	$(input[0]).bind('input', function(){
						
						var row = $('#pg').propertygrid('getSelected').row;
						var propertiesMap = visualEditor.ui.properties.propertiesMap;
						// Poor hack
						switch(row){
				        // Update name
				        case propertiesMap.nameProp:
				        	
				        	if(visualEditor.ui.selectedNode instanceof ActorUI) {
								visualEditor.ui.selectedNode.updateName($(this).val());
							}

							if((visualEditor.ui.selectedNode instanceof PolicyUI))
								visualEditor.ui.selectedNode.setText($(this).val());

							visualEditor.ui.selectedNode.repaint();
							//visualEditor.ui.selectedNode.tlabel.repaint();
				            break;
				        }
		        	});
					return input;
		        },

		        destroy: function(target){
		            $(target).text('destroy');
		        },

		        getValue: function(target){
		        	return $(target).val();
		        },

		        setValue: function(target, value){
		         	$(target)[0].value = value;
		        },

		        resize: function(target, width){
		            $(target).text('resize',width);
		        }
		    }
		});

		/**
		 * Number Spiner for propertygrid editor
		 */
		$.extend($.fn.datagrid.defaults.editors, {
		    numberspinner: {
		        init: function(container, options){
		            var input = $('<input type="text">').appendTo(container);
		            return input.numberspinner(options);
		        },

		        destroy: function(target){
		            $(target).numberspinner('destroy');
		        },

		        getValue: function(target){
		            return $(target).numberspinner('getValue');
		        },

		        setValue: function(target, value){
		            $(target).numberspinner('setValue',value);
		        },

		        resize: function(target, width){
		            $(target).numberspinner('resize',width);
		        }
		    }
		});

		/**
		 * Color picker for propertygrid editor
		 */
		$.extend($.fn.datagrid.defaults.editors, {
		    colorpicker: {
		        init: function (container, options) {
		            var input = $('<input class="colorInput">').appendTo(container);

		            input.ColorPicker({
		                color: '#0000ff',
		                onShow: function (colpkr) {
		                	$(colpkr).css("z-index","999999");
		                    $(colpkr).fadeIn(500);
		                    return false;
		                },
		                onHide: function (colpkr) {
		                	$(colpkr).css("z-index","-1");
		                    $(colpkr).fadeOut(500);
		                    return false;
		                },
		                onChange: function (hsb, hex, rgb) {
		                	// POOR HACK
		                	var row = $('#pg').propertygrid('getSelected').row;
		                	/*$('#pg').propertygrid('beginEdit', row);
							editor = $('#pg').propertygrid('getEditor', {index:row, field:'value'});
							editor.actions.setValue(editor.target, '#' + hex)
							$('#pg').propertygrid('endEdit', row);
							*/
							visualEditor.ui.properties.updateGridProp(row, '#' + hex);

							var propertiesMap = visualEditor.ui.properties.propertiesMap;
							switch(row){
					        // Update Backgroud color
					        case propertiesMap.bgColorProp:
					            visualEditor.ui.selectedNode.DEFAULT_bgColor = '#'+hex;
					            break;
					        // Update required services color
					        case propertiesMap.rsColorProp:
					            visualEditor.ui.selectedNode.DEFAULT_rsColor = '#'+hex;
					            break;
					        // Update provided services color
					        case propertiesMap.psColorProp:
					            visualEditor.ui.selectedNode.DEFAULT_psColor = '#'+hex;
					            break;
					        // Update Label color
					        case propertiesMap.labelColorProp:
					            visualEditor.ui.selectedNode.DEFAULT_labelColor = '#'+hex;
					            break;
					        }

							visualEditor.ui.selectedNode.refresh();
		                }
		            });
		            return input;
		        },

		        getValue: function (target) {
		            return $(target).val();
		        },

		        setValue: function (target, value) {
		            $(target).val(value);
		            $(target).css('backgroundColor', value);
		        },

		        resize: function (target, width) {
		            var input = $(target);
		            if ($.boxModel == true)
		                input.width(width - (input.outerWidth() - input.width()));
		            else
		                input.width(width);
		        }
		    }
		});

		/**
		 * Selectize for propertygrid editor
		 */
		$.extend($.fn.datagrid.defaults.editors, {
		    selectize: {
		        init: function(container, options){
		            var input = $('<input type="text" style="z-index:99999999;">').appendTo(container);
		            //console.log(input[0])
		             // Make it selectize
					$(input).selectize({ 
						plugins: ['remove_button','restore_on_backspace','drag_drop'],
						allowEmptyOption: false,
						persist: false, 
						createOnBlur: true, 
						create: true,
						openOnFocus: false,

			            onChange: function(event){
							if(!visualEditor.ui.properties.isUpdating){
								var services = new draw2d.util.ArrayList();
								
								this.getValue().split(',').forEach(function(p){
									if(p) services.add(p);
								});
								
								var row = $('#pg').propertygrid('getSelected').row;
								var propertiesMap = visualEditor.ui.properties.propertiesMap;
								switch(row){
						        // Update types
						        case propertiesMap.typesProp:
						            visualEditor.ui.selectedNode.updateTypes(services);
						            break;
						        // Update required services
						        case propertiesMap.rsProp:
						            visualEditor.ui.selectedNode.updateRservices(services);
						            break;
						        // Update provided services
						        case propertiesMap.psProp:
						            visualEditor.ui.selectedNode.updatePservices(services);
						            break;
						        }
							}
						}
					});
		            return input;
		        },

		        destroy: function(target){
		           // $(target).numberspinner('destroy');
		        },

		        getValue: function(target){
		            return $(target).val();
		        },

		        setValue: function(target, value){
		            visualEditor.ui.properties.isUpdating = true;
		            visualEditor.ui.properties.populateItems2($(target), value);
		            visualEditor.ui.properties.isUpdating = false;
		        },

		        resize: function(target, width){
		            $(target).css('height', '500px')
		        }
		    }
		});

		// Creating the propertygrid
		this.propertiesGrid = $('<table id="pg"></table>');
		this.propertiesPanel.append(this.propertiesGrid);
		var pg = $('#pg').propertygrid({
		    showGroup: true,
		    scrollbarSize: 0,
		    fitColumns:true,
		    columns:[[
		    	{field:'name',  title:'Name',  width:100, resizable:false, sortable:false},
   		    	{field:'value', title:'Value', width:100, resizable:false, sortable:false, styler:cellStyler}]]
		});


		/**
		 * Cell styler for the property grid
		 */
		function cellStyler(value,row,index){
			try{
				if(value.indexOf("#") == 0)
					return 'background-color:' + value + ';color: transparent;';
			}catch(err){}
        }
		

        // Property Grid rows
		this.nameProp = {
			name:'Name',
			value:'',
			height:'150px',
			group:'Node',
			editor:'etext',
			row:this.propertiesMap.nameProp
		};
		this.bgColorProp = {
			name: 'Backgroud Color',
			value: '#0000ff',
			group: "Node",
			editor: 'colorpicker',
			row: this.propertiesMap.bgColorProp
		};
		this.rsColorProp = {
			name: 'Backgroud Color',
			value: '#0000ff',
			group: 'Required Services',
			editor: 'colorpicker',
			row: this.propertiesMap.rsColorProp
		};
		this.psColorProp = {
			name: 'Backgroud Color',
			value: '#7ecf21',
			group: 'Provided Services',
			editor: 'colorpicker',
			row: this.propertiesMap.psColorProp
		};
		this.labelColorProp = {
			name: 'Color',
			value: '#0000ff',
			group: 'Label',
			editor: 'colorpicker',
			row: this.propertiesMap.labelColorProp
		};
		this.labelSizeProp = {
			name: 'Size',
			value: '12',
			group: 'Label',
			editor: 'numberspinner',
			row: this.propertiesMap.labelSizeProp
		};
		this.typesProp = {
			name: 'Types',
			value: '',
			group: 'Types',
			editor: 'selectize',
			row: this.propertiesMap.typesProp
		};
		this.rsProp = {
			name: 'Services',
			value: '',
			group: 'Required Services',
			editor: 'selectize',
			row: this.propertiesMap.rsProp
		};
		this.psProp = {
			name: 'Services',
			value: '',
			group: 'Provided Services',
			editor: 'selectize',
			row: this.propertiesMap.psProp
		};

		// Adding rows to the property grid
		pg.propertygrid('insertRow', {index: this.propertiesMap.nameProp,       row: this.nameProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.bgColorProp,    row: this.bgColorProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.rsColorProp,    row: this.rsColorProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.rsProp,         row: this.rsProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.psColorProp,    row: this.psColorProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.psProp,         row: this.psProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.labelColorProp, row: this.labelColorProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.labelSizeProp,  row: this.labelSizeProp});
		pg.propertygrid('insertRow', {index: this.propertiesMap.typesProp,      row: this.typesProp});
	},

	/**
	 * Controller
	 * @param _this
	 */
	control: function(_this) {
        this.AALEditor.control(this);
        return;
		$('#pg').propertygrid({
			onAfterEdit: function(rowIndex, rowData, changes){
				//console.log(rowIndex)
			}
		});

		// Detect size change
        $('#properties_window').mouseover(function(){$('#pg').datagrid('resize');})
								.mouseout(function(){$('#pg').datagrid('resize');});

		/*
		this.labelSizePropel.bind('input', function() { 
			visualEditor.ui.selectedNode.tlabel.setFontSize($(this).val());
			visualEditor.ui.selectedNode.tlabel.repaint();
			visualEditor.ui.selectedNode.repaint();
		});*/
	},

	/**
	 * Update properties panel with the selectedNode
	 */
	updateProps: function() {

		// Check if a node is selected
		if(visualEditor.ui.selectedNode == null)return;

		// Update properties
		this.isUpdating = true;
		
		if((visualEditor.ui.selectedNode instanceof PolicyUI)) {
			// Update a PolicyUI

			// Label text
			this.updateGridProp(this.propertiesMap.nameProp, visualEditor.ui.selectedNode.getText());
			
			// Background Color
			this.updateGridProp(this.propertiesMap.bgColorProp, visualEditor.ui.selectedNode.getBackgroundColor().hashString);

			// Policy
			visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(visualEditor.ui.selectedNode.policy);

		} else {
			// Update an ActorUI

			// Label text
			this.updateGridProp(this.propertiesMap.nameProp, visualEditor.ui.selectedNode.tlabel.text);
			
			// Background Color
			this.updateGridProp(this.propertiesMap.bgColorProp, visualEditor.ui.selectedNode.getBackgroundColor().hashString);
			
			// RS color
			this.updateGridProp(this.propertiesMap.rsColorProp, visualEditor.ui.selectedNode.DEFAULT_rsColor);

			// PS color
			this.updateGridProp(this.propertiesMap.psColorProp, visualEditor.ui.selectedNode.DEFAULT_psColor);

			// Label font size
			this.updateGridProp(this.propertiesMap.labelSizeProp, visualEditor.ui.selectedNode.tlabel.getFontSize());
			
			// Types
			this.updateGridProp(this.propertiesMap.typesProp, visualEditor.ui.selectedNode.getTypes().data);

			// Required services
			this.updateGridProp(this.propertiesMap.rsProp, visualEditor.ui.selectedNode.getRservices().data);
			
			// Provided services
			this.updateGridProp(this.propertiesMap.psProp, visualEditor.ui.selectedNode.getPservices().data);

			// Policy
			visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(visualEditor.ui.selectedNode.policy);
		}

		$('#pg').propertygrid('clearSelections');
		this.isUpdating = false;
	},

	/**
	 * Update grid property
	 * @param row
	 * @param value
	 */
	updateGridProp: function(row, value) {
		row = Number(row);
		var grid = $('#pg');
		var data = $.data(grid[0], 'datagrid').data;
		var rows = data.rows;
		rows[row].value = value;
		grid.datagrid('loadData', data);
		grid.propertygrid('selectRow', row);
	},

	/**
	 * Populate Items, with an utils.ArrayList
	 */
	populateItems: function(propel, list) {
		propel[0].selectize.clear();
		for (var i=0; i<list.getSize(); i++) {
			propel[0].selectize.setTextboxValue(list.get(i));
			propel[0].selectize.createItem();
		}
		propel[0].selectize.close();
	},

	/**
	 * Populate Items2
	 */
	populateItems2: function(propel, list) {
		var list2 =  list.toString().split(",");
		propel[0].selectize.clear();
		for (var i=0; i<list2.length; i++) {
			propel[0].selectize.setTextboxValue(list2[i]);
			propel[0].selectize.createItem();
		}
		propel[0].selectize.close();
	},

	/**
	 * rgb to hex function
	 */
	rgbTohex: function(bg) {
		if (bg.search("rgb") == -1)
            return bg;
        else {
            bg = bg.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
            function hex(x) {
                return ("0" + parseInt(x).toString(16)).slice(-2);
            }
            return "#" + hex(bg[1]) + hex(bg[2]) + hex(bg[3]);
        }
	}
};


//////////////////////////////////////////////////////////
//
//  AAL inplace editor
//
//////////////////////////////////////////////////////////
visualEditor.ui.properties.aalEditor = Class.extend({
	NAME : "visualEditor.ui.properties.aalEditor",
	inPlaceAALEditor : null,
	_this : null,

	/**
	 * init function
	 * @param attr
	 */
	init: function(attr) {
		this._this = this;
	},

	/**
	 * View
	 * @param parent
	 */
	view: function(parent) {
		this.inPlaceAALEditor = ace.edit("inPlaceAALEditor-editor");
	    this.inPlaceAALEditor.setTheme("ace/theme/" + visualEditor.aceTheme);
	    this.inPlaceAALEditor.getSession().setMode("ace/mode/AAL");

		this.templateAALBtn = $('<div title="Clause template" id="templateAALBtn" class="btn-action fa fa-code fa-lg"/>');
		this.clearAALBtn = $('<div title="Clear" id="clearAALBtn" class="btn-action fa fa-file-o fa-lg"/>');

        $("#inPlaceAALEditor-tools").append(this.templateAALBtn).append(this.clearAALBtn);
        $("#inPlaceAALEditor").hide().draggable();

		 // Hide panel prop
		//$(visualEditor.ui.propertiesPanel.children()).css("opacity", 0.15);
		//visualEditor.ui.propertiesPanel[0].addEventListener("click", visualEditor.ui.stoper, true);
	},

	/**
	 * Controller
	 * @param parent
	 */
	control: function(parent) {
		this.inPlaceAALEditor.on("change", function(e) {
			// Check if a node is selected
			if(visualEditor.ui.selectedNode == undefined || null) return;
            if(visualEditor.ui.selectedNode.type === "Policy")
			    visualEditor.ui.selectedNode.updatePolicy(visualEditor.ui.properties.AALEditor.inPlaceAALEditor.getValue());
		});
		
		this.templateAALBtn.click(function(e){
			visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue(
                visualEditor.ui.properties.AALEditor.getClauseTemplate());
		});

		this.clearAALBtn.click(function(e){
			visualEditor.ui.properties.AALEditor.inPlaceAALEditor.setValue("");
		});
	},

	/**
	 * Get clause template
	 * @returns {string}
	 */
	getClauseTemplate: function() {
		var selectedName = visualEditor.ui.selectedNode.getName();
		return "CLAUSE " + selectedName + "_policy (\n {Usage}\n AUDITING {actions}\n IF_VIOLATED_THEN {actions}\n)";
	}
});
