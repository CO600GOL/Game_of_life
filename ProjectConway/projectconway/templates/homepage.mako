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
            <div class="col-md-12">
                <h2>Welcome to Project Conway</h2>
            </div>

            <div class="col-md-8">
                <p>Project Conway is a fun and engaging way to discover John Conway's Game of Life!</p>
                <p>Let your imagination run wild with our exciting Pattern Creator where everything is possible</p>
                <p>When you've sent your pattern, see it come to life on our unique, one of a kind light display
                screen.</p>
            </div>
            <div class="col-md-4">
                <p><iframe width="100%" height="100%" src="//www.youtube.com/embed/Iy71djXqf3E" frameborder="0"
                           allowfullscreen></iframe>
                </p>
            </div>
        </div>

        <div class="row">
            <div class="col-xs-2 col-sm-2 col-md-2 col-xs-offset-4 col-sm-offset-5 col-md-offset-6">
                <a type="button" class="btn btn-primary" href="/create" id="start_button">Try it now!</a>
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