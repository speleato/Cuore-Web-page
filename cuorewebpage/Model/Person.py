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

    #return a list of Department objects
    def getAllDepartments(self):
        return store.load_related(self, "DEPARTMENT", Department)

    #returns the requested department object
    def getDepartment(self, name):
        return store.load_unique("Department", "name", name, Department)

    #gets the company node as a node object for use with creating relationships
    def getNode(self):
        return graph_db.get_indexed_node("Company", "name", self.name)

    #creates a department node with the name given if it doesn't already exist
    def addDepartment(self, name):
        newDep = Department(name)
        if not (self.getDepartment(name)):
            newsfeed = Newsfeed(newDep.name, 0)
            store.relate(newDep, "NEWSFEED", newsfeed)
            store.save_unique("Newsfeed", "name", newDep.name, newsfeed)
            store.save_unique("Department", "name", newDep.name, newDep)
            graph_db.create((self.getNode(), "DEPARTMENT", newDep.getNode()))

    def removeDepartment(self, name):
        dep=self.getDepartment(name)
        store.delete(dep.getNewsfeed())
        for i in dep.getAllTitles():
            dep.removeTitle(i.name)
        store.delete(dep)


class Department(object):
    def __init__(self, name=None):
        self.name=name

    def __str__(self):
        return self.name

    def getAllTitles(self):
        return store.load_related(self, "TITLE", Title)

    #returns the requested department object
    def getTitle(self, name):
        return store.load_unique("Title", "name", name, Title)

    def getNode(self):
        return graph_db.get_indexed_node("Department", "name", self.name)

    #creates a title node with the name given if it doesn't already exist
    def addTitle(self, name):
        newTitle = Title(name)
        if not (store.load_indexed("Title", "name", newTitle.name, newTitle)):
            store.save_unique("Title", "name", newTitle.name, newTitle)
            graph_db.create((self.getNode(), "TITLE", newTitle.getNode()))

    def removeTitle(self, name):
        title=self.getTitle(name)
        for i in title.getAllPersons():
            title.safeRemovePerson(i.email)
        store.delete(title)

    def getNewsfeed(self):
        return store.load_unique("Newsfeed", "name", self.name, Newsfeed)








class Title(object):
    def __init__(self, name=None):
        self.name=name
        #self.permissions=permissions

    def __str__(self):
        return self.name

    def getAllPersons(self):
        return store.load_related(self, "PERSON", Person)

    def getPerson(self, email):
        return store.load_unique("People", "email", email, Person)

    def getNode(self):
        return graph_db.get_indexed_node("Title", "name", self.name)

    def addTitle(self, department, titleName):
        title=store.load_unique("Department", "name", department, Department).getTitle(titleName)
        graph_db.create((person.getNode(), "UNASSIGNED", graph_db.get_or_create_indexed_node("Unassigned", "name", "unassigned")))

    #removes the relationship between the person and the Title,
    def safeRemovePerson(self, email):
        person=self.getPerson(email)
        graph_db.create((person.getNode(), "UNASSIGNED", graph_db.get_or_create_indexed_node("Unassigned", "name", "unassigned")))
        for i in person.getNode().match("TITLE"):
            i.delete()


# The confirmed variable represents the level of confirmation similar to chmod. 1 means person confirmed, 2 means
# Leo confirmed, and 3 means both confirmed
class Person(object):
    def __init__(self, first_name=None, last_name=None, email=None, title=None, confirmed=0, confirmationNumber=None, department=None, phone=None, address=None, city=None, state=None, zipcode=None, about=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.confirmed = confirmed
        self.confirmationNumber = confirmationNumber
        self.department = department
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.about = about

    def __str__(self):
        return self.first_name

    def submit_settings(self):
        store.save_unique("People", "email", self.email, self)
        return self

    def getNode(self):
        return graph_db.get_indexed_node("People", "email", self.email)

    def removePerson(self):
        store.delete(self)


sandy = Person("Sandy", "Siththanandan", "sandymeep@gmail.com", "Applications Developer", 3)
store.save_unique("People", "email", sandy.email, sandy)
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

for i in range(0, len(departments)):
    dep = Department(departmentNames[i])
    newsfeed = Newsfeed(departmentNames[i], 0)
    store.relate(cuore, "DEPARTMENT", dep)
    store.relate(dep, "NEWSFEED", newsfeed)
    for j in range(0, len(departments[i])):
        title = Title(departments[i][j][0])
        store.relate(dep, "TITLE", title)
        for k in range(1, len(departments[i][j])):
            employee = departments[i][j][k]
            print departments[i][j][k]
            print type(employee)
            store.save_unique("People", "email", employee.email, employee)
            store.relate(title, "PERSON", employee)
        store.save_unique("Title", "name", title.name, title)
    store.save_unique("Newsfeed", "name", departmentNames[i], newsfeed)
    store.save_unique("Department", "name", departmentNames[i], dep)
store.save_unique("Company", "name", "Cuore", cuore)
