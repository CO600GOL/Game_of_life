<!DOCTYPE html>
<html>
    <head>
        <title>Project Conway - ${title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap -->
        <link href="static/css/bootstrap.css" rel="stylesheet">

		<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
        	<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        	<script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <header class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        	<div class="container">
                <div class="GitHub-Fork">
                    <a href="https://github.com/CO600GOL/Game_of_life"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://github-camo.global.ssl.fastly.net/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"></a>
                </div>
        		<div class="navbar-header">
        			<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        				<span class="sr-only">Toggle navigation</span>
        				<span class="icon-bar"></span>
        				<span class="icon-bar"></span>
        				<span class="icon-bar"></span>
        			</button>

        			<a class="navbar-brand" href="/">Project Conway</a>
        		</div>

        		<div class="navbar-collapse collapse">
                    <ul class="nav navbar-nav">
                        <%
                        homeactive, tutorialactive, patternactive, aboutactive = [""] * 4
                        if page == "homepage":
                            homeactive = "active"
                        elif page == "tutorial1page":
                        	tutorialactive = "active"
                        elif page == "patternpage":
                            patternactive = "active"
                        elif page == "aboutpage":
                            aboutactive = "active"
                        %>
                        <li class="${tutorialactive}"><a href="/tutorial-1">Tutorial</a></li>
                        <li class="${patternactive}"><a href="/create">Create Pattern</a></li>
                        <li class="${aboutactive}"><a href="/about">About</a></li>
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="http://deeson-online.co.uk/" target="_blank">Deeson Online</a></li>
                    </ul>
                </div><!--/.nav-collapse -->
        	</div>
        </header>

       	<%block name="content" />

       	<header class="navbar navbar-inverse navbar-fixed-bottom" role="banner">
       		<div class="container">
				<div class="navbar-header">
					<%
         			import datetime
         			year = str(datetime.datetime.now().year)
                	%>

                	<ul class="nav navbar-nav">
             			<li><a>© Deeson Group ${year}</a></li>
                	</ul>
            	</div>
            </div>
        </header>

    	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    	<script src="https://code.jquery.com/jquery.js"></script>
        <%block name="grid_init_scripts" />
        <%block name="scripts" />
    	<!-- Include all compiled plugins (below), or include individual files as needed -->
    	<script src="static/js/bootstrap/bootstrap.js"></script>
    </body>
</html>