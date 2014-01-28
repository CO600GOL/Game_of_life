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
                $.getScript('static/js/ajaxError.js', alertOpenHandler());
            }
        });
    }
}

