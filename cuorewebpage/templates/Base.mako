## Base.mako
<!DOCTYPE html>
<html class="sidebar_default no-js" lang="en">
<%include file="head.mako"/>

<body>
    <%include file="header.mako"/>

    ${next.body()}

    <%include file="footer.mako"/>
</body>

</html>