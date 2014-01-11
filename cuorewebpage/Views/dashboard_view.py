from pyramid.view import view_config
from pyramid.response import Response
from cuorewebpage.lib.session import *

@view_config(route_name='Dashboard', renderer='cuorewebpage:templates/dashboard.mako')
def dashboard(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Dashboard'
        return ctx
    else:
        return redirectUser(request)


