from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.request import Request

from urllib import *
import json

from Model import Model
#from oneid import OneID

def authenticate(request):
    jsonurl = urlopen("https://keychain.oneid.com/register")
    parsedResponse = json.loads(jsonurl.read())
    oneid_data = request.POST
    oneid_connector = OneID(parsedResponse['API_ID'], parsedResponse['API_KEY'])
    valid = oneid_connector.validate(oneid_data)
    if oneid_connector.success(valid):
        #Request.session['uid'] = valid["uid"]
        #Request.session['logged_in'] = True
        return True
    else:
        return False
    return {}



def main(global_config, **settings):
    config = Configurator(settings=settings)

    #ROUTES

    #tree = ET.parse('Routing/routes.xml')
    #root = tree.getroot()
    #for child in root.findall('route'):
    #    config.add_route(child.find('name').text, child.find('path').text)
    #    config.add_view(child.find('module'), route_name=child.find('name').text)
    config.add_route('Login', '/')
    config.add_route('Authenticate', '/authenticate')
    #config.add_route('Registration', '/registration/{action}')
    config.add_route('Registration', '/registration')
    config.add_route('Settings', '/settings/{action}')
    config.add_route('Dashboard', '/dashboard')
    config.add_route('SubmitRegistration', '/registration/submit')
    config.add_route('ConfirmRegistration', 'registration/confirm')
    config.add_route('Profile', '/profile')
    config.add_route('Directory', '/directory')
    config.add_route('Newsfeed', '/newsfeed')
    config.add_route('Blog', '/blog')
    config.add_route('Files', '/files')
    config.add_route('Workspace', '/workspace')
    config.add_route('Calendar', '/calendar')
    config.add_route('Tasks', '/tasks')
    config.add_route('CMS', '/cms')
    config.add_route('Store', '/store')
    config.add_route('IdeaCenter', '/ideacenter')
    config.add_route('Jobs', '/jobs')
    config.add_route('Support', '/support')
    config.add_route('Contact', '/contact')
    config.add_route('Logout', '/logout')
    config.add_route('AdminPanel', '/adminpanel')
    config.add_route('Test', '/test')

    config.add_static_view(name='img', path='cuorewebpage:img')
    config.add_static_view(name='js', path='cuorewebpage:js')
    config.add_static_view(name='css', path='cuorewebpage:css')
    #config.add_view(Workspace, route_name='Tasks')

    #needed for pyramid mailer
    config.include('pyramid_mailer')

    # to scan for config via decorators
    config.scan()

    return config.make_wsgi_app()
