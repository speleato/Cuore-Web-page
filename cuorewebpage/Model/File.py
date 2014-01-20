from database_config import *
from py2neo import neo4j, node
from time import *

# Class  : File
# Methods:
#	1) 	db_init(self) 									- Private
#	2) 	getNode(self)									- Returns the File Node
#	3) 	getName(self) 									- Returns name of File
#	4) 	getFile(self)                   				- Returns the File
#	5) 	setFile(self)							        - If the file exists, it deletes (logically) the latest file. After, it creates one
# 	6) 	deleteFile(self)							    - Sets deletes the file in A LOGICAL WAY from the database.
#	7) 	setCreation(self)								- Sets the creation date of a file
#	8)	getCreation(self)					            - Gets the creation time of a file.
#	9) 	getLastModified(self)					        - Gets the last modification time of a file
#	10) setLastModified(self)						    - Sets the last modification date for a file

#
# Constants:

STS_OPEN = "Open"
STS_CLOSED = "Closed"
STS_IN_PROG = "In_Progress"


class File:
    graph_db = None
    FileInstance = None

    #
    # Function	: Constructor
    # Arguments	: Uri of Existing File Node OR Name of File
    #
    def __init__(self, URI=None, Name=None, Body=None):
        global LBL_FILE
        self.db_init()
        tempFile = None
        if URI is not None:
            tempFile = neo4j.Node(URI)

        elif Name is not None and Body is not None:
            tempFile, = self.graph_db.create({"name": Name, "file": Body})
            tempFile.add_labels(LBL_FILE)

        else:
            raise Exception("Name/Status or URI not specified")

        self.FileInstance = tempFile


    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])

    #
    # Function	: getNode
    # Arguments	:
    # Returns	: FileInstance Node
    #
    def getNode(self):
        return self.FileInstance

    #
    # Function	: getName
    # Arguments	:
    # Returns	: name of File
    #
    def getName(self):
        if self.FileInstance is not None:
            return self.FileInstance["name"]
        else:
            return None


    #
    # Function 	: getFiles
    # Arguments :
    # Returns 	: a list of File Nodes belonging to a specific department (restriction: each file belongs only to ONE department
    #
    def getFiles(self):
        global REL_HASFILE
        files = list()
        for relationship in list(self.FileInstance.match_incoming(REL_HASFILE)):
            files.append(relationship.end_node)
        return files

    #
    # Function 	: setFiles
    # Arguments :
    # Returns 	: a list of File Nodes
    #
    def setFile(self):
        global REL_HASFILE
        currentTime = time.strftime("%c")
        files = list()
        for relationship in list(self.FileInstance.match_outgoing(REL_HASFILE)):
            files.append(relationship.end_node)
        return files

    #
    # Function	: deleteFile
    # Arguments	:
    #
    def deleteFile(self):
        self.FileInstance["deleted"] = 'True'


    #
    # Function	: setCreation
    # Arguments	:
    #
    def setCreation(self):
        self.FileInstance["Creation"] = time.strftime("%c")

    #
    # Function	: getCreation
    # Arguments	:
    #
    def getCreation(self):
        return self.FileInstance["Creation"]

    #
    # Function	: getCreation
    # Arguments	:
    #
    def getLastModified(self):
        return self.FileInstance["Modification"]


    #
    # Function	: getCreation
    # Arguments	:
    #
    def setLastModified(self):
        self.FileInstance["Modification"] = time.strftime("%c")


    # Clears the entire DB for dev purposes
    def clear(self):
        self.graph_db.clear()