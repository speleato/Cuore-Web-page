from wsgiref.simple_server import make_server
from pyramid.config import Configurator
#from Model import Model
#from Views import Login_View, Registration_View

from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='Login', renderer='cuorewebpage:templates/Login.mako')
def Login(request):
    parameters = Model.get_initial_data()
    #return Login_View.pushTemplate('Login.txt', parameters)
    return {'name': 'John', 'surname': 'Doe'}

'''

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
'''

def main(global_config, **settings):
    config = Configurator(settings=settings)

    #ROUTES

    #tree = ET.parse('Routing/routes.xml')
    #root = tree.getroot()
    #for child in root.findall('route'):
    #    config.add_route(child.find('name').text, child.find('path').text)
    #    config.add_view(child.find('module'), route_name=child.find('name').text)
    config.add_route('Login', '/')
    #config.add_view(Login , route_name='Login')

    config.add_route('Registration', '/registration')
    #config.add_view(Registration, route_name='Registration')

    config.add_route('MainPage', '/main')
    #config.add_view(MainPage, route_name='MainPage')

    config.add_route('Blog', '/blog')
    #config.add_view(Blog, route_name='Blog')

    config.add_route('Files', '/files')
    #config.add_view(Files, route_name='Files')

    config.add_route('Calendar', '/calendar')
    #config.add_view(Calendar, route_name='Calendar')

    config.add_route('Workspace', '/workspace')
    #config.add_view(Workspace, route_name='Workspace')

    config.add_route('Admin', '/DoNotPutAdmin')
    #config.add_view(Workspace, route_name='Admin')

    config.add_route('Tasks', '/tasks')
    #config.add_view(Workspace, route_name='Tasks')

    #needed for pyramid mailer
    config.include('pyramid_mailer')

    # to scan for config via decorators
    config.scan()

    return config.make_wsgi_app()
