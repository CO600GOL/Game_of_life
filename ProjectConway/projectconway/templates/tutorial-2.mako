## The overarching template file with headers and more

<%inherit file="template_tutorial.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Killing a cell</h2>
        <p>A cell (square) in the Game of Life needs at least two living neighbours (indicated as black cells) or else
        in the next generation (turn) these cells will die. The game will end if all cells are dead.</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <div class="tutorial_box">
            <div class="row">
                <div class="col-md-12 col-xs-12" id="tutorial_text">
                    <h4 id="tutorial_title">Rule 1</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-md-12" id="tutorial_text">
                     <p>Any living cell with fewer than two living neighbours will die due to under-population in the
                     next generation.</p>
                </div>
            </div>
        </div>
    </div>

    <div class="col-md-12">
        <br/>
        <h4>Tip:</h4>
        <p>Why not put three living cells together? Your pattern will last longer and you could create some very
            interesting results.</p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-xs hidden-sm" id="button_left">
        <p><a href="/tutorial-1" class="btn btn-primary btn-large">Back</a></p>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-xs hidden-sm" id="button_right">
        <p><a href="/tutorial-3" class="btn btn-primary btn-large">Next</a></p>
    </div>
</%block>

<%block name="demonstration">
    <div class="col-md-12 col-md-offset-2">
       <h1> <img src="static/images/Rule1.gif" alt="Rule One demonstration" class="img-responsive"/> </h1>
        <div class="row visible-xs visible-sm">
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_left">
                <p><a href="/tutorial-1" class="btn btn-primary btn-large">Back</a></p>
            </div>
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_right">
                <p><a href="/tutorial-3" class="btn btn-primary btn-large">Next</a></p>
            </div>
        </div>
    </div>
</%block>