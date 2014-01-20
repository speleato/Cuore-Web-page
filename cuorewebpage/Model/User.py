from py2neo import neo4j, ogm, node, rel
from pyramid import request
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Workspace import Workspace

from database_config import *
from cuorewebpage.lib.session import *
from cuorewebpage.Model.Department import Department
from cuorewebpage.Model.Title import Title
from cuorewebpage.Model.Blog import Blog

# Class  : User
# Methods:
#	1) 	db_init(self) 									- Private
#	1) 	__init__(self) 									- Constructor
#	1) 	__str__(self) 									- for Print, returns name of User
#	2) 	getNode(self)									- Returns the User Node
#	3) 	getName(self) 									- Returns first name of User
#	4) 	...getters and setters for the various properties...
#       ...
#       ...
#       ...
#       ...

# Constants:
# The confirmed variable represents the level of confirmation similar to chmod. 1 means user confirmed, 2 means
# Leo confirmed, and 3 means both confirmed

class User:
    graph_db = None
    store = None
    userInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.store = ogm.Store(self.graph_db)
#            self.index = self.graph_db.schema.create_index(IND_USER, "name")

    # Function  : Constructor
    # Arguments : URI of Existing User Node OR UID of User
    def __init__(self, URI=None, uid=None, first_name=None, last_name=None,
                 email=None, phone=None, address=None, city=None, state=None, zipcode=None,
                 about=None, photo=None, req_title=None, req_dept=None, confirmed=None):
        global LBL_USER, IND_USER
        self.db_init()
        tempUser = None

        if URI is not None:
            tempUser = neo4j.Node(URI)

        elif uid is not None:
            tempUser = self.graph_db.get_or_create_indexed_node(IND_USER, 'uid', uid, {"uid": uid})
            tempUser.add_labels(LBL_USER)
#            tempUser, = self.graph_db.create({"uid": uid})

        #else:
        #    raise Exception("UID or URI not specified")

        self.userInstance = tempUser

        if uid is not None:
            self.userInstance['uid'] = uid
        if first_name is not None:
            self.userInstance['first_name'] = first_name
        if last_name is not None:
            self.userInstance['last_name'] = last_name
        if email is not None:
            self.userInstance['email'] = email
        if phone is not None:
            self.userInstance['phone'] = phone
        if address is not None:
            self.userInstance['address'] = address
        if city is not None:
            self.userInstance['city'] = city
        if state is not None:
            self.userInstance['state'] = state
        if zipcode is not None:
            self.userInstance['zipcode'] = zipcode
        if about is not None:
            self.userInstance['about'] = about
        if photo is not None:
            self.userInstance['photo'] = photo
        if req_title is not None:
            self.userInstance['req_title'] = req_title
        if req_dept is not None:
            self.userInstance['req_dept'] = req_dept
        if confirmed is not None:
            self.userInstance['confirmed'] = confirmed

    def __str__(self):
        if self.userInstance is not None:
            return self.userInstance['first_name']
        else:
            return None

    # Function	: getNode
    # Arguments	:
    # Returns	: userInstance Node
    def getNode(self):
        return self.userInstance

    # Function  : getUID
    # Arguments :
    # Returns   : uid of user
    def getUID(self):
        if self.userInstance is not None:
            return self.userInstance['UID']
        else:
            return None

    # Function  : setFirstName
    # Arguments : (String) first_name
    def setFirstName(self, first_name):
        self.userInstance['first_name'] = first_name

    # Function  : getFirstName
    # Arguments :
    # Returns   : (String) first_name
    def getFirstName(self):
        return self.userInstance['first_name']

    # Function  : setLastName
    # Arguments : (String) last_name
    def setLastName(self, last_name):
        self.userInstance['last_name'] = last_name

    # Function  : getLastName
    # Arguments :
    # Returns   : (String) last_name
    def getLastName(self):
        return self.userInstance['last_name']

    # Function  : getFullName
    # Arguments :
    # Returns   : (String) first_name + last_name
    def getFullName(self):
        full_name = self.userInstance['first_name'] + " " + self.userInstance['last_name']
        return full_name

    # Function  : setEmail
    # Arguments : (String) email
    def setEmail(self, email):
        self.userInstance['email'] = email

    # Function  : getEmail
    # Arguments :
    # Returns   : (String) email
    def getEmail(self):
        return self.userInstance['email']

    # Function  : removeUser
    # Arguments :
    # Returns   :
    # Descript: : deletes user from neo4j db
    def removeUser(self):
        self.store.delete(self)

    # Function  : setTitle
    # Arguments : (Title Node) job_title
    # Returns   : a 'Path' object containing nodes and relationships used
    def setTitle(self, job_title):
        global REL_HASUSER, LBL_TITLES
        if LBL_TITLES in job_title.get_labels():
            return self.userInstance.get_or_create_path(REL_HASUSER, job_title)
        else:
            raise Exception("The Node Provided is not a Title")

    # Function  : getTitles
    # Arguments :
    # Returns   : list of titles nodes associated with self
    def getTitles(self):
        global REL_HASUSER
        titles = list()
        for rels in list(self.userInstance.match_incoming(REL_HASUSER)):
            titles.append(rels.start_node)
        return titles[0]

    # Function  : getDepBlog
    # Arguments :
    # Returns   : list of blog nodes associated with user's departments
    def getBlog(self):
        global REL_HASBLOG
        blogs = list()
        for dep in self.getDepartments():
                blogs.append(dep.getBlog())
        return blogs

    def isAdmin(self):
        for i in self.getDepartments():
            if i.getName() == "Admin":
                return True
        return False

    # Function : getCalendar
    # Arguments :
    # Returns : a Calendar Object
    def getCalendar(self):
        global REL_HASCALENDAR
        relationship = (list(self.userInstance.match_outgoing(REL_HASCALENDAR)))[0]
        if relationship is not None:
            return Calendar(relationship.end_node)
        else:
            return None
    # Function  : getWorkspace
    # Arguments :
    # Returns   : a Workspace Object
    def getWorkspace(self):
        global REL_HASWORKSPACE
        relationship = (list(self.userInstance.match_outgoing(REL_HASWORKSPACE)))[0]
        if relationship is not None:
            return Workspace(relationship.end_node)
        else:
            return None

# ---------------------------- NON MEMBER FUNCTIONS -------------------------

# Function: getUser
# Arguments: uid
# Returns: User object from db with uid provided
def getUser(uid):
    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    store = ogm.Store(graph_db)
    return store.load_unique(IND_USER, "uid", uid, User)

# Function: getCurrentUser
# Arguments: request
# Returns: User object of current user w/ uid if found, otherwise returns none
def getCurrentUser(request):
    if isUserLoggedOn(request):
#        return getUser(request.session["uid"])
        graph_db = neo4j.GraphDatabaseService(db_config['uri'])
        store = ogm.Store(graph_db)
        return store.load_unique(IND_USER, "uid", request.session['uid'], User)
    return None

# Function: getUserBlog
# Arguments: request
# Returns: Blog object of current user (just the first one found at this point,
#          for the purpose of keeping it simple and getting the functionality working!
def getUserBlog(request):
    if isUserLoggedOn(request):
        user = User(uid=request.session['uid'])
        title = Title(user.getTitles())
        department = Department(title.getDepartments()[0])
        blog = Blog(department.getBlog()[0])
        print "==========================================================================="
        print "USER:        " + user.getFullName()
        print "TITLE:       " + title.getName()
        print "DEPARTMENT:  " + department.getName()
        print "BLOG:        " + blog.getName()
        print "==========================================================================="
        return blog
    return None
