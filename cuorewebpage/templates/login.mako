<head>

<!-- Include OneID javascript API -->
<script src="//api.oneid.com/js/oneid.js"></script>

</head>
<body>
<table>
    %for row in range(1,10):
        <a href="/registration"> this is a link<a></br>
    %endfor
</table>
<p>And this is a data field: ${name}</p>
<p>And this is another data field: ${surname}</p>
<body>
