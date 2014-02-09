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
    <div class="col-xs-1 col-sm-1 col-md-1">
        <button id="back_button" type="button" class="btn btn-default" data-toggle="modal">Back</button>
    </div>

    <div class="col-xs-1 col-sm-1 col-md-1 col-md-offset-1">
        <button id="confirm_button" type="button" class="btn btn-primary">Confirm</button>
    </div>
</%block>

<%block name="scripts">
    <link href="static/css/datepicker3.css" rel="stylesheet">
    <script src="static/js/bootstrap-datepicker.js"></script>

    <script>
        $(document).ready(function() {
            $("#datepicker").datepicker();
        });
    </script>
</%block>