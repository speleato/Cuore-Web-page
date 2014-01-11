from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

from py2neo import neo4j, ogm
from database_config import db_config

from cuorewebpage.Model.Person import User

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

"""
# /registration/{action}
/registration/create    new registration form, basic information
/registration/admin     parrot back registration info with additional fields for Admin to set and approve
/registration/confirm   user confirms after Admin approval

# /settings/{action}
/settings/edit          show settings for changes
/settings/admin         show settings including special fields for Admin edit
"""

@view_config(route_name='Registration', match_param='action=confirm', renderer='cuorewebpage:templates/settings.mako')
def registration_confirm(request):
    title=request.POST.getone('title')
    email=request.POST.getone('email')
    department=request.POST.getone('department')

    # add updated info to database
    # Note: Either another unique identifier needs to be used or the admin panel shouldn't be allowed to change email
    userNode = graph_db.get_indexed_node("Users", "email", email)
    # if leo confirmed, update confirmation flags
    confirmed=userNode.get_properties()["confirmed"]
    if(confirmed<2):
        confirmed += 2
        userNode.update_properties({"title":title, "email":email, "confirmed":confirmed})
        titleNode = graph_db.get_or_create_indexed_node("Title", "name", title, {"name":title})
        departmentNode = graph_db.get_indexed_node("Department", "name", department)
        graph_db.create((titleNode, "IS A", userNode), (departmentNode, "IN", titleNode))
        # after confirmed by Leo, send email to user
        confirmationNumber=userNode.get_properties()["confirmationNumber"]
        mailer = get_mailer(request)
        message = Message(subject="Confirm your Cuore Intranet Registration",
        sender = "kirby@cuore.io",                    # change to admin email later
        recipients = [email],
        body = "You have been added to the Cuore intranet as a " + title + " in the "
               + department + " department. Click on this link to confirm your"
               + " registration: " + request.url + "/confirm?email="+email+"&confirm=" + confirmationNumber)
        mailer.send(message)
        transaction.commit()
    return {}

@view_config(route_name='Registration', match_param='action=admin', renderer='cuorewebpage:templates/settings.mako')
def registration_admin(request):
    first_name=request.POST.getone('first_name')
    last_name=request.POST.getone('last_name')
    name=first_name + " " + last_name
    email=request.POST.getone('email')

    # generates a unique user ID for confirmation
    import uuid
    confirmationNumber=str(uuid.uuid4())
    # store confirmationNumber in db
    # create flags and set to not confirmed
    # create user node in database, put in temporary zone
    user = User(first_name, last_name, email, None, 0, confirmationNumber)
    store.save_unique("Users", "email", user.email, user)
    # after registration, send email to Leo
    mailer=get_mailer(request)
    message = Message(subject="Registration by " + name,
                      sender="kjlinvill@gmail.com",      # change to cuore mail server later
                      recipients=["kirby@cuore.io"],  # change to leo when rolled out
                      body=name + " has registered for the Cuore Intranet with the email "
                             + email + ". Click here to confirm " + name
                             + "'s registration: " + "link_to_admin_panel")
    mailer.send(message)
    transaction.commit()

    return {}


@view_config(route_name='Registration', match_param='action=create', renderer='cuorewebpage:templates/settings.mako')
@view_config(route_name='Settings', match_param='action=edit', renderer='cuorewebpage:templates/settings.mako')
def settings_edit(request):
    phone = request.POST.getone('phone')
    address = request.POST.getone('address')
    city = request.POST.getone('city')
    state = request.POST.getone('state')
    zipcode = request.POST.getone('zipcode')
    about = request.POST.getone('about')
    # update info in database, need to pass in email, currently not implemented
    # userNode = graph_db.get_indexed_node("Users", "email", email)
    # userNode.update_properties(properties='"phone":phone, "address":address, "city":city, "state":state, "zipcode":zipcode "about":about')
    print "updated"
    return {}

@view_config(route_name="Settings", match_param='action=admin', renderer="cuorewebpage:templates/settings_admin.mako")
def settings_admin(request):
    email=request.GET.getone('email')
    userNode = graph_db.get_indexed_node("Users", "email", email)
    confirmationNumber=request.GET.getone('confirm')
    # check confirmationNumber against user's confirmationNumber
    if confirmationNumber == userNode.get_properties()["confirmationNumber"]:
        # move from temp area of database to permanent area of database
        confirmed=userNode.get_properties()["confirmed"]
        if(confirmed!=1 and confirmed!=3):
            confirmed += 1
        userNode.update_properties({"confirmed":confirmed})
        print "confirmed"
    return{}

