from database_config 	import *
from py2neo 			import neo4j, node

# Class  : Project
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of the Event
#	4) 	setDescription(self, description)				- Takes description as a string
#	5)	getDescription(self)							- Returns description as a string
#	6) 	addFile(self, File)								- (File Node) File
# 	7) 	getFiles(self)									- Returns a list of 'Node' Objects that are Files
#	8)	getParentWorkspace(self)						- Returns a list of 'Node' Objects that are Workspaces
#	9) 	addTask(self, task)								- (Task Node) task
#	10) getTasks(self)									- Returns a list of 'Node' Objects that are Tasks
#

class Project:

	graph_db		= None
	projectInstance	= None

	def db_init(self):
		if self.graph_db is None:
			self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

	#
	# Function	: getNode
	# Arguments	: 
	# Returns	: projectInstance Node
	#
	def getNode(self):
		return self.projectInstance

	#
	# Function	: Constructor
	# Arguments	: Uri of Existing Task Node OR Name of Task
	#
	def __init__(self, URI = None, Name = None):
		global LBL_PROJECT
		self.db_init()
		tempProject = None
		if URI is not None:
			tempProject 	= neo4j.Node(URI)

		elif Name is not None:
			tempProject, 	= self.graph_db.create({"name": Name})
			tempProject.add_labels(LBL_PROJECT)

		else:
			raise Exception("Name or URI not specified")

		self.projectInstance = tempProject

	#
	# Function	: getName
	# Arguments	: 
	# Returns	: name of task
	#
	def getName(self):
		if self.projectInstance is not None:
			return self.projectInstance["name"]
		else:
			return None

	#
	# Function	: setDescription
	# Arguments	: (String) description
	#
	def setDescription(self, description):
		self.projectInstance["description"] = description

	#
	# Function	: getDescription
	# Arguments	: 
	# Returns	: (String) description
	#
	def getDescription(self):
		return self.projectInstance["description"];

	#
	# Function	: setFLocation
	# Arguments	: (String) flocation
	#
	def setFileLocation(self, flocation):
		self.projectInstance["flocation"] = flocation

	#
	# Function	: addFile
	# Arguments	: (File Node) File
	# Returnes	: a 'Path' object containing nodes and relationships used
	#
	def addFile(self, File):
		global REL_HASFILE, LBL_FILE
		if LBL_FILE in File.get_labels():
			return self.projectInstance.get_or_create_path(REL_HASFILE, File)
		else:
			raise Exception("The Node Provided is not a File")

	# Function	: getFiles
	# Arguments	: 
	# Returns	: a list of 'Node' Objects containing the File Nodes
	def getFiles(self):
		global REL_HASFILE
		files = list()
		for relationship in list(self.projectInstance.match_incoming(REL_HASFILE)):
			files.append(relationship.start_node)
		return files

	#
	# Function	: getParentWorkspace
	# Arguments	: 
	# Returns	: a list of 'Node' Objects containing the Workspace Nodes
	def getParentWorkspace(self):
		global REL_HASPROJECT
		workspaces = list()
		for relationship in list(self.projectInstance.match_incoming(REL_HASPROJECT)):
			workspaces.append(relationship.start_node)
		return workspaces

	#
	# Function	: addTask
	# Arguments	: (Task Node) task
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def addTask(self, task):
		global REL_HASTASK, LBL_TASK
		if LBL_TASK in task.get_labels():
			return self.projectInstance.get_or_create_path(REL_HASTASK, task)
		else:
			raise Exception("The Node Provided is not a Task")

	#
	# Function	: getTasks
	# Arguments	: 
	# Returns	: a list of 'Node' Objects containing the User Nodes
	#
	def getTasks(self):
		global REL_HASTASK
		tasks = list()
		for relationship in list(self.projectInstance.match_outgoing(REL_HASTASK)):
			tasks.append(relationship.end_node)
		return tasks