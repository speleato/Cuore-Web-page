from py2neo import neo4j, ogm
from database_config import *

# Class  : Department
# Methods:
#   1)  db_init(self)                                   - Private
#	2) 	__init__(self)          						- Constructor
#	3) 	__str__(self) 									- Returns informal string representation
#	4) 	getNode(self)									- Returns the Company Node
#	5) 	getName(self) 									- Returns name of company
#	6) 	setName(self, name)             				- Takes name as a string
#
class Department(object):
    graph_db = None
    store = None
    deptInstance = None
    index = None
    schema = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.store = ogm.Store(self.graph_db)
            #self.index = self.graph_db.get_or_create_index(neo4j.Node, IND_DEP)
            #self.schema = self.graph_db.schema.create_index(IND_DEP, "name")

    def __init__(self, URI=None, name=None, company=None):
        global LBL_DEPARTMENT, IND_DEP
        self.db_init()
        tempDept = None

        if URI is not None:
            tempDept = neo4j.Node(URI)

        elif name is not None:
            #tempDept = self.index.get_or_create("name", name, {"name": name})
#            tempDept, = self.graph_db.create({"name": name})
            tempDept = self.graph_db.get_or_create_indexed_node(IND_DEP, "name", name, {"name":name})
            tempDept.add_labels(LBL_DEPARTMENT)
            #self.store.save_unique(IND_DEP, "name", name, tempDept)
            #self.index.add("name", name, tempDept)

        self.deptInstance = tempDept

        if company is not None:
            global LBL_COMPANY, REL_HASDEP
            if LBL_COMPANY in company.get_labels():
                company.get_or_create_path(REL_HASDEP, self.deptInstance)
#                self.deptInstance.get_or_create_path(REL_HASDEP, company)
            else:
                raise Exception("The Node Provided is not a Company")


    def __str__(self):
        return self.deptInstance['name']

    def getName(self):
        return self.deptInstance['name']
    # Function  : getAllTitles
    # Arguments :
    # Returns   : list of Title objects related to self
    def getAllTitles(self):
        global REL_HASTITLE
        titles = list()
        rels = self.getNode().match_outgoing(REL_HASTITLE)
        for i in rels:
            titles.append(i.end_node)
        return titles
        #return self.store.load_related(self, REL_HASTITLE, Title)

    # Function  : getTitle
    # Arguments : name of Title (string)
    # Returns   : requested related Title object
    def getTitle(self, name):
        return self.store.load_unique(IND_TITLE, "name", name, Title)

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
            title.safeRemoveUser(i.uid)
        store.delete(title)

    # Function: getBlog
    # Arguments:
    # Returns: list of related blog nodes
    def getBlog (self):
        global REL_HASOWNER
        blogs = list()
        for rel in list(self.deptInstance.match_incoming(REL_HASOWNER)):
            blogs.append(rel.start_node)
        return blogs




