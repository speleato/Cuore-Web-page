from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction
import re

from py2neo import neo4j, ogm
from database_config import *

import os

from cuorewebpage.lib.session import *

from cuorewebpage.Model.User import *
from cuorewebpage.Model.Company import *
from cuorewebpage.Model.Department import *
from cuorewebpage.Model.Title import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

ADMIN_EMAIL = "slhsith@gmail.com"
REGISTRATION_EMAIL_SERVER = "slhsith@gmail.com"
REGISTRATION_EMAIL_RECIPIENTS = "sandymeep@gmail.com"

@view_config(route_name='Registration', renderer='cuorewebpage:templates/registration.mako')
def Registration(request):
    if not isUserLoggedOn(request):
        return redirectUser(request)
    ctx = {}
    ctx['section'] = 'Registration'
    departments = list()
    for i in getCompany().getDepartments():
        departments.append({"department":i["name"], "titles":Department(i).getTitles()})
    ctx['departments'] = departments
    ctx['user'] = getCurrentUser(request)
    if not getCurrentUser(request):
        print "------------------> create"
        ctx['view'] = 'create'
    else:
        return HTTPFound(location=request.route_url('Registration_Action', action='edit'))
    return ctx
"""
    elif getCurrentUser(request).isAdmin():
        if request.POST:
#            print "------------------> admin"
            ctx['view'] = 'admin'
            ctx['user'] = getUser(request.POST.getone('user'))
        else:
#            print "------------------> admin_edit"
            ctx['view'] = 'edit'
            ctx['user'] = getCurrentUser(request)
    else:
#        print "------------------> user_edit"
        ctx['view'] = 'edit'
        ctx['user'] = getCurrentUser(request)
"""


@view_config(route_name='Registration_Action', match_param="action=edit", renderer='cuorewebpage:templates/registration_edit.mako')
def EditRegistration(request):
    print request.POST
    ctx = {}
    departments = list()
    for i in getCompany().getDepartments():
        departments.append({"department":i["name"], "titles":Department(i).getTitles()})
    ctx['departments'] = departments

    if not getCurrentUser(request):
        return redirectToRegistration(request)
    elif getCurrentUser(request).isAdmin():
        if request.POST:
            ctx['section'] = 'Admin Panel'
        #            print "------------------> admin"
            ctx['view'] = 'admin'
            ctx['user'] = getUser(request.POST.getone('user'))
        else:
        #            print "------------------> admin_edit"
            ctx['section'] = 'Admin Edit'
            ctx['view'] = 'edit'
            ctx['user'] = getCurrentUser(request)
    else:
    #        print "------------------> user_edit"
        ctx['section'] = 'Edit Settings'
        ctx['view'] = 'edit'
        ctx['user'] = getCurrentUser(request)
    return ctx


