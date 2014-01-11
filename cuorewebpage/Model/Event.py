from database_config 	import *
from py2neo 			import neo4j, node

# Class  : Event
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of the Event
#	4) 	setDescription(self, description)				- Takes description as a string
#	5)	getDescription(self)							- Returns description as a string
# 	6) 	setStartTime(self, sTime)						- sTime in millis
#	7) 	getStartTime(self)								- Returns sTime, millis
#	8) 	setEndTime(self, eTime)							- eTime in millis
#	8) 	getEndTime(self)								- Returns eTime, millis
#	9) 	addOwner(self, owner)							- owner is a node, Owner.getNode()
#	10)	getOwners(self)									- Returns a list of 'Node' Objects containing the User Nodes
#	11) addGroup(self, group)							- group is a node, Group.getNode()
#	12) getGroups(self)									- Returns a list of 'Node' Objects containing the Group Nodes
#	13)	addTask(self, task)								- task is a node, Task.getNode()
#	14) getTasks(self)									- Returns a list of 'Node' Objects containing the Task Nodes
#	
# Constants
REL_HASEVENT 		= "has_event"
REL_HASTASK  		= "has_task"
REL_HASOWNER		= "has_owner"
LBL_CAL		= "Calendar"
LBL_EVENT	= "Event"
LBL_TASK	= "Task"
LBL_USER	= "User"

class Event: 
	graph_db	= None
	eventInstance	= None

	def db_init(self):
		if self.graph_db is None:
			self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

	#
	# Function	: getNode
	# Arguments	: 
	# Returns	: eventInstance Node
	#
	def getNode(self):
		return self.eventInstance

	#
	# Function	: Constructor
	# Arguments	: Uri of Existing Task Node OR Name of Task
	#
	def __init__(self, URI = None, Name = None, Owner = None, sTime = None, eTime = None ):
		global LBL_CAL
		self.db_init()
		tempEvent = None
		if URI is not None:
			self.eventInstance 	= neo4j.Node(URI)

		elif Name is not None and Owner is not None and sTime is not None and eTime is not None:
			tempEvent, 	= self.graph_db.create({"name": Name, "sTime": sTime, "eTime": eTime})
			tempEvent.add_labels(LBL_EVENT)
			self.eventInstance = tempEvent
			self.addOwner(Owner)

		else:
			raise Exception("Name/Owner or URI not specified")

	#
	# Function	: getName
	# Arguments	: 
	# Returns	: name of calendar
	#
	def getName(self):
		if self.eventInstance is not None:
			return self.eventInstance["name"]
		else:
			return None

	#
	# Function	: setDescription
	# Arguments	: (String) description
	#
	def setDescription(self, description):
		self.eventInstance["description"] = description

	#
	# Function	: getDescription
	# Arguments	: 
	# Returns	: (String) description
	#
	def getDescription(self):
		return self.eventInstance["description"];

	#
	# Function	: setStartTime
	# Arguments	: sTime in millis
	# Returns	: 
	#
	def setStartTime(self, sTime):
		self.eventInstance["sTime"] = sTime

	#
	# Function	: getStartTime
	# Arguments	: 
	# Returns	: sTime in millis
	#
	def getStartTime(self):
		return self.eventInstance["sTime"]

	#
	# Function	: setEndTime
	# Arguments	: eTime in millis 
	# Returns	:
	#
	def setEndTime(self, eTime):
		self.eventInstance["eTime"]

	#
	# Function	: getEndTime
	# Arguments	: 
	# Returns	: eTime in millis
	#
	def getEndTime(self):
		return self.eventInstance["eTime"]

	#
	# Function	: addOwner
	# Arguments	: (User Node) owner
	# Returns	: a 'Path' object containing nodes and relationships used
	# 
	def addOwner(self, owner):
		global REL_HASOWNER, LBL_USER
		if LBL_USER in owner.get_labels():
			return self.eventInstance.get_or_create_path(REL_HASOWNER, owner)
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
		for relationship in list(self.eventInstance.match_outgoing(REL_HASOWNER)):
			owners.append(relationship.end_node)
		return owners

	#	
	# Function	: addGroup
	# Arguments	: (Group Node) group
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def addGroup(self, group):
		global REL_HASGROUP, LBL_GROUP
		if LBL_GROUP in group.get_labels():
			return self.eventInstance.get_or_create_path(REL_HASGROUP, group)
		else:
			raise Exception("The Node Provided is not a Group")

	#
	# Function	: getGroups
	# Arguments	: 
	# Returns	: a list of 'Node' Objects containing the User Nodes
	#
	def getGroups(self):
		global REL_HASGROUP
		groups = list()
		for relationship in list(self.eventInstance.match_outgoing(REL_HASGROUP)):
			groups.append(relationship.end_node)
		return groups

	#
	# Function	: addTask
	# Arguments	: (Task Node) task
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def addTask(self, task):
		global REL_HASTASK, LBL_TASK
		if LBL_TASK in task.get_labels():
			return self.eventInstance.get_or_create_path(REL_HASTASK, task)
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
		for relationship in list(self.eventInstance.match_outgoing(REL_HASTASK)):
			tasks.append(relationship.end_node)
		return tasks