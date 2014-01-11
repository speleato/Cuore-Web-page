from pyramid.view import view_config
from pyramid.httpexceptions import HTTPForbidden, HTTPFound


from cuorewebpage.lib.oneid import OneID, init_oneid
from cuorewebpage.lib.sesssio import *

try:
    from settings_local import *
except:
    pass


@view_config(route_name='Index', renderer='cuorewebpage:templates/index.mako')
def Index(request):
    return {}

@view_config(route_name='Login', renderer='cuorewebpage:templates/login.mako')
def Login(request):
    ctx = {}
    oneid_connector = init_oneid()
    ctx['oneid_scripts'] = oneid_connector.script_header
    ctx['section'] = 'Login'
    return ctx

@view_config(route_name='Auth', renderer='cuorewebpage:templates/authenticate.mako', request_method='POST')
def oneid_login(request):
    authenticate(request)

