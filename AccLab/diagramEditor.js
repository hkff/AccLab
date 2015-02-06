//////////////////////////////////////////////////////////
//
//  AccDesigner V 0.2
//
//////////////////////////////////////////////////////////
    
var visualEditor = {
    path          : "curpath",
	/*currentCanvas : null,
    activeTab     : null,
    canvas        : [],*/
    backend       : "http://127.0.0.1:8000/",

	//////////////////////////////////////////////////////////
    //
    //  Initialize function
    //
    //////////////////////////////////////////////////////////
    init: function() {

    	// init workspace
		//visualEditor.ui.init("editor2-wrapper", "sb-actions-content", "sb-components-content", "inspector");
        visualEditor.ui.init("editor1_window", "toolbox_window", "componentbox_window", "properties_window");
        
    },


    guid: function() {
        function _p8(s) {
            var p = (Math.random().toString(16)+"000000000").substr(2,8);
            return s ? "-" + p.substr(0,4) + "-" + p.substr(4,4) : p ;
        }
       return _p8() + _p8(true) + _p8(true) + _p8();
    },
}; 