from py2neo import neo4j, ogm, node, rel

from database_config import *
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Event import Event
from cuorewebpage.Model.Workspace import Workspace
from cuorewebpage.lib.session import *

from cuorewebpage.Model.Department import *
from cuorewebpage.Model.Title import Title
from cuorewebpage.Model.Blog import Blog
from cuorewebpage.Model.Task import Task

# Class  : User
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	__init__(self) 									- Constructor
#	3) 	getNode(self)									- Returns the User Node
#	4) 	__str__(self) 									- for Print, returns name of User
#	5) 	getFirstName(self) 								- Returns first name of User
#	5) 	setFirstName(self) 								- Sets first name of User
#	6) 	getLastName(self) 								- Returns last name of User
#	6) 	setLastName(self) 								- Sets last name of User
#	7) 	getFullName(self) 								- Returns full name of User
#	7) 	getEmail(self)  								- Returns full name of User
#	7) 	setEmail(self)   								- Returns full name of User
#	4) 	...getters and setters for the various properties...
#       ...
#       ...
#       ...
#       ...
# Properties:
#   1) uid                                              - Unique ID from OneID Auth
#   2) first_name                                       - first name
#   3) last_name                                        - last name
#   4) email                                            - email address
#   5) phone                                            - phone number
#   6) address                                          - street address
#   7) city
#   8) state
#   9) zipcode                                          - zipcode
#  10) about                                            - about section for User
#  11) photo                                            - profile picture
#  12) photo_t                                          - profile thumbnail
#  13) req_title                                        - requested Title
#  14) req_dept                                         - requested Department
#  15) confirmed                                        - 1 User Confirmed 2 Leo Confirmed 3 Both
#  16)

# Relationships:
# 1) Affiliations
#    (self)<-[:REL_HASUSER]-(Title)<-[:REL_HASTITLE]<-(Department)<-[:REL_HASDEP]<-(Company)
# 2) Blogs
#    (self)<-[:REL_CREATEDBY]<-(Post)<-[:REL_HASPOST]<-(Blog)<-[:REL_HASBLOG]<-(Department)
#    (self)<-[:REL_CREATEDBY]<-(Post)<-[:REL_HASPOST]<-(Blog)<-[:REL_HASBLOG]<-(Company)
# 3) Calendar
#    (self)->[:REL_HASCAL]->(Calendar)->[:REL_HASEVENT]->(Event)->[:REL_CREATEDBY]->(self or User)
# 4) Workspace
#    (self)->[:REL_HASWORKSPACE]->(Workspace)->[:REL_HASPROJECT]->(Project)
#       ^                                                            |
#       |                                                            v
#       '----------------[:REL_ASSIGNEDTO]  <- (task)  <-[:REL_HASTASK]
# 5) Messages (future)


