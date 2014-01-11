<%inherit file="cuorewebpage:templates/layout_topnav.mako"/>

<%block name="body_tag">
<body data-spy="scroll" data-target=".navbar" data-offset='64' onLoad="$.stellar();">
</%block>

		<section id="intro">
			<div class="container">
				<div class="row">
					<div class="span8 offset2 margin25">
                        <!--LOGIN STUFF-->
                        <div id="login_page">
                            <!-- Login page -->
                            <div id="login">
                                <div class="row-fluid fluid">
                                    <div class="span5"> <img src="${request.static_url('cuorewebpage:img/thumbnail_george2.jpg')}" /> </div>
                                    <div class="span7">
                                        <div class="title">
                                            <span class="name">George</span>
                                            <span class="subtitle">Locked</span>
                                        </div>
                                        <div id="oneid-signin-button"></div>
                                    </div>

                                </div>
                            </div>
                            <!-- End #login -->
                            <!-- <img src="img/ajax-loader.gif"> -->
                        </div>
                        <!-- End #loading -->
                        <!--/LOGIN STUFF-->
<!-- 						<div id="carousel_fade_intro" class="carousel slide carousel-fade">
							<div class="carousel-inner">
								<div class="active item">
									<h2>Sync Your World</h2>
								</div>
								<div class="inactive item">
									<h2>designed for portfolio, agency</h2>
								</div>
								<div class="inactive item">
									<h2>or app landing page.</h2>
								</div>
								<div class="inactive item">
									<h2>It's easy to customize</h2>
								</div>
								<div class="inactive item">
									<h2>to fit any brand.</h2>
								</div>
							</div> -->
						</div>
					</div>
				</div>
			</div>

			<div class="fadeInUp delay animated hidden-phone" id="more">
				<a href="#services-top" class="m-btn a-btn red big icn-only"><i class="icon-sort-down icon-3x pull-left"></i></a>
			</div>
		</section>
	<!--start services header-->
		<section id="services-top">
	<!--start services-desktop header-->
			<section id="services-top-desktop" class="visible-desktop" data-stellar-background-ratio="0.6" data-stellar-vertical-offset="20">
				<h1 class="header">Apps</h1>
				<p class="header">Creating a more efficient world.</p>
			</section>
	<!--start services-mobile header-->
			<section id="services-top-mobile" class="hidden-desktop">
				<h1 class="header">Apps</h1>
				<p class="header">Creating a more efficient world.</p>
			</section>
		</section>
	<!--start services-->
		<section id="services">
			<div class="container">
				<div class="row divide">
					<div class="span12">
						<ul class="thumbnails">
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-home"></i>
									<h4>Home</h4>
									<span>Sync your world</span>
									<p>Cuore Technology is a mobile device operating platform project, which aims to maximize convenience in everyday life. Cuore will target small, medium, and large businesses throughout the United States.  By year five of operations, Cuore will begin to target international businesses as well, eventually creating a single, transparent business world.  We, at Cuore, will offer multiple contract options to appeal to the different revenue streams and customer bases of every level and category of business.  These contract options will each exist in multiple forms specific to the type of business they are being marketed to as well as the business size.  The businesses will be paying for a more interactive and extensive way to obtain and work with a customer base.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-calendar"></i>
									<h4>Planner</h4>
									<span>Organize Your Life</span>
									<p>The Cuore Planner application enables the user to achieve maximum user convenience and efficiency.  It will revolve around a calendar that sets daily, weekly, monthly, yearly routines.  These routines include obligations and events such as work, travel, important dates, and annual vacations. Planner will also integrate a diet plan into the user’s everyday schedule, targeting special diet services such as Weight Watchers and Jenny Craig. The Planner will also link with the fitness section of health by building a personal work-out routine into the users schedule; providing the capability for users to customize their routine or purchase specialized workout routines such as p90x or Insanity. Another section of Cuore Planner will schedule the user’s recreation and day-to-day activities. The products and services offered by businesses will be suggested in accordance with the user’s finances, budget, and preferences.  These businesses will be able to sync their schedules with their customers, creating efficient communication.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-usd"></i>
									<h4>Money</h4>
									<span>Financial Security</span>
									<p>The Cuore Money application will conveniently service users in daily budgeting and financial management. It will utilize user finances, income, preferences, needs, diet plan, and family situation, “money” to allow for budgeting proposals and smart purchase suggestions.  The daily budgeting proposal will display to the user how much is able to be spent per day, and suggest which items should be purchased based on availability of funds and priorities indicated by the user bio.  Money will link with the user’s credit card transactions, automatically tracking their spending.  An additional link into all financial institutions and online financial sites, such as banks and investment firms, will create efficient management of user financial information.  Cuore will use the account balances and investments to calculate user credit scores and net worth, but not allow information viewing or transactions directly from the site. Money will offer an automatic savings plan, which withdraws a specified amount or percentage of paycheck income and places it into a special account.  This special account will be set aside primarily for future investments or purchases of major consumer items.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-road"></i>
									<h4>Transit</h4>
									<span>From A to B Easier</span>
									<p>Transit combines a mapping and GPS application with complete lifestyle coordination.  It allows users to link all traveling details with their planning and budget needs. Such details include traffic and transit delays, flight and public transport information, cost, and schedules, and best-mode-of-travel recommendation based upon their budget and scheduling needs.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-music"></i>
									<h4>Media</h4>
									<span>A New Approach to the Old Media Forums</span>
									<p>An online ecosystem, contained on the Cuore server, which allows for instant streaming of all television programming and movies.  Cuore Media also provides a means for users to pull news articles, books, blog posts, and videos from the internet in a format that allows for much quicker browsing than typical search engines.</p>
								</div>
									</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-stethoscope"></i>
									<h4>Health</h4>
									<span>Live Right</span>
									<p>The Coure Health application will integrate itself into the user’s physical health by collecting information on habits, body weight, height, and lifestyle.  The platform will then suggest diet plans and workouts tailored to the specific needs of each user.  Health will track the user’s current weight, progress, and commitment to the program, providing additional motivation for users to stick with their desired lifestyle.  Also provided is an environment for purchased or completely customizable plans for meals and workouts, which are then linked with the users’ schedule in Planner.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-file"></i>
									<h4>Write</h4>
									<span>Express Your Thoughts</span>
									<p>Write allows Cuore users to utilize a word processor and publish their files directly to the web without web development.  A very useful tool for activities such as creating website content and sharing blog posts.</p>
								</div>
								</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-globe"></i>
									<h4>Search</h4>
									<span>Freedom to Explore</span>
									<p>Search allows users to surf the web at greater speeds and download files at high speed data rates.  Imagine the possibilities of a mobile device with greater searching power and speed than a computer of workstation.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-comments"></i>
									<h4>Communicate</h4>
									<span></span>
									<p>Communicate links all current forms of communication into a single, easy to navigate application.  By combining communication methods such as facetime, text messaging, e-mail, phone calls, etc… this application enables users to find the most efficient means of contacting each other given each of their current availabilities.  Through linking with the planner application, communicate displays your current available means of communication upon a message receipt of any kind.  (Ex. If you are in a work meeting, all voice and video calls will be restricted while messaging and e-mail is marked available.)</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-superscript"></i>
									<h4>Calculate</h4>
									<span>Find Out Specifics</span>
									<p>A spreadsheet calculator which allows users to utilize all forms of a typical spreadsheet calculator and publish the created files directly to the internet without any web development.  Great for creation and sharing of data spreadsheets.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-table"></i>
									<h4>Graph</h4>
									<span>It's Free and Always Will Be</span>
									<p>An application that allows users to create diagrams and pictures while simultaneously writing the code for those graphics.  Graph also has the ability to act as a graphical user interface for database creation and editing.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-pencil"></i>
									<h4>Draw</h4>
									<span>It's Free and Always Will Be</span>
									<p>Creates a single application for type, picture, and PDF file editing for seamless file creation. Draw allows the user to work with type in multiple files, edit photos in an almost limitless fashion through Photoshop or Illustrator technology, and use an automated CSS code generator to aid in web development.  Users are able to find their desired font and style, and work with type in an object oriented fashion, with full scaling and styling capabilities. Draw also allows for PDF creation and editing, which provides a full document editing, protection, and conversion environment available anywhere.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-book"></i>
									<h4>Publish</h4>
									<span>It's Free and Always Will Be</span>
									<p>An application that utilizes basic printer functions and 3D printing for a wide range of product and craft creation.  Useful for the everyday printing purposes as well as professionals in the printing industry.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-headphones"></i>
									<h4>Listen</h4>
									<span>It's Free and Always Will Be</span>
									<p>An all-in-one sound editor and music player.  The listen application provides the user with the ability to edit, mix, and record tracks as well as the ability to publish and share those tracks on their computer or with the central music database.  It combines these tools with a music player than links with the central music database, along with the user’s personal music collection, allowing them to listen to any song in the world.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-edit"></i>
									<h4>Design</h4>
									<span>It's Free and Always Will Be</span>
									<p>Utilizes a computer aided design system with identical user interfaces for seamless end to end design.  The design application will provide the various CAD tool necessary for every step of the design process in a single application that also interfaces with 3D printers for the creation of a physical final product.  This application removes the hassles of file incompatibilities, eliminates the need to purchase all different CAD programs for each step of the design process, and reduces the confusion created from having to work on a project through multiple user interface.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-microphone"></i>
									<h4>Present</h4>
									<span>It's Free and Always Will Be</span>
									<p>The present application allows for a user to create any form of presentation, such as slide (like powerpoint) or fluid movement (like prezi), and easily upload them onto the web.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-film"></i>
									<h4>Watch</h4>
									<span>It's Free and Always Will Be</span>
									<p>The watch application is an all-in-one professional quality video editor.  Watch allows for video recording and editing, along with special effects creation.  It also communicates with the listen application for the purpose of importing sound to created videos.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-group"></i>
									<h4>Educate</h4>
									<span>It's Free and Always Will Be</span>
									<p>A centralized solution for all schools and universities where all data is able to be uploaded and managed in a single, easy to operate environment.  The Educate application is made to handle data such as school records, ID card information, grades, and meal plan data.  Educate even provides an environment for teachers and professors to build online learning environments and run their classes in a more effective and involved manner.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-search"></i>
									<h4>Learn</h4>
									<span>It's Free and Always Will Be</span>
									<p>The Learn application is the student end of the educate application, communicating with both the administrative and class databases for all of their needs and tasks.  Learn allows students to view their billing account, link their bill payment with their planner and budget, manage their degree, courses, and homework, and check their logged grade book.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-bullseye"></i>
									<h4>Target</h4>
									<span>It's Free and Always Will Be</span>
									<p>The Target Service allows companies to set up accounts, build pages, track marketing analytics, and market their products on Cuore.  Target service payments, per-subscriber (“Sync”) charges following the initial base fee for the marketing package, are tracked through the amount of subscribers (“Synced” users)  each company’s products, services, or stores are able to obtain. The Target service application is connected with the money application to determine if the product being marketed fits into the targeted user’s budget, and also provides for direct e-commerce within the application.</p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<i class="icon-link"></i>
									<h4>Connect</h4>
									<span>It's Free and Always Will Be</span>
									<p>The Connect service application allows companies to build and sell plans, such as workout and diet plans, that users can subscribe to.  It also provide banks, credit card companies, or creditors to bill or loan money to people when it is needed through a secure uplink to the users’ budget, finances, assets, and credit score.  Other sites will be able to link to Cuore Business, allowing Cuore users to subscribe directly to that site through their Cuore accounts, or for the site to offer their service through the Cuore application.</p>
								</div>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</section>
	<!--start works header-->
		<section id="works-top">
	<!--start works-desktop header-->
			<section id="works-top-desktop" class="visible-desktop" data-stellar-background-ratio="0.6" data-stellar-vertical-offset="20">
				<h1 class="header">System</h1>
				<p class="header">Spawning efficiency through functionality</p>
			</section>
	<!--start works-mobile header-->
			<section id="works-top-mobile" class="hidden-desktop">
				<h1 class="header">System</h1>
				<p class="header">Spawning efficiency through functionality</p>
			</section>
		</section>
	<!--start works-->
		<section id="works">
			<div class="container">
				<div class="row divide">
					<div class="span12">
						<div id="carousel_vertical_slide" class="carousel slide vertical">
							<div class="carousel-inner">
							<h1>ALAN</h1>
							<center>Asynchronous Local Area Network</center>
								<div class="active item">
									<img src="${request.static_url('cuorewebpage:img/front/system-1.png')}" alt="">
								</div>
								<div class="inactive item">
									<img src="${request.static_url('cuorewebpage:img/front/system-2.png')}" alt="">
								</div>
								<div class="inactive item">
									<img src="${request.static_url('cuorewebpage:img/front/system-3.png')}" alt="">
								</div>
							</div>
							<button class="carousel-control left m-btn icn-only" href="#carousel_vertical_slide" data-slide="prev"><i class="icon-chevron-left"></i></button>
							<button class="carousel-control right m-btn icn-only" href="#carousel_vertical_slide" data-slide="next"><i class="icon-chevron-right"></i></button>
						</div>
					</div>
					<div class="span8 offset2">
						<!--<h4>Features</h4>
						<p class="center">• Cuore uses wifi to pass touch screen inputs and outputs from the individual devices back to the server.  The server then processes the information and sends it back a different screen if anything was altered.  The server processes the data and runs the device through wifi communication rather than the device doing the work itself.  This allows for lighter, smaller and more versatile devices as most of the hardware, usually required for processing power, can be omitted.  In this way, Cuore devices have greater range in the shapes and architecture and can be designed radically different.  </p>
						<p class="center">• The server not only serves as the processing power for the devices, but also as the router.  Using the latest in wifi technology 802.11ac, the Cuore server is able to provide data rates of 1 gbps, optimal device frequency connection, and device targeted wifi beaming.</p>
						<p class="center">• The hardware that runs the server, and therefore the devices as well, is easily replaceable thanks to the Cuore’s various individual block processors- both data and graphical.</p>-->
					</div>
				</div>
				<div class="divider"></div>
				<div class="row divide">
					<div class="span12">
						<div id="carousel_horizontal_slide" class="carousel slide horizontal">
							<div class="carousel-inner">
							<h1>LusciOS</h1>
							<center>The worlds first 100% Client-Based Operating System</center>
								<div class="active item">
									<img src="${request.static_url('cuorewebpage:img/front/system-4.png')}" alt="">
								</div>
								<!--<div class="inactive item">
									<img src="${request.static_url('cuorewebpage:img/front/works_4.png')}" alt="">
								</div>
							</div>
							<button class="carousel-control left m-btn icn-only" href="#carousel_horizontal_slide" data-slide="prev"><i class="icon-chevron-left"></i></button>
							<button class="carousel-control right m-btn icn-only" href="#carousel_horizontal_slide" data-slide="next"><i class="icon-chevron-right"></i></button>
						</div>-->

						<!--<h4>Features</h4>
						<p class="center">• Contains terabytes of main memory with lower latency than RAM using a specific memory controller</p>
						<p class="center">• Fast multicore processor with 60 GB Cache Memory</p>
						<p class="center">• Highest end x86 architecture which provides 20x processing power of single computer</p>
						<p class="center">• Able to run on any device</p>
						<p class="center">• Smart home controller capabilities</p>
						<p class="center">• Ubuntu Based OS</p>
						<p class="center">• Utilizes Open Sourcing</p>
						<p class="center">• NVIDIA GRID GPU- network accelerated graphics using hypervisor technology, high power allows for multiple streaming devices</p>
						<p class="center">• Devices with 4x the resolution of HD, allowing system GPU to be experienced by the user at the highest level</p>
						<p class="center">• Ran through node use- only temporary memory sending touch inputs to the server system</p>-->
					</div>
					<!--<div class="span7 offset1">
						<p>Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are,
						the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae.
						The rset can be a toatl mses and you can sitll raed it wouthit porbelm.
						Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Awesomeness, true story!</p>
					</div>
					<div class="span2 offset1">
						<p><strong>Client:</strong> Cuore<br>
						<strong>Date:</strong> 21.02.1986
						<a href="#" class="m-btn red span2">View online</a>
					</div>-->
				<!--</div>
				<div class="divider"></div>
				<div class="row divide">
					<div class="span12">
					</div>
					<div class="span7">
						<div id="carousel_fade" class="carousel slide carousel-fade">
							<div class="carousel-inner">
								<div class="active item">
									<img src="img/front/works_5.png" alt="">
								</div>
								<div class="inactive item">
									<img src="img/front/works_6.png" alt="">
								</div>
							</div>
							<button class="carousel-control left m-btn icn-only" href="#carousel_fade" data-slide="prev"><i class="icon-chevron-left"></i></button>
							<button class="carousel-control right m-btn icn-only" href="#carousel_fade" data-slide="next"><i class="icon-chevron-right"></i></button>
						</div>
					</div>
					<!--<div class="span5 divide">
						<h1>Tons of shortcodes</h1>
						<h4>Works layout 3 + carousel with fade effect</h4>
						<p>Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are,
						the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae.
						The rset can be a toatl mses and you can sitll raed it wouthit porbelm.
						Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Awesomeness, true story!</p>
						<a href="#" class="m-btn red pull-right">View online</a>
						<p><strong>Client:</strong> Cuore<br>
						<strong>Date:</strong> 21.02.1986
					</div>
				</div>
				<div class="divider"></div>
				<div class="row divide">
					<div class="span5 divide">
						<h1>Supereasy to customize</h1>
						<h4>Works layout 3 + carousel with fade effect</h4>
						<p>Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are,
						the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae.
						The rset can be a toatl mses and you can sitll raed it wouthit porbelm.
						Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Awesomeness, true story!</p>
						<a href="#" class="m-btn red pull-right">View online</a>
						<p><strong>Client:</strong> Cuore<br>
						<strong>Date:</strong> 21.02.1986
					</div>
					<div class="span7">
						<div id="carousel_fade_2" class="carousel slide carousel-fade">
							<div class="carousel-inner">
								<div class="active item">
									<img src="img/front/works_6.png" alt="">
								</div>
								<div class="inactive item">
									<img src="img/front/works_5.png" alt="">
								</div>
							</div>
							<button class="carousel-control left m-btn icn-only" href="#carousel_fade_2" data-slide="prev"><i class="icon-chevron-left"></i></button>
							<button class="carousel-control right m-btn icn-only" href="#carousel_fade_2" data-slide="next"><i class="icon-chevron-right"></i></button>
						</div>
					</div>-->
				</div>
			</div>
		</section>
	<!--start gallery header-->
		<section id="gallery-top">
	<!--start gallery-desktop header-->
			<section id="gallery-top-desktop" class="visible-desktop" data-stellar-background-ratio="0.6" data-stellar-vertical-offset="20">
				<h1 class="header">Devices</h1>
				<p class="header">Redefining the Limits of Mobile and Personal Computing</p>
			</section>
	<!--start gallery-mobile header-->
			<section id="gallery-top-mobile" class="hidden-desktop">
				<h1 class="header">Devices</h1>
				<p class="header">Redefining the Limits of Mobile and Personal Computing</p>
			</section>
		</section>
	<!--start gallery-->
	<!--start thumbnails section-->
		<section id="gallery">
			<div class="container">
				<div class="row divide">
					<div class="span8 offset2">
						<h1>Sync Your World</h1>
						<p class="center">Thanks to the revolutionary client-based OS, the Cuore devices are lighter, faster, more powerful, and more impressive in every aspect.  They can be designed to leverage all of the new available technology in hardware, such as clear and bendable LED screens.</p>
					</div>
					<div class="span12">
						<ul class="thumbnails">
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_1" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newphone1.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_2" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newphone2.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_3" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newphone3.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_4" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newphone4.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_5" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newserver1.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_6" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newserver2.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_7" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newserver3.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_8" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newserver4.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_9" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/1tablet.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_10" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/2tablet.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_11" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/3tablet.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/4tablet.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newtv1.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newtv2.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newtv3.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newtv4.jpg')}" alt="">
									</a>
								</div>
								</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newspeaker1.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newspeaker2.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="top">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newspeaker3.jpg')}" alt="">
									</a>
								</div>
							</li>
							<li class="span3">
								<div class="thumbnail" data-thumb="tooltip" title="Click to View Larger Image" data-placement="bottom">
									<a href="#gallery_12" data-toggle="lightbox">
										<img src="${request.static_url('cuorewebpage:img/front/newspeaker4.jpg')}" alt="">
									</a>
								</div>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</section>
	<!--end thumbnails section-->
	<!--start lightboxes-->
		<div id="gallery_1" class="lightbox hide fade"  tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newphone1_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_2" class="lightbox hide fade"  tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newphone2_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_3" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newphone3_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_4" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newphone4_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_5" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/1server2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_6" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/2server2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_7" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/3server2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_8" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/4server2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_9" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/1tablet2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_10" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/2tablet2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_11" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/3tablet2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/4tablet2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newtv1_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newtv2_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newtv3_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newtv4_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newspeaker1_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newspeaker2_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newspeaker3_2x.jpg')}" alt="">
			</div>
		</div>
		<div id="gallery_12" class="lightbox hide fade" tabindex="-1" role="dialog" aria-hidden="true">
			<div class='lightbox-content'>
				<img src="${request.static_url('cuorewebpage:img/front/newspeaker4_2x.jpg')}" alt="">
			</div>
		</div>
	<!--end lightbox section-->
	<!--start team header-->
		<section id="team-top">
	<!--start team-desktop header-->
			<section id="team-top-desktop" class="visible-desktop" data-stellar-background-ratio="0.6" data-stellar-vertical-offset="20">
				<h1 class="header">Features</h1>
				<p class="header">Lighter, Faster & More Powerful</p>
			</section>
	<!--start team-mobile header-->
			<section id="team-top-mobile" class="hidden-desktop">
				<h1 class="header">Features</h1>
				<p class="header">Lighter, Faster & More Powerful</p>
			</section>
		</section>
	<!--start team-->
		<section id="team">
			<div class="container">
				<div class="row divide">
					<div class="span8 offset2">
						<h1>The Future of Computing</h1>
						<p class="center">Cuore devices are able to be lighter thanks to the elimination of the bulky data and graphical processors from the devices themselves.  The remaining hardware within the device is little more than its various specialized features (speakers/video card/ etc..) and the parts necessary to communicate with the server. Cuore’s revolutionary client-based OS transfers the data and graphical processing operations to the server, which allows for far more powerful devices in spite of their smaller and lighter design. The devices are faster, and create more impressive outputs (both graphically and data-wise). Cuore’s devices find freedom in design architecture through their lack of necessity for bulky processors.  Less hardware needed in the creation of the devices means more versatility in design shape and creative functionality. From bendable screens to clear screen displays, imagine endless possibilities.</p>
					</div>
					<div class="span12">
						<ul class="thumbnails">
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features1.jpg" alt="">
									<h4>Lighter</h4>
									<span>Replacing bulk with efficiency</span>
									<p></p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features2.jpg" alt="">
									<h4>Faster</h4>
									<span>Enhancing processing power through innovation</span>
									<p></p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features3.jpg" alt="">
									<h4>Create Versatility</h4>
									<span>Mobile never looked so good</span>
									<p></p>
								</div>
							</li>
						</ul>
					</div>
					<div class="span12">
						<ul class="thumbnails">
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features4.jpg" alt="">
									<h4>Two in One</h4>
									<span>Tablet is able to double as a laptop and the user is able to hook up a keyboard for easier use.</span>
									<p></p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features5.jpg" alt="">
									<h4>Sync</h4>
									<span>Television is synced to music and video accounts on the other devices, making it able to act as a full media player for television, music, movies, and videos.</span>
									<p></p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features6.jpg" alt="">
									<h4>Ease of Use</h4>
									<span>Devices offer smart voice command recognition. So, for the television you can ask to watch a specific program or channel. Utilizing either the phone or tablet, you can navigate all apps and input data or text.</span>
									<p></p>
								</div>
							</li>
						</ul>
					</div>
					<div class="span12">
						<ul class="thumbnails">
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features7.jpg" alt="">
									<h4>Wifi Maximized</h4>
									<span>All devices are connected to wifi and able to be controlled by other devices through that local wifi connection.</span>
									<p></p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features8.jpg" alt="">
									<h4>Wireless Speakers</h4>
									<span>The user can output the sound from any device to the speakers with the push of a button or voice command.</span>
									<p></p>
								</div>
							</li>
							<li class="span4">
								<div class="thumbnail">
									<img src="img/front/features9.jpg" alt="">
									<h4>Device Unity</h4>
									<span>There is a single session running on all devices. This allows for a session on your phone or tablet to be picked up on the television if a larger screen is needed.</span>
									<p></p>
								</div>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</section>
	<!--start contact header-->
		<section id="contact-top">
	<!--start contact-desktop header-->
			<section id="contact-top-desktop" class="visible-desktop" data-stellar-background-ratio="0.6" data-stellar-vertical-offset="20">
				<h1 class="header">Contact</h1>
				<p class="header">We look forward to hearing from you!</p>
			</section>
	<!--start contact-mobile header-->
			<section id="contact-top-mobile" class="hidden-desktop">
				<h1 class="header">Contact</h1>
				<p class="header">We look forward to hearing from you!</p>
			</section>
		</section>
	<!--start contact-->
		<section id="contact">
			<div class="container">
				<div class="row divide">
					<div class="span8">
						<div class="row">
							<form action="js/sendmail.php" method="post" id="contactForm">
								<div class="span4">
									<label>Name:</label>
									<input type="text" name="name" value="" id="name" class="span4"/>
								</div>
								<div class="span4">
									<label>Email:</label>
									<input type="text" name="email" value="" id="email"  class="span4"/>
								</div>
								<span class="honeypot">
									<label>Honeypot:</label>
									<input type="text" name="last" value="" id="last"/>
								</span>
								<div class="span8">
									<label>Message:</label>
									<textarea rows="6" name="message" class="span8"></textarea>
								</div>
								<div class="span8">
									<div class="message"><div class="alert"></div></div>
									<input type="submit" value="Send" class="m-btn green"/>
								</div>
							</form>
						</div>
					</div>
	<!--start sidebar-->
					<div class="span4" id="address">
						<b>Corporate HQ</b><br>
						<p>1144 Maryvale Dr.<br>
						Cheektowaga, NY 14221</p>
						<p>P: 716.969.0945<br>
						E: info@cuore.io</p>

						<b>Technical HQ</b><br>
						<p>500 El Camino Real - SCU 3122<br>
						Santa Clara, CA 95050</p>

						<p>E: support@cuore.io</p>
					</div>
				</div>
			</div>
		</section>
	<!--start footer-->
		<section id="footer">
			<div class="container">
				<div class="row divide">
	<!--logo and copyright-->
					<div class="span3">
						<a href="#intro" class="brand"><img src="img/front/logo-dark.png" alt="" id="footer_logo"></a><br>
						<a href="http://www.cuore-tech.com/" target="_blank" class="copywrite">2013 © Cuore Technology</a><br>
					</div>
	<!--footer menu-->
					<div class="span2 offset4">
						<ul>
							<li><h5>Menu</h5></li>
							<li><a href="#intro">Home</a></li>
							<li><a href="#services-top">Apps</a></li>
							<li><a href="#works-top">Products</a></li>
							<li><a href="#gallery-top">System</a></li>
							<li><a href="#team-top">Team</a></li>
						</ul>
					</div>
	<!--link to social networks-->
					<div class="span2 offset1">
						<ul>
							<li><h5>Social</h5></li>
							<li><a class="facebook" href="http://www.facebook.com/cuoretechnology" target="_blank">Facebook</a></li>
							<li><a class="twitter" href="http://www.twitter.com/CuoreTech" target="_blank">Twitter</a></li>
							<li><a class="google" href="https://plus.google.com/u/0/b/100775672381507910758/100775672381507910758/posts" target="_blank">Google+</a></li>
							<li><a class="instagram" href="http://www.instagram.com/" target="_blank">Instagram</a></li>
							<li><a class="pinterest" href="http://www.pinterest.com/" target="_blank">Pinterest</a></li>
						</ul>
					</div>
				</div>
			</div>
		</section>

