## The overarching template file with headers and more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
        <canvas id="pattern_input"></canvas>

        <script src="http://code.jquery.com/jquery-1.10.2.min.js" ></script>
        <script src="static/js/input_grid.js" type="text/javascript"></script>
        <script>
            var g = new CanvasGrid("#pattern_input", 10, 10, 20);
            g.setup();
        </script>
</%block>