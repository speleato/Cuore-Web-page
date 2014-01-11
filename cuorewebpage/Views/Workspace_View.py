__author__ = 'boggle_eye'

from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Files", renderer="cuorewebpage:templates/files.mako")
def Files(request):
    return {}

@view_config(route_name="Calendar", renderer="cuorewebpage:templates/calendar.mako")
def Calendar(request):
    return {}

@view_config(route_name="Tasks", renderer="cuorewebpage:templates/tasks.mako")
def Tasks(request):
    return {}
