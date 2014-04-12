from pyramid.view import view_config

from py2neo import neo4j, ogm
from database_config import db_config
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *
from cuorewebpage.Model.Company import Company

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Directory", renderer="cuorewebpage:templates/Directory.mako")
def Directory(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        ctx = {}
        ctx['user'] = getCurrentUser(request)
        ctx['section'] = 'Directory'

        company = Company(Name="Cuore")

        departments = {}
        for d in company.getDepartments():
            dept = Department(d)
            if dept.getName() != "Admin":
                titles = list()
                for t in dept.getTitles():
                    titles.append(Title(t))
                departments[dept] = titles

        ctx['departments'] = departments
        ctx['company'] = company
        return ctx
    else:
        return redirectUser(request)
