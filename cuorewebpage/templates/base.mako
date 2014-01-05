## base.mako

<%namespace name="UIutil" file="UIutil.mako"/>

<!DOCTYPE html>
<html class="sidebar_default no-js" lang="en">
<%block name="head">
<%include file="head.mako"/>
</%block>

<body>
<%include file="ajax_loader.mako"/>

<%block name="nav_bar">
<%include file="cuorewebpage:templates/nav_bar.mako"/>
</%block>

    <div id="main">
      <div class="container">

<%block name="header">
<%include file="header.mako"/>
</%block>


${next.body()}

<%block name="footer">
<%include file="footer.mako"/>
</%block>

      </div>
      <!-- end class="container" -->
    </div>
    <!-- end class="main"-->

<%block name="javascript">
<%include file="general_js.mako"/>
</%block>
</body>
</html>
