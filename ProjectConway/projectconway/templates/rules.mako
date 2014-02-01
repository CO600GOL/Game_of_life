## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
    <div class="row">
        <div class="col-md-12">
            <h1>Game of Life Rules</h1>
        </div>
    </div>

    <div class="row">
        <div class="col-md-8">
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
            tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna
            mollis euismod. Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
            tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna
            mollis euismod. Donec sed odio dui.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/Rule_Test.gif" alt="Test Image" class="img-responsive"/>
        </div>
    </div>

</%block>