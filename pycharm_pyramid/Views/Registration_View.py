from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
from pyramid.response import Response

def pushTemplate(templatename):
    mylookup = TemplateLookup(directories=['Views/templates'])
    mytemplate = mylookup.get_template(templatename)
    return Response(mytemplate.render())