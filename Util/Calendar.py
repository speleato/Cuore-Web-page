from database_config 	import *
from py2neo 			import neo4j, node

# Class  : Calendar
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of the Calendar
#	4) 	setDescription(self, description)				- Takes description as a string
#	5)	getDescription(self)							- Returns description as a string
#	6) 	addOwner(self, owner)							- owner is a node, Owner.getNode()
#	7) 	getOwners(self)									- Returns a list of 'Node' Objects containing the User Nodes
#	8) 	addGroup(self, group)							- group is a node, Group.getNode()
#	9) 	getGroups(self)									- Returns a list of 'Node' Objects containing the Group Nodes
#	10) addEvent(self, event)							- event is a node, Event.getNode()
#	11)	getEvents(self)									- Returns a list of 'Node' Objects containing the Event Nodes
#	12) addGeneralTask(self, task)						- task is a node, Task.getNode() that has a deadline
#	13) getGeneralTasks(self)							- Returns a list of 'Node' Objects containing all the Task Nodes under Calendar
#	
# Constants:

REL_HASEVENT	= "has_event"
REL_HASGROUP	= "has_group"
REL_HASOWNER	= "has_owner"
REL_HASGENTASK	= "has_gentask"

LBL_TASK		= "Task"
LBL_USER		= "User"
LBL_EVENT		= "Event"
LBL_GROUP		= "Group"
LBL_CALENDAR	= "Calendar"

class Calendar: 
	graph_db	= None
	calInstance	= None

	def db_init(self):
		if self.graph_db is None:
			self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

	#
	# Function	: getNode
	# Arguments	: 
	# Returns	: calInstance Node
	#
	def getNode(self):
		return self.calInstance

	#
	# Function	: Constructor
	# Arguments	: Uri of Existing Task Node OR Name of Task
	#
	def __init__(self, URI = None, Name = None, Owner = None):
		global LBL_CALENDAR
		self.db_init()
		tempCal = None
		if URI is not None:
			self.calInstance 	= neo4j.Node(URI)

		elif Name is not None and Owner is not None:
			tempCal, 	= self.graph_db.create({"name": Name})
			tempCal.add_labels(LBL_CALENDAR)
			self.calInstance = tempCal
			self.addOwner(Owner)

		else:
			raise Exception("Name/Owner or URI not specified")

	#
	# Function	: getName
	# Arguments	: 
	# Returns	: name of calendar
	#
	def getName(self):
		if self.calInstance is not None:
			return self.calInstance["name"]
		else:
			return None

	#
	# Function	: setDescription
	# Arguments	: (String) description
	#
	def setDescription(self, description):
		self.calInstance["description"] = description

	#
	# Function	: getDescription
	# Arguments	: 
	# Returns	: (String) description
	#
	def getDescription(self):
		return self.calInstance["description"];

	#
	# Function	: addOwner
	# Arguments	: (User Node) owner
	# Returns	: a 'Path' object containing nodes and relationships used
	# 
	def addOwner(self, owner):
		global REL_HASOWNER, LBL_USER
		if LBL_USER in owner.get_labels():
			return self.calInstance.get_or_create_path(REL_HASOWNER, owner)
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
		for relationship in list(self.calInstance.match_outgoing(REL_HASOWNER)):
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
			return self.calInstance.get_or_create_path(REL_HASGROUP, group)
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
		for relationship in list(self.calInstance.match_outgoing(REL_HASGROUP)):
			groups.append(relationship.end_node)
		return groups

	#
	# Function	: addEvent
	# Arguments	: (Event Node) event
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def addEvent(self, event):
		global REL_HASEVENT, LBL_EVENT
		if LBL_EVENT in event.get_labels():
			return self.calInstance.get_or_create_path(REL_HASEVENT, event)
		else:
			raise Exception("The Node Provided is not an Event")

	#
	# Function	: getEvents
	# Arguments	: 
	# Returns	: a list of 'Node' Objects containing the Event Nodes
	#
	def getEvents(self):
		global REL_HASEVENT
		events = list()
		for relationship in list(self.calInstance.match_outgoing(REL_HASEVENT)):
			events.append(relationship.end_node)
		return events

	#
	# Function	: addGeneralTask
	# Arguments	: (Task Node) task
	# Returns	: a 'Path' object containing nodes and relationships used
	#
	def addGeneralTask(self, task):
		global REL_HASGENTASK, LBL_TASK
		if LBL_TASK in task.get_labels():
			return self.calInstance.get_or_create_path(REL_HASGENTASK, task)
		else:
			raise Exception("The Node Provided is not a Task")

	#
	# Function	: getGeneralTasks
	# Arguments	: 
	# Returns 	: a list of 'Node' Objects containing the Task Nodes
	# 
	def getGeneralTasks(self):
		global REL_HASGENTASK
		tasks = list()
		for relationship in list(self.calInstance.match_outgoing(REL_HASGENTASK)):
			tasks.append(relationship.end_node)
		return tasks