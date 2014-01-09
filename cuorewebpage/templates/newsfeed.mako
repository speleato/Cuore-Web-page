<%inherit file="cuorewebpage:templates/base.mako"/>

<h1>Newsfeed</h1>
<%
    #constants to represent user's permissions
    viewDepartment = "Business"
    author = "Kirby"

    from py2neo import neo4j, ogm, cypher
    from database_config import db_config
    from math import ceil
    import datetime
    from cuorewebpage.Model.Person import Company, Department

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])

    # get what page you're on (which 15 posts to display)
    if request.GET:
        page=int(request.GET.getone('page'))
    else:
        page=1

    #get number of total pages of posts
    numPages=int(ceil(float(graph_db.get_or_create_indexed_node("Newsfeed", "name", viewDepartment)["numPosts"])/15))+1

    session = cypher.Session("http://localhost:7474")
    tx = session.create_transaction()
    tx.append ('MATCH a,b WHERE a.name="'+viewDepartment+'" and a-[:NEWS]-b RETURN b ORDER BY b.time DESC SKIP '+str(((page-1)*15))+' LIMIT 15')
    result = tx.execute()

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    postDepartment = store.load_related(store.load_unique("Company", "name", "Cuore", Company), "DEPARTMENT", Department)
%>
%for i in result[0]:
    <%
        # i.values[0] is a node type from neo4j
        time=datetime.datetime.fromtimestamp(i.values[0]["time"]).strftime("%B %d, %Y %I:%M%p")
    %>
    <h5>${i.values[0]["author"]} ${time}</h5>
    <p>${i.values[0]["news"]}</p>
%endfor
<div>
    Page:
    %for i in range (1,numPages):
        %if page==i:
            ${i}
        %else:
            <a href="/newsfeed?page=${i}">${i}</a>
        %endif
    %endfor
</div>
<form action="/newsfeed" method="post">
    <input type="hidden" name="author" value=${author}>
    <h4>Post to Newsfeed</h4>
    <textarea name="news"></textarea>
    <h5>Post to:</h5>
    %for i in postDepartment:
        <input type="checkbox" name="postTo[]" value=${i.name}>${i.name}<br/>
    %endfor
    <input type="submit" value="submit">
</form>
