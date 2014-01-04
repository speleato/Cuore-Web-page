from pyramid.view import view_config
from pyramid.response import Response

@view_config(route_name='Dashboard', renderer='cuorewebpage:templates/dashboard.mako')
def dashboard(request):
    session = request.session

    return {}


