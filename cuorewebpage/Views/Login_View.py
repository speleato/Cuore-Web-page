from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
from pyramid.response import Response
from pyramid.view import view_config
from ..Model import Model

@view_config(route_name='Login', renderer='cuorewebpage:templates/login.mako')
def Login(request):
    parameters = Model.get_initial_data()
    #return Login_View.pushTemplate('Login.txt', parameters)
    return {'name': 'John', 'surname': 'Doe'}

def pushTemplate(templatename, args):
    mylookup = TemplateLookup(directories=['Views/templates'])
    mytemplate = mylookup.get_template(templatename)
    buf = StringIO()
    ctx = Context(buf, name = args['name'], surname = args['surname'])
    #ctx = Context(buf, args[0][0] = args[0][1].text, args[0][0].text = args[0][1].text)
    mytemplate.render_context(ctx)
    return Response(buf.getvalue())