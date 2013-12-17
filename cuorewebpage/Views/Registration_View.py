from pyramid.response import Response
from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message

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
                       + "registration: " + "user_link")
            mailer.send(message)

        elif request.POST.getone('task') == "create":
            name=request.POST.getone('firstName') + " " + request.POST.getone('lastName')
            email=request.POST.getone('email')

            print "created"
            # create user node in database, put in temporary zone
            # after registration, send email to Leo
            mailer=get_mailer(request)
            message = Message(subject="Registration by " + name,
                              sender="kirby@cuore.io",      # change to cuore mail server later
                              recipients=["kirby@cuore.io"],  # change to leo when rolled out
                              body=name + " has registered for the Cuore Intranet with the email "
                                     + email + ". Click here to confirm " + name
                                     + "'s registration: " + "link_to_admin_panel")
            mailer.send(message)
        elif request.POST.getone('task')=="edit":
            # update info in database
            print "updated"
    return {}


