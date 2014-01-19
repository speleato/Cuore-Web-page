from cuorewebpage.Model.Blog import Blog
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Comment import Comment
from cuorewebpage.Model.Department import Department
from cuorewebpage.Model.Event import Event
from cuorewebpage.Model.Post import Post
from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task, STS_OPEN
from cuorewebpage.Model.Title import Title
from cuorewebpage.Model.User import User
from cuorewebpage.Model.Workspace import Workspace

__author__ = 'vincente'

#create Company
mDept       = Department(name="Applications")
mTitle      = Title(name="Applications Developer", dept=mDept.getNode())
mUser       = User(first_name="Vincente", last_name="Ciancio", email="vciancio@socaldevs.com")
mUser2      = User(first_name="Billy", last_name="bob", email="billybob@myspace.com")
mBlog       = Blog(Name="Applications Blog")
mPost1      = Post(Name="Getting Stuff Done!", Content="We are making a lot of progress!")
mComment    = Comment(Name="Good Job!", Content="Good Job Guys!")
mCalendar   = Calendar(Name="Applications Calendar")
mEvent      = Event(Name="Hackathon Day!", sTime=7, eTime=8, Owner=mUser.getNode())
mWorkspace  = Workspace(Name="Vincente's Workspace")
mProject    = Project(Name="Intranet")
mTask       = Task(Name="Finish the Intranet!", Status=STS_OPEN)


#Link everything together

mBlog.addPost(mPost1.getNode())
mPost1.addComment(mComment.getNode())
mUser.setTitle(mTitle.getNode())
mCalendar.addEvent(mEvent.getNode())
mCalendar.addOwner(mUser.getNode())
mEvent.addInvitee(mUser2.getNode())
mWorkspace.addProject(mProject.getNode())
mWorkspace.addOwner(mUser.getNode())
mProject.addTask(mTask.getNode())
mTask.assignToUser(mUser.getNode())