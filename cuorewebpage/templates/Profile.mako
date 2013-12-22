<%
    #get_info_from_db using ${name}
    from py2neo import cypher
    session = cypher.Session("http://localhost:7474")
    tx = session.create_transaction()
    name=request.GET.getone('name')
    print name
    tx.append("MATCH (n) WHERE n.first_name='"+name+"' RETURN n.first_name, n.last_name, n.email")
    result=tx.execute()
    info=list()
    for i in result[0]:
        node=i.values
        #print node
        #print type(node)
        x,y,z=node
        info.append(str(x))
        info.append(str(y))
        info.append(str(z))
%>
%for i in info:
    <h3>${i}</h3>
%endfor
