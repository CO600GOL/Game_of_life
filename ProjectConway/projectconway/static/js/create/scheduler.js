/**
 * Javascript library that deals with the event handling and
 * Ajax involved with collecting scheduling information from the database
 */

function Scheduler() {
    var URL = "/scheduler.json";
    var timeSlots = null;

    /**
     * Init function that updatese the viewing hour and time_slot on startup
     */
    this.init = function(date) {
        render(date);
    }

    /**
     * Event listener for the datepicker object
     */
    this.datepickerEventHandler = function(event) {
        var chosenDate = event.date;
        render(chosenDate);
    }

    /**
     */
    this.hourSelectEventHandler = function(event) {
        var hour = $("#viewing_hour").val();
        updateMinuteSlot(parseInt(hour));
    }

    /**
     * This renders the page for a given date.
     * i.e. update the hour slot and the minute slot for a given day
     */
    function render(date) {
        requestTimeSlots(date);
        updateHourSlot(timeSlots["hours"]);
        updateMinuteSlot(timeSlots["hours"][0]);
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
        timeSlots = null;
        $.ajax({
            url: URL,
            async: false,
            type: "POST",
            data: "date=" + JSON.stringify(date.getTime()),
            dataType: 'json',
            success: function(data){
                timeSlots = data;
            }
        });

    }

    /**
     * Update the hour dropdown with for a given list of hours
     */
    function updateHourSlot(hours) {
        var hour_slot = $("#viewing_hour");
        hour_slot.empty();
        hour_slot.prop("disabled", true);

        for (var hour in hours) {
            hour = hours[hour];
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
            minute = minutes[minute];
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

    function throwError(error) {
        var hour_slot = $("#viewing_hour");
        hour_slot.empty();
        hour_slot.prop("disabled", true);
        var minute_slot = $("#viewing_slot");
        minute_slot.empty();
        minute_slot.prop("disabled", true);
        //$.getScript('static/js/create/ajaxError.js');
        //alertOpenHandler();
        //$("#error_content").html("<p>" + error + "</p>");
    }

};