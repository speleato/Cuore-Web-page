<h1>Admin Panel</h1>
<form action="/adminpanel" method="post">
    Search by name, group (department or title), or email:
    <input type="text" name="search">
    <input type="submit" name="searchType" value="Search">
    Or:
    <input type="submit" name="searchType" value="Get All Unconfirmed">
    Or:
    <input type="submit" name="searchType" value="Get All">
</form>
<%
    #get_info_from_db using ${email}
    from py2neo import neo4j, ogm, cypher
    from database_config import db_config

    from cuorewebpage.Model.Person import Person, Title, Department, Company

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)
%>
%if request.POST:
    %if request.POST.getone("searchType")=="Get All":
        <%
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
                    <form action="/registration" method="post">
                        <input type="text" name="user" hidden value="${k.email}">
                        <input type="submit" value="Edit ${k.first_name} ${k.last_name}'s info">
                    </form>
                %endfor
            %endfor
        %endfor
        <h2>Unconfirmed People</h2>
        <%
        unconfirmed=[]
        for k in graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed").match("IS"):
            unconfirmed.append(store.load(Person, k.start_node))
        %>
        %for k in unconfirmed:
            <form action="/registration" method="post">
                <input type="text" name="user" hidden value="${k.email}">
                <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
            </form>
        %endfor
    %elif request.POST.getone("searchType")=="Get All Unconfirmed":
        <h2>Unconfirmed People</h2>
        <%
        unconfirmed=[]
        for k in graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed").match("IS"):
            unconfirmed.append(store.load(Person, k.start_node))
        %>
        %for k in unconfirmed:
            <form action="/registration" method="post">
                <input type="text" name="user" hidden value="${k.email}">
                <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
            </form>
        %endfor
    %else:
        <%
        from string import split, find, strip

        query=strip(request.POST.getone('search'))
        if find(query,'@')!=-1:
            nodes = store.load_indexed("People", "email", query, Person)
            print nodes
            print 1
        elif find(query, ' ')!=-1:
            session = cypher.Session("http://localhost:7474")
            tx = session.create_transaction()
            tx.append ('MATCH a WHERE a.first_name="'+query.split(' ')[0]+'" and a.last_name="'+query.split(' ')[1]+'" RETURN a')
            nodes = [store.load(Person, tx.commit()[0][0].values[0])]
            print nodes
            print 2
        else:
            nodes = store.load_indexed("Department", "name", query, Department)
            print nodes
            print 3
            if not (nodes):
                nodes=store.load_indexed("Title", "name", query, Title)
                print nodes
                print 4
                if not (nodes):
                    session = cypher.Session("http://localhost:7474")
                    tx = session.create_transaction()
                    tx.append ('MATCH a WHERE a.first_name="'+query+'" RETURN a')
                    nodes = [store.load(Person, tx.commit()[0][0].values[0])]

        print nodes
        print query
        %>
        %if not(nodes):
            <h2>No results found</h2>
        %elif type(nodes[0])==Department:
            %for i in nodes:
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
                        <form action="/registration" method="post">
                            <input type="text" name="user" hidden value="${k.email}">
                            %if k.confirmed < 2:
                                <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
                            %else:
                                <input type="submit" value="Edit ${k.first_name} ${k.last_name}'s info">
                            %endif
                        </form>
                    %endfor
                %endfor
            %endfor
        %elif type(nodes[0])==Title:
            %for j in nodes:
                <h2>${j.name}</h2>
                    <%
                    person = store.load_related(store.load_unique("Title", "name", j, Title), "IS A", Person)
                    %>
                    %for k in person:
                        <form action="/registration" method="post">
                            <input type="text" name="user" hidden value="${k.email}">
                            %if k.confirmed < 2:
                                <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
                            %else:
                                <input type="submit" value="Edit ${k.first_name} ${k.last_name}'s info">
                            %endif
                        </form>
                    %endfor
            %endfor
        %elif type(nodes[0])==Person:
            %for k in nodes:
                <form action="/registration" method="post">
                    <input type="text" name="user" hidden value="${k.email}">
                    %if k.confirmed < 2:
                        <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
                    %else:
                        <input type="submit" value="Edit ${k.first_name} ${k.last_name}'s info">
                    %endif
                </form>
            %endfor
        %endif
    %endif
%endif


