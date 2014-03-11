/**
 * Javascript library that deals with the event handling and
 * Ajax involved with collecting scheduling information from the database
 */

function Scheduler() {
    var URL = "/scheduler.json";
    var timeSlots; // a days worth of time slots

    /**
     * This renders the page for a given date.
     * i.e. update the hour slot and the minute slot for a given day
     */
    this.render = function(date) {

    }

    /**
     */
    this.datepickerEventHandler = function(event) {

    }

    /**
     */
    this.hourSelectEventHandler = function(event) {

    }

    /**
     * This function does a request to scheduler.json for a given day.
     * This should receive a dictionary of the available time slots in the
     * format below, this then gets assigned to the timeSlots variable.
     *
     * {"hours": [2, 3, 4, 5, 6],
     *  2: [0, 5, 15, 25],
     *  3: [5, 25, 45]
     *  ... }
     */
    function requestTimeSlots(date) {

    }

    /**
     * Update the hour dropdown with for a given list of hours
     */
    function updateHourSlot(hours) {
        var hour_slot = $("#viewing_hour");
        hour_slot.empty();
        hour_slot.prop("disabled", true);

        for (var hour in hours) {
             hour_slot.append($("<option />").val(hour).text(sFormat(hour)));
        }

        hour_slot.prop("disabled", false);
    }

    /**
     * Update the minutes/timeslots dropdown for a given hour
     */
    function updateMinuteSlot(hour) {
        var minute_slot = $("#viewing_slot");
        minute_slot.empty();
        minute_slot.prop("disabled", true);

        var minutes = timeSlots[hour];
        for (var minute in minutes) {
            minute_slot.append($("<option />").val(minute).text(sFormat(minute)));
        }

        minute_slot.prop("disabled", false);
    }


    /**
     * Function that takes an int and returns a string. If the int results in 1 digit, it adds a leading zero
     * @param s
     * @returns {string|*}
     */
    function sFormat(s){
        var s = s.toString();
        if (s.length < 2) {
            s = "0" + s;
        }
        return s;
    }

};