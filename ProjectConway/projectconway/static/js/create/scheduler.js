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

        populateMinuteSlotDate(event.date, hour);
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

        populateMinuteSlotDate(date, hour);
    }

    this.populateMinuteSlot = function() {
        /**
         *
         */
        var d = new Date();
        d.setMinutes(0);
        d.setSeconds(0);
        d.setMilliseconds(0);
        populateMinuteSlotDate(d, d.getHours());
    }

    function populateMinuteSlotDate(date, hour) {
        /**
         * Supports the event handlers...
         */
        var timestring = JSON.stringify(date).replace("T00", "T" + hour);
        var minute_slot = $("#viewing_slot");

        minute_slot.empty();
        minute_slot.prop("disabled", true);

        $.ajax({
            url: URL,
            type: "POST",
            data: timestring,
            dataType: 'json',
            success: function(data){
                $.each(data["time_slots"], function() {
                    minute_slot.append($("<option />").val(this).text(this));
                })

                minute_slot.prop("disabled", false);
            }
        });
    }

};