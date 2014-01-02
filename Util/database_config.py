#**************************************
# Current Database Info 
#**************************************

#	To Access...
#	from database_config 	import db_config
#	from py2neo 			import neo4j 
#		graph_db = neo4j.GraphDatabaseService(db_config['uri'])

db_config   			= {}
#db_config['address']	= "http://162.212.130.189"
db_config['address']	= "http://127.0.0.1"
db_config['port']		= "7474"
db_config['ending']		= "db/data"
db_config['uri']		= db_config['address'] 		+ ":" \
							+ db_config['port']		+ "/" \
							+ db_config['ending']	+ "/"
db_config['username'] 	= "your_username_here"
db_config['password'] 	= "your_password_here"

#Moar constants

#Relationship Constants
REL_HASEVENT 		= "has_event"
REL_HASTASK  		= "has_task"
REL_HASSUBTASK		= "has_subtask"
REL_HASDEADLINE 	= "has_deadline"
REL_HASSUBCALENDAR	= "has_subcalendar"
REL_HASOWNER		= "has_owner"
REL_HASGROUP		= "has_group"
REL_HASGENTASK		= "has_gentask"
REL_HASTASK			= "has_task"
REL_HASFILE			= "has_file"
REL_HASPROJECT		= "has_project"

#Label Constants
LBL_CAL			= "Calendar"
LBL_EVENT		= "Event"
LBL_TASK		= "Task"
LBL_SUBTASK		= "SubTask"
LBL_DEADLINE	= "Deadline"
LBL_USER		= "User"
LBL_GROUP		= "Group"
LBL_WORKSPACE	= "Workspace"
LBL_PROJECT		= "Project"
LBL_FILE		= "File"
