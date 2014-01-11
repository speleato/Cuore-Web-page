__author__ = 'boggle_eye'

from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Files", renderer="cuorewebpage:templates/files.mako")
def Files(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Files'
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name="Calendar", renderer="cuorewebpage:templates/calendar.mako")
def Calendar(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Calendar'
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name="Tasks", renderer="cuorewebpage:templates/tasks.mako")
def Tasks(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Tasks'
        return ctx
    else:
        return redirectUser(request)
