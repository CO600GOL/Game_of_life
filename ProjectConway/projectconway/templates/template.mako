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
        <div class="container">
            <div class="row">
                <img src="static/images/conwaylogo.svg" alt="Project Conway logo" class="img-responsive" />
            </div>

            <div class="row">
                <div class="col-md-12">
                    <!-- NAVBAR!-->
                    <div class="navbar navbar-inverse" role="navigation">
                        <div class="navbar-header">
                            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>
                            <span class="navbar-brand">Menu</span>
                        </div>
                        <div class="navbar-collapse collapse">
                            <ul class="nav navbar-nav">
                                <%
                                homeactive, tutorialactive, patternactive, aboutactive = [""] * 4
                                if page == "homepage":
                                    homeactive = "active"
                                elif page == "tutorialpage":
                                    tutorialactive = "active"
                                elif page == "patternpage":
                                    patternactive = "active"
                                elif page == "aboutpage":
                                    aboutactive = "active"
                                %>
                                <li class="${homeactive}"><a href="/">Home</a></li>
                                <li class="${tutorialactive}"><a href="#">Tutorial</a></li>
                                <li class="${patternactive}"><a href="/create">Create Pattern</a></li>
                                <li class="${aboutactive}"><a href="/about">About</a></li>
                            </ul>
                            <ul class="nav navbar-nav navbar-right">
                                <li><a href="http://deeson-online.co.uk/" target="_blank">Deeson Online</a></li>
                            </ul>
                        </div><!--/.nav-collapse -->
                    </div>
                </div>
            </div>

            <%block name="content" />

            <div class="row">
                <div class="col-md-12">
                   <div class="navbar navbar-inverse">
                        <%
                        import datetime
                        year = str(datetime.datetime.now().year)
                        %>
                        <ul class="nav navbar-nav">
                           <li><a>© Deeson Group ${year}</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

    	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    	<script src="https://code.jquery.com/jquery.js"></script>
        <%block name="scripts" />
    	<!-- Include all compiled plugins (below), or include individual files as needed -->
    	<script src="static/js/bootstrap.js"></script>
    </body>
</html>