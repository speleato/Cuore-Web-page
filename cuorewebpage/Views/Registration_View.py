from pyramid.response import Response
from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction

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
            # after confirmed by Leo, send email to user
            mailer = get_mailer(request)
            message = Message(subject="Confirm your Cuore Intranet Registration",
                  sender = "kirby@cuore.io",                    # change to admin email later
                  recipients = [email],
                  body = "You have been added to the Cuore intranet as a " + title + " in the "
                       + department + " department. Click on this link to confirm your"
                       + " registration: " + request.url + "/confirm?confirm=" + "confirmationNumber_from_db")
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "create":
            firstName=request.POST.getone('firstName')
            lastName=request.POST.getone('lastName')
            name=firstName + " " + lastName
            email=request.POST.getone('email')

            print "created"
            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            # generates a unique user ID for confirmation
            import uuid
            confirmationNumber=uuid.uuid4()
            print confirmationNumber
            # store confirmationNumber in db
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
            # update info in database
            print "updated"
    return {}

@view_config(route_name="ConfirmRegistration", renderer="cuorewebpage:templates/Registration.mako")
def ConfirmRegistration(request):
    #confirmationNumber=request.GET.getone('confirm')
    #check confirmationNumber against user's confirmationNumber
    #move from temp area of database to permanent area of database
    #remove flags
    print "confirmed"
    return{}

@view_config(route_name="Directory", renderer="cuorewebpage:templates/Directory.mako")
def Directory(request):
    return {}

@view_config(route_name="Profile", renderer="cuorewebpage:templates/Profile.mako")
def Profile(request):
    return {'name': 'request.GET.getone("name")'}