from py2neo import neo4j, node
from database_config import *

# Class  : Blog
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Blog Node
#	3) 	getName(self) 									- Returns name of blog
#	4) 	setDescription(self, description)				- Takes description as a string
#	5) 	setOwner(self, owner)							- owner is a node, Department.getNode()
#	6) 	getOwner(self)									- Returns a Department Node
#	7) 	addPost(self, post)								- Adds a Post node to the Blog
#	8)	getPosts(self)									- Returns a list of Post Nodes
# Constants: 

class Blog:
    graph_db = None
    blogInstance = None
    index = None

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])
            self.index = self.graph_db.get_or_create_index(neo4j.Node, IND_BLOG)

    #
    # Function	: getNode
    # Arguments	:
    # Returns	: blogInstance Node
    #
    def getNode(self):
        return self.blogInstance

    #
    # Function	: Constructor
    # Arguments	: Uri of Existing Blog Node OR Name of Blog
    #
    def __init__(self, URI=None, Name=None, Owner=None):
        global LBL_BLOG, LBL_COMPANY
        self.db_init()
        tempBlog = None
        if URI is not None:
            tempBlog = neo4j.Node(URI)

        elif Name is not None:
            tempBlog = self.graph_db.get_or_create_indexed_node(IND_BLOG, "name", Name, {"name": Name})
            tempBlog.add_labels(LBL_BLOG)

        else:
            raise Exception("Name/Status or URI not specified")

        self.blogInstance = tempBlog

        if Owner is not None:
            if (LBL_DEPARTMENT in Owner.get_labels()) or (LBL_COMPANY in Owner.get_labels()):
                self.blogInstance.get_or_create_path(REL_HASOWNER, Owner)
            else:
                raise Exception("The Node Provided is not a Department")


    # Function	: __str__
    # Arguments	:
    # Returns	: name of blog
    #
    def __str__(self):
        if self.blogInstance is not None:
            return self.blogInstance["name"]
        else:
            return None

    # Function	: getName
    # Arguments	:
    # Returns	: name of blog
    #
    def getName(self):
        if self.blogInstance is not None:
            return self.blogInstance["name"]
        else:
            return None

    #
    # Function	: setDescription
    # Arguments	: (String) description
    #
    def setDescription(self, description):
        self.blogInstance["description"] = description

    #
    # Function	: getDescription
    # Arguments	:
    # Returns	: (String) description
    #
    def getDescription(self):
        return self.blogInstance["description"]

    #
    # Function	: setOwner
    # Arguments	: (Department Node) owner
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def setOwner(self, owner):
        global HAS_OWNER, LBL_USER
        if LBL_DEPARTMENT in owner.get_labels():
            return owner.get_or_create_path(REL_HASOWNER, self.blogInstance)
        else:
            raise Exception("The Node Provided is not a Department")

    #
    # Function	: getOwner
    # Arguments	:
    # Returns	: a Department Node or None (if there is no node)
    #
    def getOwner(self):
        global REL_HASOWNER
        relationships = list(self.blogInstance.match_incoming(REL_HASOWNER))
        if len(relationships) != 0:
            return relationships[0].start_node
        else:
            return None

    #
    # Function 	: addPost
    # Arguments	: Post Node
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def addPost(self, post):
        global REL_HASPOST, LBL_POST
        if LBL_POST in post.get_labels():
            return self.blogInstance.get_or_create_path(REL_HASPOST, post)
        else:
            raise Exception("The Node given is not a Post")

    #
    # Function	: getPosts
    # Arguments	:
    # Returns	: a list of Post Nodes
    #
    def getPosts(self):
        global REL_HASPOST
        posts = list()
        for relationship in list(self.blogInstance.match_outgoing(REL_HASPOST)):
            posts.append(relationship.end_node)
        return posts


