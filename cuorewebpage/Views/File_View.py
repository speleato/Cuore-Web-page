from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.File import *
from cuorewebpage.Model.Person import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Project import *

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
        mUser     = User(uid=request.session['uid'])
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        ctx = {}
        ctx['section'] = 'Files'
        user = User(uid = request.session['uid'])
        projects = list()
        tasks = list()
        departments = user.getDepartments()
        workspace = user.getWorkspace()
        if workspace is not None:
            projects = workspace.getProjects()
            #we have a set of nodes
            if projects is not None:
                for k in projects:
                    for v in Project(None, k["name"]).getTasks():
                        tasks.append(v)


        ctx['department'] = list()
        ctx['workspaces'] = list()
        ctx['projects'] = list()
        ctx['tasks'] = list()
        ctx['user'] = mUser

        if departments is not None:
            for i in departments:
                ctx['department'].append(i['name'])
        if projects is not None:
            for i in projects:
                ctx['projects'].append(i['name'])
        if tasks is not None:
            for i in tasks:
                ctx['tasks'].append(i['name'])

        #We will now display the files that the user has access.
        fileList = list()
        if departments is not None:
            for i in departments:
                dept = Department(name=i['name'])
                departamentFiles = dept.getFiles()
                for k in departamentFiles:
                    fileList.append([k['name'], dept.getName(), k['file']])
        ctx['fileList'] = fileList
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name="FileUpload", renderer="cuorewebpage:templates/files.mako")
def FileUpload(request):
    if isUserLoggedOn(request):
        if request.POST.get('file') is not None:

            user = request.session['uid']

            fileString = request.POST.get('file').value
            name = request.POST.get('file').filename
            department = request.POST.get('department')
            project = request.POST.get('project')
            task = request.POST.get('task')

            #We store the file in the database
            file = File(None, name, department, task)
            file.storeFile(fileString, project, task, request.session['uid'])
        else:
            print "error in POST file upload."
        return HTTPFound(location=request.route_url('Files'))
    else:
        return redirectUser(request)


@view_config(route_name="FileDownload", renderer="cuorewebpage:templates/files.mako")
def FileDownload(request):
    if isUserLoggedOn(request):
        if request.POST.get('file') is not None:

            user = request.session['uid']

            fileToDownload = request.POST.get('file')
            department = request.POST.get('department')

            #We store the file in the database
            file = File(None, fileToDownload, department)
            return file.downloadFile(department, fileToDownload, request)

        else:
            print "error in POST file upload."
            print request
        return HTTPFound(location=request.route_url('Files'))
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
