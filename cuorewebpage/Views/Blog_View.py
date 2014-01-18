import re
from pyramid.response import Response
from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Post import *
from cuorewebpage.Model.Blog import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])


@view_config(route_name='Blog', renderer='cuorewebpage:templates/blog.mako')
def blog_view(request):
    if isUserLoggedOn(request):
        print "==========================================================================="
        print "SESSION UID : " + request.session['uid']
        print "==========================================================================="
        ctx = {}
        ctx['section'] = 'Blog'
        ctx['user'] = getCurrentUser(request)
#        ctx['blog'] = ctx['user'].getBlog()

        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Action', match_param='action=create', renderer='cuorewebpage:templates/blog_create.mako', )
def post_create(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = "Create Blog Post"
        ctx['user'] = getCurrentUser(request)
#        ctx['user_blog'] = ctx['user'].getBlog()
        if request.POST:
            post_name =re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('name'))
            post_content =re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('content'))
            post = Post(Name=post_name, Content=post_content, Owner=getCurrentUser(request).getNode())
#            post.setOwner(getCurrentUser(request).getNode())
        return ctx
    else:
        return redirectUser(request)

@view_config(route_name='Blog_Action', match_param='action=update', renderer='cuorewebpage:templates/blog_edit.mako')
def post_update(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = "Update Blog Post"
        return ctx
    else:
        return redirectUser(request)
