from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
from pyramid.response import Response

def pushTemplate(templatename, args):
    mylookup = TemplateLookup(directories=['Views/templates'])
    mytemplate = mylookup.get_template(templatename)
    buf = StringIO()
    ctx = Context(buf, name = args['name'], surname = args['surname'])
    #ctx = Context(buf, args[0][0] = args[0][1].text, args[0][0].text = args[0][1].text)
    mytemplate.render_context(ctx)
    return Response(buf.getvalue())