<%inherit file="cuorewebpage:templates/Base.mako"/>

<%
    #get_info_from_db using ${email}
    from py2neo import neo4j, ogm
    from database_config import db_config

    from cuorewebpage.Model.Person import Person

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    email=request.GET.getone('email')
    print email
    print type(email)
    person = store.load_unique("People", "email", email, Person)
%>


<h1>${person.first_name} ${person.last_name}</h1>
<h2>${person.title}</h2>
<h3>${person.email}</h3>
