from database_config import *
from py2neo import neo4j, node

# Class  : Workspace
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of the Event
#	4) 	setDescription(self, description)				- Takes description as a string
#	5)	getDescription(self)							- Returns description as a string
#	6) 	addProject(self, project)						- (Project Node) project
# 	7) 	getProjects(self)								- Returns a list of 'Node' Objects that are Projects
#	8)	addOwner(self, group)							- (User Node) group
# 	9) 	getOwner(self)      							- Returns a User Node
#

class Workspace:
    graph_db = None
    workspaceInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

    #
    # Function	: getNode
    # Arguments	:
    # Returns	: workspaceInstance Node
    #
    def getNode(self):
        return self.workspaceInstance

    #
    # Function	: Constructor
    # Arguments	: Uri of Existing Task Node OR Name of Task
    #
    def __init__(self, URI=None, Name=None, Owner=None):
        global LBL_WORKSPACE
        self.db_init()
        tempWorkspace = None
        if URI is not None:
            tempWorkspace = neo4j.Node(URI)

        elif Name is not None:
            tempWorkspace, = self.graph_db.create({"name": Name})
            tempWorkspace.add_labels(LBL_WORKSPACE)

        else:
            raise Exception("Name or URI not specified")

        if Owner is not None:
            if LBL_USER in Owner.get_labels():
                return Owner.get_or_create_path(REL_HASWORKSPACE, tempWorkspace)
            else:
                raise Exception("The Node provided is not a User")

        self.workspaceInstance = tempWorkspace

    #
    # Function	: getName
    # Arguments	:
    # Returns	: name of task
    #
    def getName(self):
        if self.workspaceInstance is not None:
            return self.workspaceInstance["name"]
        else:
            return None

    #
    # Function	: setDescription
    # Arguments	: (String) description
    #
    def setDescription(self, description):
        self.workspaceInstance["description"] = description

    #
    # Function	: getDescription
    # Arguments	:
    # Returns	: (String) description
    #
    def getDescription(self):
        return self.workspaceInstance["description"]

    #
    # Function	: addProject
    # Arguments	: Project Node
    # Returns	:
    #
    def addProject(self, project):
        global REL_HASPROJECT
        return self.workspaceInstance.get_or_create_path(REL_HASPROJECT, project)

    #
    # Function	: getProject
    # Arguments	:
    # Returns	: a list of 'Node' Objects that are Projects
    #
    def getProjects(self):
        global REL_HASPROJECT, LBL_PROJECT
        projects = list()
        for relationship in list(self.workspaceInstance.match_outgoing(REL_HASPROJECT)):
            projects.append(relationship.end_node)
        return projects

    #
    # Function	: addOwner
    # Arguments	: User Node
    # Returns	:
    #
    def addOwner(self, owner):
        global REL_HASWORKSPACE, LBL_USER
        if len(list(self.workspace.match_incoming(REL_HASWORKSPACE))) == 0:
            if LBL_USER in owner.get_labels():
                return owner.get_or_create_path(REL_HASWORKSPACE, self.workspaceInstance)
            else:
                raise Exception("The Node provided is not a User")
        else:
            raise Exception("There is already an Owner")
    #
    # Function	: getOwner
    # Arguments	:
    # Returns	: User Node or None
    #
    def getOwner(self):
        global REL_HASWORKSPACE
        relationships = list(self.workspaceInstance.match_incoming(REL_HASWORKSPACE))
        if len(relationships) is 1:
            return relationships[0]
        else:
            return None