## layout.mako
<div id="loading"><img src="${request.static_url('cuorewebpage:img/ajax-loader.gif')}"></div>
<div id="responsive_part">
    <div class="logo"> <a href="index.html"><img src="${request.static_url('cuorewebpage:img/logo.png')}"/></a> </div>
    <ul class="nav responsive">
      <li><button class="btn responsive_menu icon_item" data-toggle="collapse" data-target=".overview">
      <i class="icon-reorder"></i> </button>
      </li>
    </ul>
</div>
<!-- Responsive part -->

<%include file="cuorewebpage:templates/nav_bar.mako"/>

<div id="main">
  <div class="container">
    <div class="header row-fluid">
      <div class="logo"> <a href="index.html"><span>Cuore</span><span class="icon"></span></a> </div>
      <div class="top_right">
        <ul class="nav nav_menu">
          <li class="dropdown"> <a class="dropdown-toggle administrator" id="dLabel" role="button" data-toggle="dropdown" data-target="#" href="/page.html">
            <div class="title"><span class="name">George</span><span class="subtitle">Future Buyer</span></div>
            <span class="icon"><img src="img/thumbnail_george.jpg"></span></a>
            <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
              <li><a href="profile.html"><i class=" icon-user"></i> My Profile</a></li>
              <li><a href="forms_general.html"><i class=" icon-cog"></i>Settings</a></li>
              <li><a href="index2.html"><i class=" icon-unlock"></i>Log Out</a></li>
              <li><a href="search.html"><i class=" icon-flag"></i>Help</a></li>
            </ul>
          </li>
        </ul>
      </div>
      <!-- End top-right --> 
    </div>