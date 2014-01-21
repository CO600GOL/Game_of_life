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
            success: function(result) {alert("Turns: " + result["turns"] + " Time: " + result["runtime"])}
        });
    }
}

