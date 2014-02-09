/**
 * Javascript library that deals with the event handling and
 * AJAX involved in clearing the input grid of any saved patterns.
 */
 
function Clearer(grid) {
 	var URL = "/pattern_clearer.json";
 	
 	this.clearEventHandler = function(event) {
 		/**
 		 * An event handling function that begins the process of clearing any 
 		 * saved pattern from the grid and the web session.
 		 */
 		 
 		 $.ajax({
            url: URL,
            type: "POST",
            dataType: 'json',
            success: function() {
            	$("#clear_warning").modal({show: true});
            	$("#warning_content").html("<p>Are you sure you want to clear your pattern?</p><p>Once it's gone, it can't come back!</p>")
            },
            error: function() {
            	$.getScript('static/js/create/ajaxError.js', alertOpenHandler());
                $("#error_alert").css("top", "5%").css("left", "3%");
            }
        });
 	}
 	
 	this.clearConfirmEventHandler = function(event) {
 		/**
 		 * An event confirming the clear of a user's saved pattern from the grid
 		 * and the web session.
 		 */
 		 
 		 $.ajax({
 		 	url: URL,
 		 	type: "POST",
 		 	dataType: 'json',
 		 	success: function() {
 		 		grid.clearGrid();
 		 		$("#clear_warning").modal("hide");
 		 	},
 		 	error: function() {
 		 		$.getScript('static/js/create/ajaxError.js', alertOpenHandler());
 		 		$("#error_alert").css("top", "5%").css("left", "3%");
 		 	}
 		 });
 	}
 }