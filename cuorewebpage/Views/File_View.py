from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.File import *
from cuorewebpage.Model.Person import *
from cuorewebpage.Model.User import *

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
        currentUser = getUser(request.session['uid'])

        departments = file.getDepartmentByUID(request.session['uid'])
        if departments:
            for i in departments:
                ctx['department'].append(departments(i)['name'])
        else:
            ctx['department'] = []
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name="FileUpload", renderer="cuorewebpage:templates/files.mako")
def FileUpload(request):
    if isUserLoggedOn(request):
        if request.POST.get('file') is not None:

            user = request.session['uid']

            file = request.POST.get('file').value
            name = request.POST.get('file').filename
            #We store the file in the database
            file = File(None, name, file)
            file.storeFile()

            #Now that we have the file we relate it to the title.
            #file.assignToDepartment()
            #userNode = graph_db.getNodeById(IND_FILE)
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