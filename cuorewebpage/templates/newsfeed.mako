<%inherit file="cuorewebpage:templates/layout_sidebar_default.mako"/>

<h1>Newsfeed</h1>
<div>
    % for p in posts:
    <h1>${p.getName()}</h1>
    <p>${p.getContent()}</p>
    % endfor
</div>

