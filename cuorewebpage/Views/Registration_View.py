from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

from py2neo import neo4j, ogm
from database_config import *

from cuorewebpage.Model.Person import User

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name='Registration', renderer='cuorewebpage:templates/Registration.mako')
def Registration(request):
    return {}

@view_config(route_name='SubmitRegistration', renderer='cuorewebpage:templates/Registration.mako')
def SubmitRegistration(request):
    #parameters = Model.process_business_logic()
    if request.POST:
        if request.POST.getone('task') == "admin":
            title=request.POST.getone('title')
            email=request.POST.getone('email')
            department=request.POST.getone('department')

            # add updated info to database
            # Note: Either another unique identifier needs to be used or the admin panel shouldn't be allowed to change email
            userNode = graph_db.get_indexed_node(IND_USER, "email", email)
            # if leo confirmed, update confirmation flags
            confirmed=userNode.get_properties()["confirmed"]
            if(confirmed<2):
                confirmed += 2
            userNode.update_properties({"title":title, "email":email, "confirmed":confirmed})
            titleNode = graph_db.get_or_create_indexed_node(IND_TITLE, "name", title, {"name":title})
            departmentNode = graph_db.get_indexed_node(IND_DEP, "name", department)
            graph_db.create((titleNode, "IS A", userNode), (departmentNode, "IN", titleNode))
            unconfirmedNode = graph_db.get_indexed_node("Unconfirmed", "name", "unconfirmed")
            graph_db.match(userNode, "IS", unconfirmedNode).delete()
            # after confirmed by Leo, send email to user
            confirmationNumber=userNode.get_properties()["confirmationNumber"]
            mailer = get_mailer(request)
            message = Message(subject="Confirm your Cuore Intranet Registration",
                  sender = "kirby@cuore.io",                    # change to admin email later
                  recipients = [email],
                  body = "You have been added to the Cuore intranet as a " + title + " in the "
                       + department + " department. Click on this link to confirm your"
                       + " registration: " + request.url + "/confirm")
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "create":
            firstName=request.POST.getone('firstName')
            lastName=request.POST.getone('lastName')
            name=firstName + " " + lastName
            email=request.POST.getone('email')

            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            user = User(firstName, lastName, email)
            store.save_unique(IND_USER, "email", user.email, user)
            unconfirmedNode=graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed", {"name":"unconfirmed"})
            userNode=graph_db.get_indexed_node(IND_USER, "email", user.email)
            graph_db.create((userNode, "IS", unconfirmedNode))

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
        elif request.POST.getone('task') == "edit":
            phone = request.POST.getone('phone')
            address = request.POST.getone('address')
            city = request.POST.getone('city')
            state = request.POST.getone('state')
            zipcode = request.POST.getone('zipcode')
            about = request.POST.getone('about')
            # update info in database, need to pass in email, currently not implemented
            # userNode = graph_db.get_indexed_node(IND_USER, "email", email)
            # userNode.update_properties(properties='"phone":phone, "address":address, "city":city, "state":state, "zipcode":zipcode "about":about')
    return {}

@view_config(route_name="ConfirmRegistration", renderer="cuorewebpage:templates/Registration.mako")
def ConfirmRegistration(request):
    #email=request.GET.getone('email')
    userNode = graph_db.get_indexed_node(IND_USER, "email", email)
    # move from temp area of database to permanent area of database
    confirmed=userNode.get_properties()["confirmed"]
    if(confirmed!=1 and confirmed!=3):
        confirmed += 1
    userNode.update_properties({"confirmed":confirmed})
    return {}