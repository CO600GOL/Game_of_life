## The overarching template file with headers and more

<%inherit file="template_pattern_creation.mako" />
<%namespace name="rule_texts" file="rule_texts.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Give it a go!</h2>
        <p>This is where you create your pattern!</p>
        <p>Click a cell to begin!</p>
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
    <button id="clear_button" type="button" class="btn btn-default left-button">Clear</button>
    <button id="submit_button" type="button" class="btn btn-primary right-button" data-toggle="modal" data-target="#loading_popup">Submit</button>
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
