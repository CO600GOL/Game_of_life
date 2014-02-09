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

    <div class="col-md-12">
        <div class="input-group date" id="datepicker" data-date=${viewing_date} data-date-format="dd-mm-yyyy">
          <input class="form-control" type="text" readonly="" value=${viewing_date}>
          <span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
        </div>
    </div>

    <div class="col-md-2">
        <label class="control-label">Viewing Hour</label>
    </div>

    <div class="col-md-3">
        <div class="dropdown">
            <button class="btn dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown">
                ${str(viewing_hour)}
                <span class="caret"></span>
            </button>
            <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu">
                % for i in range(0, 24):
                    <li>${str(i)}</li>
                % endfor
            </ul>
        </div>
    </div>

    <div class="col-md-1"></div>

    <div class="col-md-2">
        <label class="contol-label">Viewing Slot</label>
    </div>

    <div class="col-md-3">
        <div class="dropdown">
            <button class="btn dropdown-toggle" type="button" id="dropdownMenu1" data-toggle="dropdown">
                ${str(format(viewing_slot, '02d'))}
                <span class="caret"></span>
            </button>
            <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu">
                % for i in range(0, 60, 5):
                    <li>${str(format(i, '02d'))}</li>
                % endfor
            </ul>
        </div>
    </div>
</%block>

<%block name="extras">
    <form method="post">
        <div class="col-xs-1 col-sm-1 col-md-1">
            <button name="create_page" type="submit" class="btn btn-default" value="pattern_input">Back</button>
        </div>

        <div class="col-xs-1 col-sm-1 col-md-1 col-md-offset-1">
            <button name="create_page" type="submit" class="btn btn-primary" value="confirmation">Confirm</button>
        </div>
    </form>
</%block>

<%block name="scripts">
    <link href="static/css/datepicker3.css" rel="stylesheet">
    <script src="static/js/bootstrap/bootstrap-datepicker.js"></script>
    <script src="static/js/create/inputGrid.js"></script>
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
            $("#datepicker").datepicker().on("changeDate", s.datepickerEventHandler)

            // Lock the grid so that it cannot be edited
            g.lockGrid();
        });
    </script>
</%block>