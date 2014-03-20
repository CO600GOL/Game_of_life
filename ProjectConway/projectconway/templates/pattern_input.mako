## The overarching template file with headers and more

<%inherit file="template_pattern_creation.mako" />
<%namespace name="rule_texts" file="rule_texts.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Give it a go!</h2>
        <p>This is where you create your pattern!</p>
        <p>Click a cell to begin!</p>
         <p><a href="/tutorial-1" class="btn btn-primary btn-large">Tutorial</a></p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <h3>Rules</h3>
        <p>Here is a quick reminder of the rules:</p>
        <ol>
            <li>${rule_texts.rule_one()}</li>
            <li>${rule_texts.rule_two()}</li>
            <li>${rule_texts.rule_three()}</li>
            <li>${rule_texts.rule_four()}</li>
        </ol>
    </div>
</%block>

<%block name="extras">
    <div class="col-xs-11 col-md-10 col-md-offset-2">
        <button id="clear_button" type="button" class="btn btn-default left-button">Clear</button>
        <button id="submit_button" type="button" class="btn btn-primary right-button" data-toggle="modal" data-target="#loading_popup">Submit</button>
    </div>

    <div class="alert alert-danger alert-block in" id="error_alert">
        <button type="button" class="close" id="closealert_button">x</button>
        <h4>Opps! There has been an error:</h4>
        <div id="error_content"></div>
    </div>

    <div class="modal fade" id="loading_popup" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <p class="loading_popup_txt">Loading...</p>
                    <img class="loading_image" src="static/images/loading.gif"/>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="success_popup" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4>Success!</h4>
                </div>

                <div class="modal-body">
                    <div id="success_content"></div>
                </div>

                <div class="modal-footer">
                    <form method="post">
                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
                        <button name="create_page" type="submit" class="btn btn-primary" value="scheduler">Next</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="clear_warning" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4>Warning!</h4>
                </div>

                <div class="modal-body">
                    <div id="warning_content"></div>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
                    <button type="button" class="btn btn-danger" id="clearconfirm_button" data-dismiss="modal">Clear</button>
                </div>
            </div>
        </div>
    </div>
</%block>

<%block name="scripts">
    <script src="static/js/create/patternSubmission.js"></script>
    <script src="static/js/create/patternClear.js"></script>
    <script src="static/js/create/ajaxError.js"></script>

    <script>
        $(document).ready(function() {
            var g = window.g;

            // Set up pattern submission
            var s = new Submitter(g);
            $("#submit_button").click(s.submissionEventHandler);
            $('#closealert_button').click(s.alertCloseHandler);

            // Set up pattern clearer
            var c = new Clearer(g);
            $("#clear_button").click(c.clearEventHandler);
            $("#clearconfirm_button").click(c.clearConfirmEventHandler);
            $('#closealert_button').click(c.alertCloseHandler);
        });
    </script>
</%block>