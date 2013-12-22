import sys

from py2neo import neo4j, ogm
from database_config import db_config

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

class Person(object):
    def __init__(self, first_name=None, last_name=None, email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        '''
        self.title = title
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



sandy = Person("Sandy", "Siththanandan", "sandymeep@gmail.com")
store.save_unique("People", "email", sandy.email, sandy)
chippie = Person("Chippie", "Siththanandan", "chippie.vbs@gmail.com")
lauren = Person("Lauren", "Ruge", "lruge008@gmail.com")
store.relate(sandy, "LIKES", chippie)
store.relate(sandy, "LIKES", lauren)
store.save(sandy)
leo = Person("Leo", "Schultz", "leo@cuore.io")
leo.submit_settings()

friends = store.load_related(sandy, "LIKES", Person)
print ("Sandy likes {0}".format(" and ".join(str(f) for f in friends)))

me = store.load_unique("People", "email", sandy.email, Person)
print me

president = store.load_unique("People", "email", leo.email, Person)
print president

#if store.load_unique("People", "first_name", "george", Person) = None:
#    print me
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