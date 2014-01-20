__author__ = 'boggle_eye'

from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import User, getCurrentUser
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Event import Event


graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Calendar", renderer="cuorewebpage:templates/calendar.mako")
def Calendar(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section']  = 'Calendar'
        if getCurrentUser(request) is None:
            return redirectUser(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            print "We have an actual user!!"
            ctx['user']     = User(uid=request.session['uid'])
            ctx['calendar'] = ctx['user'].getCalendar()
            events = list()
            for event in ctx['calendar'].getEvents():
                events.append(Event(URI=event))
            ctx['events'] = events

            #Get Tasks for the tasks sidebar

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
