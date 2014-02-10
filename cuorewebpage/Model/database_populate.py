"""
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

departments = [ Department(name="Business", company=company).getNode(),
                Department(name="Applications", company=company).getNode(),
                Department(name="Hardware", company=company).getNode(),
                Department(name="Systems", company=company).getNode(),
                Department(name="Admin", company=company).getNode(), ]
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
               req_title="Applications Developer", photo="cuorewebpage:img/menu_icons/profile.png").getNode(),
    vincente=User(uid="ENIFCyZRQceEalwDDBI8nA==", first_name="Vincente", last_name="Ciancio", email="vincente@cuore.io", confirmed=3,
                  req_title="Applications Developer", ).getNode(),
    sergio=User(uid="tFNm//nfbPwzHfYyVYHv6w==", first_name="Sergio", last_name="Peleo", email="sergio@cuore.io", confirmed=3,
                req_title="Lead Applications Developer", ).getNode(),
    mason=User(uid="5", first_name="Mason", last_name="Borda", email="mason@cuore.io", confirmed=3,
               req_title="Lead Hardware Engineer").getNode(),
    kevin_a=User(uid="6", first_name="Kevin", last_name="Aloysius", email="luscious@cuore.io", confirmed=3,
                 req_title="Lead Systems Engineer").getNode(),
    test=User(uid="7", first_name="Tester", last_name="Jones", email="TJones@cuore.io", confirmed=0, req_dept="Applications",
               req_title="Applications Developer", photo="cuorewebpage:img/menu_icons/profile.png").getNode())

unconfirmedNode=graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed", {"name":"unconfirmed"})
graph_db.create((users['test'], REL_UNCONFIRMED, unconfirmedNode))
#Calendar(Name=(user.getFullName() + "'s Calendar"), Owner=user.getNode())

graph_db.create(
    (titles['Admin'], REL_HASUSER, users['kirby']),
    (titles['Admin'], REL_HASUSER, users['leo']),
#    (titles['Admin'], REL_HASUSER, users['sandy']),
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

for team in departments:
    workspaces = list()
    workspaces.append(Workspace(Name=(Department(team).getName() + " Workspace"), Owner=Department(team).getNode()))

bus_blog = Blog(Name="Business", Owner=departments[0])
app_blog = Blog(Name="Applications", Owner=departments[1])
hw_blog = Blog(Name="Hardware", Owner=departments[2])
sys_blog = Blog(Name="Systems", Owner=departments[3])
adm_blog = Blog(Name="Admin", Owner=departments[4])
cuore_blog = Blog(Name="Cuore", Owner=company)
cuore_blog.setDescription("Company wide news")

event_meet_time = (datetime.now()-datetime(1970,1,1)).total_seconds()
event_meeting   = Event(Name="General Meeting", Owner=users['leo'], sTime=event_meet_time, eTime=event_meet_time)
leo_calendar    = Calendar(Name=(User(users['leo']).getFullName() + "'s Calendar"), Owner=User(users['leo']).getNode())
leo_calendar.addEvent(event_meeting.getNode())

app_team = Department(departments[1]).getUsers()


for person in app_team:
    mUser = User(person)
    workspace = mUser.getWorkspace()

    app_calendar    = Calendar(Name=(mUser.getFullName() + "'s Calendar"), Owner=mUser.getNode())
    event_app_time  = (datetime(2014, 1, 19)-datetime(1970,1,1)).total_seconds()
    event_app_hack  = Event(Name="Applications Hack Event", sTime=event_app_time, eTime=event_app_time)
    event_app_hack.addOwner(users['sergio'])

    app_calendar.setDescription("Calendar which outlines all of the tasks that are assigned to" + mUser.getFirstName())
    app_calendar.addEvent(event_app_hack.getNode())
    event_meeting.addInvitee(mUser.getNode())

    project     = Project(Name="Intranet Project")
    task1       = Task(Name="Finish the Intranet", Status=STS_IN_PROG)
    task1.assignToUser(mUser.getNode())

    workspace.addProject(project.getNode())
#    workspace.addOwner(mUser.getNode())
    project.addTask(task1.getNode())


for key in users.keys():
    mUser = User(users[key])
    calendar    = Calendar(Name=(mUser.getFullName() + "'s Calendar"), Owner=mUser.getNode())
#    workspace   = Workspace(Name=(mUser.getFullName() + "'s Workspace"), Owner=mUser.getNode())

sandy = User(users['sandy'])
"""
"""post1 = Post(Name="My Goodness", Content="I am so totally cracked out from doing this all night, I really should" \
                                         " learn not to procrastinate so that I don't have to pull all nighters", Owner=sandy.getNode())
post2 = Post(Name="Quite Exciting", Content="Maybe it is time for me to go to sleep, although looking at the clock" \
    " I almost feel like what a wuss, it's only 12:25!", Owner=sandy.getNode())
post3 = Post(Name="Maybe it's the lead paint though", Content="Did you know that lead paint vaporizes around or above 1100 degrees" \
    " Fahrenheit? Yeah, so maybe house paint from 1906 and blowtorches aren't the best combination for your health" \
    " but what are you going to do?", Owner=sandy.getNode())
post1.setBlog(cuore_blog.getNode())
post2.setBlog(cuore_blog.getNode())
post3.setBlog(cuore_blog.getNode())


"""
