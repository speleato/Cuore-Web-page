from pyramid.view import view_config

from cuorewebpage.Model.User import getCurrentUser
from cuorewebpage.lib.session import *


@view_config(route_name='CMS', renderer='cuorewebpage:templates/cms.mako')
def CMS(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        else:
            ctx = {}
            ctx['user'] = getCurrentUser(request)
            ctx['section'] = "CMS"
            return ctx
    else:
        return redirectUser(request)


