## The overarching template file with headers and more

<%inherit file="template_tutorial.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Cheating death...</h2>
        <p>Cells stay alive when they have two or three living neighbours. Giving a cell neighbours can help it stay
        alive longer!</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <div class="tutorial_box">
            <div class="row">
                <div class="col-md-12 col-xs-12" id="tutorial_text">
                    <h4 id="tutorial_title">Rule 3</h4>
                </div>
            </div>
                <div class="row">
                    <div class="col-md-12" id="tutorial_text">
                         <p>Any living cell with two or three living neighbours will survive on into the next generation.</p>
                    </div>
                </div>
        </div>
    </div>
    <div class="col-md-12">
        <br/>
        <h4>Tip:</h4>
        <p>Don't put four cells too close together, you might create a 'still life'; this means the cells will forever
        be alive, resulting in a boring pattern that will not change from generation to generation. </p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-xs hidden-sm" id="button_left">
        <p><a href="/tutorial-3" class="btn btn-primary btn-large">Back</a></p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-xs hidden-sm" id="button_right">
        <p><a href="/tutorial-5" class="btn btn-primary btn-large">Next</a></p>
    </div>
</%block>

<%block name="demonstration">
    <div class="col-md-12 col-md-offset-2">
       <h1> <img src="static/images/Rule3.gif" alt="Rule Three demonstration" class="img-responsive"/> </h1>
        <div class="row visible-xs visible-sm">
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_left">
                <p><a href="/tutorial-3" class="btn btn-primary btn-large">Back</a></p>
            </div>
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_right">
                <p><a href="/tutorial-5" class="btn btn-primary btn-large">Next</a></p>
            </div>
        </div>
    </div>
</%block>
