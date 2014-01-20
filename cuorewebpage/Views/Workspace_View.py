from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task
from datetime import datetime

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
            mUser     = User(uid=request.session['uid'])
            mCalendar = mUser.getCalendar()

            #Handle the POST request here
            if request.POST:
                title = request.POST.getone('title')
                start = long(request.POST.getone('sTime'))/1000
                end   = long(request.POST.getone('eTime'))/1000
                print "============================="
                print "\tNew Event!"
                print "\tTitle: " + title
                print "\tsTime: " + str(start)
                print "\teTime: " + str(end)
                print "============================="

                nEvent = Event(Name=title, sTime=start, eTime=end, Owner=mUser.getNode())
                mCalendar.addEvent(nEvent.getNode())

            events = list()
            for event in mCalendar.getEvents():
                events.append(Event(URI=event))

            #Get Tasks for the tasks sidebar
            tasks       = list()

            workspace   = mUser.getWorkspace()
            projects    = workspace.getProjects()
            for project in projects:
                for task in (Project(project)).getTasks():
                    tasks.append(Task(task))

            ctx['user']     = mUser
            ctx['tasks']    = tasks
            ctx['events']   = events
            ctx['calendar'] = mCalendar
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
