from database_config import *
from py2neo import neo4j, node

# Class  : Task
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of task
#	4) 	setDescription(self, description)				- Takes description as a string
#	5) 	getDescription(self)							- Gets the description as a string
# 	6) 	setEndTime(self, sTime)							- Sets eTime in millis
#	7) 	getEndTime(self)								- Gets eTime in millis
#	8)	setInvestedTime(self, iTime)					- Sets iTime in millis
#	9) 	getInvestedTime(self, iTime)					- Gets iTime in millis
#	10) setDeadline(self, deadline)						- Sets the deadline in millis
#	11) getDeadline(self)								- Gets the deadline in millis						
#	10)	setPriority(self, priority)						- Sets the priority of the task
#	11) getPriority(self)								- Gets the priority of the task
#	12) assignToUser(self, owner)						- owner is a node, Owner.getNode()
#	13)	getAssignedUsers(self)							- Returns a list of 'Node' Objects containing the User Nodes
#	14)	setStatus(self, Status)							- Status should be one of the STS Constants contained in Task
#	15)	getStatus(self)									- Returns status of Task
#	16)	addSubTask(self, subtask)						- Takes a (Task Node) subTask, returns a 'Path' object
#                                                             containing nodes and relationships used
#	17)	getSubTasks(self)								- a list of subtasks the current task has
#	18) addFile(self, file)								- adds a file to the task
#	19) getFiles(self)									- Returns a list of File Nodes
#
# Constants: 

STS_OPEN = "Open"
STS_CLOSED = "Closed"
STS_IN_PROG = "In_Progress"


class Task:
    graph_db = None
    taskInstance = None

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
    def __init__(self, URI=None, Name=None, Status=None):
        global LBL_TASK
        self.db_init()
        tempTask = None
        if URI is not None:
            tempTask = neo4j.Node(URI)

        elif Name is not None and Status is not None:
            tempTask, = self.graph_db.create({"name": Name, "status": Status})
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
    # Function	: setEndTime
    # Arguments	: eTime in millis
    # Returns	:
    #
    def setEndTime(self, eTime):
        self.taskInstance["eTime"] = eTime

    #
    # Function	: getEndTime
    # Arguments	:
    # Returns	: eTime in millis
    #
    def getEndTime(self):
        return self.taskInstance["eTime"]

    #
    # Function	: setInvestedTime
    # Arguments	: iTime
    # Returns 	:
    #
    def setInvestedTime(self, iTime):
        self.taskInstance["iTime"] = iTime

    #
    # Function	: getInvestedTime
    # Arguments	:
    # Returns 	: iTime in millis
    #
    def getInvestedTime(self):
        return self.taskInstance["iTime"]

    #
    # Function 	: setDeadline
    # Arguments : deadline
    # Returns	:
    #
    def setDeadline(self, deadline):
        self.taskInstance["deadline"] = deadline

    #
    # Function 	: getDeadline
    # Arguments :
    # Returns	: list of deadlines for the task
    #
    def getDeadline(self):
        return self.taskInstance["deadline"]

    #
    # Function 	: setPriority
    # Arguments : priority integer as string
    # Returns 	:
    #
    def setPriority(self, priority):
        self.taskInstance["priority"] = priority

    #
    # Function 	: getPriority
    # Arguments :
    # Returns 	: priority as string
    #
    def getPriority(self):
        return self.taskInstance["priority"]

    #
    # Function	: assignToUser
    # Arguments	: (User Node) owner
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def assignToUser(self, user):
        global REL_ASSIGNEDTO, LBL_USER
        if LBL_USER in user.get_labels():
            return self.taskInstance.get_or_create_path(REL_ASSIGNEDTO, user)
        else:
            raise Exception("The Node Provided is not a User")

    #
    # Function	: getAssignedUsers
    # Arguments	:
    # Returns	: a list of 'Node' Objects containing the User Nodes
    #
    def getAssignedUsers(self):
        global REL_ASSIGNEDTO
        users = list()
        for relationship in list(self.taskInstance.match_outgoing(REL_ASSIGNEDTO)):
            users.append(relationship.end_node)
        return users

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

    #
    # Function	: addFile
    # Arguments : File Node
    # Returns 	: a 'Path' object
    #
    def addFile(self, File):
        global LBL_FILE, REL_HASFILE
        if File is not None and LBL_FILE in File.get_labels():
            return self.taskInstance.get_or_create_path(REL_HASFILE, File)
        else:
            raise Exception("Please supply a proper File Node (Node in Label)")

    #
    # Function 	: getFiles
    # Arguments :
    # Returns 	: a list of File Nodes
    #
    def getFiles(self):
        global REL_HASFILE
        files = list()
        for relationship in list(self.taskInstance.match_outgoing(REL_HASFILE)):
            files.append(relationship.end_node)
        return files

    # Clears the entire DB for dev purposes
    def clear(self):
        self.graph_db.clear()