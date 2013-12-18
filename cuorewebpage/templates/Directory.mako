<h1>Cuore Directory</h1>
%for department in graph_db:
    <h2>${department}</h2>
    %for title in ${department}:
        <h3>${title}</h3>
        %for employee in ${title}:
            <h4>${employee}</h4>
            <%doc>employee info</%doc>
            <%doc>add link to person's profile, i think can be done using get and then rendering the profile with the
                    name as a parameter </%doc>
            <a href="/profile?name=${name}">${name}</a>
        %endfor
    %endfor
%endfor