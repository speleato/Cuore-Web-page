from cuorewebpage.Model.Blog import Blog
from cuorewebpage.Model.Calendar import Calendar
from cuorewebpage.Model.Comment import Comment
from cuorewebpage.Model.Post import Post
from cuorewebpage.Model.Project import Project
from cuorewebpage.Model.Task import Task, STS_OPEN
from cuorewebpage.Model.Workspace import Workspace

__author__ = 'vincente'
'''
#create Company
#create Department
#create title
#create User
mBlog       = Blog(Name="Applications Blog")
mPost1      = Post(Name="Getting Stuff Done!", Content="We are making a lot of progress!")
mComment    = Comment(Name="Good Job!", Content="Good Job Guys!")
mCalendar   = Calendar(Name="Applications Calendar")
#mEvent      = Event(Name="Hackathon Day!", sTime=7, eTime=8)
mWorkspace  = Workspace(Name="Vincente's Workspace")
mProject    = Project(Name="Intranet")
mTask       = Task(Name="Finish the Intranet!", Status=STS_OPEN)


#Link everything together

mBlog.addPost(mPost1)
mPost1.addComment(mComment)

#mCalendar.addEvent(mEvent)
mWorkspace.addProject(mProject)
mProject.addTask(mTask)
'''