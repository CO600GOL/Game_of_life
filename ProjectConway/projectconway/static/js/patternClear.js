/**
 * Javascript library that deals with the event handling and
 * AJAX involved in clearing the input grid of any saved patterns.
 */
 
function Clearer(grid) {
 	var URL = "/pattern_clearer.json";
 	
 	this.clearEventHandler = function(event) {
 		/**
 		 * An event handling function that clears any saved pattern from the
 		 * grid and the web session.
 		 */
 		 
 		 $.ajax({
            url: URL,
            type: "POST",
            dataType: 'json',
            success: function() {
            	grid.clearGrid();
            },
            error: function() {
            	$.getScript('static/ajaxError.js', alertOpenHandler());
            }
        });
 	}
 }