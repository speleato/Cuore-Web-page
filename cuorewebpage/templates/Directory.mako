<h1>Cuore Directory</h1>
<%
    from py2neo import cypher
    session = cypher.Session("http://localhost:7474")
    tx = session.create_transaction()
    tx.append("MATCH (n) WHERE (n:Department) RETURN n.name")
    result=tx.execute()
    department=list()
    for i in result[0]:
        node=i.values
        #print node
        #print type(node)
        x,=node
        department.append(str(x))
%>
%for i in department:
    <h2>${i}</h2>
    <%
    title=list()
    tx.append("MATCH (a),(b) WHERE  (a:Title)-->(b:Department) AND b.name='"+i+"' RETURN a.name")
    result1=tx.execute()
    for j in result1[0]:
        node=j.values
        x,=node
        title.append(str(x))
    %>
    %for j in title:
        <h3>${j}</h3>
        <%
        person=list()
        tx.append("MATCH (a),(b) WHERE  (a:Person)-->(b:Title) AND b.name='"+j+"' RETURN a.first_name")
        result1=tx.execute()
        for k in result1[0]:
            node=k.values
            x,=node
            person.append(str(x))
        %>
        %for k in person:
            <h4>${k}</h4>
            <%doc>add link to person's profile, i think can be done using get and then rendering the profile with the
                        name as a parameter
              <a href="/profile?name=${k}">${k}</a></%doc>
        %endfor
    %endfor
%endfor