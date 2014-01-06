<head>

<!-- Include OneID javascript API -->
<script src="//api.oneid.com/js/oneid.js"></script>

</head>
<body>

<div id="oneid-signin-button"></div>

<script type="text/javascript">
OneID.init({
 buttons: {
   "signin #oneid-signin-button": [{
     challenge: {
       "callback": "/authenticate",
       "attr": "email name"
     }
   }]
 }
});
</script>

</body>
</html>
