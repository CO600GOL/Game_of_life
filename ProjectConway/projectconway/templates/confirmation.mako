<%inherit file="template_pattern_creation.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Confirm It!</h2>
        <p>You're done! Just check over your pattern, and time. If you need to, you can still
           change it! But once you've pressed submit, there's no going back!</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <h3>When?</h3>
        <p>Your pattern will run on...</p>
    </div>

    <div class="col-md-12 centered_text">
        <h4>${viewing_date}</h4>
    </div>

    <div class="col-md-12 centered_text">
        <p>at:</p>
    </div>

    <div class="col-md-12 centered_text">
        <h4>${viewing_hour}:${viewing_slot}</h4>
    </div>

    <div class="col-md-12 centered_text">
        <p>in:</p>
    </div>

    <div class="col-md-12 centered_text">
        <h4>
        % for line in display_address.split(","):
            ${line}${"," if not display_address.endswith(line) else ""}<br>
        % endfor
        </h4>
    </div>

</%block>

<%block name="extras">
    <form method="post">
        <div class="col-xs-1 col-sm-1 col-md-1">
            <button name="create_page" type="submit" class="btn btn-default" value="pattern_input">Edit Pattern</button>
        </div>

        <div class="col-xs-1 col-sm-1 col-md-1">
            <button name="create_page" type="submit" class="btn btn-default" value="scheduler">Change Time</button>
        </div>

        <div class="col-xs-1 col-sm-1 col-md-1">
            <button name="create_page" type="submit" class="btn btn-primary" value="confirm">Confirm</button>
        </div>
    </form>
</%block>

<%block name="scripts">
    <script>
        $(document).ready(function() {
            // Lock the grid so that it cannot be edited
            g.lockGrid();
        });
    </script>
</%block>