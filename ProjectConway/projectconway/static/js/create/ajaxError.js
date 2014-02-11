this.alertOpenHandler = function() {
	/**
	 * Shows the error alert.
	 * I.E. Move it onto screen
	 */
	 
	 $("#error_alert").css("top", "auto").css("left", "auto");
     $("#error_content").html("<p>An issue occurred while connecting with the server. Please try again.</p>");
}

this.alertCloseHandler = function(event) {
    /**
     * Deal with the error alert close button being clicked.
     * Ie. move it back off the screen.
     */
    $("#error_alert").css("top", "").css("left", "");
    }