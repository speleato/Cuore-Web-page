import sys

from py2neo import neo4j, ogm
from database_config import db_config

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

# Newsfeed class keeps track of the number of posts in each department, used for pagination
class Newsfeed(object):
    def __init__(self, name=None, numPosts=0):
        self.name=name
        self.numPosts=numPosts

    def __str__(self):
        return self.name


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

# The confirmed variable represents the level of confirmation similar to chmod. 1 means Leo confirmed, 2 means
# person confirmed, and 3 means both confirmed
class Person(object):
    def __init__(self, first_name=None, last_name=None, email=None, title=None, confirmed=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.confirmed = confirmed
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



sandy = Person("Sandy", "Siththanandan", "sandymeep@gmail.com", "Applications Developer", 3)
store.save_unique("People", "email", sandy.email, sandy)
chippie = Person("Chippie", "Siththanandan", "chippie.vbs@gmail.com")
lauren = Person("Lauren", "Ruge", "lruge008@gmail.com")
store.save_unique("People", "email", chippie.email, chippie)
store.save_unique("People", "email", lauren.email, lauren)
store.relate(sandy, "LIKES", chippie)
store.relate(sandy, "LIKES", lauren)
store.save(sandy)
leo = Person("Leo", "Schultz", "leo@cuore.io", "President", 3)
leo.submit_settings()

friends = store.load_related(sandy, "LIKES", Person)
print ("Sandy likes {0}".format(" and ".join(str(f) for f in friends)))

me = store.load_unique("People", "email", sandy.email, Person)
print me

president = store.load_unique("People", "email", leo.email, Person)
print president

#if store.load_unique("People", "first_name", "george", Person) = None:
#    print me

Kirby = Person("Kirby", "Linvill", "kirby@cuore.io", "Applications Developer", 3)
Kevin = Person("Kevin", "Ryan", "kevincryan23@gmail.com", "Vice President", 3)
#List of people in each position, first entry is the name of the position
President = ["President", leo]
Vice_President = ["Vice President", Kevin]
Lead_Applications_Developer = ["Lead Applications Developer"]
Applications_Developer = ["Applications Developer", Kirby, sandy]
Web_Applications_Developer = ["Web Applications Developer"]
Lead_Systems_Engineer = ["Lead Systems Engineer"]
Lead_Hardware_Engineer = ["Lead Hardware Engineer"]

#Lists of titles in each department
business = [President, Vice_President]
applications = [Lead_Applications_Developer, Applications_Developer, Web_Applications_Developer]
systems = [Lead_Systems_Engineer]
hardware = [Lead_Hardware_Engineer]

#List of departments containing the lists of titles in that department
departments = [business, applications, systems, hardware]
departmentNames = ["Business", "Applications", "Systems", "Hardware"]

#Company node tying departments together
cuore = Company("Cuore")
'''
#List of employees
Kirby = Person("Kirby", "Linvill", "kirby@cuore.io", "Applications Developer")
Kevin = Person("Kevin", "Ryan", "kevincryan23@gmail.com", "Vice President")
employees = [Kirby, Kevin]

for i in range(0, len(employees)):
    title=Title(employees[i].title)
    store.relate(title, "IS A", employees[i])
    store.save_unique("People", "email", employees[i].email, employees[i])
'''
for i in range(0, len(departments)):
    dep = Department(departmentNames[i])
    newsfeed = Newsfeed(departmentNames[i], 0)
    store.relate(cuore, "UNDER", dep)
    store.relate(dep, "NEWSFEED", newsfeed)
    for j in range(0, len(departments[i])):
        title = Title(departments[i][j][0])
        store.relate(dep, "IN", title)
        for k in range(1, len(departments[i][j])):
            employee = departments[i][j][k]
            print departments[i][j][k]
            print type(employee)
            store.save_unique("People", "email", employee.email, employee)
            store.relate(title, "IS A", employee)
        store.save_unique("Title", "name", title.name, title)
    store.save_unique("Newsfeed", "name", departmentNames[i], newsfeed)
    store.save_unique("Department", "name", departmentNames[i], dep)
store.save_unique("Company", "name", "Cuore", cuore)


'''
for i in range(0, len(employees)):
    store.relate(employees[i], "IS A", store.load_unique("Title", "name", employees[i].title, Title))
    store.save_unique("People", "email", employees[i].email, employees[i])

Same thing as above but in Cypher
neo4j.CypherQuery(graph_db, "CREATE (Business:Department{name:'Business'})").run()
neo4j.CypherQuery(graph_db, "CREATE (Systems:Department{name:'Systems'})").run()
neo4j.CypherQuery(graph_db, "CREATE (Hardware:Department{name:'Hardware'})").run()
neo4j.CypherQuery(graph_db, "CREATE (Applications:Department{name:'Applications'})").run()
neo4j.CypherQuery(graph_db, "CREATE (President:Title{name:'President'})").run()
neo4j.CypherQuery(graph_db, "CREATE (Vice_President:Title{name:'Vice President'})").run()
neo4j.CypherQuery(graph_db, "CREATE (Applications_Developer:Title{name:'Applications Developer'})").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE a:Department AND b:Title AND a.name='Business' AND b.name='President' CREATE b-[:in]->a").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE a:Department AND b:Title AND a.name='Business' AND b.name='Vice President' CREATE b-[:in]->a").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE a:Department AND b:Title AND a.name='Applications' AND b.name='Applications Developer' CREATE b-[:in]->a").run()
neo4j.CypherQuery(graph_db, "CREATE (Kirby:Person{first_name:'Kirby', last_name:'Linvill', email:'kirby@cuore.io'})").run()
neo4j.CypherQuery(graph_db, "CREATE (Kevin:Person{first_name:'Kevin', last_name:'Ryan', email:'kevincryan23@gmail.com'})").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE b:Title AND a.first_name='Leo' AND b.name='President' CREATE a-[:is_a]->b").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE b:Title AND a.first_name='Kevin' AND b.name='Vice President' CREATE a-[:is_a]->b").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE b:Title AND a.first_name='Sandy' AND b.name='Applications Developer' CREATE a-[:is_a]->b").run()
neo4j.CypherQuery(graph_db, "MATCH a,b WHERE b:Title AND a.first_name='Kirby' AND b.name='Applications Developer' CREATE a-[:is_a]->b").run()
'''