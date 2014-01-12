<head>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
</head>
<body>
<h1>Admin Panel</h1>
<form action="/adminpanel" method="post">
    <input type="text" name="addDep" value="" hidden>
    <input type="text" name="addTitle" value="" hidden>
    <input type="text" name="remDep" value="" hidden>
    <input type="text" name="remTitle" value="" hidden>

    Search by name, group (department or title), or email:
    <input type="text" name="search" value="">
    <input type="submit" name="searchType" value="Search">
    Or:
    <input type="submit" name="searchType" value="Get All Unconfirmed">
    Or:
    <input type="submit" name="searchType" value="Get All Unassigned">
    Or:
    <input type="submit" name="searchType" value="Get All">
</form>
<%
    #get_info_from_db using ${email}
    from py2neo import neo4j, ogm, cypher
    from database_config import db_config, IND_COMP, IND_DEP, IND_TITLE, IND_USER, IND_UNASSIGNED, IND_UNCONFIRMED, REL_HASTITLE, REL_UNCONFIRMED, REL_UNASSIGNED

    from cuorewebpage.Model.Person import User, Title, Department, Company

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)
%>
%if request.POST:
    %if request.POST.getone("searchType")=="Get All":
        <%
            departments = store.load_unique(IND_COMP, "name", "Cuore", Company).getAllDepartments()
        %>
        %for i in departments:
            <h2>${i.name}</h2>
            <%
                titles = i.getAllTitles()
            %>
            %for j in titles:
                <h3>${j.name}</h3>
                <%
                    users = j.getAllUsers()
                %>
                %for k in users:
                    <form action="/registration" method="post">
                        <input type="text" name="user" hidden value="${k.email}">
                        <input type="submit" value="Edit ${k.first_name} ${k.last_name}'s info">
                    </form>
                %endfor
            %endfor
        %endfor
        <h2>Unconfirmed Users</h2>
        <%
            unconfirmed=[]
            for k in graph_db.get_or_create_indexed_node(IND_UNCONFIRMED, "name", "unconfirmed").match(REL_UNCONFIRMED):
                unconfirmed.append(store.load(User, k.start_node))
        %>
        %for k in unconfirmed:
            <form action="/registration" method="post">
                <input type="text" name="user" hidden value="${k.email}">
                <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
            </form>
        %endfor
        <h2>Unassigned Users</h2>
        <%
            unassigned=[]
            for k in graph_db.get_or_create_indexed_node(IND_UNASSIGNED, "name", "unassigned").match(REL_UNASSIGNED):
                unassigned.append(store.load(User, k.start_node))
        %>
        %for k in unassigned:
            <form action="/registration" method="post">
                <input type="text" name="user" hidden value="${k.email}">
                <input type="submit" value="Assign ${k.first_name} ${k.last_name}">
            </form>
        %endfor
    %elif request.POST.getone("searchType")=="Get All Unconfirmed":
        <h2>Unconfirmed Users</h2>
        <%
            unconfirmed=[]
            for k in graph_db.get_or_create_indexed_node(IND_UNCONFIRMED, "name", "unconfirmed").match(REL_UNCONFIRMED):
                unconfirmed.append(store.load(User, k.start_node))
        %>
        %for k in unconfirmed:
            <form action="/registration" method="post">
                <input type="text" name="user" hidden value="${k.email}">
                <input type="submit" value="Confirm ${k.first_name} ${k.last_name}">
            </form>
        %endfor
    %elif request.POST.getone("searchType")=="Get All Unassigned":
        <h2>Unassigned Users</h2>
        <%
            unassigned=[]
            for k in graph_db.get_or_create_indexed_node(IND_UNASSIGNED, "name", "unassigned").match(REL_UNASSIGNED):
                unassigned.append(store.load(User, k.start_node))
        %>
        %for k in unassigned:
            <form action="/registration" method="post">
                <input type="text" name="user" hidden value="${k.email}">
                <input type="submit" value="Assign ${k.first_name} ${k.last_name}">
            </form>
        %endfor
    %elif request.POST.getone("searchType")=="Search":
        <%
        from string import split, find, strip

        query=strip(request.POST.getone('search'))
        if find(query,'@')!=-1:
            nodes = store.load_indexed(IND_USER, "email", query, User)
        elif find(query, ' ')!=-1:
            session = cypher.Session("http://localhost:7474")
            tx = session.create_transaction()
            tx.append ('MATCH a WHERE a.first_name="'+query.split(' ')[0]+'" and a.last_name="'+query.split(' ')[1]+'" RETURN a')
            nodes = [store.load(User, tx.commit()[0][0].values[0])]
        else:
            nodes = store.load_indexed(IND_DEP, "name", query, Department)
            if not (nodes):
                nodes=store.load_indexed(IND_TITLE, "name", query, Title)
                if not (nodes):
                    session = cypher.Session("http://localhost:7474")
                    tx = session.create_transaction()
                    tx.append ('MATCH a WHERE a.first_name="'+query+'" RETURN a')
                    nodes = [store.load(User, tx.commit()[0][0].values[0])]
        %>
        %if not(nodes):
            <h2>No results found</h2>
        %elif type(nodes[0])==Department:
            %for i in nodes:
                <h2>${i.name}</h2>
                <%
                title = store.load_related(store.load_unique(IND_DEP, "name", i.name, Department), REL_HASTITLE, Title)
                %>
                %for j in title:
                    <h3>${j.name}</h3>
                    <%
                    user = store.load_related(store.load_unique(IND_TITLE, "name", j, Title), REL_HASUSER, User)
                    %>
                    %for k in user:
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
                    user = store.load_related(store.load_unique(IND_TITLE, "name", j, Title), REL_HASUSER, User)
                    %>
                    %for k in user:
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
        %elif type(nodes[0])==User:
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

<form action="/adminpanel" method="post">
    <input type="text" name="searchType" value="" hidden>
    <input type="text" name="search" value="" hidden>

    Add a Department:
    <input type="text" name="addDep">
    <input type="submit" value="Add Department"><br/>

    <span>Add a Title to</span>
    <%
        departments = store.load_unique(IND_COMP, "name", "Cuore", Company).getAllDepartments()
    %>
    <select name="addToDep">
    %for i in departments:
        <option value=${i.name}>${i.name}</option>
    %endfor
    </select>
    <span>department:</span>
    <input type="text" name="addTitle">
    <input type="submit" value="Add Title"><br/>

    <span>Remove Department:</span>
    <select name="remDep">
    %for i in departments:
        <option value=${i.name}>${i.name}</option>
    %endfor
    </select>
    <input type="submit" value="Remove Department"><br/>

<%doc>
    <span>Remove Title in</span>
    <select name="remFromDep" id="remFromDep">
    %for i in departments:
        <option value=${i.name}>${i.name}</option>
    %endfor
    </select>
    <span>department:</span>
    %for i in departments:
        <select name="remTitle" id="remTitle${i.name}" style="display:none">
            <%
                titles=i.getAllTitles()
            %>
            %for j in titles:
                <option value=${j.name}>${j.name}</option>
            %endfor
    %endfor
    </select>
    <input type="submit" value="Remove Title"><br/>
</form>

<%doc> will need to use AJAX
<script>
    $("#remFromDep").change(function(){
        var department = $("#remFromDep").val();
        $("#remTitle"+department).attr("style", "display:inline");
    })
</script>
</%doc>
</body>

