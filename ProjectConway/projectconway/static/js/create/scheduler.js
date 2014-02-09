/**
 * Javascript library that deals with the event handling and
 * Ajax involved with collecting scheduling information from the database
 */

function Scheduler() {
    var URL = "/scheduler.json";

    this.datepickerEventHandler = function(event) {
        /**
         * An event-handling function that is fired when a date is
         * picked from the datepicker, requesting the five minute
         * time slots that are still available for the combination of
         * the date and the hour.
         */
        // Collect the date and hour for use in the AJAX call.

    }

    function eventHandlerHelper(date, hour) {
        /**
         * Supports the event handlers...
         */

        $.ajax({
            url: URL,
            type: "POST"
        });
    }

};