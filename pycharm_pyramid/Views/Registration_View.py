from mako.template import Template
from mako.runtime import Context
from StringIO import StringIO
from mako.lookup import TemplateLookup
from pyramid.response import Response
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

def pushTemplate(templatename):
    mylookup = TemplateLookup(directories=['Views/templates'])
    mytemplate = mylookup.get_template(templatename)
    return Response(mytemplate.render())


#after registration, send email to leo
#mailer=get_mailer(request)
#message = Message(subject="Registration by "+name,
#                  sender=cuore_email,
#                  recipients=["kirby@cuore.io"], #change to leo when rolled out
#                  body=name+" has registered for the Cuore Intranet with the email "+email+". Click here to confirm "
#                       +name+"'s registration: "+link_to_admin_panel)
#mailer.send(message)