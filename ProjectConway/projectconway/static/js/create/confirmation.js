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
                if (data["success"] == true) {
                    $("#confirmation_popup").modal({show: true});
                    $("#confirmation_header").html("<h4>It is done!</h4>");
                    $("#confirmation_body").html("<h5>Congratulations! Your pattern is going to the display!</h5>" +
                        "<h5>See you there!</h5>");
                    $("#confirmation_footer").html("<a type='button' class='btn btn-primary' href='/'>Done!</a>");
                } else {
                    $("#confirmation_popup").modal({show: true});
                    $("#confirmation_header").html("<h4>Uh-oh!</h4>");
                    $("#confirmation_body").html("<h5>There seems to have been a problem along the way.</h5>" +
                        "<h5>You're going to have to go back and change something...</h5>");
                    $("#confirmation_footer").html("<a type='button' class='btn btn-primary' href='/'>Go back</a>");
                }
            },
            error: function() {
                $.getScript('static/js/create/ajaxError.js', alertOpenHandler());
                $("#loading_popup").modal("hide");
                $("#error_alert").css("top", "5%").css("left", "3%");
                $("#error_content").html("<p>An issue occurred while connecting with the server. Please try again.</p>");
            }
        });
    }
}
