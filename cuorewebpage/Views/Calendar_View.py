__author__ = 'vincente'

from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task
from cuorewebpage.Model.Department import Department
from datetime import datetime
from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import User, getCurrentUser
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Event import Event
from cuorewebpage.Model.Post import Post


graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Calendar", renderer="cuorewebpage:templates/calendar.mako")
def Calendar(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section']  = 'Calendar'
        ctx['id'] = -1
        if getCurrentUser(request) is None:
            return redirectUser(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            mUser     = User(uid=request.session['uid'])
            mCalendar = mUser.getCalendar()

            #Populate the Event List to pass to the mako file
            events = list()
            for event in mCalendar.getEvents():
                events.append(Event(URI=event))

            #Get all the Events that we have been invited to
            for event in mUser.getInvitedEvents():
                events.append(event)

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

@view_config(route_name="Calendar_Action", match_param='action=create', renderer='json')
def calendar_event_create(request):
    if not isUserLoggedOn(request):
        return redirectUser(request)

    data = {};
    mUser     = User(uid=request.session['uid'])
    mCalendar = mUser.getCalendar()

    #Create New Event
    title = request.POST.getone('title')
    start = long(request.POST.getone('sTime'))/1000
    end   = long(request.POST.getone('eTime'))/1000

    nEvent = Event(Name=title, sTime=start, eTime=end, Owner=mUser.getNode())
    mCalendar.addEvent(nEvent.getNode())
    data['id'] = nEvent.getNode()._id

    print "============================="
    print "\tNew Event!"
    print "\tTitle: " + title
    print "\tId   : " + str(data['id'])
    print "\tsTime: " + str(start)
    print "\teTime: " + str(end)
    print "============================="

    return data

@view_config(route_name="Calendar_Action", match_param='action=reschedule', renderer='json')
def calendar_event_reschedule(request):
    if not isUserLoggedOn(request):
        return redirectUser(request)

    data = {};

    print "============================="
    print "\tEdited Event!"
    print "\tId   \t: " + request.POST.getone('id')
    print "\tsTime\t: " + str(long(request.POST.getone('sTime'))/1000)
    print "\teTime\t: " + str(long(request.POST.getone('eTime'))/1000)
    print "============================="

    mEvent = Event(graph_db.node(request.POST.getone('id')))
    mEvent.setStartTime(long(request.POST.getone('sTime'))/1000)
    mEvent.setEndTime(long(request.POST.getone('eTime'))/1000)

    return data

@view_config(route_name="Calendar_Action", match_param='action=rename', renderer='json')
def calendar_event_rename(request):
    if not isUserLoggedOn(request):
        return redirectUser(request)

    data = {};

    print "============================="
    print "\tRenaming Event"
    print "\tId  \t: " + request.POST.getone('id')
    print "\tname\t: " + request.POST.getone('name')
    print "============================="

    mEvent = Event(graph_db.node(request.POST.getone('id')))
    mEvent.setName(request.POST.getone('name'))
    data['success'] = True

    return data

@view_config(route_name="Calendar_Action", match_param='action=delete', renderer='json')
def calendar_event_delete(request):
    if not isUserLoggedOn(request):
        return redirectUser(request)

    data = {};
    print "============================="
    print "\tDeleting Event"
    print "\tId  \t: " + request.POST.getone('id')
    print "============================="

    mEvent = Event(graph_db.node(request.POST.getone('id')))

    data['success'] = mEvent.deleteSelf()

    return data
