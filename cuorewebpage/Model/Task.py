from database_config 	import *
from py2neo 			import neo4j, node

# Class  : Task
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of task
#	4) 	setDescription(self, description)				- Takes description as a string
#	5) 	setOwner(self, owner)							- owner is a node, Owner.getNode()
#	6) 	getOwners(self)									- Returns a list of 'Node' Objects containing the User Nodes
#	7) 	setStatus(self, Status)							- Status should be one of the STS Constants contained in Task
#	8) 	getStatus(self)									- Returns status of Task
#	9) 	setDeadline(self, deadline)						- Returns a 'Path' object containing nodes and relationships used
#	10)	getDeadline(self)								- Returns a list of deadlines for the task
#	11)	addSubTask(self, subtask)						- Takes a (Task Node) subTask, returns a 'Path' object containing nodes and relationships used
#	12)	getSubTasks(self)								- a list of subtasks the current task has
#
# Constants: 

REL_HASEVENT 		= "has_event"
REL_HASTASK  		= "has_task"
REL_HASSUBTASK		= "has_subtask"
REL_HASDEADLINE 	= "has_deadline"
REL_HASOWNER		= "has_owner"

LBL_TASK	= "Task"
LBL_USER	= "User"

STS_OPEN	= "Open"
STS_CLOSED	= "Closed"
STS_IN_PROG	= "In_Progress"

class Task:

	graph_db	= None
	taskInstance= None

	def db_init(self):
		if self.graph_db is None:
			self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

	#
	# Function	: getNode
	# Arguments	: 
	# Returns	: TaskInstance Node
	#
	def getNode(self):
		return self.taskInstance

	#
	# Function	: Constructor
	# Arguments	: Uri of Existing Task Node OR Name of Task
	#
	def __init__(self, URI = None, Name = None, Status = None):
		global LBL_TASK
		self.db_init()
		tempTask = None
		if URI is not None:
			tempTask 	= neo4j.Node(URI)

		elif Name is not None and Status is not None:
			tempTask, 	= self.graph_db.create({"name": Name, "status": Status})
			tempTask.add_labels(LBL_TASK)

		else:
			raise Exception("Name/Status or URI not specified")

		self.taskInstance = tempTask

	#
	# Function	: getName
	# Arguments	: 
	# Returns	: name of task
	#
	def getName(self):
		if self.taskInstance is not None:
			return self.taskInstance["name"]
		else:
			return None

	#
	# Function	: setDescription
	# Arguments	: (String) description
	#
	def setDescription(self, description):
		self.taskInstance["description"] = description

	#
	# Function	: getDescription
	# Arguments	: 
	# Returns	: (String) description
	#
	def getDescription(self):
		return self.taskInstance["description"];

	#
	# Function	: setOwner
	# Arguments	: (User Node) owner
	# Returns	: a 'Path' object containing nodes and relationships used
	# 
	def setOwner(self, owner):
		global HAS_OWNER, LBL_USER
		if LBL_USER in owner.get_labels():
			return self.taskInstance.get_or_create_path(REL_HASOWNER, owner)
		else:
			raise Exception("The Node Provided is not a User")

	#
	# Function	: getOwners
	# Arguments	: 
	# Returns	: a list of 'Node' Objects containing the User Nodes
	# 
	def getOwners(self):
		global REL_HASOWNER
		owners = list()
		for relationship in list(self.taskInstance.match_outgoing(REL_HASOWNER)):
			owners.append(relationship.end_node)
		return owners
	#
	# Function	: setStatus
	# Arguments	: (String) Status
	# Returns	: 
	#
	def setStatus(self, Status):
		self.taskInstance["status"] = Status

	#
	# Function	: getStatus
	# Arguments	: 
	# Returns	: Status of Task
	#
	def getStatus(self):
		return self.taskInstance["status"]

	#
	# Function 	: setDeadline
	# Arguments : deadline
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def setDeadline(self, deadline):
		global REL_HASDEADLINE
		return self.taskInstance.get_or_create_path(REL_HASDEADLINE, deadline)

	#
	# Function 	: getDeadline
	# Arguments : 
	# Returns	: list of deadlines for the task
	#
	def getDeadline(self):
		global REL_HASDEADLINE
		deadlines = list()
		for relationship in list(self.taskInstance.match_outgoing(REL_HASDEADLINE)):
			deadlines.append(relationship.end_node)
		return deadlines

	#
	# Function	: addSubTask
	# Arguments	: (Task Node) subTask
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def addSubTask(self, subtask):
		global REL_HASSUBTASK, LBL_TASK
		if subtask is not None and LBL_TASK in subtask.get_labels():
			return self.taskInstance.get_or_create_path(REL_HASSUBTASK, subtask)
		else:
			raise Exception("Please supply a proper Task Node(Task in Labels")


	#
	# Function	: getSubTask
	# Arguments	: 
	# Returns	: a list of subtasks the current task has
	#
	def getSubTasks(self):
		global REL_HASSUBTASK
		subTasks = list()
		for relationship in list(self.taskInstance.match_outgoing(REL_HASSUBTASK)):
			subTasks.append(relationship.end_node)
		return subTasks

	# Clears the entire DB for dev purposes
	def clear(self):
		self.graph_db.clear()