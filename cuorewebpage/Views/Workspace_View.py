from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task
from cuorewebpage.Model.Department import Department
from datetime import datetime

__author__ = 'boggle_eye'

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

@view_config(route_name="Tasks", renderer="cuorewebpage:templates/tasks.mako")
def Tasks(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section']  = 'Tasks'
        ctx['id'] = -1
        if getCurrentUser(request) is None:
            return redirectUser(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            print "We have an actual user!!"
            mUser     = User(uid=request.session['uid'])
            mCalendar = mUser.getCalendar()

            #Handle the POST request here
            if request.POST:
                print "============================="
                print "\tGot a POST!"
                print "\tAction = " + str(request.POST.getone('action'))
                print "============================="

                #Create New Event
                if request.POST.getone('action') == '0':
                    title = request.POST.getone('title')
                    start = long(request.POST.getone('sTime'))/1000
                    end   = long(request.POST.getone('eTime'))/1000

                    nEvent = Event(Name=title, sTime=start, eTime=end, Owner=mUser.getNode())
                    mCalendar.addEvent(nEvent.getNode())
                    ctx['id'] = nEvent.getNode()._id

                    print "============================="
                    print "\tNew Event!"
                    print "\tTitle: " + title
                    print "\tId   : " + str(ctx['id'])
                    print "\tsTime: " + str(start)
                    print "\teTime: " + str(end)
                    print "============================="


                #Adjust Time of Event
                elif request.POST.getone('action') == '1':
                    print "============================="
                    print "\tId   \t: " + request.POST.getone('id')
                    print "\tsTime\t: " + str(long(request.POST.getone('sTime'))/1000)
                    print "\teTime\t: " + str(long(request.POST.getone('eTime'))/1000)
                    print "============================="
                    mEvent = Event(graph_db.node(request.POST.getone('id')))
                    mEvent.setStartTime(long(request.POST.getone('sTime'))/1000)
                    mEvent.setEndTime(long(request.POST.getone('eTime'))/1000)


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

@view_config(route_name="Workspace", renderer="cuorewebpage:templates/workspace.mako")
def Workspace(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectUser(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            print "We have an actual user!!"
            mUser     = User(uid=request.session['uid'])
            mCalendar = mUser.getCalendar()
        ctx = {}
        ctx['section'] = 'Workspace'
        ctx['user'] = mUser
#        ctx['department'] = Department(User(mUser).getDepartment())
        ctx['posts'] = list()

        posts = ctx['user'].getMainDepBlogPosts()

        for p in posts:
            ctx['posts'].append(Post(p))

        return ctx
    else:
        return redirectUser(request)
