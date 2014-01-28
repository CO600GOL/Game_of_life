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
            success: function(result) {
            	grid.clearGrid();
            },
            error: function() {
                $("#error_alert").css("top", "auto").css("left", "auto");
                $("#error_content").html("<p>An issue occurred while connecting with the server. Please try again.</p>");
            }
        });
 	}
 	
 	this.alertCloseHandler = function(event) {
        /**
         * Deal with the error alert close button being clicked.
         * Ie. move it back off the screen.
         */
        $("#error_alert").css("top", "").css("left", "");
    }
 }