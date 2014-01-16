## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
    <div class="row">
        <div class="col-md-12">
            <h1>About...</h1>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
            <h2>UKC School of Computing</h2>
        </div>
    </div>

    <div class="row">
        <div class="col-md-8">
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
            tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna
            mollis euismod. Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
            tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna
            mollis euismod. Donec sed odio dui.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/ukcschoolofcomputing.jpg" alt="UKC School of Computing Logo" class="img-responsive"/>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
            <h2>Tinkersoc</h2>
        </div>
    </div>

    <div class="row">
        <div class="col-md-8">
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
           condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
           Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
           condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
           Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
           condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
           Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
           condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
           Donec sed odio dui.</p>
        </div>
        <div class="col-md-4">
            <img src="static/images/tinkersoc.png" alt="Tinkersoc Logo" class="img-responsive"/>
        </div>
    </div>

    <div class="row">
        <div class="col-md-12">
            <h2>The Deeson Group</h2>
        </div>
    </div>

    <div class="row">
        <div class="col-md-8">
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
            condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
            Donec sed odio dui. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
            commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
            condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
            Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
            condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
            Donec sed odio dui. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
            commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada
            magna mollis euismod. Donec sed odio dui.</p>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris
            condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod.
            Donec sed odio dui.</p>
        </div>
        <div class="col-md-1">
            <!-- N.B. Creates a buffer between the text and image columns on medium devices but is ignored on small
             and extra-small devices. -->
        </div>
        <div class="col-md-3">
            <img src="static/images/deeson-online.png" alt="Deeson Online Logo" class="img-responsive"
                 style="max-width:75%"/>
        </div>
    </div>
</%block>