## The overarching template file with headers and more

<%inherit file="template_tutorial.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Too many cells!</h2>
        <p>Cells die when they have more than three living neighbours this is because
            there are too many cells close to it, the cell suffers the effect of over-crowing.</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <div class="tutorial_box">
            <div class="row">
                <div class="col-md-12 col-xs-12" id="tutorial_text">
                    <h4 id="tutorial_title">Rule 2</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" id="tutorial_text">
                     <p>Any living cell with more than three living neighbours will die
                         due to over-population in the next Generation.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <br/>
        <h4>Tip:</h4>
        <p>Spread out your cells, try not to have too may cells too close together!</p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-sm hidden-xs" id="button_left">
        <p><a href="/tutorial-2" class="btn btn-primary btn-large">Back</a></p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-sm hidden-xs" id="button_right">
        <p><a href="/tutorial-4" class="btn btn-primary btn-large">Next</a></p>
    </div>
</%block>

<%block name="demonstration">
    <div class="col-md-12 col-md-offset-2">
        <h1> <img src="static/images/Rule2.gif" alt="Rule Two demonstration" class="img-responsive"/> </h1>
        <div class="row visible-xs visible-sm">
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_left">
                <p><a href="/tutorial-2" class="btn btn-primary btn-large">Back</a></p>
            </div>
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_right">
                <p><a href="/tutorial-4" class="btn btn-primary btn-large">Next</a></p>
            </div>
        </div>
    </div>
</%block>