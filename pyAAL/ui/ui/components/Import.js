//////////////////////////////////////////////////////////
//
//  AccLab UI : Import.js
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

Import = Class.extend({
    NAME: "Import",
    type: "Import",

    init: function() {
        this.parent = visualEditor.ui.components;
    },

    view: function(_this) {
        this.cmp_data = $('<div title="Import AAL file" class="btn-components fa fa-file-text"></div>');
        this.cmp_data.click(_this, this.addElement);
        this.parent.componentsPanel.append(this.cmp_data);
    },

    addElement: function(event, position) {
        var a = new ImportUI({width:100, height:25}, true);
        if(position == undefined) position = {x:100, y:100};
        visualEditor.ui.canvas.add(a, position.x, position.y);
        return a;
    }
});


ImportUI = draw2d.shape.basic.Label.extend({
	NAME   : "ImportUI",
	type   : "Import",
	DEFAULT_bgColor : "#0d0d0d",
    DEFAULT_labelColor : "#0d0d0d",

    init: function(attr) {
        this._super(attr);
        this.resizeable = true;
        //this.installEditor(new draw2d.ui.LabelInplaceEditor());
        this.setText("Click to set AAL file")
    },

    onDoubleClick: function() {
        var _this = this;
        visualEditor.fileChooser("Select an AAL file", function(path) {
            _this.text = path;
            _this.repaint();
        }, ".aal");
    }
});
