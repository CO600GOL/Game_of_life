## The overarching template file with headers and more

<%inherit file="template_tutorial.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>The circle of life...</h2>
        <p>Cells are born in the next generation when they have exactly three living neighbours.</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <div class="tutorial_box">
            <div class="row">
                <div class="col-md-12 col-xs-12" id="tutorial_text">
                    <h4 id="tutorial_title">Rule 4</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" id="tutorial_text">
                     <p>Any cell with exactly three living neighbours will be born
                         in the next generation.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <br/>
        <h4>Tip:</h4>
        <p>Why not start by bringing a cell to live? Just give a cell three neighbours!</p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-sm hidden-xs" id="button_left">
        <p><a href="/tutorial-4" class="btn btn-primary btn-large">Back</a></p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-sm hidden-xs" id="button_right">
        <p><a href="/tutorial-6" class="btn btn-primary btn-large">Next</a></p>
    </div>
</%block>

<%block name="demonstration">
    <div class="col-md-12 col-md-offset-2">
       <h1> <img src="static/images/Rule4.gif" alt="Rule Four demonstration" class="img-responsive"/> </h1>
       <div class="row visible-xs visible-sm">
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_left">
                <p><a href="/tutorial-4" class="btn btn-primary btn-large">Back</a></p>
            </div>
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_right">
                <p><a href="/tutorial-6" class="btn btn-primary btn-large">Next</a></p>
            </div>
       </div>
    </div>
</%block>