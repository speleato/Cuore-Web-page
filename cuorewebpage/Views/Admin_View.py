from pyramid.response import Response
from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

import time

from py2neo import neo4j, ogm
from database_config import db_config

from cuorewebpage.Model.Person import Company, Department, Title, Person

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="AdminPanel", renderer="cuorewebpage:templates/admin.mako")
def admin_panel(request):
    print request
    if request.POST:
        if request.POST.getone("addDep"):
            store.load_unique("Company", "name", "Cuore", Company).addDepartment(request.POST.getone("addDep"))
            print 1
        elif request.POST.getone("addTitle"):
            store.load_unique("Department", "name", request.POST.getone("addToDep"), Department).addTitle(request.POST.getone("addTitle"))
            print 2
        elif request.POST.getone("remDep"):
            store.load_unique("Company", "name", "Cuore", Company).removeDepartment(request.POST.getone("remDep"))
            print 3
        elif request.POST.getone("remTitle"):
            store.load_unique("Department", "name", request.POST.getone("remFromDep"), Department).removeTitle(request.POST.getone("remTitle"))
            print 4

    return {'section': 'Admin Panel'}