@view_config(route_name='Registration_Action', match_param="action=submit", renderer='cuorewebpage:templates/registration_confirmation.mako')
def SubmitRegistration(request):
    #parameters = Model.process_business_logic()
    if not isUserLoggedOn(request):
        return redirectUser(request)
    if request.POST:
        if request.POST.getone('task') == "admin":
            # note: titles is a list of department and title names in the format: ["department_name,title_name", ...]
            #       however the list will also contain some strings that represent a department/title combo that is not
            #       associated with user, these strings are "None" strings (quick fix, go back later w/ AJAX)
            titles=request.POST.getall('titles[]')
            equity_rate = request.POST.getone('equity_rate')
            uid=request.POST.getone('uid')

            # add updated info to database
            user = User(uid=uid)

            # notify user if equity rate is changed
            if (user.getEquityRate() != equity_rate) and (equity_rate != "None"):
                mailer = get_mailer(request)
                message = Message(subject="Your Equity Rate for Cuore has been changed",
                    sender = "info@cuore.io",                    # change to admin email later
                    recipients = [user.getEmail()],
                    body = "Your equity rate has been changed from " + str(user.getEquityRate()) + " to " + str(equity_rate))
                mailer.send(message)
                user.userInstance['equity_rate'] = equity_rate
                transaction.commit()

            split_titles = []

            for i in titles:
                if i != "None":
                    Department(name=i.split(",")[0]).addTitle(Title(name=i.split(",")[1]))
                    Title(name=i.split(",")[1]).addUser(user)
                    split_titles.append(i.split(",")[1])


            #temporary way of removing titles
            for i in user.getTitles():
                if Title(i).getName() not in split_titles:
                    user.removeTitle(Title(i))


            # after confirmed by Leo, send email to user
            # if leo confirmed, update confirmation flags
            if(user.getConfirmed()<2):
                for i in user.userInstance.match(REL_UNCONFIRMED):
                    i.delete()
                user.userInstance['confirmed'] += 2
                mailer = get_mailer(request)
                message = Message(subject="Confirm your Cuore Intranet Registration",
                    sender = "info@cuore.io",                    # change to admin email later
                    recipients = [User(uid=uid).getEmail()],
                    body = "You have been added to the Cuore intranet. Click on this link to confirm your registration: "
                         + request.url + "/confirm")
                mailer.send(message)
                transaction.commit()
        elif request.POST.getone('task') == "create":
            first_name=re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('first_name'))
            last_name=re.sub("[^A-Za-z0-9,.\-()]", "", request.POST.getone('last_name'))
            name=first_name + " " + last_name
            email=re.sub("[^A-Za-z0-9.@!#$%&'*+\-/=?^_`{|}~]", "", request.POST.getone('email'))
            phone=re.sub("[^0-9]", "", request.POST.getone('phone'))
            address = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('street_address'))
            city = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('city'))
            state = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('state'))
            zipcode = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('zip_code'))
            about = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('about'))
            req_title = request.POST.getone('req_title').split(",")[1]
            req_dept = request.POST.getone('req_title').split(",")[0]
            uid = request.session["uid"]
            # default profile picture
            photo="cuorewebpage:img/menu_icons/profile.png"
            if request.POST.getone('profile_image') != "":
                ext = os.path.splitext(request.POST.getone('profile_image').filename)[-1].lower()
                photo = "cuorewebpage/Profile_Pictures/" + uid + "/profile_picture" + ext

                dir = os.path.dirname(photo)
                try:
                    os.stat(dir)
                except:
                    dir2 = os.path.dirname(dir)
                    try:
                        os.stat(dir2)
                    except:
                        os.mkdir(dir2)
                    os.mkdir(dir)
                f = open(photo, 'w')
                f.write(request.POST.getone('profile_image').value)
                f.close()

            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            user = User(uid=uid, first_name=first_name, last_name=last_name, email=email, confirmed=0,
                        phone=phone, address=address, city=city, state=state, zipcode=zipcode, about=about, photo=photo, req_title=req_title, req_dept=req_dept)
#            store.save_unique(IND_USER, "uid", user.uid, user)
            unconfirmedNode=graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed", {"name":"unconfirmed"})
#            userNode=graph_db.get_indexed_node(IND_USER, "uid", user.uid)
            graph_db.create((user.getNode(), REL_UNCONFIRMED, unconfirmedNode))
            Calendar(Name=(user.getFullName() + "'s Calendar"), Owner=user.getNode())

            # after registration, send email to admins
            mailer=get_mailer(request)
            admin_emails = []
            for i in getAdmins():
                admin_emails.append(User(i).getEmail())

            message = Message(subject="Registration by " + name,
                              sender="info@cuore.io",      # change to cuore mail server later
                              recipients=admin_emails,  # change to leo when rolled out
                              body=name + " has registered for the Cuore Intranet. Click here to go to the admin panel and confirm " + name
                                     + "'s registration: " + request.route_url('AdminPanel'))
            mailer.send(message)
            transaction.commit()
        elif request.POST.getone('task') == "edit":
            # reg-ex, remove non-digit characters
            email=re.sub("[^A-Za-z0-9.@!#$%&'*+\-/=?^_`{|}~]", "", request.POST.getone('email'))
            phone=re.sub("[^0-9]", "", request.POST.getone('phone'))
            address = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('street_address'))
            city = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('city'))
            state = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('state'))
            zipcode = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('zip_code'))
            about = re.sub("[^A-Za-z0-9,.!?\-() ]", "", request.POST.getone('about'))
            photo = getCurrentUser(request).getPhoto()
            if request.POST.getone('profile_image') != "":
                ext = os.path.splitext(request.POST.getone('profile_image').filename)[-1].lower()
                photo_file = getCurrentUser(request).userInstance['uid'] + "/profile_picture" + ext
                photo_full_path = "cuorewebpage/img/Profile_Pictures/" + photo_file
                photo_asset_spec = "cuorewebpage:img/Profile_Pictures/" + photo_file
                photo = photo_asset_spec

                dir = os.path.dirname(photo_full_path)
                try:
                    os.stat(dir)
                except:
                    dir2 = os.path.dirname(dir)
                    try:
                        os.stat(dir2)
                    except:
                        os.mkdir(dir2)
                    os.mkdir(dir)
                f = open(photo_full_path, 'w')
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