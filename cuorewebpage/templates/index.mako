<head>

<!-- Include OneID javascript API -->
<script src="//api.oneid.com/js/oneid.js"></script>

</head>
<body>


<table>
    %for row in range(1,2):
        <a href="${request.route_url('Login')}">Login<a></br>
        <a href="${request.route_url('Registration')}">Registration<a></br>
        <%doc>
        <a href="${request.route_url('Admin')}">Admin<a></br>
        <a href="${request.route_url('Blog')}">Blog<a></br>
        <a href="${request.route_url('Calendar')}">Calendar<a></br>
        <a href="${request.route_url('Directory')}">Directory<a></br>
        <a href="${request.route_url('Files')}">Files<a></br>
        <a href="${request.route_url('MainPage')}">MainPage<a></br>
        <a href="${request.route_url('Profile')}">Profile<a></br>
        <a href="${request.route_url('Tasks')}">Tasks<a></br>
        <a href="${request.route_url('Workspace')}">Workspace<a></br>
        </%doc>
    %endfor
</table>

<!-- Drawing a OneID signin button on your page -->
<div id=”oneid-signin-button”></div>
<script type=”text/javascript”>
OneID.init({
  buttons: {
    "signin #oneid-signin-button": [{
      challenge: {
        "callback": "/auth/",
        "attr": "email name"
      }
    }]
  }
});
</script>

<%doc><p>And this is a data field: ${name}</p>
<p>And this is another data field: ${surname}</p>
</%doc>
<body>
