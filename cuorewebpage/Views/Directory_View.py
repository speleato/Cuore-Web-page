from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Directory", renderer="cuorewebpage:templates/Directory.mako")
def Directory(request):
    ctx = {}
    ctx['section'] = 'Directory'
    return ctx

