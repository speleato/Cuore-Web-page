from py2neo import neo4j, ogm
from database_config import *
from Title import Title
from Workspace import Workspace

# Class  : Department
# Methods:
#   1)  db_init(self)                                   - Private
#	2) 	__init__(self)          						- Constructor
#	3) 	__str__(self) 									- Returns informal string representation
#	4) 	getNode(self)									- Returns the Company Node
#	5) 	getName(self) 									- Returns name of company
#	6) 	setName(self, name)             				- Takes name as a string
#
# Properties:
#   1) name                                             - Company name
#
# Relationships:
# 1) Affiliations
#   [:REL_HASBLOG]->(Blog)
#      |
#    (self)-[:REL_HASTITLE]-(Title)->[:REL_HASUSER]->(User)
#      ^
#   [:REL_HASDEP]
#      |
#    (company)

class Department(object):
    graph_db = None
    store = None
    deptInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.store = ogm.Store(self.graph_db)

    def __init__(self, URI=None, name=None, company=None):
        global LBL_DEPARTMENT, IND_DEP
        self.db_init()
        tempDept = None

        if URI is not None:
            tempDept = neo4j.Node(URI)

        elif name is not None:
            tempDept = self.graph_db.get_or_create_indexed_node(IND_DEP, "name", name, {"name":name})
            tempDept.add_labels(LBL_DEPARTMENT)

        self.deptInstance = tempDept

        if company is not None:
            global LBL_COMPANY, REL_HASDEP
            if LBL_COMPANY in company.get_labels():
                company.get_or_create_path(REL_HASDEP, self.deptInstance)
            else:
                raise Exception("The Node Provided is not a Company")


    def __str__(self):
        return self.deptInstance['name']

    def getName(self):
        return self.deptInstance['name']

    # Function: getNode
    # Arguments:
    # Returns: the neo4j node object of self (needed for graph_db.create function)
    def getNode(self):
        return self.deptInstance
#        return self.graph_db.get_indexed_node(IND_DEP, "name", self.name)

    # Function: addTitle
    # Arguments: name of Title (string)
    # Returns:
    # Description: creates a related Title node in neo4j with the given name if it doesn't already exist
    def addTitle(self, name):
        newTitle = Title(name=name, dept=self.getNode())
        #if not (self.store.load_indexed(IND_TITLE, "name", newTitle.name, newTitle)):
        #    self.store.save_unique(IND_TITLE, "name", newTitle.name, newTitle)
        #    self.graph_db.create((self.getNode(), REL_HASTITLE, newTitle.getNode()))



    # Function: removeTitle
    # Arguments: name of the title (string)
    # Returns:
    # Description: deletes a related title node, safely removes the people related to the title (attaches the people to
    #       an unassigned node)
    def removeTitle(self, name):
        title=Title(name=name)
        for i in title.getAllUsers():
            title.safeRemoveUser(i.uid)
        self.store.delete(title.getNode())

    # Function  : getTitles
    # Arguments :
    # Returns   : list of Title nodes related to self
    def getTitles(self):
        global REL_HASTITLE
        titles = list()
        for t in list(self.deptInstance.match_outgoing(REL_HASTITLE)):
            titles.append(t.end_node)
        return titles

    # Function: getBlog
    # Arguments:
    # Returns: related Blog node
    def getBlog(self):
        global REL_HASOWNER
        relationships = list(self.deptInstance.match_incoming(REL_HASOWNER))
        if len(relationships) != 0:
            return relationships[0].start_node
        else:
            return None

    # Function  : getWorkspace
    # Arguments :
    # Returns   : a Workspace Object
    def getWorkspace(self):
        global REL_HASWORKSPACE
        relationship = (list(self.deptInstance.match_outgoing(REL_HASWORKSPACE)))[0]
        if relationship is not None:
            return Workspace(relationship.end_node)
        else:
            return None

    # Function  : getUsers
    # Arguments :
    # Returns   : a list with the users asociated with the current Department
    def getUsers(self):
        global REL_HASUSER
        users = list()
        for t in self.getTitles():
            users.extend(Title(t).getUsers())
        return users

    # Function  : getFiles
    # Arguments :
    # Returns   : a list with the files asociated with the current Department
    def getFiles(self):
        global REL_HASFILE
        files = list()
        for i in list(self.deptInstance.match_outgoing(REL_HASFILE)):
            files.append(i.end_node)
        return files

    # Connect a title node to self
    def addTitle(self, title_name):
        Title(name=title_name, dept=self.deptInstance)
        #if LBL_TITLES in title_object.titleInstance.get_labels():
            #self.deptInstance.get_or_create_path(REL_HASTITLE, title_object.titleInstance)
        #else:
            #raise Exception("The Node Provided is not a Title")



