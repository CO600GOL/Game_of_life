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
        var hour = $("#viewing_hour").val();

        eventHandlerHelper(event.date, hour);
    }

    this.hourSelectEventHandler = function(event) {
        /**
         * This function deals with changes to the "viewing hour"
         * select element.
         * It will fire a request for the available five minute slots,
         * for the combination the date and the hour and changes the minute
         * select accordingly.
         */
        var hour = $("#viewing_hour").val();
        var date = $("#datepicker").datepicker("getDate");

        eventHandlerHelper(date, hour);
    }

    function eventHandlerHelper(date, hour) {
        /**
         * Supports the event handlers...
         */
        var timestring = JSON.stringify(date).replace("T00", "T" + hour)

        $.ajax({
            url: URL,
            type: "POST",
            data: timestring,
            dataType: 'json',
            success: function(){console.log("Getting slots succeeded")},
            error: function(){console.log("Getting slots failed")}
        });
    }

};