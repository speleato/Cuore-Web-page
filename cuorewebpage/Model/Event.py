from database_config import *
from py2neo import neo4j, node

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
#	9)	setLocation(self, location)						- location as a string
#	10)	getLocation(self)								- Returns location as a string
#	11)	addOwner(self, owner)							- owner is a node, Owner.getNode()
#	12)	getOwners(self)									- Returns a list of 'Node' Objects containing the User Nodes
#	
# Constants
STS_NOTGOING = "not_going"
STS_MAYBE = "maybe"
STS_GOING = "going"


class Event:
    graph_db = None
    eventInstance = None

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
    def __init__(self, URI=None, Name=None, Owner=None, sTime=None, eTime=None):
        global LBL_CAL
        self.db_init()
        tempEvent = None
        if URI is not None:
            self.eventInstance = neo4j.Node(URI)

        elif Name is not None and sTime is not None and eTime is not None:
            tempEvent = self.graph_db.get_or_create_indexed_node(IND_EVENT, "name", Name, {"name": Name, "sTime": sTime, "eTime": eTime})
            tempEvent.add_labels(LBL_EVENT)
            self.eventInstance = tempEvent

        else:
            raise Exception("Name/sTime/eTime or URI not specified")

        if Owner is not None:
            self.addOwner(Owner)

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
    # Function  : setName
    # Arguments : String name
    # Returns   :
    #
    def setName(self, name):
        self.eventInstance["name"] = name

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
        self.eventInstance["eTime"] = eTime

    #
    # Function	: getEndTime
    # Arguments	:
    # Returns	: eTime in millis
    #
    def getEndTime(self):
        return self.eventInstance["eTime"]

    #
    # Function 	: setLocation
    # Arguments : (String) location
    # Returns 	:
    #
    def setLocation(self, location):
        self.eventInstance["location"] = location

    #
    # Function 	: getLocation
    # Arguments :
    # Returns	: (String) location
    #
    def getLocation(self):
        return self.eventInstance["location"]

    #
    # Function	: addOwner
    # Arguments	: (User Node) owner
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def addOwner(self, owner):
        global REL_CREATEDBY, LBL_USER
        if len(list(self.eventInstance.match_outgoing(REL_HASOWNER))) == 0:
            if LBL_USER in owner.get_labels():
                return self.eventInstance.get_or_create_path(REL_CREATEDBY, owner)
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
        for relationship in list(self.eventInstance.match_outgoing(REL_CREATEDBY)):
            owners.append(relationship.end_node)
        return owners

    #
    # Function 	: addInvitee
    # Arguments	: (User Node) invitee
    # Returns	: a 'Path' object containing nodes and relationships used
    #
    def addInvitee(self, invitee):
        global REL_INVITED, LBL_USER, STS_MAYBE
        if LBL_USER in invitee.get_labels():
            path = self.eventInstance.get_or_create_path(REL_INVITED, invitee)
            if len(path.relationships) == 1:
                path.relationships[0]["status"] = STS_MAYBE
            return path
        else:
            raise Exception("The Node Provided is not a User")

    #
    # Function 	: getInvitees
    # Arguments :
    # Returns	: a list of 'Node' Objects containing the User Nodes
    #
    def getInvitees(self):
        global REL_INVITED
        invitees = list()
        for relationship in list(self.eventInstance.match_outgoing(REL_INVITED)):
            invitees.append(relationship.end_node)
        return invitees