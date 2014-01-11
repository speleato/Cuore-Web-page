from database_config 	import *
from Task 				import *
from py2neo 			import neo4j, node
from datetime 			import datetime,time
from Calendar 			import Calendar
from Event 				import Event
from Project			import Project
from Workspace 			import Workspace

if __name__ == '__main__':

	def dateTimeToMillis(dateTime):
		return (dateTime-datetime(1970,1,1)).total_seconds()*1000

	#Fill in node id with your own User Node
	nodeID = 140

	mUser = neo4j.Node("http://localhost:7474/db/data/node/" + str(nodeID))
	mUser2= neo4j.Node("http://localhost:7474/db/data/node/" + str(nodeID+1))

	if "User" in mUser.get_labels():
		print(mUser["name"] + " is a User with id of " + str(mUser._id))
	else:
		raise Exception("No User")

	#Get the Times that everything occurs
	event_winterbreak_sTime 	= datetime(2013, 12, 15)
	event_winterbreak_eTime 	= datetime(2014, 1, 2)

	#Create the Calendar
	appCalendar				= Calendar(Name="Applications Team", Owner=mUser)
	
	#Create our Break Event
	event_winterbreak 		= Event(Name="Winter Break Development", Owner=mUser, 
		sTime=dateTimeToMillis(event_winterbreak_sTime), 
		eTime=dateTimeToMillis(event_winterbreak_eTime))
	
	#Create all the tasks that have to be done
	task_develop_calendar 			= Task(Name="Develop Calendar System", Status=STS_CLOSED)
	task_develop_task_system		= Task(Name="Develop Task System", Status=STS_CLOSED)
	task_develop_workspace_system	= Task(Name="Develop Workspace System", Status=STS_IN_PROG)
	task_develop_project_system		= Task(Name="Develop Project System", Status=STS_OPEN)	
	
	#Create our workspace and intranet project
	workspace_appteam				= Workspace(Name="Applications Team")
	project_intranet				= Project(Name="Intranet Project")

	#Set the description of our winterbreak project
	event_winterbreak.setDescription("Developing the Intranet to a useable state")

	#Set the description of our tasks
	task_develop_calendar.setDescription("Develop a working Calendar System to implement into the intranet")
	task_develop_task_system.setDescription("Develop a working task system to implement into the intranet")
	task_develop_workspace_system.setDescription("Develop a working workspace system to implement into the intranet")
	task_develop_project_system.setDescription("Develop a working project system under workspace system in the intranet")

	#Add the Owner of each task (Who is going to fulfill the task)
	appCalendar.addOwner(mUser)
	task_develop_calendar.setOwner(mUser)
	task_develop_task_system.setOwner(mUser)
	task_develop_workspace_system.setOwner(mUser2)
	task_develop_project_system.setOwner(mUser2)

	#Add the event to our calendar
	appCalendar.addEvent(event_winterbreak.getNode())

	#add the tasks to both our event and our project
	event_winterbreak.addTask(task_develop_calendar.getNode())
	event_winterbreak.addTask(task_develop_task_system.getNode())
	event_winterbreak.addTask(task_develop_workspace_system.getNode())
	project_intranet.addTask(task_develop_calendar.getNode())
	project_intranet.addTask(task_develop_task_system.getNode())
	project_intranet.addTask(task_develop_workspace_system.getNode())
	project_intranet.addTask(task_develop_project_system.getNode())

	#Add a project subtask to the workspace task
	task_develop_workspace_system.addSubTask(task_develop_project_system.getNode())

	#Add the Intranet Project to our workspace
	workspace_appteam.addProject(project_intranet.getNode())

	#task_develop_calendar.clear()