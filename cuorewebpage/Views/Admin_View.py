from pyramid.response import Response
from pyramid.view import view_config
import re

from py2neo import neo4j, ogm
from database_config import *

from cuorewebpage.Model.Person import *
from cuorewebpage.Model.Company import Company
from cuorewebpage.Model.Department import Department
from cuorewebpage.lib.session import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="AdminPanel", renderer="cuorewebpage:templates/admin.mako")
def admin_panel(request):
    print request
    if isUserLoggedOn(request):
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

        return {'section': 'Admin Panel'}
    else:
        return redirectUser(request)

