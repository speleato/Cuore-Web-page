from py2neo import neo4j, ogm
from database_config import *
from cuorewebpage.lib.session import *

class Title(object):
    graph_db = None
    store = None
    index = None
    titleInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.store = ogm.Store(self.graph_db)
            self.index = self.graph_db.get_or_create_index(neo4j.Node, IND_TITLE)

    def __init__(self, URI=None, name=None, dept=None):
        global LBL_TITLES, IND_TITLE
        self.db_init()
        tempTitle = None
        if URI is not None:
            tempTitle = neo4j.Node(URI)

        elif name is not None:
        #   tempTitle, = self.graph_db.create({"name": name})
            tempTitle = self.graph_db.get_or_create_indexed_node(IND_TITLE, 'name', name, {"name": name})
            tempTitle.add_labels(LBL_TITLES)
#            self.index.add("name", name, tempTitle)

        self.titleInstance = tempTitle

        if dept is not None:
            global REL_HASTITLE, LBL_DEPARTMENT
            if LBL_DEPARTMENT in dept.get_labels():
                dept.get_or_create_path(REL_HASTITLE, self.titleInstance)
            else:
                raise Exception("The Node Provided is not a Department")

    def __str__(self):
        return self.titleInstance['name']

    def getName(self):
        return self.titleInstance['name']

    # Function	: getNode
    # Arguments	:
    # Returns	: titleInstance Node
    def getNode(self):
        return self.titleInstance

    # Function: getAllUsers
    # Arguments:
    # Returns: list of User objects related to self
    def getAllUsers(self):
        return self.store.load_related(self, REL_HASUSER, User)

    #
    # Function	: setDept
    # Arguments	: (Department Node) dept
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def setDepartment(self, dept):
        global REL_HASTITLE, LBL_DEPARTMENT
        if LBL_DEPARTMENT in dept.get_labels():
            return dept.get_or_create_path(REL_HASTITLE, self.titleInstance)
        else:
            raise Exception("The Node Provided is not a Department")

    #
    # Function	: getDepartments
    # Arguments	:
    # Returns	: a list of Department objects related to self
    #
    def getDepartments(self):
        global REL_HASTITLE
        deps = list()
        for rels in list(self.titleInstance.match_incoming(REL_HASTITLE)):
            deps.append(rels.start_node)
        return deps

    #def addTitle(self, department, titleName):
    #    title=store.load_unique(IND_DEPT, "name", department, Department).getTitle(titleName)
    #    graph_db.create((user.getNode(), "UNASSIGNED", graph_db.get_or_create_indexed_node("Unassigned", "name", "unassigned")))

    # Function: safeRemoveUser
    # Arguments: email of the User (string)
    # Returns:
    # Description: safely removes the the relationship between User and selfin neo4j (attaches the people to an
    #       unassigned node)
    def safeRemoveUser(self, uid):
        user=self.getUser(uid)
        graph_db.create((user.getNode(), "UNASSIGNED", graph_db.get_or_create_indexed_node("Unassigned", "name", "unassigned")))
        for i in user.getNode().match(REL_HASTITLE):
            i.delete()
