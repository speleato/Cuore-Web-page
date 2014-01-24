from pyramid.view import view_config
from pyramid.response import Response
from cuorewebpage.lib.session import *
from cuorewebpage.Model.User import *

@view_config(route_name='Dashboard', renderer='cuorewebpage:templates/dashboard.mako')
def dashboard(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Dashboard'
        ctx['user'] = getCurrentUser(request)

        return ctx
    else:
        return redirectUser(request)



