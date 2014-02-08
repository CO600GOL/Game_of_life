## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">
	
	<div class="container">
		<div class="row">
			<div class="col-md-4 col-md-offset-2">
                <%block name="small_text" />

                <%block name="large_text" />
			</div>
			
			<div class="col-md-6">
                <%block name="extras" />

                <%block name="grid">
                        <div class="col-xs-9 col-sm-7 col-md-6" id="canvas-container">
                            <canvas id="pattern_input"></canvas>
                        </div>
                </%block>
			</div>
		</div>
	</div>
</%block>