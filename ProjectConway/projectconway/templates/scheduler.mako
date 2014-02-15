<%inherit file="template_pattern_creation.mako" />

<%block name="small_text">
    <h2>Save your pattern!</h2>
    <p>Now that you've created a pattern, it's time to send it to the display!</p>
    <p>Just select a date and time in the section below and press submit.</p>
    <b>Note: To edit your work so far, just press the back button below the grid!</b>
</%block>

<%block name="large_text">
    <h2>Scheduler</h2>
    <p>Choose a date and time to go and see your pattern come to life!</p>

    <div class="col-md-12">
        <label class="control-label">Date of Viewing</label>
    </div>

    <form method="post">
    <div class="col-md-12">
        <div class="input-group date" id="datepicker" data-date="${viewing_date}" data-date-format="dd/mm/yyyy">
          <input class="form-control" type="text" readonly="" value="${viewing_date}" name="viewing_date">
          <span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
        </div>
    </div>

    <div class="col-md-2">
        <label class="control-label" for="viewing_hour">Viewing Hour</label>
    </div>


    <div class="col-md-3">
          <select class="form-control" name="viewing_hour" id="viewing_hour">
              <%
              import datetime
              current_hour = datetime.datetime.now().hour
              %>
              % for i in range(current_hour, 24):
                  <option value="${str(i)}" ${"selected" if (i == viewing_hour) else ""}>${format(i, "02d")}</option>
              % endfor
          </select>
    </div>

    <div class="col-md-2 col-md-offset-1">
        <label class="contol-label" for="viewing_slot">Viewing Slot</label>
    </div>

    <div class="col-md-3">
        <select class="form-control" name="viewing_slot" id="viewing_slot" disabled>
        </select>
    </div>
</%block>

<%block name="extras">

        <div class="col-xs-12 col-md-12">
            <button name="create_page" type="submit" class="btn btn-default left-button" value="pattern_input">Back</button>
            <button name="create_page" type="submit" class="btn btn-primary right-button" value="confirmation">Confirm</button>
        </div>
    </form>
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
            %>

            // Set up some options for the datepicker including setting a start and end date and
            // automatically closing the calender when a date is picked.
            $("#datepicker").datepicker({
                "autoclose": true,
                "format": "dd/mm/yyyy",
                "startDate": "${today.strftime("%d/%m/%Y")}",
                "endDate": "${enddate.strftime("%d/%m/%Y")}"
            });

            // Set up event handling for the datepicker
            var s = new Scheduler();
            s.populateMinuteSlot();
            $("#datepicker").datepicker().on("changeDate", s.datepickerEventHandler);
            $("#viewing_hour").change(s.hourSelectEventHandler);

            // Lock the grid so that it cannot be edited
            g.lockGrid();
        });
    </script>
</%block>