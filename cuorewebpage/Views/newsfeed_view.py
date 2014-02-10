from pyramid.view import view_config

import time

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Blog import *
from cuorewebpage.Model.Post import *
from cuorewebpage.Model.Event import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Newsfeed", renderer="cuorewebpage:templates/newsfeed.mako")
def Newsfeed(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Newsfeed'
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            mUser     = User(uid=request.session['uid'])
            mBlog = Blog(Name="Cuore")
            mCalendar = mUser.getCalendar()

            alerts = list()

            posts     = list()
            for p in mBlog.getPosts():
                post = Post(p)
                print "!! POST !!----------------------------"
                print post
                print "!!!!!!!-------------------------------"
                posts.append(post)
                alerts.append({"type": "post", "time": post.getUpdateTime(), "node": post})

            events    = list()
            for e in mCalendar.getEvents():
                event = Event(e)
                print "!! EVENT !!----------------------------"
                print event
                print "!!!!!!!-------------------------------"
                events.append(event)
                alerts.append({"type": "event", "time": event.getUpdateTime(), "node": event})

            #Get all the Events that we have been invited to
            for event in mUser.getInvitedEvents():
                events.append(event)
            #                alerts.append({"type": "event", "node": Event(URI=event).getNode()})

            if request.POST:
                print "making a Cuore blog post"

            ctx['alerts'] = alerts

            ctx['user']     = mUser
            ctx['calendar'] = mCalendar
            ctx['posts']    = posts
            ctx['events']   = events

            return ctx
    else:
        return redirectUser(request)
