from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task
from cuorewebpage.Model.Department import Department
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Workspace import Workspace
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
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        ctx = {}
        ctx['section']  = 'Tasks'

        if getCurrentUser(request) is None:
            return redirectUser(request)
        else:
            print "We have an actual user!!"
            mUser     = getCurrentUser(request)
            mDept     = Department(mUser.getDepartment())
            mWorkspace = Workspace(mDept.getWorkspace())

            projects  = list()
            for p in mWorkspace.getProjects():
                projects.append(Project(p))

            tasks     = list()
            for t in mUser.getAssignedTasks():
                tasks.append(Task(t))

            #Handle the POST request here
            if request.POST:
                print "============================="
                print "\tGot a POST!"
                print "\tAction = " + str(request.POST.getone('action'))
                print "============================="

                #Create New Task

            ctx['user']     = mUser
            ctx['tasks']    = tasks
            ctx['projects']   = projects

        return ctx
    else:
        return redirectUser(request)

@view_config(route_name="Workspace", renderer="cuorewebpage:templates/workspace.mako")
def Workspace(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Workspace'
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            mUser     = User(uid=request.session['uid'])
            mDept     = mUser.getDepartment()
            mWorkspace = Department(mDept).getWorkspace()
            projects = list()
            for p in mWorkspace.getProjects():
                projects.append(Project(p))
            mBlog      = Department(mDept).getBlog()

        posts = list()
        for p in mUser.getMainDepBlogPosts():
            posts.append(Post(URI=p))

        tasks = list()
        for p in projects:
            for t in p.getTasks():
                tasks.append(Task(t))


        ctx['user'] = mUser
        ctx['department'] = Department(mDept)
        ctx['posts'] = posts
        ctx['projects'] = projects
        ctx['tasks'] = tasks
        return ctx
    else:
        return redirectUser(request)
