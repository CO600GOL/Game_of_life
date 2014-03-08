## The overarching template file with headers anmd more
<%inherit file="projectconway:templates/template.mako" />

<%block name="content">
	<link href="static/css/projectConway.css" rel="stylesheet">

	<div class="container">
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
                <p>Each year, the UKC School of Computing sets its final-year students the daunting task that is the
                CO600 Project. The limits of this project depend only on the interests of the lecturers and students involved
                with the module that year. The project is the final educational chance each student has of proving their
                worth to the industry.</p>
                <p>The four UKC Computing students involved in this project; Richard Lancaster, Michael Wilson, Geoff Dodds
                and Niklas Scholz, chose to participate in this particular project for a wide variety of reasons. It proved
                an interesting challenge, both technically and educationally, with every one of them having to learn and
                adapt in order to keep up with the huge amount of work needed to succeed.</p>
                <p>Still, the result of their hard work has seen every piece of software, from the engine that runs the display
                to the logic of the website, meticulously developed and rigorously tested, ensuring the best possible quality
                for both the project leaders and the end users.</p>
	    	</div>
	    	<div class="col-md-4">
	        	<img src="static/images/ukcschoolofcomputing.jpg" alt="UKC School of Computing Logo" class="img-responsive"/>
	    	</div>
		</div>

        <div class="row">
	    	<div class="col-md-12">
	        	<h2>The Deeson Group</h2>
	    	</div>
		</div>

        <div class="row">
	    	<div class="col-md-8">
                <h4>About Deeson Online:</h4>
                <p>Deeson Online has built some of the UK's biggest websites for e-commerce, community and the third
                    sector. Our clients include: Robbie Williams, Jimmy Page, Brit Awards, ITV Press Centre and Johnson
                    & Johnson. We foster a partnership approach where we lead clients to innovative solutions. Follow
                    us on @deeson_labs.</p>

                <h4>Why are we involved in this project?</h4>
                <p>We’re involved with this project for many reasons including giving students the opportunity
                to work with a commercial organisation, and the chance to collaborate with the art world... but the more
                juicy stuff is yet to be discovered. Which makes it particularly exciting. Why? Because even though we're
                not entirely sure what's going to fall from this, we know learning through experimentation is critical to
                discovering new ideas and trends in technology. So experiment we shall.</p>
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
	
		<div class="row">
	    	<div class="col-md-12">
	        	<h2>Tinkersoc</h2>
	    	</div>
		</div>
	
		<div class="row">
	    	<div class="col-md-8">
                <p>Tinkersoc is the 'maker' society at the University of Kent. It is the society where you can build,
                    hack and (sometimes) blow things up.</p>
                <p> During the summer Tinkersoc made a call out for project ideas and sponsors to the local community
                    and that is where Deesons Online got involved and this ultimately led to the creation of Project
                    Conway! Although the GOL display is being built by Daniel Knox (president of Tinkersoc and a
                    supervisor of the School of Computing software project), the society regularly gets involved with
                    design and the building of parts for the display.</p>
                <p>To contact Tinkersoc, send an email to committee@tinkersoc.org or checkout their site tinkersoc.org
                    for more details.</p>
	    	</div>
	    	<div class="col-md-4">
	        	<img src="static/images/tinkersoc.png" alt="Tinkersoc Logo" class="img-responsive"/>
	    	</div>
		</div>
	</div>
</%block>