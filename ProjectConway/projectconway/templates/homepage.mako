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
            <div class="col-md-8">
                <h2>Welcome to Project Conway</h2>
                <p>Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn. Ron cn'gha 'bthnkoth y'hah nilgh'ri, 'bthnk ph'gnaiih Chaugnar
                    Faugn hai nw naflhlirgh kn'a hai gnaiih chtenff phlegeth, ehye 'ai nog vulgtlagln ch' h'kn'a chtenff mnahn'og
                    chlirgh. NgAzathoth 'fhalma uh'e nnnkn'a f'athg ph'hupadgh, 'bthnkog ebunmayar hrii shagg grah'n, ctharanak nw
                    tharanak fhtagn. Athg naflYoggoth h'Yoggoth r'luh lw'nafh kn'a Shub-Niggurath, R'lyeh bugagl zhro Azathoth n'gha,
                    li'heeagl ebunma hrii gothaog shagg. Zhro r'luh shugg fm'latgh syha'h y'hah n'gha geb lw'nafhog, nog
                    Chaugnar Faugnnyth r'luh gotha ebunma sll'ha stell'bsna nw Hastur, geb Dagon fm'latgh f'throd n'ghft Yoggoth
                    ph'ooboshu.</p>
            </div>
        </div>

        <div class="row">
            <div class="col-xs-2 col-sm-2 col-md-2 col-xs-offset-4 col-sm-offset-5 col-md-offset-6">
                <button type="button" class="btn btn-primary" id="start_button">Try it now!</button>
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