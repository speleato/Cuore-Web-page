from py2neo import neo4j, ogm, node, rel
from database_config import *
from cuorewebpage.Model.Department import *
from cuorewebpage.Model.Blog import *
from cuorewebpage.Model.Workspace import *

# Class  : Company
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

# Relationships:
# 1) Affiliations
#    (self)-[:REL_HASDEP]->(Department)-[:REL_HASTITLE]-(Title)->[:REL_HASUSER]->(User)
# 2) Blog
#    (self)-[:REL_HASBLOG]->(Blog)

class Company(object):
    graph_db = None
    companyInstance = None
    store = None
    index = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.store = ogm.Store(self.graph_db)
            self.index = self.graph_db.get_or_create_index(neo4j.Node, IND_COMP)

    def __init__(self, URI=None, Name=None):
        global LBL_COMPANY, IND_COMP
        self.db_init()
        tempCompany = None
        if URI is not None:
            tempCompany = neo4j.Node(URI)

        elif Name is not None:
            tempCompany = self.graph_db.get_or_create_indexed_node(IND_COMP, "name", Name, {"name": Name})
            tempCompany.add_labels(LBL_COMPANY)

        else:
            raise Exception("UID or Company Name not specified")

        self.companyInstance = tempCompany

    def __str__(self):
        if self.companyInstance is not None:
            return self.getName()
        else:
            return None

    def getName(self):
        if self.companyInstance is not None:
            return self.companyInstance['name']
        else:
            return None

    def setName(self, name):
        self.companyInstance['name'] = name

    # Function: getNode
    # Arguments:
    # Returns: the neo4j node object of self (needed for graph_db.create function)
    def getNode(self):
        return self.companyInstance

    # Function: getDepartments
    # Arguments:
    # Returns: list of Department nodes related to self
    def getDepartments(self):
        global REL_HASDEP
        depts = list()
        for relationship in list(self.companyInstance.match_outgoing(REL_HASDEP)):
            depts.append(relationship.end_node)
        return depts

    # Function: addDepartment
    # Arguments: name of the department (string)
    # Returns:
    # Description: creates a related department node in neo4j with the given name if it doesn't already exist
    def addDepartment(self, name):
        newDep = Department(name=name, company=Company(Name="Cuore").getNode())
        Blog(Name=name, Owner=newDep.getNode())
        Workspace(Name=name+" Workspace", Owner=newDep.getNode())
        #if not (self.getDepartment(name)):
        #    self.store.save_unique(IND_DEP, "name", newDep.name, newDep)
        #    self.graph_db.create((self.getNode(), REL_HASDEP, newDep.getNode()))

    # Function: removeDepartment
    # Arguments: name of the department (string)
    # Returns:
    # Description: deletes a related department node and all associated titles, safely removes the people associated
    #       with those titles (attaches the people to an unassigned node)
    def removeDepartment(self, name):
        dep = Department(name=name)
        blog = Blog(Name=name, Owner=dep.getNode())
        workspace = Workspace(Name=name+" Workspace", Owner=dep.getNode())

        for i in dep.getTitles():
            dep.removeTitle(i['name'])
        self.store.delete(dep.getNode())

        #eventually need to replace these shallow deletes w/ a deep delete
        self.store.delete(blog.getNode())
        self.store.delete(workspace.getNode())

    def getBlog(self):
        global REL_HASBLOG
        relationships = list(self.companyInstance.match_outgoing(REL_HASBLOG))
        if len(relationships) != 0:
            return relationships[0].end_node
        else:
            return None

def getCompany():
    company = Company(Name="Cuore")
    return company

def getUnconfirmed():
    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    unconfirmedNode=graph_db.get_or_create_indexed_node(IND_UNCONFIRMED, "name", "unconfirmed", {"name":"unconfirmed"})
    unconfirmed = []
    for relationship in list(unconfirmedNode.match_incoming(REL_UNCONFIRMED)):
        unconfirmed.append(relationship.start_node)
    return unconfirmed

def getUnassigned():
    graph_db = neo4j.GraphDatabaseService(db_config['uri'])
    unassignedNode = graph_db.get_or_create_indexed_node(IND_UNASSIGNED, "name", "unassigned", {"name":"unassigned"})
    unassigned = []
    for relationship in list(unassignedNode.match_incoming(REL_UNASSIGNED)):
        unassigned.append(relationship.start_node)
    return unassigned


