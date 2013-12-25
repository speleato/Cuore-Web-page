<%
    #get_info_from_db using ${email}
    #from py2neo import cypher
    from py2neo import neo4j, ogm
    from database_config import db_config

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    class Person(object):
        def __init__(self, first_name=None, last_name=None, email=None, title=None):
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.title = title
            '''
            self.department = department
            self.phone = phone
            self.address = address
            self.city = city
            self.state = state
            self.zipcode = zipcode
            '''
        def __str__(self):
            return (self.first_name)

        def submit_settings(self):
            store.save_unique("People", "email", self.email, self)
            return self

    email=request.GET.getone('email')
    print email
    print type(email)
    person = store.load_unique("People", "email", email, Person)
    '''
    session = cypher.Session("http://localhost:7474")
    tx = session.create_transaction()
    email=request.GET.getone('email')
    tx.append("MATCH (n) WHERE n.email='"+email+"' RETURN n.first_name, n.last_name, n.email, n.title")
    result=tx.execute()
    info=list()
    for i in result[0]:
        node=i.values
        #print node
        #print type(node)
        a,b,c,d=node
        info.append(str(a))
        info.append(str(b))
        info.append(str(d))
    '''
%>
<h1>${person.first_name} ${person.last_name}</h1>
<h2>${person.title}</h2>
<h3>${person.email}</h3>
<%doc>
%for i in info:
    <h3>${i}</h3>
%endfor
</%doc>
