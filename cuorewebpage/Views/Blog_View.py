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

@view_config(route_name="Blog", renderer="cuorewebpage:templates/blog.mako")
def blog(request):
    return {}