<%block name="javascript">
	<!-- Le javascript
	    ================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<!--latest jQuery-->
		<script src="http://code.jquery.com/jquery-latest.js"></script>
	<!--main bootstrap js-->
		<script src="js/ext-bootstrap.js" type="text/javascript"></script>
	<!--custom js-->
		<script src="js/script.js" type="text/javascript"></script>
	<!--preloader-->
		<script type="text/javascript">
			$(window).load(function() {
				$("#status").fadeOut();
				$("#preloader").delay(350).fadeOut("slow");
			})
		</script>
	<!--retina support-->
		<script src="js/retina.js" type="text/javascript"></script>
	<!--smooth scroll on page-->
		<script src="js/easing.js" type="text/javascript"></script>
	<!--custom scrollbar-->
		<script src="js/scroll.js" type="text/javascript"></script>
	<!--parallax-->
		<script src="js/stellar.js" type="text/javascript"></script>
	<!--contact-->
		<script src="js/form.js"></script>
	<!--gallery lightbox-->
		<script src="js/lightbox.js"></script>
	<!--login box-->

<!--
<table>
    %for row in range(1,2):
        <a href="${request.route_url('Login')}">Login<a></br>
        <a href="${request.route_url('Registration')}">Registration<a></br>
        <a href="${request.route_url('AdminPanel')}">Admin Panel<a></br>
        <a href="${request.route_url('Blog')}">Blog<a></br>
        <a href="${request.route_url('Calendar')}">Calendar<a></br>
        <a href="${request.route_url('Directory')}">Directory<a></br>
        <a href="${request.route_url('Files')}">Files<a></br>
        <a href="${request.route_url('Profile')}">Profile<a></br>
        <a href="${request.route_url('Tasks')}">Tasks<a></br>
        <a href="${request.route_url('Workspace')}">Workspace<a></br>
    %endfor
</table>
-->


<script type=”text/javascript”>
OneID.init({
  buttons: {
    "signin #oneid-signin-button": [{
      challenge: {
        "callback": "/dashboard",
        "attr": "email name"
      }
    }]
  }
});
</script>
</%block>
