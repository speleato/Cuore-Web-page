from database_config import *
from py2neo import neo4j, node
import json

# Class  : Blog
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Comment Node
#	3) 	getName(self) 									- Returns name of Comment
#	4) 	setDescription(self, description)				- Takes description as a string
#   5)  getDescription(self)                            - Returns description
#   6)  setContent(self, content)                       - Takes content in as a string
#   7)  getContent(self)                                - Returns content as a string
#   8)  setTime(self, time)                             - Set the time of when the post was created (in millis)
#   9)  getTime(self)                                   - Gets the time in millis
#	12)	setOwner(self, owner)							- owner is a User node, Owner.getNode()
#	13)	getOwner(self)									- Returns a User Node
# Constants:

class Comment:
    graph_db = None
    commentInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

    #
    # Function	: getNode
    # Arguments	:
    # Returns	: instance Node
    #
    def getNode(self):
        return self.commentInstance

    #
    # Function	: Constructor
    # Arguments	: Uri of Existing Blog Node OR Name of Blog
    #
    def __init__(self, URI=None, Name=None, Content=None, Owner=None, Parent=None):
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

        self.commentInstance = temp

        if Content is not None:
            self.commentInstance["content"] = Content

        if Owner is not None:
            global REL_CREATEDBY, LBL_USER
            if LBL_USER in Owner.get_labels():
                self.commentInstance.get_or_create_path(REL_CREATEDBY, Owner)
            else:
                raise Exception("The Node Provided is not a User")

        if Parent is not None:
            global REL_HASCOMMENT, LBL_TASK, LBL_POST, LBL_EVENT
            if (LBL_TASK in Parent.get_labels()) or (LBL_POST in Parent.get_labels()):
                Parent.get_or_create_path(REL_HASCOMMENT, self.commentInstance)

    #
    # Function	: getName
    # Arguments	:
    # Returns	: name of blog
    #
    def getName(self):
        if self.commentInstance is not None:
            return self.commentInstance["name"]
        else:
            return None

    #
    # Function	: setDescription
    # Arguments	: (String) description
    #
    def setDescription(self, description):
        self.commentInstance["description"] = description

    #
    # Function	: getDescription
    # Arguments	:
    # Returns	: (String) description
    #
    def getDescription(self):
        return self.commentInstance["description"]

    #
    # Function	: setContent
    # Arguments	: String content
    # Returns	:
    #
    def setContent(self, content):
        self.commentInstance["content"] = content

    #
    # Function	: getContent
    # Arguments	:
    # Returns	: (String) content
    #
    def getContent(self):
        return self.commentInstance["content"]

    #
    # Function	: setTime
    # Arguments	: String time (in milliseconds)
    # Returns	:
    #
    def setTime(self, time):
        self.commentInstance["time"] = time
    #
    # Function	: getTime
    # Arguments	:
    # Returns	: (String) time
    #
    def getTime(self):
        return self.commentInstance["time"]

    #
    # Function	: setOwner
    # Arguments	: (User Node) owner
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def setOwner(self, owner):
        global HAS_OWNER, LBL_USER
        if LBL_USER in owner.get_labels():
            return self.commentInstance.get_or_create_path(REL_HASOWNER, owner)
        else:
            raise Exception("The Node Provided is not a User")

    #
    # Function	: getOwner
    # Arguments	:
    # Returns	: a Owner Node or None (if there is no node)
    #
    def getOwner(self):
        global REL_HASOWNER
        relationships = list(self.commentInstance.match_outgoing(REL_HASOWNER))
        if len(relationships) != 0:
            return relationships[0].end_node
        else:
            return None

    #
    # Function	: setParent
    # Arguments	: (Task or Post or Comment Node) parent
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def setParent(self, parent):
        global REL_HASCOMMENT, LBL_POST, LBL_TASK, LBL_COMMENT
        if (LBL_POST in parent.get_labels()) \
            or (LBL_TASK in parent.get_labels()) \
            or (LBL_COMMENT in parent.get_labels()):
            return parent.get_or_create_path(REL_HASCOMMENT, self.commentInstance)
        else:
            raise Exception("The Node Provided is not a Post or Task")

    #
    # Function	: getParent
    # Arguments	:
    # Returns	: a Parent Node or None (if there is no node)
    #
    def getParent(self):
        global REL_HASCOMMENT
        relationships = list(self.commentInstance.match_incoming(REL_HASCOMMENT))
        if len(relationships) != 0:
            return relationships[0].start_node
        else:
            return None

