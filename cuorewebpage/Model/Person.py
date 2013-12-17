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

