from pyramid.response import Response
from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

from py2neo import neo4j, ogm
from database_config import db_config

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

class Person(object):
    def __init__(self, first_name=None, last_name=None, email=None, title=None, confirmed=0, confirmationNumber=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.confirmed = confirmed
        self.confirmationNumber = confirmationNumber
        '''
        self.department = department
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        '''
    def __str__(self):
        return (self.first_name)

    def submit_settings(self):
        store.save_unique("People", "email", self.email, self)
        return self

@view_config(route_name='Registration', renderer='cuorewebpage:templates/Registration.mako')
def Registration(request):
    #parameters = Model.process_business_logic()
    print "bingo"
    if request.POST:
        print "submitted"
        if request.POST.getone('task') == "admin":
            title=request.POST.getone('title')
            email=request.POST.getone('email')
            department=request.POST.getone('department')

            print "admin path"
            # add updated info to database
            # Note: Either another unique identifier needs to be used or the admin panel shouldn't be allowed to change email
            personNode = graph_db.get_indexed_node("People", "email", email)
            # if leo confirmed, update confirmation flags
            confirmed=personNode.get_properties()["confirmed"]
            if(confirmed<2):
                confirmed += 2
            personNode.update_properties({"title":title, "email":email, "confirmed":confirmed})
            titleNode = graph_db.get_or_create_indexed_node("Title", "name", title, {"name":title})
            departmentNode = graph_db.get_indexed_node("Department", "name", department)
            graph_db.create((titleNode, "IS A", personNode), (departmentNode, "IN", titleNode))
            # after confirmed by Leo, send email to user
            confirmationNumber=personNode.get_properties()["confirmationNumber"]
            mailer = get_mailer(request)
            message = Message(subject="Confirm your Cuore Intranet Registration",
                  sender = "kirby@cuore.io",                    # change to admin email later
                  recipients = [email],
                  body = "You have been added to the Cuore intranet as a " + title + " in the "
                       + department + " department. Click on this link to confirm your"
                       + " registration: " + request.url + "/confirm?email="+email+"&confirm=" + confirmationNumber)
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "create":
            firstName=request.POST.getone('firstName')
            lastName=request.POST.getone('lastName')
            name=firstName + " " + lastName
            email=request.POST.getone('email')

            print "created"
            # generates a unique user ID for confirmation
            import uuid
            confirmationNumber=str(uuid.uuid4())
            print confirmationNumber
            # store confirmationNumber in db
            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            person = Person(firstName, lastName, email, None, 0, confirmationNumber)
            store.save_unique("People", "email", person.email, person)
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
            about = request.POST.getone('about')
            # update info in database, need to pass in email, currently not implemented
            # personNode = graph_db.get_indexed_node("People", "email", email)
            # personNode.update_properties(properties='"phone":phone, "address":address, "about":about')
            print "updated"
    return {}

@view_config(route_name="ConfirmRegistration", renderer="cuorewebpage:templates/Registration.mako")
def ConfirmRegistration(request):
    email=request.GET.getone('email')
    personNode = graph_db.get_indexed_node("People", "email", email)
    confirmationNumber=request.GET.getone('confirm')
    # check confirmationNumber against user's confirmationNumber
    if confirmationNumber == personNode.get_properties()["confirmationNumber"]:
        # move from temp area of database to permanent area of database
        confirmed=personNode.get_properties()["confirmed"]
        if(confirmed!=1 and confirmed!=3):
            confirmed += 1
        personNode.update_properties({"confirmed":confirmed})
        print "confirmed"
    return{}

@view_config(route_name="Directory", renderer="cuorewebpage:templates/Directory.mako")
def Directory(request):
    return {}

@view_config(route_name="Profile", renderer="cuorewebpage:templates/Profile.mako")
def Profile(request):
    return {'name': 'request.GET.getone("name")'}