<!DOCTYPE html>
<html>
    <head>
        <title>Project Conway</title>
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
                        <li class="active"><a href="#">Home</a></li>
                        <li><a href="#">Tutorial</a></li>
                        <li><a href="#">Create Pattern</a></li>
                        <li><a href="#">Help</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                        <li><a href="http://deeson-online.co.uk/" target="_blank">Deeson Online</a></li>
                      </ul>
                    </div><!--/.nav-collapse -->
                  </div>

            </div>
            <%block name="content" />
        </div>

    	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    	<script src="https://code.jquery.com/jquery.js"></script>
    	<!-- Include all compiled plugins (below), or include individual files as needed -->
    	<script src="static/js/bootstrap.js"></script>
    </body>
</html>