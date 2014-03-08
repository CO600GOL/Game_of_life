## The overarching template file with headers and more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">

    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <img src="static/images/conwaylogo.svg" alt="Project Conway logo" class="img-responsive" />
            </div>
        </div>

        <div class="row">
            <div class="col-md-7">
                <h2>Welcome to Project Conway</h2>
            </div>
        </div>

        <div class="row">
            <div class="col-md-7">
               <p>Project Conway is a fun and engaging way to discover John Conway's Game of Life!</p>
                <br />
                <p>The Game, developed by John Conway in 1970, demonstrates how a set of simple rules can
                make something that become very complicated. Using a grid, players create an initial pattern by
                specifying whether a cell is alive or dead; once the Game has begun, the life of the cell depends
                on its eight neighbours. Playing the game could not be simpler; input a pattern and watch it run.
                What makes the Game so unique and fun is that anything could happen.</p>
                <br />
                <p>Project Conway allows you to experience the Game of Life in a fun way. You can create a pattern
                on our web application, then pick a time and date to watch your pattern come to life on our unique,
                one-of-a-kind display.</p>

                <div class="row">
                    <div class="col-xs-7 col-sm-7 col-md-7">
                       <p> <a type="button" class="btn btn-primary" href="/create" id="start_button">Try it now!</a></p>
                    </div>
                </div>
            </div>

            <div class="col-md-5">
                <div class="row">
                    <div class="col-md-12 hidden-xs">
                       <iframe src="//www.youtube.com/embed/CgOcEZinQ2I" frameborder="0" allowfullscreen></iframe>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-12">
                        <h3>Working with...</h3>
                    </div>
                </div>

                <div class="row">
                    <div class="col-xs-2 col-md-2">
                        <img src="static/images/deeson-online.png" alt="Deeson Online logo" class="img-responsive" />
                    </div>

                    <div class="col-xs-7 col-md-7">
                        <img src="static/images/ukcschoolofcomputing.jpg" alt="UKC School of Computing logo" class="img-responsive" />
                    </div>

                    <div class="col-xs-3 col-md-3">
                        <img src="static/images/tinkersoc.png" alt="Tinkersoc logo" class="img-responsive" />
                    </div>
                </div>
            </div>
        </div>
	</div>
</%block>













<!--        _.---._
        .-'         '-.
     .'                 '.
    '       '.   .'       '
   / /        \ /        \ \
  '  |         :         |  '
 /   |         .         |   \
 |   \         |         /   |
 '. . \        |        / . .'
  |   .\      .'.      /.   |
  \  .  `-           -'  .  /
   '.      .. ... ..      .'
    |  `` ` .     . ` ``  |
    | .-_-.  '. .'  .-_-. |
   .'( (O) )|  :  |( (O) )'.
    \.'---'/   :   \'---'./
      \_ .'  . ' .  '. _/
     .' /             \ '.
     './ / /  / \ \  \ \.'
      : | | /|  : |  | :
      | : | \\  | '  : |
      | /\ \/ \ | : /\ :
      ' :/\ \ : ' ||  \ \
      / | /\ \| : ' \  \ \
     / / /  \/ /| :  |  \ \
    / / :   / /\ \ \ /   \ \
   ' /\ \  | /\ :.\ \    / |
   \ \ \ \ \/ / || \ \   \/
    \/  \|    \/ \/ |/ Cthulu -->