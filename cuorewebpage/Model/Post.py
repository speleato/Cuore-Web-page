from database_config 	import *
from py2neo 			import neo4j, node

# Class  : Blog
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Blog Node
#	3) 	getName(self) 									- Returns name of blog
#	4) 	setDescription(self, description)				- Takes description as a string
#	5) 	setOwner(self, owner)							- owner is a node, Owner.getNode()
#	6) 	getOwner(self)									- Returns a User Node
# Constants: 

class Post:

	graph_db	= None
	postInstance= None

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
	def __init__(self, URI = None, Name = None, Content = None, Owner = None):
		global LBL_POST
		self.db_init()
		tempPost = None
		if URI is not None:
			tempPost 	= neo4j.Node(URI)

		elif Name is not None:
			tempPost, 	= self.graph_db.create({"name": Name})
			tempPost.add_labels(LBL_POST)

		else:
			raise Exception("Name/Status or URI not specified")

		self.postInstance = tempPost

		if Content is not None:
			self.postInstance["content"] = Content
		
		if Owner is not None:
			global HAS_OWNER, LBL_USER
			if LBL_USER in Owner.get_labels():
				self.postInstance.get_or_create_path(REL_HASOWNER, Owner)
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
	# Function	: setOwner
	# Arguments	: (User Node) owner
	# Returns	: a 'Path' object containing nodes and relationships used
	# 
	def setOwner(self, owner):
		global HAS_OWNER, LBL_USER
		if LBL_USER in owner.get_labels():
			return self.postInstance.get_or_create_path(REL_HASOWNER, owner)
		else:
			raise Exception("The Node Provided is not a User")

	#
	# Function	: getOwner
	# Arguments	: 
	# Returns	: a Owner Node or None (if there is no node)
	# 
	def getOwner(self):
		global REL_HASOWNER
		relationships = list(self.postInstance.match_outgoing(REL_HASOWNER))
		if len(relationships) != 0:
			return relationships[0].end_node
		else:
			return None