## base.mako

<%namespace name="UIutil" file="UIutil.mako"/>

<!DOCTYPE html>
<html class="sidebar_default no-js" lang="en">
<%include file="head.mako"/>

<body>
${UIutil.ajax_loader()}

<%include file="cuorewebpage:templates/nav_bar.mako"/>

    <div id="main">
      <div class="container">

${next.body()}

    <div id="footer">
        <p> &copy; Cuore 2011 </p>
        <span class="company_logo"><a href="http://www.cuoretechnology.com"></a></span> </div>
    </div>

      </div>
      <!-- end class="container" -->
    </div>
    <!-- end class="main"-->

${UIutil.general_js()}
</body>
</html>
