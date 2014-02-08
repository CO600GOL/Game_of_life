<%inherit file="template_pattern_creation.mako" />

<%block name="small_text">
    <h2>Save your pattern!</h2>
    <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.</p>
</%block>

<%block name="large_text">
    <h2>Scheduler</h2>
    <p>Choose a date and time to go and see your pattern come to life!</p>

    <label class="control-label">Date of Viewing</label>

    <div class="input-group date" id="datepicker" data-date=${viewing_date} data-date-format="dd-mm-yyyy">
      <input class="form-control" type="text" readonly="" value=${viewing_date}>
      <span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
    </div>
</%block>

<%block name="extras">

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