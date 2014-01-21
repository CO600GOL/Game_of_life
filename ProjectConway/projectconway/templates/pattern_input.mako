## The overarching template file with headers and more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
        <div class="row">
            <div class="col-xs-10 col-sm-8 col-md-6 col-xs-offset-1 col-sm-offset-2 col-md-offset-3" id="canvas-container">
                <canvas id="pattern_input"></canvas>
            </div>
            <div class="col-xs-1 col-sm-2 col-md-3">
                <button id="submit_button" type="button" class="btn btn-primary">Submit</button>
            </div>
        </div>
</%block>

<%block name="scripts">
        <script src="static/js/jcanvas.js"></script>
        <script src="static/js/inputGrid.js"></script>
        <script src="static/js/patternSubmission.js"></script>
        <script>
            <%
                from game_of_life import X_CELLS, Y_CELLS
                x_cells = str(X_CELLS)
                y_cells = str(Y_CELLS)
            %>
            $(document).ready(function() {
                // Setup grid
                var g = new CanvasGrid("#pattern_input", ${x_cells}, ${y_cells}, 20);
                g.setup();

                // Set up pattern submission
                var s = new Submitter(g);
                $("#submit_button").click(s.submissionEventHandler);
            });
        </script>
</%block>