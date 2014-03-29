## The overarching template file with headers and more

<%inherit file="template_tutorial.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Getting started with Project Conway!</h2>
        <p>Project Conway is an exciting new way to see John Conway's Game of Life; which is a zero player game
            - all you have to do is design a pattern and watch it come to life on our LED display!</p>
        <p>The aim of the game, is to make your pattern have a large number of different turns.</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-12">
        <div class="tutorial_box">
            <div class="row">
                <div class="col-md-12 col-xs-12" id="tutorial_text">
                    <h4 id="tutorial_title">Who was this John Conway Guy anyway?</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 col-xs-3">
                    <img src="static/images/Conway.JPG" alt="John Conway" class="img-responsive" id="image_spacing" />
                </div>
                <div class="col-md-8" id="tutorial-text">
                     <p>John Conway is a British mathematician from Liverpool. He is currently
                        a professor at Princeton University in America. As well as the
                        Game of Life, he is also known for the look-and-say sequence.
                        The Game of Life has become the defining feature of the academic's career.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-12">
        <br/>
        <p>The game is very simple but becomes more complex as it evolves.
            All you need to do is input a pattern using our website,
            the game will run on a display. When designing a pattern, it might
            be a good idea to take into account the rules - which we will teach you in this tutorial!</p>
    </div>
    <div class="col-xs-12 col-sm-12 col-md-12" id="button_right">
        <p><a href="/tutorial-2" class="btn btn-primary btn-large">Start Here!</a></p>
    </div>
</%block>

<%block name="demonstration">
    <div class="col-md-12 col-md-offset-2 hidden-xs hidden-sm">
       <h1> <img src="static/images/octagon.gif" alt="Octagon based pattern" class="img-responsive"/> </h1>
    </div>
</%block>