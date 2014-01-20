import re

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
    print "this is starting to get to my nerves"
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Blog'
        ctx['user'] = getCurrentUser(request)
        ctx['blog'] = getUserBlog(request)
        ctx['posts'] = getUserBlog(request).getPosts() # A LIST OF NODES (one 'object', the list)
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Entry', renderer='cuorewebpage:templates/blogentry.mako')
def blog_post_view(request):
    if isUserLoggedOn(request):
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
        ctx['section'] = "Create Blog Post"
        ctx['user'] = getCurrentUser(request)
        owner = User(uid=request.session['uid'])
        blog = getUserBlog(request)
        if request.POST:
            post_name =re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('name'))
            post_content =re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('content'))
            post = Post(Name=post_name, Content=post_content, Owner=owner.getNode())
            post.setBlog(blog.getNode())
            return HTTPFound(location=request.route_url('Blog'))
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Action', match_param='action=update', renderer='cuorewebpage:templates/blog_edit.mako')
def blog_post_update(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = "Update Blog Post"
        ctx['user'] = getCurrentUser(request)
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Action', match_param='action=dashboard', renderer='cuorewebpage:templates/blog_dashboard.mako')
def blog_post_update(request):
    if isUserLoggedOn(request):
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
