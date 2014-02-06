from pyramid.response import Response
from pyramid.view import view_config
import re

from py2neo import neo4j, ogm
from database_config import *

from cuorewebpage.Model.User import *
from cuorewebpage.Model.Company import *
from cuorewebpage.Model.Department import Department
from cuorewebpage.Model.Title import Title
from cuorewebpage.lib.session import *

import pyramid.httpexceptions

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="AdminPanel", renderer="cuorewebpage:templates/admin.mako")
def admin_panel(request):
    print request
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        if not getCurrentUser(request).isAdmin():
            raise pyramid.httpexceptions.HTTPForbidden()
        ctx = {}
        ctx['section'] = 'Admin Panel'
        # ctx['departments'] holds a dictionary in the form {Department_name : array_of_title_dictionaries}
        #       array_of_title_dictionaries is in the form: [{title_name : array_of_user_dictionaries}, {title_name: ...]
        #       user dictionaries are in the form: {full_name : UID}
        ctx['departments'] = {}
        for i in Company(Name="Cuore").getDepartments():
            print i
            print type(i)
            titles=[]
            for j in Department(i).getTitles():
                users = []
                for k in Title(j).getUsers():
                    users.append({User(k).getFullName(): User(k).getUID()})
                titles.append({Title(j).getName(): users})
            ctx['departments'][Department(i).getName()] = titles
        ctx['unconfirmed'] = []
        # holds array of unconfirmed user dictionaries in the form of {Full_name: uid}
        for i in getUnconfirmed():
            ctx['unconfirmed'].append({i.getFullName(): i.getUID()})
        ctx['unassigned'] = []
        # holds array of unassigned user dictionaries in the form of {Full_name: uid}
        for i in getUnassigned():
            ctx['unassigned'].append({i.getFullName(): i.getUID()})



        if request.POST:
            if request.POST.getone("addDep"):
                store.load_unique(IND_COMP, "name", "Cuore", Company).addDepartment(re.escape(request.POST.getone("addDep")))
                print 1
            elif request.POST.getone("addTitle"):
                store.load_unique(IND_DEP, "name", request.POST.getone("addToDep"), Department).addTitle(re.escape(request.POST.getone("addTitle")))
                print 2
            elif request.POST.getone("remDep"):
                store.load_unique(IND_COMP, "name", "Cuore", Company).removeDepartment(re.escape(request.POST.getone("remDep")))
                print 3
            elif request.POST.getone("remTitle"):
                store.load_unique(IND_DEP, "name", request.POST.getone("remFromDep"), Department).removeTitle(re.escape(request.POST.getone("remTitle")))
                print 4

        return (ctx)
    else:
        return redirectUser(request)

