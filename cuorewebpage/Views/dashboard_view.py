from pyramid.view import view_config
from pyramid.response import Response
from py2neo import neo4j, node
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Project import *
from cuorewebpage.Model.Task import *
from cuorewebpage.Model.Post import *
from cuorewebpage.Model.Company import getCompany


@view_config(route_name='Dashboard', renderer='cuorewebpage:templates/dashboard.mako')
def dashboard(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Dashboard'
        if getCurrentUser(request) is None:
            return redirectUser(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            print "We have an actual user!!"
            mUser     = User(uid=request.session['uid'])
            mCalendar = mUser.getCalendar()

            alerts = list()

            posts     = list()
            for p in Blog(Name="Cuore").getPosts():
                posts.append(Post(p))
                alerts.append({"type": "post", "node": Post(URI=p).getNode()})

            events    = list()
            for event in mCalendar.getEvents():
                events.append(Event(URI=event))
                alerts.append({"type": "event", "node": Event(URI=event).getNode()})

            #Get all the Events that we have been invited to
            for event in mUser.getInvitedEvents():
                events.append(event)
#                alerts.append({"type": "event", "node": Event(URI=event).getNode()})

            #Get Tasks for the tasks sidebar
            tasks       = list()
            for task in mUser.getAssignedTasks():
                tasks.append(task)
                alerts.append({"type": "task", "node": Task(URI=task).getNode()})

#            workspace   = mUser.getWorkspace()
#            projects    = workspace.getProjects()
#            for project in projects:
#                for task in (Project(project)).getTasks():
#                    if Task(task).getAssignedUsers() == mUser:
#                        tasks.append(Task(task))

            ctx['alerts'] = alerts

            ctx['user']     = mUser
            ctx['calendar'] = mCalendar
            ctx['posts']    = posts
            ctx['events']   = events
            ctx['tasks']    = tasks

#            for item in alerts:
#                print "========================="
#                print item.getName()
        return ctx
    else:
        return redirectUser(request)



# Function  : sortNodesByTime
# Arguments : a list of nodes, a type of Time (eTime, sTime, iTime)
def sortNodesByTime(nodeList=None, tTime=None):
    return ()

def checkAlertType(alert):
    global LBL_POST, LBL_EVENT, LBL_TASK, LBL_COMMENT
    labels = neo4j.Node(alert).get_labels()
    if len(labels) != 0:
        return labels[0]
    return None


