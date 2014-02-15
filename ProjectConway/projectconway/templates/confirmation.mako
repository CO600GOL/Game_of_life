<%inherit file="template_pattern_creation.mako" />

<%block name="small_text">
    <div class="row">
        <div class="col-md-12">
            <h2>Confirm It!</h2>
            <p>You're done! Just check over your pattern, and time. If you need to, you can still
               change it! But once you've pressed submit, there's no going back!</p>
        </div>
    </div>
</%block>

<%block name="large_text">
    <div class="row">
        <div class="col-md-12">
            <h3>When?</h3>
            <p>Your pattern will run on...</p>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12 centered_text">
        </div>
    </div>

    <div class="row">
        <div class="col-md-12 centered_text">
            <p>at:</p>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12 centered_text">
        </div>
    </div>

    <div class="row">
        <div class="col-md-12 centered_text">
            <p>in:</p>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12 centered_text">
        </div>
    </div>

</%block>

<%block name="extras">
</%block>

<%block name="scripts">
    <script>
        $(document).ready(function() {
            // Lock the grid so that it cannot be edited
            g.lockGrid();
        });
    </script>
</%block>