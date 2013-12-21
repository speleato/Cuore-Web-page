<h1>Cuore Directory</h1>
<%
    from py2neo import cypher
    session = cypher.Session("http://localhost:7474")
    tx = session.create_transaction()
    tx.append("MATCH (n) WHERE (n:Department) RETURN n.name")
    result=tx.commit()
    print result
    for i in result[0]:
        node=i.values
        print node
        print type(node)
        x,=node
        print x #gives you department, now use x to find titles
        '''tx = session.create_transaction()
        tx.append("MATCH (a),(b) WHERE  (b:Title)-->(a:Department) RETURN a.name")
        result=tx.commit()
            for j in result[0]:
                node=j.values
                print node
                print type(node)
                x,=node
                print x'''
%>
<%doc>%for :
    ${node}
    %for department in node:
        <h2>${type(department)}</h2>
        %for title in department:
            <h3>${type(title)}</h3><%doc>
            %for employee in ${title}:
                <h4>${employee}</h4>
                <%doc>employee info</%doc>
                <%doc>add link to person's profile, i think can be done using get and then rendering the profile with the
                        name as a parameter
              <a href="/profile?name=${name}">${name}</a></%doc><%doc>
            %endfor</%doc>
       <%doc> %endfor
    %endfor
%endfor</%doc>