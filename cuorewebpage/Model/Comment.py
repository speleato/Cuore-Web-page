from database_config import *
from py2neo import neo4j, node
import json

# Class  : Blog
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Blog Node
#	3) 	getName(self) 									- Returns name of blog
#	4) 	setDescription(self, description)				- Takes description as a string
#   5)  getDescription(self)                            - Returns description
#   6)  setContent(self, content)                       - Takes content in as a string
#   7)  getContent(self)                                - Returns content as a string
#   8)  setTime(self, time)                             - Set the time of when the post was created (in millis)
#   9)  getTime(self)                                   - Gets the time in millis
#	12)	setOwner(self, owner)							- owner is a node, Owner.getNode()
#	13)	getOwner(self)									- Returns a User Node
# Constants:

class Post:
    graph_db = None
    instance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

    #
    # Function	: getNode
    # Arguments	:
    # Returns	: instance Node
    #
    def getNode(self):
        return self.instance

    #
    # Function	: Constructor
    # Arguments	: Uri of Existing Blog Node OR Name of Blog
    #
    def __init__(self, URI=None, Name=None, Content=None, Owner=None):
        global LBL_COMMENT
        self.db_init()
        temp = None
        if URI is not None:
            temp = neo4j.Node(URI)

        elif Name is not None:
            temp, = self.graph_db.create({"name": Name})
            temp.add_labels(LBL_COMMENT)

        else:
            raise Exception("Name or URI not specified")

        self.instance = temp

        if Content is not None:
            self.instance["content"] = Content

        if Owner is not None:
            global REL_CREATEDBY, LBL_USER
            if LBL_USER in Owner.get_labels():
                self.instance.get_or_create_path(REL_CREATEDBY, Owner)
            else:
                raise Exception("The Node Provided is not a User")

    #
    # Function	: getName
    # Arguments	:
    # Returns	: name of blog
    #
    def getName(self):
        if self.instance is not None:
            return self.instance["name"]
        else:
            return None

    #
    # Function	: setDescription
    # Arguments	: (String) description
    #
    def setDescription(self, description):
        self.instance["description"] = description

    #
    # Function	: getDescription
    # Arguments	:
    # Returns	: (String) description
    #
    def getDescription(self):
        return self.instance["description"]

    #
    # Function	: setContent
    # Arguments	: String content
    # Returns	:
    #
    def setContent(self, content):
        self.instance["content"] = content

    #
    # Function	: getContent
    # Arguments	:
    # Returns	: (String) content
    #
    def getContent(self):
        return self.instance["content"]

    #
    # Function	: setTime
    # Arguments	: String time (in milliseconds)
    # Returns	:
    #
    def setTime(self, time):
        self.instance["time"] = time
    #
    # Function	: getTime
    # Arguments	:
    # Returns	: (String) time
    #
    def getTime(self):
        return self.instance["time"]

    #
    # Function	: setOwner
    # Arguments	: (User Node) owner
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def setOwner(self, owner):
        global HAS_OWNER, LBL_USER
        if LBL_USER in owner.get_labels():
            return self.instance.get_or_create_path(REL_HASOWNER, owner)
        else:
            raise Exception("The Node Provided is not a User")

    #
    # Function	: getOwner
    # Arguments	:
    # Returns	: a Owner Node or None (if there is no node)
    #
    def getOwner(self):
        global REL_HASOWNER
        relationships = list(self.instance.match_outgoing(REL_HASOWNER))
        if len(relationships) != 0:
            return relationships[0].end_node
        else:
            return None
