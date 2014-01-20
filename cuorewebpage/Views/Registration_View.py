from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction
import re

from py2neo import neo4j, ogm
from database_config import *

import os

from cuorewebpage.lib.session import *

from cuorewebpage.Model.Person import getCompany, getCurrentUser, getUser
from cuorewebpage.Model.User import User
from cuorewebpage.Model.Company import *
from cuorewebpage.Model.Department import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

ADMIN_EMAIL = "slhsith@gmail.com"
REGISTRATION_EMAIL_SERVER = "slhsith@gmail.com"
REGISTRATION_EMAIL_RECIPIENTS = "sandymeep@gmail.com"

@view_config(route_name='Registration', renderer='cuorewebpage:templates/registration.mako')
def Registration(request):
    '''if getCurrentUser(request):
        print "==========================================================================="
        print request.session['uid']
        print getCurrentUser(request)
        #    print getCurrentUser(request)['last_name']
        print "==========================================================================="
    '''
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Registration'
        departments = list()
        for i in getAllDepartments():#getCompany().getAllDepartments():
            departments.append({"department":i.name, "titles":i.getAllTitles()})
        ctx['departments'] = departments
        ctx['user'] = getCurrentUser(request)
        if not getCurrentUser(request):
            print "------------------> create"
            ctx['view'] = 'create'
        elif getCurrentUser(request).isAdmin():
            if request.POST:
                print "------------------> admin"
                ctx['view'] = 'admin'
                ctx['user'] = getUser(request.POST.getone('user'))
            else:
                print "------------------> admin_edit"
                ctx['view'] = 'edit'
                ctx['user'] = getCurrentUser(request)
        else:
            print "------------------> user_edit"
            ctx['view'] = 'edit'
            ctx['user'] = getCurrentUser(request)
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name='Registration_Action', match_param="action=submit", renderer='cuorewebpage:templates/Registration.mako')
def SubmitRegistration(request):
    #parameters = Model.process_business_logic()
    if not isUserLoggedOn(request):
        return redirectUser(request)
    if request.POST:
        if request.POST.getone('task') == "admin":
            title=re.sub("[^A-Za-z0-9,.\-()] ", "", request.POST.getone('title'))
            email=re.sub("[^A-Za-z0-9.@!#$%&'*+\-/=?^_`{|}~]", "", request.POST.getone('email'))
            department=re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('department'))
            uid=request.POST.getone('uid')

            # add updated info to database
            userNode = graph_db.get_indexed_node(IND_USER, "uid", uid)
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
                  sender = ADMIN_EMAIL,                    # change to admin email later
                  recipients = [email],
                  body = "You have been added to the Cuore intranet as a " + title + " in the "
                       + department + " department. Click on this link to confirm your"
                       + " registration: " + request.url + "/confirm")
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "create":
            first_name=re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('first_name'))
            last_name=re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('last_name'))
            name=first_name + " " + last_name
            email=re.sub("[^A-Za-z0-9.@!#$%&'*+\-/=?^_`{|}~]", "", request.POST.getone('email'))
            phone=re.sub("[^0-9\-()+ ]", "", request.POST.getone('phone'))
            address = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('street_address'))
            city = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('city'))
            state = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('state'))
            zipcode = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('zip_code'))
            about = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('about'))
            req_title = request.POST.getone('req_title')
            uid = request.session["uid"]

            ext = os.path.splitext(request.POST.getone('profile_image').filename)[-1].lower()
            photo = "cuorewebpage/Profile_Pictures/" + getCurrentUser(request).uid + "/profile_picture" + ext


            dir = os.path.dirname(photo)
            try:
                os.stat(dir)
            except:
                os.mkdir(dir)
            f = open(photo, 'w')
            f.write(request.POST.getone('profile_image').value)
            f.close()

            print request.POST

            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            user = User(uid=uid, first_name=first_name, last_name=last_name, email=email, confirmed=0,
                        phone=phone, address=address, city=city, state=state, zipcode=zipcode, about=about, req_title=req_title)
#            store.save_unique(IND_USER, "uid", user.uid, user)
            unconfirmedNode=graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed", {"name":"unconfirmed"})
#            userNode=graph_db.get_indexed_node(IND_USER, "uid", user.uid)
            graph_db.create((user.getNode(), REL_UNCONFIRMED, unconfirmedNode))

            # after registration, send email to Leo
            mailer=get_mailer(request)
            message = Message(subject="Registration by " + name,
                              sender=REGISTRATION_EMAIL_SERVER,      # change to cuore mail server later
                              recipients=[REGISTRATION_EMAIL_RECIPIENTS],  # change to leo when rolled out
                              body=name + " has registered for the Cuore Intranet with the email "
                                     + email + ". Click here to confirm " + name
                                     + "'s registration: " + "link_to_admin_panel")
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "edit":
            # reg-ex, remove non-digit characters
            email=re.sub("[^A-Za-z0-9.@!#$%&'*+\-/=?^_`{|}~]", "", request.POST.getone('email'))
            phone=re.sub("[^0-9\-()+ ]", "", request.POST.getone('phone'))
            address = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('street_address'))
            city = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('city'))
            state = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('state'))
            zipcode = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('zip_code'))
            about = re.sub("[^A-Za-z0-9,.!?\-() ]", "", request.POST.getone('about'))

            ext = os.path.splitext(request.POST.getone('profile_image').filename)[-1].lower()
            photo = "cuorewebpage/Profile_Pictures/" + getCurrentUser(request).uid + "/profile_picture" + ext

            dir = os.path.dirname(photo)
            try:
                os.stat(dir)
            except:
                os.mkdir(dir)
            f = open(photo, 'w')
            f.write(request.POST.getone('profile_image').value)
            f.close()

            getCurrentUser(request).getNode().update_properties({"email":email, "phone":phone, "address":address, "city":city, "state":state, "zipcode":zipcode, "photo":photo, "about":about})
    return {}

@view_config(route_name="Registration_Action", match_param="action=confirm", renderer="cuorewebpage:templates/Registration.mako")
def ConfirmRegistration(request):
    #email=request.GET.getone('email')
    userNode = graph_db.get_indexed_node(IND_USER, "uid", request.session['uid'])
    # move from temp area of database to permanent area of database
    confirmed=userNode.get_properties()["confirmed"]
    if(confirmed!=1 and confirmed!=3):
        confirmed += 1
    userNode.update_properties({"confirmed":confirmed})
    return {}