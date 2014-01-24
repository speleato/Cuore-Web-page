from py2neo import neo4j, ogm, node, rel
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Event import Event

from datetime import datetime
from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task, STS_OPEN, STS_IN_PROG
from cuorewebpage.Model.Workspace import Workspace
from database_config import *
#from Person import getCurrentUser, getUser
from Company import Company
from Department import Department
from Title import Title
from User import User, getCurrentUser, getUser
from Blog import Blog
from Post import Post

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
graph_db.clear()


company = Company(Name="Cuore").getNode()

departments = [ Department(name="business", company=company).getNode(),
                Department(name="applications", company=company).getNode(),
                Department(name="hardware", company=company).getNode(),
                Department(name="systems", company=company).getNode(),
                Department(name="admin", company=company).getNode(), ]
titles = dict(
    Pres=Title(name="President", dept=departments[0]).getNode(),
    VP=Title(name="Vice-President", dept=departments[0]).getNode(),
    AppDev=Title(name="Applications Developer", dept=departments[1]).getNode(),
    WebAppDev=Title(name="Web Applications Developer", dept=departments[1]).getNode(),
    LeadAppDev=Title(name="Lead Applications Developer", dept=departments[1]).getNode(),
    LeadHwEngr=Title(name="Lead Hardware Engineer", dept=departments[2]).getNode(),
    LeadSysEngr=Title(name="Lead Systems Engineer", dept=departments[3]).getNode(),
    Admin=Title(name="Admin", dept=departments[4]).getNode(),
    )

users = dict(
    leo=User(uid="0", first_name="Leo", last_name="Schultz", email="leo@cuore.io", confirmed=3, req_title="President").getNode(),
    kevin_r=User(uid="1", first_name="Kevin", last_name="Ryan", email="kevin@cuore.io", confirmed=3, req_title="Vice-President").getNode(),
    sandy=User(uid="2C1F3V0RiQqS0rJY5qEejQ==", first_name="Sandy", last_name="Siththanandan", email="sandy@cuore.io",
               confirmed=3, req_title="Applications Developer", phone="6502695948", city="SF", state="CA", zipcode="94112").getNode(),
    kirby=User(uid="7jxjnWJGsgCTBjzKX7Yk3Q==", first_name="Kirby", last_name="Linvill", email="kirby@cuore.io", confirmed=3,
               req_title="Applications Developer", ).getNode(),
    vincente=User(uid="ENIFCyZRQceEalwDDBI8nA==", first_name="Vincente", last_name="Ciancio", email="vincente@cuore.io", confirmed=3,
                  req_title="Applications Developer", ).getNode(),
    sergio=User(uid="4", first_name="Sergio", last_name="Peleo", email="sergio@cuore.io", confirmed=3,
                req_title="Lead Applications Developer", ).getNode(),
    mason=User(uid="5", first_name="Mason", last_name="Borda", email="mason@cuore.io", confirmed=3,
               req_title="Lead Hardware Engineer").getNode(),
    kevin_a=User(uid="6", first_name="Kevin", last_name="Aloysius", email="luscious@cuore.io", confirmed=3,
                 req_title="Lead Systems Engineer").getNode())

graph_db.create(
    (titles['Admin'], REL_HASUSER, users['kirby']),
    (titles['Admin'], REL_HASUSER, users['leo']),
    (titles['Pres'], REL_HASUSER, users['leo']),
    (titles['VP'], REL_HASUSER, users['kevin_r']),
    (titles['AppDev'], REL_HASUSER, users['sandy']),
    (titles['AppDev'], REL_HASUSER, users['kirby']),
    (titles['AppDev'], REL_HASUSER, users['vincente']),
    (titles['LeadAppDev'], REL_HASUSER, users['sergio']),
    (titles['LeadHwEngr'], REL_HASUSER, users['mason']),
    (titles['LeadSysEngr'], REL_HASUSER, users['kevin_a']),
#    (users['sandy'], REL_ISMEMBER, departments[1]),
#    (users['sandy'], REL_ISMEMBER, departments[4]),
    )

bus_blog = Blog(Name="Business", Owner=departments[0])
app_blog = Blog(Name="Applications", Owner=departments[1])
hw_blog = Blog(Name="Hardware", Owner=departments[2])
sys_blog = Blog(Name="Systems", Owner=departments[3])
adm_blog = Blog(Name="Admin", Owner=departments[4])

event_meet_time = (datetime.now()-datetime(1970,1,1)).total_seconds()
event_meeting   = Event(Name="General Meeting", Owner=users['leo'], sTime=event_meet_time, eTime=event_meet_time)
leo_calendar    = Calendar(Name=(User(users['leo']).getFirstName() + "'s Calendar"), Owner=User(users['leo']).getNode())
leo_calendar.addEvent(event_meeting.getNode())

app_team = Department(departments[1]).getUsers()

for person in app_team:
    mUser = User(person)
    app_calendar    = Calendar(Name=(mUser.getFullName() + "'s Calendar"), Owner=mUser.getNode())
    event_app_time  = (datetime(2014, 1, 19)-datetime(1970,1,1)).total_seconds()
    event_app_hack  = Event(Name="Applications Hack Event", Owner=mUser.getNode(), sTime=event_app_time, eTime=event_app_time)

    app_calendar.setDescription("Calendar which outlines all of the tasks that are assigned to" + mUser.getFirstName())
    app_calendar.addEvent(event_app_hack.getNode())
    event_meeting.addInvitee(mUser.getNode())

    workspace   = Workspace(Name=(mUser.getFullName() + "'s Workspace"), Owner=mUser.getNode())
    project     = Project(Name="Intranet Project")
    task1       = Task(Name="Finish the Intranet", Status=STS_IN_PROG)
    task1.assignToUser(mUser.getNode())

    workspace.addProject(project.getNode())
#    workspace.addOwner(mUser.getNode())
    project.addTask(task1.getNode())


for key in users.keys():
    mUser = User(users[key])
    calendar    = Calendar(Name=(mUser.getFullName() + "'s Calendar"), Owner=mUser.getNode())
    workspace   = Workspace(Name=(mUser.getFullName() + "'s Workspace"), Owner=mUser.getNode())

"""
sandy = User(uid="0", first_name="sandy")
sandy.getNode().add_labels(LBL_USER)
print sandy.getNode().get_labels()
#post = Post(Name="hello", Content="blah", Owner=sandy)

user_index = graph_db.get_or_create_index(neo4j.Node, IND_USER)
menode=user_index.get("uid", "0")
print menode
#print menode.getNode()
#print menode.getName()


store = ogm.Store(graph_db)
#cuore = store.load_unique(IND_COMP, "name", "cuore", Company)
comp_index = graph_db.get_or_create_index(neo4j.Node, IND_COMP)
anode = comp_index.get("name", "Cuore")
print "-------->"
print anode
# what you get back is the URI
#   [Node('http://127.0.0.1:7474/db/data/node/44364')]
# if comma after anode, unpacking the list, you get
#   (44312 {"name":"Cuore"})
"""
