/**
 * Javascript library that sets up event handling for the confirmation
 * button that saves user information to the database.
 */

function Confirmer() {
    var URL = "/confirm.json";

    this.confirmationButtonEventHandler = function(event) {
        /**
         * An event-handling function that requests a view to
         * submit the user's information to the database.
         */

        $.ajax({
            url: URL,
            type: "GET",
            dataType: 'json',
            success: function(data) {
                console.log("SUCCESS");
                if (data["success"] == true) {
                    $("#confirmation_success_popup").modal({show: true});
                }
            },
            error: function() {
                console.log("ERROR");
                $.getScript('static/js/create/ajaxError.js', alertOpenHandler());
                $("#loading_popup").modal("hide");
                $("#error_alert").css("top", "5%").css("left", "3%");
                $("#error_content").html("<p>An issue occurred while connecting with the server. Please try again.</p>");
            }
        });
    }
}
