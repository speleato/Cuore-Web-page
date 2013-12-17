from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from Model import Model
from Views import Login_View, Registration_View
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

def Login(request):
    parameters = Model.get_initial_data()
    return Login_View.pushTemplate('Login.txt', parameters)


def Registration(request):
    parameters = Model.process_business_logic()
    print "bingo"
    if request.POST:
        print "submitted"
        if request.POST.getone('task') == "admin":
            title=request.POST.getone('title')
            email=request.POST.getone('email')
            department=request.POST.getone('department')

            print "admin path"
            # add updated info to database
            # after confirmed by Leo, send email to user
            mailer = get_mailer(request)
            message = Message(subject="Confirm your Cuore Intranet Registration",
                  sender = "kirby@cuore.io",                    # change to admin email later
                  recipients = [email],
                  body = "You have been added to the Cuore intranet as a " + title + " in the "
                       + department + " department. Click on this link to confirm your"
                       + "registration: " + "user_link")
            mailer.send(message)
        elif request.POST.getone('task') == "create":
            name=request.POST.getone('firstName') + " " + request.POST.getone('lastName')
            email=request.POST.getone('email')

            print "created"
            # create user node in database, put in temporary zone
            # after registration, send email to Leo
            mailer=get_mailer(request)
            message = Message(subject="Registration by " + name,
                              sender="kirby@cuore.io",      # change to cuore mail server later
                              recipients=["kirby@cuore.io"],  # change to leo when rolled out
                              body=name + " has registered for the Cuore Intranet with the email "
                                     + email + ". Click here to confirm " + name
                                     + "'s registration: " + "link_to_admin_panel")
            mailer.send(message)
        elif request.POST.getone('task')=="edit":
            # update info in database
            print "updated"
    return Registration_View.pushTemplate('Registration.mako')

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

def main(global_config, **settings):
    config = Configurator(settings=settings)

    #ROUTES

    #tree = ET.parse('Routing/routes.xml')
    #root = tree.getroot()
    #for child in root.findall('route'):
    #    config.add_route(child.find('name').text, child.find('path').text)
    #    config.add_view(child.find('module'), route_name=child.find('name').text)
    config.add_route('Login', '/')
    config.add_view(Login , route_name='Login')

    config.add_route('Registration', '/registration')
    config.add_view(Registration, route_name='Registration')

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

    #needed for pyramid mailer
    config.include('pyramid_mailer')

    # to scan for config via decorators
    config.scan()

    return config.make_wsgi_app()
