from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from Model import Model
from Views import Login_View, Registration_View

def Login(request):
    parameters = Model.get_initial_data()
    return Login_View.pushTemplate('Login.txt', parameters)


def Registration(request):
    parameters = Model.process_business_logic()
    return Registration_View.pushTemplate('Registration.txt')

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
    config = Configurator()

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

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

