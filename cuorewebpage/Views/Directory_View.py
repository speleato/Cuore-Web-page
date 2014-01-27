from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Company import Company

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Directory", renderer="cuorewebpage:templates/Directory.mako")
def Directory(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Directory'
        ctx['user'] = getCurrentUser(request)
        ctx['company'] = Company(Name="Cuore").getName()
        ctx['departments'] = Company(Name="Cuore").getDepartments()
        return ctx
    else:
        return redirectUser(request)
