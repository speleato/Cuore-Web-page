from pyramid.view import view_config
from pyramid.httpexceptions import HTTPForbidden, HTTPFound

from urllib import *
import json

from cuorewebpage.lib.oneid import OneID

try:
    from settings_local import *
except:
    pass

def init_oneid():
    oneid_our_key = urlopen("https://keychain.oneid.com/register")
    oneid_our_key = json.loads(oneid_our_key.read())
    oneid_connector = OneID(oneid_our_key['API_ID'], oneid_our_key['API_KEY'])
    return oneid_connector

@view_config(route_name='Login', renderer='cuorewebpage:templates/login.mako')
def Login(request):
    ctx = {}
    oneid_connector = init_oneid()
    ctx['oneid_scripts'] = oneid_connector.script_header
    return ctx

@view_config(route_name='Signin', renderer='cuorewebpage:templates/signin.mako')
def Signin():
    ctx = {}
    oneid_connector = init_oneid()
    ctx['oneid_scripts'] = oneid_connector.script_header
    return ctx

@view_config(route_name='Auth', renderer='cuorewebpage:templates/authenticate.mako', request_method='POST')
def oneid_login(request):
    print request
    ctx = {}
    oneid_data = request.POST.get('json_data', {})
    oneid_connector = init_oneid()
    valid = oneid_connector.validate(oneid_data)

    if oneid_connector.success(valid):
        ctx['uid'] = valid['uid']
        #session['two_factor_token'] = valid['two_factor_token']
        ctx['logged_in'] = True
        url = request.route_url('Dashboard')
        return ctx
    return HTTPForbidden

