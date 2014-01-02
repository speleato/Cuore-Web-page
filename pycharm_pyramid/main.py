from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from Model import Model
from Views import Login_View, Registration_View

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

import time

from py2neo import neo4j, ogm
from database_config import db_config

import init_data

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

def Login(request):
    parameters = Model.get_initial_data()
    return Login_View.pushTemplate('Login.txt', parameters)


def Registration(request):
    parameters = Model.process_business_logic()
    if request.POST:
        if request.POST.getone('task') == "admin":
            title=request.POST.getone('title')
            email=request.POST.getone('email')
            department=request.POST.getone('department')

            # add updated info to database
            # Note: Either another unique identifier needs to be used or the admin panel shouldn't be allowed to change email
            personNode = graph_db.get_indexed_node("People", "email", email)
            # if leo confirmed, update confirmation flags
            confirmed=personNode.get_properties()["confirmed"]
            if(confirmed<2):
                confirmed += 2
            personNode.update_properties({"title":title, "email":email, "confirmed":confirmed})
            titleNode = graph_db.get_or_create_indexed_node("Title", "name", title, {"name":title})
            departmentNode = graph_db.get_indexed_node("Department", "name", department)
            graph_db.create((titleNode, "IS A", personNode), (departmentNode, "IN", titleNode))
            # after confirmed by Leo, send email to user
            confirmationNumber=personNode.get_properties()["confirmationNumber"]
            mailer = get_mailer(request)
            message = Message(subject="Confirm your Cuore Intranet Registration",
                  sender = "kirby@cuore.io",                    # change to admin email later
                  recipients = [email],
                  body = "You have been added to the Cuore intranet as a " + title + " in the "
                       + department + " department. Click on this link to confirm your"
                       + " registration: " + request.url + "/confirm?email="+email+"&confirm=" + confirmationNumber)
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "create":
            firstName=request.POST.getone('firstName')
            lastName=request.POST.getone('lastName')
            name=firstName + " " + lastName
            email=request.POST.getone('email')

            # generates a unique user ID for confirmation
            import uuid
            confirmationNumber=str(uuid.uuid4())
            # store confirmationNumber in db
            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            person = Person(firstName, lastName, email, None, 0, confirmationNumber)
            store.save_unique("People", "email", person.email, person)
            # after registration, send email to Leo
            mailer=get_mailer(request)
            message = Message(subject="Registration by " + name,
                              sender="kjlinvill@gmail.com",      # change to cuore mail server later
                              recipients=["kirby@cuore.io"],  # change to leo when rolled out
                              body=name + " has registered for the Cuore Intranet with the email "
                                     + email + ". Click here to confirm " + name
                                     + "'s registration: " + "link_to_admin_panel")
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "edit":
            phone = request.POST.getone('phone')
            address = request.POST.getone('address')
            about = request.POST.getone('about')
            # update info in database, need to pass in email, currently not implemented
            # personNode = graph_db.get_indexed_node("People", "email", email)
            # personNode.update_properties(properties='"phone":phone, "address":address, "about":about')
    return Registration_View.pushTemplate('Registration.mako')

def ConfirmRegistration(request):
    email=request.GET.getone('email')
    personNode = graph_db.get_indexed_node("People", "email", email)
    confirmationNumber=request.GET.getone('confirm')
    # check confirmationNumber against user's confirmationNumber
    if confirmationNumber == personNode.get_properties()["confirmationNumber"]:
        # move from temp area of database to permanent area of database
        confirmed=personNode.get_properties()["confirmed"]
        if(confirmed!=1 and confirmed!=3):
            confirmed += 1
        personNode.update_properties({"confirmed":confirmed})
    return Registration_View.pushTemplate('Registration.mako')

def Directory(request):
    return Registration_View.pushTemplate('Directory.mako')

def Profile(request):
    return Registration_View.pushTemplate('Profile.mako')

def Newsfeed(request):
    if request.POST:
        newsNode=graph_db.create({"news":request.POST.getone('news'), "time":time.time(), "author":request.POST.getone('author')})
        departments=request.POST.getall('postTo[]')
        for i in departments:
            depNode=graph_db.get_indexed_node("Newsfeed", "name", i)
            number=depNode.get_properties()["numPosts"]
            depNode.update_properties({"numPosts":(number+1)})
            graph_db.create((depNode, "NEWS", newsNode[0]))
    return Registration_View.pushTemplate('Newsfeed.mako')

def MainPage(request):
    return Registration_View.pushTemplate('MainPage.txt')

def Blog(request):
    return Registration_View.pushTemplate('Blog.txt')

def Files(request):
    return Registration_View.pushTemplate('Files.txt')

def Calendar(request):
    return Registration_View.pushTemplate('Calendar.txt')

def Workspace(request):
    return Registration_View.pushTemplate('Workspace.txt')

def Workspace(request):
    return Registration_View.pushTemplate('Admin.txt')

def Tasks(request):
    return Registration_View.pushTemplate('Admin.txt')

if __name__ == '__main__':
    #needed for pyramid mailer
    settings = {'mail.host': 'smtp.gmail.com', 'mail.port': '587', 'mail.username': 'username@gmail.com',
                'mail.password': 'password', 'mail.tls': 'True'}

    config = Configurator(settings=settings)
    config.include('pyramid_mailer')

    #ROUTES

    #tree = ET.parse('Routing/routes.xml')
    #root = tree.getroot()
    #for child in root.findall('route'):
    #    config.add_route(child.find('name').text, child.find('path').text)
    #    config.add_view(child.find('module'), route_name=child.find('name').text)
    config.add_route('Login', '/')
    config.add_view(Login, route_name='Login')

    config.add_route('Registration', '/registration')
    config.add_view(Registration, route_name='Registration')

    config.add_route('ConfirmRegistration', 'registration/confirm')
    config.add_view(ConfirmRegistration, route_name='ConfirmRegistration')

    config.add_route('Directory', '/directory')
    config.add_view(Directory, route_name='Directory')

    config.add_route('Profile', '/profile')
    config.add_view(Profile, route_name='Profile')

    config.add_route('Newsfeed', '/newsfeed')
    config.add_view(Newsfeed, route_name='Newsfeed')

    config.add_route('MainPage', '/main')
    config.add_view(MainPage, route_name='MainPage')

    config.add_route('Blog', '/blog')
    config.add_view(Blog, route_name='Blog')

    config.add_route('Files', '/files')
    config.add_view(Files, route_name='Files')

    config.add_route('Calendar', '/calendar')
    config.add_view(Calendar, route_name='Calendar')

    config.add_route('Workspace', '/workspace')
    config.add_view(Workspace, route_name='Workspace')

    config.add_route('Admin', '/DoNotPutAdmin')
    config.add_view(Workspace, route_name='Admin')

    config.add_route('Tasks', '/tasks')
    config.add_view(Workspace, route_name='Tasks')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

