<h1>Cuore Directory</h1>
<%
    from py2neo import neo4j, ogm
    from database_config import db_config
    from cuorewebpage.Model.Person import Company, Department, Title, Person

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    department = store.load_related(store.load_unique("Company", "name", "Cuore", Company), "UNDER", Department)
%>

%for i in department:
    <h2>${i.name}</h2>
    <%
        title = store.load_related(store.load_unique("Department", "name", i.name, Department), "IN", Title)
    %>
    %for j in title:
        <h3>${j.name}</h3>
        <%
        person = store.load_related(store.load_unique("Title", "name", j, Title), "IS A", Person)
        %>
        %for k in person:
            <%doc>add link to person's profile, i think can be done using get and then rendering the profile with the
                        name as a parameter</%doc>
            <a href="/profile?email=${k.email}">${k.first_name}</a>
        %endfor
    %endfor
%endfor
