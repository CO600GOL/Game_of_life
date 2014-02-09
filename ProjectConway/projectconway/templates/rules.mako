## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">
    <%namespace name="rule_texts" file="rule_texts.mako" />

	<div class="container">
	    <div class="row">
	        <div class="col-md-12">
	            <h1>Game of Life Rules</h1>
	        </div>
	    </div>
	    
	    <div class="row">
			<div class="col-md-12">
				<p>Conway's Game of Life is an interesting game that can simulate many things, one such use could be
                    population. The game takes place on a grid with cells that can be either be dead or alive, each of
                    these cells interact with its eight neighbours in order to determine its fate. </p>
				<p><b> The standard rules of the game are:</b></p>
			</div>
		</div>
	
	    <div class="row">
	        <div class="col-md-12">
	            <h2>Rule 1</h2>
                ${rule_texts.rule_one()}
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule1_a.jpg" alt="Rule 1 current generation diagram"
                         class="img-responsive"/></h2>
                 <p><b>Current Generation</b></p>
                </div>
            <div class="col-md-6">
                <span class="arrow-inverse-large" data-angle="90"></span>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam bibendum massa eget elementum
                    pharetra. Suspendisse convallis scelerisque elit. Aenean elit risus.</p>
            </div>
             <div class="col-md-3">
                <h2><img src="static/images/rule1_b.jpg" alt="Rule 1 next generation diagram"
                         class="img-responsive"/></h2>
                 <p><b>Next Generation</b></p>
	        </div>
	    </div>
	
	    <div class="row">
	        <div class="col-md-12">
	            <h2>Rule 2</h2>
	            ${rule_texts.rule_two()}
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule2_a.jpg" alt="Rule 2 current generation diagram"
                         class="img-responsive"/></h2>
                <p><b>Current Generation</b></p>
            </div>
            <div class="col-md-6">
                <span class="arrow"></span>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam bibendum massa eget elementum
                    pharetra. Suspendisse convallis scelerisque elit. Aenean elit risus.</p>
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule2_b.jpg" alt="Rule 2 next generation diagram"
                         class="img-responsive"/></h2>
                <p><b>Next Generation</b></p>
	        </div>
	    </div>
	    
	     <div class="row">
	        <div class="col-md-12">
	            <h2>Rule 3</h2>
	            ${rule_texts.rule_three()}
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule3_a.jpg" alt="Rule 3 current generation diagram"
                         class="img-responsive"/></h2>
                <p><b>Current Generation</b></p>
            </div>
            <div class="col-md-6">
                <span class="arrow"></span>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam bibendum massa eget elementum
                    pharetra. Suspendisse convallis scelerisque elit. Aenean elit risus.</p>
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule3_b.jpg" alt="Rule 3 next generation diagram"
                         class="img-responsive"/></h2>
                <p><b>Next Generation</b></p>
            </div>
	    </div>
	    
	     <div class="row">
	        <div class="col-md-12">
	            <h2>Rule 4</h2>
	            ${rule_texts.rule_four()}
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule4_a.jpg" alt="Rule 4 current generation diagram"
                         class="img-responsive"/></h2>
                <p><b>Current Generation</b></p>
            </div>
            <div class="col-md-6">
                <span class="arrow"></span>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam bibendum massa eget elementum
                    pharetra. Suspendisse convallis scelerisque elit. Aenean elit risus.</p>
            </div>
            <div class="col-md-3">
                <h2><img src="static/images/rule4_b.jpg" alt="Rule 4 next generation diagram"
                            class="img-responsive"/></h2>
                <p><b>Next Generation</b></p>
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
	</div>

</%block>

