## layout_sidebar_default.mako
<%inherit file="cuorewebpage:templates/base.mako"/>
<%block name="html_tag">
<html lang="en" xmlns:og="http://ogp.me/ns#" xmlns:fb="https://www.facebook.com/2008/fbml" class="" >
</%block>
<%block name="head">
<%include file="cuorewebpage:templates/head_external.mako"/>
</%block>
<%block name="body_tag">
<body data-spy="scroll" data-target=".navbar" data-offset='64' onLoad="$.stellar();">
</%block>

<%block name="header">
    <div id="preloader">
        <div id="status">&nbsp;</div>
    </div>
<%include file="nav_bar_fixed_top.mako"/>
</%block>

${next.body()}
