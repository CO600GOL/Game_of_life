## The overarching template file with headers anmd more
<%inherit file="template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">
	
	<div class="container">
		<div class="row">
			<div class="col-md-5">
                <div class="row">
                    <%block name="small_text" />
                </div>

                <div class="row">
                    <%block name="large_text" />
                </div>
			</div>

            <div class="col-md-1"></div>
			
			<div class="col-md-5">
                <div class="row" id="extra_row">
                    <%block name="extras" />
                </div>

                <%block name="grid">
                        <div class="row" id="grid_row">
                            <div class="col-xs-9 col-sm-7 col-md-12" id="canvas-container">
                                <canvas id="pattern_input"></canvas>
                            </div>
                        </div>
                </%block>
			</div>
		</div>
	</div>
</%block>

<%block name="grid_init_scripts">
    <script src="static/js/jcanvas.js"></script>
    <script src="static/js/inputGrid.js"></script>
    <script src="static/js/patternSubmission.js"></script>
    <script src="static/js/patternClear.js"></script>
    <script src="static/js/ajaxError.js"></script>
    <script>
    <%
        from game_of_life import X_CELLS, Y_CELLS
        x_cells = str(X_CELLS)
        y_cells = str(Y_CELLS)
     %>

    $(document).ready(function() {
        // Setup grid
        var g = new CanvasGrid("#pattern_input", ${x_cells}, ${y_cells});
        g.setup();
        // Check the variable has been passed in
        % if pattern:
            g.setGridPattern("${pattern}");
        % endif

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