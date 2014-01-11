## layout_sidebar_default.mako
<%inherit file="cuorewebpage:templates/base.mako"/>
<%block name="html_tag">
<html class="sidebar_default  no-js" lang="en">
</%block>
<%block name="head">
<%include file="cuorewebpage:templates/head_intranet.mako"/>
</%block>

<%include file="ajax_loader.mako"/>
<%include file="cuorewebpage:templates/nav_bar_side.mako"/>
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
