<%inherit file="template_pattern_creation.mako" />

<%block name="small_text">
</%block>

<%block name="large_text">
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