<%inherit file="template_pattern_creation.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Schedule your pattern!</h2>
        <p>Now that you've created a pattern, it's time to send it to the display!</p>
        <p>Just select a date and time in the section below and press submit.</p>
        <b>Note: To edit your work so far, just press the back button below the grid!</b>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <h3>Pick a date!</h3>
        <p>Choose a date to go and see your pattern come to life!</p>
    </div>

    <div class="col-md-12">
        <label class="control-label">Viewing Date</label>
    </div>

    <div class="col-md-12">
        <form method="post">
            <div class="input-group date" id="datepicker" data-date="${viewing_date}" data-date-format="dd/mm/yyyy">
              <input class="form-control" id="datepicker_form" type="text" readonly="" name="viewing_date">
              <span class="input-group-addon" id="datepicker_pic"><i class="glyphicon glyphicon-calendar"></i></span>
            </div>
    </div>

    <div class="col-md-12">
        <h3>Pick a time!</h3>
        <p>Now choose a time on that date to go and watch the display!</p>
    </div>

    <div class="col-xs-2 col-md-2">
        <label class="control-label" for="viewing_hour">Viewing Time</label>
    </div>


    <div class="col-xs-4 col-md-3">
          <select class="form-control" name="viewing_hour" id="viewing_hour" disabled>
          </select>
    </div>

    <div class="col-xs-1 col-md-1" id="time_sep">
        <label class="control-label" for="viewing_slot">:</label>
    </div>

    <div class="col-xs-4 col-md-3">
        <select class="form-control" name="viewing_slot" id="viewing_slot" disabled>
        </select>
    </div>

</%block>

<%block name="extras">
    <div class="col-xs-11 col-md-10 col-md-offset-2">
            <button name="create_page" type="submit" class="btn btn-default left-button" value="pattern_input">Back</button>
            <button name="create_page" type="submit" class="btn btn-primary right-button" value="confirmation">Confirm</button>
        </form>
    </div>
</%block>

<%block name="scripts">
    <link href="static/css/datepicker3.css" rel="stylesheet">
    <script src="static/js/bootstrap/bootstrap-datepicker.js"></script>
    <script src="static/js/create/scheduler.js"></script>

    <script>
        $(document).ready(function() {
            <%
                import datetime
                today = datetime.datetime.today()
                enddate = today + datetime.timedelta(weeks=12)

                from projectconway import project_config

                if project_config["start_date"]:
                    start_date = project_config["start_date"]
                else:
                    start_date = datetime.date.today()

                if project_config["date_range"]:
                    end_date = start_date + project_config["date_range"]
                else:
                    end_date = None
            %>

            // Set up some options for the datepicker including setting a start and end date and
            // automatically closing the calender when a date is picked.
            var d = $("#datepicker").datepicker({
                "autoclose": true,
                "format": "dd/mm/yyyy",
                "startDate": "${start_date.strftime("%d/%m/%Y")}",
                ${'"endDate": "%s"' % end_date.strftime("%d/%m/%Y") if end_date else '' | n}
            });
            $("#datepicker_form").val("${start_date.strftime("%d/%m/%Y")}");
            $("#datepicker").datepicker("setDate",  "${start_date.strftime("%d/%m/%Y")}")

            // Set up event handling for the datepicker
            var s = new Scheduler();
            //s.populateMinuteSlot();
            $("#datepicker").datepicker().on("changeDate", s.datepickerEventHandler);
            $("#viewing_hour").change(s.hourSelectEventHandler);
            s.init($("#datepicker").datepicker("getDate"));

            // Lock the grid so that it cannot be edited
            g.lockGrid();
        });
    </script>
</%block>
