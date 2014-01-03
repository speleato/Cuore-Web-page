from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from model import Model
from views import login_view, registration_view

from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='Login', renderer='cuorewebpage:templates/Login.mako')
def Login(request):
    parameters = model.get_initial_data()
    #return Login_View.pushTemplate('Login.txt', parameters)
    return {'name': 'John', 'surname': 'Doe'}

def main(global_config, **settings):
    config = Configurator(settings=settings)

    #ROUTES

    #tree = ET.parse('Routing/routes.xml')
    #root = tree.getroot()
    #for child in root.findall('route'):
    #    config.add_route(child.find('name').text, child.find('path').text)
    #    config.add_view(child.find('module'), route_name=child.find('name').text)
    config.add_route('Login', '/')
    config.add_route('Registration', '/registration')
    config.add_route('ConfirmRegistration', 'registration/confirm')
    config.add_route('Directory', '/directory')
    config.add_route('Profile', '/profile')
    config.add_route('Newsfeed', '/newsfeed')
    config.add_route('Dashboard', '/dashboard')
    config.add_route('Blog', '/blog')
    config.add_route('Files', '/files')
    config.add_route('Calendar', '/calendar')
    config.add_route('Workspace', '/workspace')
    config.add_route('Admin', '/DoNotPutAdmin')
    config.add_route('Tasks', '/tasks')
    config.add_static_view(name='img', path='cuorewebpage:img')
    config.add_static_view(name='js', path='cuorewebpage:js')
    config.add_static_view(name='css', path='cuorewebpage:css')
    #config.add_view(Workspace, route_name='Tasks')

    #needed for pyramid mailer
    config.include('pyramid_mailer')

    # to scan for config via decorators
    config.scan()

    return config.make_wsgi_app()
