## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">
	
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<div class="row">
					<div class="col-md-12">
						<%block name="small_text" />
					</div>
				</div>
				
				<div class="row">
					<div class="col-md-12">
						<%block name="large_text" />
					</div>
				</div>
			</div>
			
			<div class="col-md-8">
				<div class="row">
					<div class="col-md-12">
						<%block name="extras" />
					</div>
				</div>
				
				<div class="row">
					<div class="col-md-12">
						<%block name="grid" />
					</div>
				</div>
			</div>
			
		</div>
	</div>
</%block>