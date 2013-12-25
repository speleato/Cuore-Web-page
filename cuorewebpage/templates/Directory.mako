<h1>Cuore Directory</h1>
<%
    from py2neo import neo4j, ogm
    from database_config import db_config
    #from ..Model.Person import Company, Department, Title, Person

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


    class Title(object):
        def __init__(self, name=None):
            self.name=name
            #self.permissions=permissions

        def __str__(self):
            return self.name


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

    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)

    department = store.load_related(store.load_unique("Company", "name", "Cuore", Company), "UNDER", Department)
    '''
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
    '''
%>

%for i in department:
    <h2>${i.name}</h2>
    <%
        title = store.load_related(store.load_unique("Department", "name", i.name, Department), "IN", Title)
        '''
        title=list()
        tx.append("MATCH (a),(b) WHERE  (b:Department)-->(a:Title) AND b.name='"+i+"' RETURN a.name")
        result1=tx.execute()
        for j in result1[0]:
            node=j.values
            x,=node
            title.append(str(x))
        '''
    %>
    %for j in title:
        <h3>${j.name}</h3>
        <%
        person = store.load_related(store.load_unique("Title", "name", j, Title), "IS A", Person)
        '''
        person=list()
        tx.append("MATCH (a),(b) WHERE  (b:Title)-->(a) AND b.name='"+j+"' RETURN a.first_name")
        result1=tx.execute()
        for k in result1[0]:
            node=k.values
            x,=node
            person.append(str(x))
        '''
        %>
        %for k in person:
            <%doc>add link to person's profile, i think can be done using get and then rendering the profile with the
                        name as a parameter</%doc>
            <a href="/profile?email=${k.email}">${k.first_name}</a>
        %endfor
    %endfor
%endfor
