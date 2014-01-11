from database_config import *
from py2neo import neo4j, node

# Class  : Calendar
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the Task Node
#	3) 	getName(self) 									- Returns name of the Calendar
#	4) 	setDescription(self, description)				- Takes description as a string
#	5)	getDescription(self)							- Returns description as a string
#	6) 	addOwner(self, owner)							- owner is a node, Owner.getNode()
#	7) 	getOwners(self)									- Returns a list of 'Node' Objects containing the User Nodes
#	8) addEvent(self, event)							- event is a node, Event.getNode()
#	9)	getEvents(self)									- Returns a list of 'Node' Objects containing the Event Nodes
#
# Constants:

class Calendar:
    graph_db = None
    calInstance = None

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
    def __init__(self, URI=None, Name=None, Owner=None):
        global LBL_CALENDAR
        self.db_init()
        tempCal = None
        if URI is not None:
            self.calInstance = neo4j.Node(URI)

        elif Name is not None and Owner is not None:
            tempCal, = self.graph_db.create({"name": Name})
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
        global REL_HASCALENDAR, LBL_USER
        if LBL_USER in owner.get_labels():
            return owner.get_or_create_path(REL_HASCALENDAR, self.calInstance)
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
        for relationship in list(self.calInstance.match_incoming(REL_HASCALENDAR)):
            owners.append(relationship.start_node)
        return owners

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