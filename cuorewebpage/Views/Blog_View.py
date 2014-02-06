import re
import datetime

from pyramid.response import Response
from pyramid.view import view_config
from py2neo import neo4j, ogm

from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Title import *
from cuorewebpage.Model.Department import *
from cuorewebpage.Model.Blog import *
from cuorewebpage.Model.Post import *

#graph_db = neo4j.GraphDatabaseService(db_config['uri'])
#store = ogm.Store(graph_db)


@view_config(route_name='Blog', renderer='cuorewebpage:templates/blog.mako')
def blog_list_view(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Blog'

        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            print "We have an actual user!!"
            mUser     = User(uid=request.session['uid'])
            mBlog     = Blog(Name="Cuore")

            posts     = list()
            for p in mBlog.getPosts():
                posts.append(Post(p))

            ctx['user']     = mUser
            ctx['blog']     = mBlog
            ctx['posts']    = posts

        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Entry', renderer='cuorewebpage:templates/blogentry.mako')
def blog_post_view(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        ctx = {}
        ctx['section'] = "Blog Dashboard"
        ctx['user'] = getCurrentUser(request)
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name='Blog_Action', match_param='action=create', renderer='cuorewebpage:templates/blog_create.mako', )
def blog_post_create(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Create Blog Post'

        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        else: #Get the user, calendar, and events so we can populate them in the template
            print "We have an actual user!!"
            mUser     = User(uid=request.session['uid'])
            mBlog     = Blog(Name="Cuore")

            if request.POST:
#                post_blog = request.POST.getone('blog')
                post_name =re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('name'))
                post_content =re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('content'))
                post = Post(Name=post_name, Content=post_content, Owner=mUser.getNode(), Blog=mBlog.getNode())
                #            post.setBlog(blog.getNode())
    #            post.setBlog(Blog(Name=post_blog).getNode())
                return HTTPFound(location=request.route_url('Blog'))

            ctx['user']     = mUser
            ctx['blog']     = mBlog
            return ctx
    else:
        return redirectUser(request)


@view_config(route_name='Blog_Action', match_param='action=update', renderer='cuorewebpage:templates/blog_edit.mako')
def blog_post_update(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        ctx = {}
        ctx['section'] = "Update Blog Post"
        ctx['user'] = getCurrentUser(request)
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Action', match_param='action=dashboard', renderer='cuorewebpage:templates/blog_dashboard.mako')
def blog_post_update(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        ctx = {}
        ctx['section'] = "Blog Dashboard"
        ctx['user'] = getCurrentUser(request)
        return ctx
    else:
        return redirectUser(request)





"""
        print "==========================================================================="
        print "SESSION UID : " + request.session['uid']
        print getCurrentUser(request).first_name
        print "==========================================================================="
"""
"""
        print "==========================================================================="
        print owner
        title = Title(owner.getTitles())
        print "TITLE:   " + title.getName()
        department = Department(title.getDepartments()[0])
        print "DEPARTMENT:  " + department.getName()
        blog = Blog(department.getBlog()[0])
        print "BLOG:  " + blog.getName()
        print "==========================================================================="
"""
"""        for node in post_nodes_list:
            tempPost = { "name": Post(node).getName(), "content": Post(node).getContent()}
            print "this is what the post looks like for now"
            print tempPost
            ctx['posts'].append(tempPost)
            """
"""     print "==========================================================================="
        for p in ctx['posts']:
            print "------POST-------"
            print Post(p).getName()
            print Post(p).getContent()
            print "==========================================================================="
"""
#        page = int(request.params.get('page', 1))
#        ctx['paginator'] = Post.get_paginator(request, page)

#        blogs = ctx['user'].getDepBlogs() # a list of Blog nodes
#        posts = list()
#        for b in blogs:
#            posts.extend(Blog(b).getPosts()) # a list of Post nodes
