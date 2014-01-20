## The overarching template file with headers and more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
        <div class="row">
            <div class="col-md-6 col-md-offset-3" id="canvas-container">
                <canvas id="pattern_input"></canvas>
            </div>
        </div>
</%block>

<%block name="scripts">
        <script src="static/js/jcanvas.js"></script>
        <script src="static/js/input_grid.js"></script>
        <script>
            <%
                from game_of_life import X_CELLS, Y_CELLS
                x_cells = str(X_CELLS)
                y_cells = str(Y_CELLS)
            %>
            $(document ).ready(function() {
                var g = new CanvasGrid("#pattern_input", ${x_cells}, ${y_cells}, 20);
                g.setup();
            });
        </script>
</%block>