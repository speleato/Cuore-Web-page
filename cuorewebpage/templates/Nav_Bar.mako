<!DOCTYPE html>
<html class="sidebar_default no-js" lang="en">
    <head>
                            <!-- Le styles -->
                            <link href="js/plugins/chosen/chosen/chosen.css" rel="stylesheet">
                                <link href="css/twitter/bootstrap.css" rel="stylesheet">
                                    <link href="css/base.css" rel="stylesheet">
                                        <link href="css/twitter/responsive.css" rel="stylesheet">
                                            <link href="css/jquery-ui-1.8.23.custom.css" rel="stylesheet">
                                                <script src="js/plugins/modernizr.custom.32549.js"></script>
                                                <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
                                                <!--[if lt IE 9]>
                                                 <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
                                                 <![endif]-->
    </head>

    <body>
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
                <li class="accordion-group  color_4"> <a class="dashboard " href="index.html"><img src="img/menu_icons/dashboard.png"><span>Dashboard</span></a> </li>
                <li class="accordion-group color_7"> <a class="accordion-toggle widgets collapsed" data-toggle="collapse" data-parent="#sidebar_menu" href="#collapse1"> <img src="img/menu_icons/forms.png"><span>Directory</span></a>
                    <ul id="collapse1" class="accordion-body collapse">
                        <li><a href="tables_static.html">Profile</a></li>
                        <li><a href="tables_static.html">Groups</a></li>
                    </ul>
                <li class="accordion-group color_3 active"> <a class="accordion-toggle widgets collapsed" data-toggle="collapse" data-parent="#sidebar_menu" href="#collapse2"> <img src="img/menu_icons/widgets.png"><span>Workspace</span></a>
                    <ul id="collapse2" class="accordion-body collapse">
                        <li><a href="tables_static.html">Files</a></li>
                        <li><a href="tables_static.html">Calendar</a></li>
                        <li><a href="tables_static.html">Tasks</a></li>
                    </ul>
                <li class="color_13"> <a class="widgets" href="calendar2.html"> <img src="img/menu_icons/calendar.png"><span>Idea Center</span></a> </li>
                <li class="color_10"> <a class="widgets"data-parent="#sidebar_menu" href="maps.html"> <img src="img/menu_icons/maps.png"><span>CMS</span></a> </li>
                <li class="accordion-group color_12"> <a class="widgets" data-toggle="collapse" data-parent="#sidebar_menu" href="#collapse3"> <img src="img/menu_icons/tables.png"><span>Store</span></a> </li>
                <li class="color_24"> <a class="widgets"data-parent="#sidebar_menu" href="grid.html"> <img src="img/menu_icons/grid.png"><span>Jobs</span></a> </li>
                <li class="accordion-group color_19"> <a class="widgets" data-toggle="collapse" data-parent="#sidebar_menu" href="#collapse4"> <img src="img/menu_icons/statistics.png"><span>Support</span></a> </li>
                <li class="color_8"> <a class="widgets"data-parent="#sidebar_menu" href="media.html"> <img src="img/menu_icons/gallery.png"><span>Contact Us</span></a> </li>
                <li class="accordion-group color_25"> <a class="widgets" data-toggle="collapse" data-parent="#sidebar_menu" href="#collapse5"> <img src="img/menu_icons/others.png"><span>Logout</span></a> </li>
            </ul>
            <div class="menu_states row-fluid container ">
                <h2 class="pull-left">Menu Settings</h2>
                <div class="options pull-right">
                    <button id="menu_state_1" class="color_4" rel="tooltip" data-state ="sidebar_icons" data-placement="top" data-original-title="Icon Menu">1</button>
                    <button id="menu_state_2" class="color_4 active" rel="tooltip" data-state ="sidebar_default" data-placement="top" data-original-title="Fixed Menu">2</button>
                    <button id="menu_state_3" class="color_4" rel="tooltip" data-placement="top" data-state ="sidebar_hover" data-original-title="Floating on Hover Menu">3</button>
                </div>
            </div>
            <!-- End sidebar_box -->
        </div>
    </div>
</div>

<!-- Le javascript
 ================================================== -->
<!-- General scripts -->
<script src="js/jquery.js" type="text/javascript"> </script>
<!--[if !IE]> -->
<script src="js/plugins/enquire.min.js" type="text/javascript"></script>
<!-- <![endif]-->
<script language="javascript" type="text/javascript" src="js/plugins/jquery.sparkline.min.js"></script>
<script src="js/plugins/excanvas.compiled.js" type="text/javascript"></script>
<script src="js/bootstrap-transition.js" type="text/javascript"></script>
<script src="js/bootstrap-alert.js" type="text/javascript"></script>
<script src="js/bootstrap-modal.js" type="text/javascript"></script>
<script src="js/bootstrap-dropdown.js" type="text/javascript"></script>
<script src="js/bootstrap-scrollspy.js" type="text/javascript"></script>
<script src="js/bootstrap-tab.js" type="text/javascript"></script>
<script src="js/bootstrap-tooltip.js" type="text/javascript"></script>
<script src="js/bootstrap-popover.js" type="text/javascript"></script>
<script src="js/bootstrap-button.js" type="text/javascript"></script>
<script src="js/bootstrap-collapse.js" type="text/javascript"></script>
<script src="js/bootstrap-carousel.js" type="text/javascript"></script>
<script src="js/bootstrap-typeahead.js" type="text/javascript"></script>
<script src="js/bootstrap-affix.js" type="text/javascript"></script>
<script src="js/fileinput.jquery.js" type="text/javascript"></script>
<script src="js/jquery-ui-1.8.23.custom.min.js" type="text/javascript"></script>
<script src="js/jquery.touchdown.js" type="text/javascript"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.uniform.min.js"></script>
<script language="javascript" type="text/javascript" src="js/plugins/jquery.tinyscrollbar.min.js"></script>
<script language="javascript" type="text/javascript" src="js/jnavigate.jquery.min.js"></script>
<script language="javascript" type="text/javascript" src="js/jquery.touchSwipe.min.js"></script>
    <script language="javascript" type="text/javascript" src="js/plugins/jquery.peity.min.js"></script>