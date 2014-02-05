## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
    <div class="row">
        <div class="col-md-12">
            <h1>Game of Life Rules</h1>
        </div>
    </div>
    
    <div class="row">
		<div class="col-md-12">
			<p>Conway's Game of Life is an interesting game simulating population. The game takes place on a
			grid with cells that can be either be dead or alive, each of these cells interact with its eight
			neighbours in order to determine its fate. </p>
			<p><b> The rules of the game are:</b></p>
		</div>
	</div>

    <div class="row">
        <div class="col-md-8">
            <p><h3><u>Rule 1:</u></h3> </p>
            <p>Any cell that is alive and has less than two alive neighbours will die due to under-population.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/Rule_1.gif" alt="Rule 1 diagram" class="img-responsive"/>
        </div>
    </div>

 <div class="row">
        <div class="col-md-8">
            <p><h3><u>Rule 2:</u></h3> </p>
            <p>Any cell that is alive and has two or three neighbours lives onto the next generation.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/Rule_2.gif" alt="Rule 2 diagram" class="img-responsive"/>
        </div>
    </div>
    
     <div class="row">
        <div class="col-md-8">
            <p><h3><u>Rule 3:</u></h3> </p>
            <p>Any cell that is alive and has more than three alive neighbours will die due to over-population.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/Rule_3.gif" alt="Rule 3 diagram" class="img-responsive"/>
        </div>
    </div>
    
     <div class="row">
        <div class="col-md-8">
            <p><h3><u>Rule 4:</u></h3> </p>
            <p>Any cell that is dead and has exactly three alive neighbours will become alive due to reproduction.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/Rule_4.gif" alt="Rule 4 diagram" class="img-responsive"/>
        </div>
    </div>
    
    <div class="row">
		<div class="col-md-12">
			<p><h3>Playing the game:</h3></p>
			<p>To play the game using Project Conway you will need to create a starting pattern. At first each cell will be dead,
			you can then click the cells to bring them to life. After that submit the pattern and see the game come to life
			before your very eyes.</p>
			<p>The aim of the game is to make your pattern last as long as possible, the maximum length of a project
			conway pattern is 600 turns (5 minutes).</p>
		</div>
	</div>

</%block>