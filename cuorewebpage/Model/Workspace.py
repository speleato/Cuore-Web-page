from database_config 	import *
from py2neo 			import neo4j, node

# Class  : Workspace
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of the Event
#	4) 	setDescription(self, description)				- Takes description as a string
#	5)	getDescription(self)							- Returns description as a string
#	6) 	addProject(self, project)						- (Project Node) project
# 	7) 	getProjects(self)								- Returns a list of 'Node' Objects that are Projects
#	8)	addGroup(self, group)							- (Group Node) group
# 	9) 	getGroups(self, group)							- Returns a list of 'Node' Objects that are Groups
#

class Workspace:

	graph_db			= None
	workspaceInstance	= None

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
	def __init__(self, URI = None, Name = None):
		global LBL_TASK
		self.db_init()
		tempWorkspace = None
		if URI is not None:
			tempWorkspace 	= neo4j.Node(URI)

		elif Name is not None:
			tempWorkspace, 	= self.graph_db.create({"name": Name})
			tempWorkspace.add_labels(LBL_WORKSPACE)

		else:
			raise Exception("Name or URI not specified")

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
		return self.workspaceInstance["description"];

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
	# Function	: addGroup
	# Arguments	: Group Node
	# Returns	: 
	#
	def addGroup(self, group):
		global REL_HASGROUP
		return self.workspaceInstance.get_or_create_path(REL_HASGROUP, group)

	#
	# Function	: getGroups
	# Arguments	: 
	# Returns	: a list of 'Node' Objects that are Groups
	#
	def getGroups(self):
		global REL_HASGROUP, LBL_GROUP
		groups = list()
		for relationship in list(self.workspaceInstance.match_outgoing(REL_HASGROUP)):
			groups.append(relationship.end_node)
		return groups
