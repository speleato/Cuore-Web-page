from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *


from py2neo import neo4j, ogm
from database_config import *

import cgi
import cgitb
import urllib2

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Files", renderer="cuorewebpage:templates/files.mako")
def Files(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Files'
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name="FileUpload", renderer="cuorewebpage:templates/files.mako")
def FileUpload(request):
    if isUserLoggedOn(request):
        if request.POST.get('file') is not None:
            file = request.POST.get('file').file
            name = request.POST.get('file').filename

            #We store the file in the database
            userNode = graph_db.getNodeById(IND_FILE)
            print userNode
        else:
            print "error in POST file upload."
        return HTTPFound(location=request.route_url('Files'))
    else:
        return redirectUser(request)


@view_config(route_name="FileDownload", renderer="cuorewebpage:templates/files.mako")
def FileDownload(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Files'
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name="FileDelete", renderer="cuorewebpage:templates/files.mako")
def FileDelete(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Files'
        return ctx
    else:
        return redirectUser(request)