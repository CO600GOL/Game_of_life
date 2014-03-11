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
        <h4>${"%02d" % int(viewing_hour)}:${"%02d" % int(viewing_slot)}</h4>
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
    <div class="col-xs-11 col-md-10 col-md-offset-2">
        <form method="post">
            <button name="create_page" type="submit" class="btn btn-default left-button" value="pattern_input">Edit Pattern</button>
            <button name="create_page" type="submit" class="btn btn-default center-button" value="scheduler">Edit Time</button>
            <button type="button" class="btn btn-primary right-button" id="confirm_button">Confirm</button>
        </form>
    </div>

    <div class="alert alert-danger alert-block in" id="error_alert">
        <button type="button" class="close" id="closealert_button">x</button>
        <h4>Opps! There has been an error:</h4>
        <div id="error_content"></div>
    </div>

    <div class="modal fade" id="confirmation_popup" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <div id="confirmation_header"></div>
                </div>

                <div class="modal-body">
                    <div id="confirmation_body"></div>
                </div>

                <div class="modal-footer">
                    <div id="confirmation_footer"></div>
                </div>
            </div>
        </div>
    </div>
</%block>

<%block name="scripts">
    <script src="static/js/create/confirmation.js"></script>
    <script src="static/js/create/ajaxError.js"></script>
    <script>
        $(document).ready(function() {
            // Lock the grid so that it cannot be edited
            g.lockGrid();

            // Set up the event handling on the final confirmation button
            var c = new Confirmer();
            $('#confirm_button').click(c.confirmationButtonEventHandler);

            // Set up the closing of the ajax error warning.
            $('#closealert_button').click(alertCloseHandler);

        });
    </script>
</%block>