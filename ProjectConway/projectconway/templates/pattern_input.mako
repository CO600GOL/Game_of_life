## The overarching template file with headers and more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">
	
	<div class="container">
        <div class="row">
            <div class="col-xs-9 col-sm-7 col-md-5 col-xs-offset-1 col-sm-offset-2 col-md-offset-3" id="canvas-container">
                <canvas id="pattern_input"></canvas>
            </div>

            <div class="col-xs-1 col-sm-2 col-md-3">
                <button id="submit_button" type="button" class="btn btn-primary" data-toggle="modal" data-target="#loading_popup">Submit</button>
            </div>
            
            <div class="col-xs-1 col-sm-2 col-md-3">
            	<button id="clear_button" type="button" class="btn btn-primary">Clear</button>
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
                        <button type="button" class="btn btn-default" data-dismiss="modal">Cancel</button>
                        <a class="btn btn-primary" href="#">Next</a>
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
        				<button type="button" class="btn btn-danger" id="clearconfirm_button" "data-dismiss="modal">Clear</button>
        			</div>
        		</div>
        	</div>
        </div>
		
        <div class="alert alert-danger alert-block in" id="error_alert">
            <button type="button" class="close" id="closealert_button">x</button>
            <h4>Opps! There has been an error:</h4>
            <div id="error_content"></div>
        </div>
    </div>
		
</%block>

<%block name="scripts">
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
