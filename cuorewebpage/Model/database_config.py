#**************************************
# Current Database Info
#**************************************

#        To Access...
#        from database_config         import db_config
#        from py2neo                         import neo4j
#                graph_db = neo4j.GraphDatabaseService(db_config['uri'])

db_config                           = {}
db_config['address']        = "http://localhost"
db_config['port']                = "7474"
db_config['ending']                = "db/data"
db_config['uri']                = db_config['address']                 + ":" \
                                                        + db_config['port']                + "/" \
                                                        + db_config['ending']        + "/"
db_config['username']         = "cuore"
db_config['password']         = "your_password_here"