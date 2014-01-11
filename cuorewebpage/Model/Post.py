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
#   10) setTags(self, tags)                             - Tags is an array of strings
#   11) getTags(self)                                   - Returns the tags as an array
#	12)	setOwner(self, owner)							- owner is a node, Owner.getNode()
#	13)	getOwner(self)									- Returns a User Node
#   14) addComment(self, comment)                       - Adds a comment node
#   15) getComments(self)                               - Returns a list of Comment Nodes
# Constants: 

class Post:
    graph_db = None
    postInstance = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

    #
    # Function	: getNode
    # Arguments	:
    # Returns	: postInstance Node
    #
    def getNode(self):
        return self.postInstance

    #
    # Function	: Constructor
    # Arguments	: Uri of Existing Blog Node OR Name of Blog
    #
    def __init__(self, URI=None, Name=None, Content=None, Owner=None):
        global LBL_POST
        self.db_init()
        tempPost = None
        if URI is not None:
            tempPost = neo4j.Node(URI)

        elif Name is not None:
            tempPost, = self.graph_db.create({"name": Name})
            tempPost.add_labels(LBL_POST)

        else:
            raise Exception("Name or URI not specified")

        self.postInstance = tempPost

        if Content is not None:
            self.postInstance["content"] = Content

        if Owner is not None:
            global HAS_OWNER, LBL_USER
            if LBL_USER in Owner.get_labels():
                self.postInstance.get_or_create_path(REL_CREATEDBY, Owner)
            else:
                raise Exception("The Node Provided is not a User")

    #
    # Function	: getName
    # Arguments	:
    # Returns	: name of blog
    #
    def getName(self):
        if self.postInstance is not None:
            return self.postInstance["name"]
        else:
            return None

    #
    # Function	: setDescription
    # Arguments	: (String) description
    #
    def setDescription(self, description):
        self.postInstance["description"] = description

    #
    # Function	: getDescription
    # Arguments	:
    # Returns	: (String) description
    #
    def getDescription(self):
        return self.postInstance["description"]

    #
    # Function	: setContent
    # Arguments	: String content
    # Returns	:
    #
    def setContent(self, content):
        self.postInstance["content"] = content

    #
    # Function	: getContent
    # Arguments	:
    # Returns	: (String) content
    #
    def getContent(self):
        return self.postInstance["content"]

    #
    # Function	: setTime
    # Arguments	: String time (in milliseconds)
    # Returns	:
    #
    def setTime(self, time):
        self.postInstance["time"] = time
    #
    # Function	: getTime
    # Arguments	:
    # Returns	: (String) time
    #
    def getTime(self):
        return self.postInstance["time"]

    #
    # Function	: setTags
    # Arguments	: Array(String tags)
    # Returns	:
    #
    def setTags(self, tags):
        self.postInstance["tags"] = json.JSONEncoder.encode(tags)

    #
    # Function	: getTags
    # Arguments	:
    # Returns	: (Array(String)) tags
    #
    def getTags(self):
        return json.JSONDecoder.decode(self.postInstance["tags"])

    #
    # Function	: setOwner
    # Arguments	: (User Node) owner
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def setOwner(self, owner):
        global REL_CREATEDBY, LBL_USER
        if LBL_USER in owner.get_labels():
            return self.postInstance.get_or_create_path(REL_CREATEDBY, owner)
        else:
            raise Exception("The Node Provided is not a User")

    #
    # Function	: getOwner
    # Arguments	:
    # Returns	: a Owner Node or None (if there is no node)
    #
    def getOwner(self):
        global REL_CREATEDBY
        relationships = list(self.postInstance.match_outgoing(REL_CREATEDBY))
        if len(relationships) != 0:
            return relationships[0].end_node
        else:
            return None

    #
    # Function  : addComment
    # Arguments : (Comment Node) comment
    # Returns   :
    #
    def addComment(self, comment):
        global REL_HASCOMMENT, LBL_COMMENT
        if LBL_COMMENT in comment.get_labels():
            return self.postInstance.get_or_create_path(REL_HASCOMMENT, comment)
        else:
            raise Exception("The Node Provided is not a comment")

    #
    # Function  : addComment
    # Arguments : (Comment Node) comment
    # Returns   :
    #
    def getComments(self):
        global REL_HASCOMMENT
        comments = list()
        for relationships in list(self.postInstance.match_outgoing(REL_HASCOMMENT)):
            comments.append(relationships.end_node)
        return comments