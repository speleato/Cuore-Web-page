from pyramid.view import view_config
from pyramid.httpexceptions import HTTPForbidden, HTTPFound

from cuorewebpage.Model.User import getCurrentUser
from cuorewebpage.lib.session import *


@view_config(route_name='IdeaCenter', renderer='cuorewebpage:templates/ideacenter.mako')
def IdeaCenter(request):
    if isUserLoggedOn(request):
        if getCurrentUser(request) is None:
            return redirectToRegistration(request)
        else:
            ctx = {}
            ctx['user'] = getCurrentUser(request)
            ctx['section'] = "Idea Center"
            return ctx
    else:
        return redirectUser(request)


