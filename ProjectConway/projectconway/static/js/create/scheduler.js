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
        populateHourSlot(event.date);
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

    function populateHourSlot(date) {
        /**
         * Populates the hour slot selection with hours that are viable.
         */
        var hour_slot = $("#viewing_hour");
        hour_slot.empty();
        hour_slot.prop("disabled", true);

        var stringify = function(hour){
            var h = hour.toString();
            if (h.length < 2) {
                h = "0" + h;
            }
            return h;
        }

        var now = new Date();
        for (var i=0; i<24; i++){
            if (date > now){
                hour_slot.append($("<option />").val(stringify(i)).text(stringify(i)));
            }
            else {
                if (i >= now.getHours()){
                    hour_slot.append($("<option />").val(stringify(i)).text(stringify(i)));
                }
            }
        }
        hour_slot.prop("disabled", false);
    }

    this.populateMinuteSlot = function() {
        /**
         * Populates the minute slot selection with minutes that are viable.
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