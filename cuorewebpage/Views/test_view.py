from pyramid.response import Response
from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config

from cuorewebpage.Model.Person import Person

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Test", renderer="cuorewebpage:templates/test.mako")
def Test(request):
    return {}
