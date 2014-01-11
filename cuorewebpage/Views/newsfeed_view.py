from pyramid.response import Response
from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

import time

from py2neo import neo4j, ogm
from database_config import db_config

from cuorewebpage.Model.Person import Person

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name="Newsfeed", renderer="cuorewebpage:templates/newsfeed.mako")
def Newsfeed(request):
    if request.POST:
        newsNode=graph_db.create({"news":request.POST.getone('news'), "time":time.time(), "author":request.POST.getone('author')})
        departments=request.POST.getall('postTo[]')
        for i in departments:
            depNode=graph_db.get_indexed_node("Newsfeed", "name", i)
            number=depNode.get_properties()["numPosts"]
            depNode.update_properties({"numPosts":(number+1)})
            graph_db.create((depNode, "NEWS", newsNode[0]))
    return {}
