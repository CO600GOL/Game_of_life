## The overarching template file with headers and more

<%inherit file="template_tutorial.mako" />

<%block name="small_text">
    <div class="col-md-12">
        <h2>Quiz! - A boring pattern</h2>
        <p>Question 1: Have a look at the pattern given. Can you guess what the next generation will be?</p>
    </div>
</%block>

<%block name="large_text">
    <div class="col-md-6 hidden-xs hidden-sm">
        <a href="/about"><img src="static/images/quiz1.png" data-toggle="modal" data-target="#correctdialog" alt="Quiz Answer A: Stay the same" class="img-responsive"/></a>
        <h3><button id="quiz1_correct" class="btn btn-primary btn-large" data-toggle="modal" data-target="#correctdialog">It will create a still life.</button></h3>
    </div>
    <div class="col-md-6 hidden-xs hidden-sm">
        <a href="/about"><img src="static/images/empty_grid.jpg" data-toggle="modal" data-target="#incorrectdialog" alt="Quiz Answer B: All the cells will die" class="img-responsive"/></a>
        <h3><button ="quiz1_incorrect" class="btn btn-primary btn-large" data-toggle="modal" data-target="#incorrectdialog">All the cells will die.</button></h3>
    </div>
    <div class="col-xs-6 col-sm-6 col-md-6 hidden-xs hidden-sm" id="button_left">
        <h3><a href="/tutorial-5" class="btn btn-primary btn-large">Back</a></h3>
    </div>

    <div class="modal fade" id="correctdialog" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">Correct!</h4>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-md-6">
                            <p>A still life will be created. The next generation will look like this:</p>
                        </div>
                        <div class="col-md-6">
                            <img src="static/images/quiz1.png" alt="Quiz Question 1 Answer: Still life created" class="img-responsive"/>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <p><a href="/tutorial-7" class="btn btn-primary btn-large">Continue</a></p>
                </div>
            </div><!-- /.modal-content -->
        </div><!-- /.modal-dialog -->
    </div><!-- /.modal -->
    <div class="modal fade" id="incorrectdialog" role="dialog" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">Wrong!</h4>
                </div>
                <div class="modal-body">
                    <div class="row">
                        <div class="col-md-6">
                            <p>A still life will be created. The next generation will look like this:</p>
                        </div>
                        <div class="col-md-6">
                            <img src="static/images/quiz1.png" alt="Quiz Question 1 Answer: Still life created" class="img-responsive"/>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <p><a href="/tutorial-7" class="btn btn-primary btn-large">Continue</a></p>
                </div>
            </div><!-- /.modal-content -->
        </div><!-- /.modal-dialog -->
    </div><!-- /.modal -->
</%block>

<%block name="demonstration">
    <div class="col-md-12 col-md-offset-2">
       <h1> <img src="static/images/quiz1.png" alt="Quiz Question 1" class="img-responsive"/> </h1>
        <div class="row visible-xs visible-sm">
            <div class="col-md-6" id="mobile_button">
                <h3><button id="quiz1_correct" class="btn btn-primary btn-large" data-toggle="modal" data-target="#correctdialog">It will create a still life.</button></h3>
                <h3><button ="quiz1_incorrect" class="btn btn-primary btn-large" data-toggle="modal" data-target="#incorrectdialog">All the cells will die.</button></h3>
            </div>
            <div class="col-xs-6 col-sm-6 col-md-6" id="button_left">
                <h3><a href="/tutorial-5" class="btn btn-primary btn-large">Back</a></h3>
            </div>
        </div>
    </div>
</%block>

