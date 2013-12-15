import sys
from database_config 	import db_config
from py2neo				import neo4j
if __name__ == "__main__":
	print "The Uri to connect to the db: " + db_config['uri']

	graph_db = neo4j.GraphDatabaseService(db_config['uri'])

	sys.stdout.write("Version: ")
	print graph_db.neo4j_version

	node = graph_db.node(188)
	print node["name"]