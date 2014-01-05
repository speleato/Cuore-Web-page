    <div id="sidebar" class=" collapse1 in">
        <div class="scrollbar">
            <div class="track">
                <div class="thumb">
                    <div class="end"></div>
                </div>
            </div>
        </div>
        <div class="viewport ">
            <div class="overview collapse">
                <div class="search row-fluid container">
                    <h2>Search</h2>
                    <form class="form-search">
                        <div class="input-append">
                            <input type="text" class=" search-query" placeholder="">
                            <button class="btn_search color_4">Search</button>
                        </div>
                    </form>
                </div>
                <ul id="sidebar_menu" class="navbar nav nav-list container full">
                    <li class="accordion-group color_4 active">
                        <a class="dashboard " href="${request.route_url('Dashboard')}">
                        <img src="img/menu_icons/dashboard.png"><span>Dashboard</span></a> </li>
                    <li class="accordion-group color_7">
                        <a class="accordion-toggle widgets collapsed" data-toggle="collapse"
                        data-parent="#sidebar_menu" href="#collapse1">
                        <img src="img/menu_icons/forms.png"><span>Directory</span></a>
                        <ul id="collapse1" class="accordion-body collapse">
                            <li><a href="${request.route_url('Profile')}">Profile</a></li>
                            <li><a href="${request.route_url('Directory')}">Departments</a></li>
                        </ul>
                    <li class="accordion-group color_3">
                        <a class="accordion-toggle widgets collapsed" data-toggle="collapse"
                            data-parent="#sidebar_menu" href="#collapse2">
                        <img src="img/menu_icons/widgets.png"><span>Workspace</span></a>
                        <ul id="collapse2" class="accordion-body collapse">
                            <li><a href="${request.route_url('Files')}">Files</a></li>
                            <li><a href="${request.route_url('Calendar')}">Calendar</a></li>
                            <li><a href="${request.route_url('Tasks')}">Tasks</a></li>
                        </ul>
                    <li class="color_13">
                        <a class="widgets" href="${request.route_url('IdeaCenter')}">
                        <img src="img/menu_icons/calendar.png"><span>Idea Center</span></a> </li>
                    <li class="color_10">
                        <a class="widgets"data-parent="#sidebar_menu" href="${request.route_url('CMS')}">
                        <img src="img/menu_icons/maps.png"><span>CMS</span></a> </li>
                    <li class="accordion-group color_12">
                        <a class="widgets" data-parent="#sidebar_menu" href="${request.route_url('Store')}">
                        <img src="img/menu_icons/tables.png"><span>Store</span></a> </li>
                    <li class="color_24">
                        <a class="widgets"data-parent="#sidebar_menu" href="${request.route_url('Jobs')}">
                        <img src="img/menu_icons/grid.png"><span>Jobs</span></a> </li>
                    <li class="accordion-group color_19">
                        <a class="widgets"data-parent="#sidebar_menu" href="${request.route_url('Support')}">
                        <img src="img/menu_icons/statistics.png"><span>Support</span></a> </li>
                    <li class="color_8">
                        <a class="widgets"data-parent="#sidebar_menu" href="${request.route_url('Contact')}">
                        <img src="img/menu_icons/gallery.png"><span>Contact Us</span></a> </li>
                    <li class="accordion-group color_25">
                        <a class="widgets" data-parent="#sidebar_menu" href="${request.route_url('Logout')}">
                        <img src="img/menu_icons/others.png"><span>Logout</span></a> </li>
                </ul>
                <div class="menu_states row-fluid container ">
                    <h2 class="pull-left">Menu Settings</h2>
                    <div class="options pull-right">
                        <button id="menu_state_1" class="color_4" rel="tooltip" data-state ="sidebar_icons"
                            data-placement="top" data-original-title="Icon Menu">1</button>
                        <button id="menu_state_2" class="color_4 active" rel="tooltip" data-state ="sidebar_default"
                            data-placement="top" data-original-title="Fixed Menu">2</button>
                        <button id="menu_state_3" class="color_4" rel="tooltip" data-state ="sidebar_hover"
                            data-placement="top" data-original-title="Floating on Hover Menu">3</button>
                    </div>
                </div>
            </div>
        </div>
        <!-- end viewport -->
    </div>
    <!--End sidebar -->
