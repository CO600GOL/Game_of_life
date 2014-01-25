/**
 * Javascript library that deals with the event handling and
 * Ajax involved in pattern submission.
 */

function Submitter(grid) {
    var URL = "/pattern_receiver.json";

    this.submissionEventHandler = function(event) {
        /**
         * An event handling function that submits the current pattern of the grid
         * to the central webserver
         */
        console.log("Submit button pressed");
        var pattern = grid.getGridPattern();

        $.ajax({
            url: URL,
            type: "POST",
            data: JSON.stringify(pattern),
            dataType: 'json',
            success: function(result) {
                $("#loading_popup").modal("hide");
                $("#success_popup").modal({show: true});
                var gen_string = (result["turns"] > 1) ? "generations" : "generation";
                var sec_string = (result["runtime"] != 1) ? "seconds" : "second";
                $("#success_content").html("<p>This pattern will last " + result["turns"] + " " + gen_string + " and " + result["runtime"] + " " + sec_string + ".</p> <p>Do you wish to continue?</p>");
            },
            error: function() {
                $("#loading_popup").modal("hide");

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

