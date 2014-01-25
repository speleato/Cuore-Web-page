from py2neo import neo4j, ogm, node, rel
from pyramid import request

from database_config import *
from cuorewebpage.lib.session import *
from cuorewebpage.Model.Blog import Blog
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Event import Event
from cuorewebpage.Model.Department import *
from cuorewebpage.Model.Title import Title
from cuorewebpage.Model.Workspace import Workspace

class Newsfeed:
    graph_db = None
    stream = list()

    def db_init(self):
        if self.graph_db is None:
            self.graph_db = neo4j.GraphDatabaseService(db_config['uri'])


