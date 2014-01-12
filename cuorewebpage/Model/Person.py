from py2neo import neo4j, ogm
from database_config import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

class Company(object):
    def __init__(self, name=None):
        self.name=name

    def __str__(self):
        return self.name

    # Function: getAllDepartments
    # Arguments:
    # Returns: list of Department objects related to self
    def getAllDepartments(self):
        return store.load_related(self, REL_HASDEP, Department)

    # Function: getDepartment
    # Arguments: name of department to be returned (string)
    # Returns: requested Department object related to self
    def getDepartment(self, name):
        return store.load_unique(IND_DEP, "name", name, Department)

    # Function: getNode
    # Arguments:
    # Returns: the neo4j node object of self (needed for graph_db.create function)
    def getNode(self):
        return graph_db.get_indexed_node(IND_COMP, "name", self.name)

    # Function: addDepartment
    # Arguments: name of the department (string)
    # Returns:
    # Description: creates a related department node in neo4j with the given name if it doesn't already exist
    def addDepartment(self, name):
        newDep = Department(name)
        if not (self.getDepartment(name)):
            store.save_unique(IND_DEP, "name", newDep.name, newDep)
            graph_db.create((self.getNode(), REL_HASDEP, newDep.getNode()))

    # Function: removeDepartment
    # Arguments: name of the department (string)
    # Returns:
    # Description: deletes a related department node and all associated titles, safely removes the people associated
    #       with those titles (attaches the people to an unassigned node)
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

    # Function: getAllTitles
    # Arguments:
    # Returns: list of Title objects related to self
    def getAllTitles(self):
        return store.load_related(self, REL_HASTITLE, Title)

    # Function: getTitle
    # Arguments: name of Title (string)
    # Returns: requested related Title object
    def getTitle(self, name):
        return store.load_unique(IND_TITLE, "name", name, Title)

    # Function: getNode
    # Arguments:
    # Returns: the neo4j node object of self (needed for graph_db.create function)
    def getNode(self):
        return graph_db.get_indexed_node(IND_DEP, "name", self.name)

    # Function: addTitle
    # Arguments: name of Title (string)
    # Returns:
    # Description: creates a related Title node in neo4j with the given name if it doesn't already exist
    def addTitle(self, name):
        newTitle = Title(name)
        if not (store.load_indexed(IND_TITLE, "name", newTitle.name, newTitle)):
            store.save_unique(IND_TITLE, "name", newTitle.name, newTitle)
            graph_db.create((self.getNode(), REL_HASTITLE, newTitle.getNode()))

    # Function: removeTitle
    # Arguments: name of the title (string)
    # Returns:
    # Description: deletes a related title node, safely removes the people related to the title (attaches the people to
    #       an unassigned node)
    def removeTitle(self, name):
        title=self.getTitle(name)
        for i in title.getAllUsers():
            title.safeRemoveUser(i.email)
        store.delete(title)

    # Function: getBlog
    # Arguments:
    # Returns: list of related blog nodes
    def getBlog (self):
        blogs = list()
        for i in self.getNode().match_outgoing(REL_HASBLOG):
            blogs.append(i.end_node)
        return blogs








class Title(object):
    def __init__(self, name=None):
        self.name=name

    def __str__(self):
        return self.name

    # Function: getAllUsers
    # Arguments:
    # Returns: list of User objects related to self
    def getAllUsers(self):
        return store.load_related(self, REL_HASUSER, User)

    # Function: getUser
    # Arguments: email of user (string)
    # Returns: requested related User object
    def getUser(self, email):
        return store.load_unique(IND_USER, "email", email, User)

    # Function: getNode
    # Arguments:
    # Returns: the neo4j node object of self (needed for graph_db.create function)
    def getNode(self):
        return graph_db.get_indexed_node(IND_TITLE, "name", self.name)

    #def addTitle(self, department, titleName):
    #    title=store.load_unique(IND_DEP, "name", department, Department).getTitle(titleName)
    #    graph_db.create((user.getNode(), "UNASSIGNED", graph_db.get_or_create_indexed_node("Unassigned", "name", "unassigned")))

    # Function: safeRemoveUser
    # Arguments: email of the User (string)
    # Returns:
    # Description: safely removes the the relationship between User and selfin neo4j (attaches the people to an
    #       unassigned node)
    def safeRemoveUser(self, email):
        user=self.getUser(email)
        graph_db.create((user.getNode(), "UNASSIGNED", graph_db.get_or_create_indexed_node("Unassigned", "name", "unassigned")))
        for i in user.getNode().match(REL_HASTITLE):
            i.delete()


# The confirmed variable represents the level of confirmation similar to chmod. 1 means user confirmed, 2 means
# Leo confirmed, and 3 means both confirmed
class User(object):
    def __init__(self, userID=None, first_name=None, last_name=None, email=None, phone=None, address=None, city=None, state=None, zipcode=None, about=None, photo=None, req_title=None, req_dep=None):
        self.userID = userID
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.confirmed = 0
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.about = about
        self.photo = photo
        self.req_title = req_title
        self.req_dep = req_dep

    def __str__(self):
        return self.first_name

    def submit_settings(self):
        store.save_unique(IND_USER, "email", self.email, self)
        return self

    def getNode(self):
        return graph_db.get_indexed_node(IND_USER, "email", self.email)

    # Function: removeUser
    # Arguments:
    # Returns:
    # Description: deletes user from neo4j db
    def removeUser(self):
        store.delete(self)

    # Function: getTitles
    # Arguments:
    # Returns: list of titles nodes associated with self
    def getTitles (self):
        titles = list()
        rels = self.getNode().match_incoming(REL_HASUSER)
        for i in rels:
            titles.append(i.start_node)
        return titles

    def getDepartments (self):
        deps = list()
        for i in self.getTitles():
            rels = i.match_incoming(REL_HASTITLE)
            for j in rels:
                deps.append(j.start_node)
        return deps

    def isAdmin(self):
        if store.load_related(self,"ADMIN", Admin):
            return True
        return False




sandy = User("Sandy", "Siththanandan", "sandymeep@gmail.com", "Applications Developer", 3)
store.save_unique(IND_USER, "email", sandy.email, sandy)
leo = User("Leo", "Schultz", "leo@cuore.io", "President", 3)
leo.submit_settings()

friends = store.load_related(sandy, "LIKES", User)
print ("Sandy likes {0}".format(" and ".join(str(f) for f in friends)))

me = store.load_unique(IND_USER, "email", sandy.email, User)
print me

president = store.load_unique(IND_USER, "email", leo.email, User)
print president

#if store.load_unique(IND_USER, "first_name", "george", User) = None:
#    print me
Kirby = User("Kirby", "Linvill", "kirby@cuore.io", "Applications Developer", 3)
Kevin = User("Kevin", "Ryan", "kevincryan23@gmail.com", "Vice President", 3)
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
    store.relate(cuore, REL_HASDEP, dep)
    for j in range(0, len(departments[i])):
        title = Title(departments[i][j][0])
        store.relate(dep, REL_HASTITLE, title)
        for k in range(1, len(departments[i][j])):
            employee = departments[i][j][k]
            print departments[i][j][k]
            print type(employee)
            store.save_unique(IND_USER, "email", employee.email, employee)
            store.relate(title, REL_HASUSER, employee)
        store.save_unique(IND_TITLE, "name", title.name, title)
    store.save_unique(IND_DEP, "name", departmentNames[i], dep)
store.save_unique(IND_COMP, "name", "Cuore", cuore)
