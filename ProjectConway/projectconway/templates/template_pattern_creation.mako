## The overarching template file with headers anmd more
<%inherit file="template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">
	
	<div class="container">
		<div class="row">
			<div class="col-md-6">
                <div class="row">
                    <%block name="small_text" />
                </div>

                <div class="row" id="large_text_row">
                    <%block name="large_text" />
                </div>
			</div>

			<div class="col-md-6">
                <%block name="grid">
                        <div class="row" id="grid_row">
                            <div class="col-xs-11 col-md-10 col-md-offset-2" id="canvas-container">
                                <canvas id="pattern_input"></canvas>
                            </div>
                        </div>
                </%block>

                <div class="row" id="extra_row">
                        <%block name="extras" />
                </div>

			</div>
		</div>
	</div>
</%block>

<%block name="grid_init_scripts">
    <script src="static/js/create/jcanvas.js"></script>
    <script src="static/js/create/inputGrid.js"></script>

    <script>
    <%
        from game_of_life import X_CELLS, Y_CELLS
        x_cells = str(X_CELLS)
        y_cells = str(Y_CELLS)
     %>

    $(document).ready(function() {
        // Setup grid
        var g = new CanvasGrid("#pattern_input", ${x_cells}, ${y_cells});
        window.g = g;
        g.setup();
        // Check the variable has been passed in
        % if pattern:
            g.setGridPattern("${pattern}");
        % endif
    });
    </script>
</%block>