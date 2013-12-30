<h1>Newsfeed</h1>
<%
    #constants to represent user's permissions
    viewDepartment = "Business"
    author = "Kirby"

    from py2neo import neo4j, ogm, cypher
    from database_config import db_config

    import datetime
    class Company(object):
        def __init__(self, name=None):
            self.name=name

        def __str__(self):
            return self.name


    class Department(object):
        def __init__(self, name=None):
            self.name=name

        def __str__(self):
            return self.name

    session = cypher.Session("http://localhost:7474")
    tx = session.create_transaction()
    tx.append ('MATCH a,b WHERE a.name="'+viewDepartment+'" and a-[:NEWS]-b RETURN b ORDER BY b.time DESC LIMIT 15')
    result = tx.execute()

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    postDepartment = store.load_related(store.load_unique("Company", "name", "Cuore", Company), "UNDER", Department)
%>
%for i in result[0]:
    <%
        # i.values[0] is a node type from neo4j
        time=datetime.datetime.fromtimestamp(i.values[0]["time"]).strftime("%B %d, %Y %I:%M%p")
    %>
    <h5>${i.values[0]["author"]} ${time}</h5>
    <p>${i.values[0]["news"]}</p>
%endfor
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