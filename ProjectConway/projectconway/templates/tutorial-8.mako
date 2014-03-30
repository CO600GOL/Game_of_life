<%inherit file="template_pattern_creation.mako" />
<%namespace name="rule_texts" file="rule_texts.mako" />

<%block name="small_text">
    <div class="col-md-12 hidden-sm hidden-xs">
        <h2>Now it's your turn!</h2>
        <p>You know the rules, now you can make your own pattern - and send it to our display! Still stuck? We have some ideas
            for some good patterns for you!</p>
        <p>To make a cell come alive, just click it. To make it dead, just click the cell again!</p>
    </div>
    <div class="col-md-12 visible-sm visible-xs">
        <h2>Now it's your turn!</h2>
        <p>You know the rules, now you can make your own pattern - and send it to our display!</p>
        <p>To make a cell come alive, just click it. To make it dead, just click the cell again!</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12 hidden-sm hidden-xs">
     <div class="row">
        <div class="col-md-6">
            <img src="static/images/Spaceship.png" alt="A spaceship pattern" class="img-responsive" width="75%" height="75%"/>
        </div>
        <div class="col-md-6">
            <img src="static/images/Tumbler.png" alt="Tumbler pattern" class="img-responsive" width="75%" height="75%"/>
        </div>
    </div>
         <br/>
    <div class="row">
        <div class="col-md-6">
            <img src="static/images/R-pentomino.png" alt="R-Pentomino pattern" class="img-responsive" width="75%" height="75%"/>
        </div>
        <div class="col-md-6">
            <img src="static/images/Glider.png" alt="Glider pattern" class="img-responsive" width="75%" height="75%"/>
        </div>
    </div>
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
                    <form method="post" action="/create">
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