class User:
    graph_db = None
    store = None
    userInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.store = ogm.Store(self.graph_db)

    # Function  : Constructor
    # Arguments : URI of Existing User Node OR UID of User
    def __init__(self, URI=None, uid=None, first_name=None, last_name=None,
                 email=None, phone=None, address=None, city=None, state=None, zipcode=None,
                 about=None, photo=None, req_title=None, req_dept=None, confirmed=None, equity_rate=None):
        global LBL_USER, IND_USER
        self.db_init()
        tempUser = None
        if URI is not None:
            tempUser = neo4j.Node(URI)
        elif uid is not None:
            tempUser = self.graph_db.get_or_create_indexed_node(IND_USER, 'uid', uid, {"uid": uid})
            tempUser.add_labels(LBL_USER)

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
        if equity_rate is not None:
            self.userInstance['equity_rate'] = equity_rate


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

    # =================== Property Getters & Setters ========================

    # Function  : getUID
    # Arguments :
    # Returns   : uid of user
    def getUID(self):
        if self.userInstance is not None:
            return self.userInstance['uid']
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

    # Function  : getPhone
    # Arguments :
    # Returns   : (String) phone
    def getPhone(self):
        return self.userInstance['phone']

    # Function  : getAddress
    # Arguments :
    # Returns   : (String) address
    def getAddress(self):
        return self.userInstance['address']

    # Function  : getCity
    # Arguments :
    # Returns   : (String) city
    def getCity(self):
        return self.userInstance['city']

    # Function  : getState
    # Arguments :
    # Returns   : (String) state
    def getState(self):
        return self.userInstance['state']

    # Function  : getZipcode
    # Arguments :
    # Returns   : (String) zipcode
    def getZipcode(self):
        return self.userInstance['zipcode']

    # Function  : getAbout
    # Arguments :
    # Returns   : (String) about
    def getAbout(self):
        return self.userInstance['about']

    # Function  : getPhoto
    # Arguments :
    # Returns   : (String) profile picture url
    def getPhoto(self):
        return self.userInstance['photo']

    # Function  : getReqTitle
    # Arguments :
    # Returns   : (String) requested title
    def getReqTitle(self):
        return self.userInstance['req_title']

    # Function  : getReqDept
    # Arguments :
    # Returns   : (String) requested department
    def getReqDept(self):
        return self.userInstance['req_dept']

     # Function  : getConfirmed
    # Arguments :
    # Returns   : (Number (probably integer?)) confirmation status
    def getConfirmed(self):
        return self.userInstance['confirmed']

    # Function  : getEquityRate
    # Arguments :
    # Returns   : equity rate
    def getEquityRate(self):
        return self.userInstance['equity_rate']

    # =================== Relationship Getters & Setters ====================
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

    def removeTitle(self, title_object):
        if LBL_TITLES in title_object.getNode().get_labels():
            for i in self.getNode().match(REL_HASUSER, title_object.getNode()):
                i.delete()
            # if no longer given a title, attach to unassigned node
            count = 0
            for i in self.getNode().match(REL_HASUSER):
                count += 1
            if count == 0:
                unassigned_node = self.graph_db.get_or_create_indexed_node(IND_UNASSIGNED, "name", "unassigned", {"name":"unassigned"})
                self.getNode().get_or_create_path(REL_UNASSIGNED, unassigned_node)
        else:
            raise Exception("The Object Provided is not a Title")

    # Function  : getTitles
    # Arguments :
    # Returns   : list of titles nodes associated with self
    def getTitles(self):
        global REL_HASUSER
        titles = list()
        if self.userInstance.match_incoming(REL_HASUSER) is not None:
            for rels in list(self.userInstance.match_incoming(REL_HASUSER)):
                titles.append(rels.start_node)
        return titles

    # Function  : getTitle
    # Arguments :
    # Returns   : desired title node of user
    def getTitle(self, name):
        for t in self.getTitles():
            if Title(t).getName() == name:
                return t
        return None

    # Function  : getDepartments
    # Arguments :
    # Returns   : list of department nodes associated w/ self
    def getDepartments(self):
        departments = list()
        if self.getTitles() is not None:
            for t in self.getTitles():
                departments.extend(Title(t).getDepartments())
        return departments

    # Function  : getDepartment
    # Arguments :
    # Returns   : the desired department the user belongs to
    def getDepartment(self, name):
        for d in self.getDepartments():
            if Department(d).getName() == name:
                return d
        return None

    # ---------------------------------------------------------------Blogs---

    # Function  : getDepBlogs
    # Arguments :
    # Returns   : list of blog nodes associated with user's departments
    def getDepBlogs(self):
        global REL_HASBLOG
        blogs = list()
        for dep in self.getDepartments():
                blogs.extend(Department(dep).getBlog())
        return blogs

    # Function  : getDepBlog
    # Arguments :
    # Returns   : the blog belonging to user's department (not-Admin)
    def getDepBlog(self):
        return Blog(self.getDepBlogs()[0])

    # Function  : getMergedBlogPosts
    # Arguments :
    # Returns   : list of post nodes from all blogs User is subscribed to -
    #             Company wide and department based
    def getMainDepBlogPosts(self):
        blogs = list()
        for dep in self.getDepartments():
            if Department(dep).getName() != "Admin":
                blogs.append(dep)
        posts = list()
        for b in blogs:
            posts.extend(Blog(b).getPosts())
        return posts

    # Function  : getMergedBlogPosts
    # Arguments :
    # Returns   : list of post nodes from all blogs User is subscribed to -
    #             Company wide and department based
    def getMergedBlogPosts(self):
        blogs = list()
        blogs.append(Blog(Name="Cuore").getNode())
        blogs.extend(self.getDepBlogs())
        posts = list()
        for b in blogs:
            posts.extend(Blog(b).getPosts())
        return posts

    # -----------------------------------------------------------Dashboard---

    # -------------------------------------------------------------Profile---

    # ------------------------------------------------------------Calendar---

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
        if self.getDepartments() is not None and len(self.getDepartments()) > 0:
            return Department(self.getDepartments()[0]).getWorkspace()
        else:
            return None

    def getInvitedEvents(self):
        global REL_INVITED
        events = list()
        for relationship in list(self.userInstance.match_incoming(REL_INVITED)):
            events.append(Event(URI=relationship.start_node))
        return events

    def getAssignedTasks(self):
        global REL_ASSIGNEDTO
        tasks = list()
        for relationship in list(self.userInstance.match_incoming(REL_ASSIGNEDTO)):
            tasks.append(Task(URI=relationship.start_node))
        return tasks
    # ------------------------------------------------------------Workspace--


    # =================== Miscellaneous Methods =============================

    # Function  : removeUser
    # Arguments :
    # Returns   :
    # Descript: : deletes user from neo4j db
    def removeUser(self):
        self.store.delete(self)

    def isAdmin(self):
        for i in self.getDepartments():
            if Department(i).getName() == "Admin" or Department(i).getName() == "admin":
                return True
        return False


# ---------------------------- NON MEMBER FUNCTIONS -------------------------

# Function: getUser
# Arguments: uid
# Returns: User object from db with uid provided
def getUser(userID):
    #graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    #store = ogm.Store(graph_db)
    #return store.load_unique(IND_USER, "uid", uid, User)
    return User(uid=userID)

# Function: getCurrentUser
# Arguments: request
# Returns: User object of current user w/ uid if found, otherwise returns none
def getCurrentUser(request):
    if isUserLoggedOn(request):
        graph_db = neo4j.GraphDatabaseService(db_config['uri'])
        # Check to see if user already registered. Note: don't use User(uid=request.session['uid']) to do this check
        #       since it will create a node if it doesn't already exist (basically returns a false positive/clutters db)
        if graph_db.get_indexed_node(IND_USER, 'uid', request.session['uid']):
            return User(uid=request.session['uid'])
    return None

# Function: getUserBlog
# Arguments: request
# Returns: Blog object of current user (just the first one found at this point,
#          for the purpose of keeping it simple and getting the functionality working!
def getUserBlog(request):
    if isUserLoggedOn(request):
        user = User(uid=request.session['uid'])
        blogs = list()
        for d in list(user.getDepartments()):
            blog = Blog(d.getBlog()[0])
            #return None

            print "==========================================================================="
            '''
            print "USER:        " + user.getFullName()
            print "TITLE:       " + title.getName()
            '''
            print "DEPARTMENT:  " + d.getName()
            print "BLOG:        " + blog.getName()
            print "==========================================================================="
        return blog
