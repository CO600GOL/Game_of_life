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
                <%block name="demonstration">
                        <div class="row" id="grid_row">
                            <div class="col-xs-11 col-md-10 col-md-offset-2" id="demonstration-area">
                            </div>
                        </div>
                </%block>
            </div>
        </div>
	</div>
</%block>

