from pyramid.view import view_config

from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
import transaction
import re

from py2neo import neo4j, ogm
from database_config import *

from cuorewebpage.lib.session import *

from cuorewebpage.Model.Person import *

graph_db = neo4j.GraphDatabaseService(db_config['uri'])
store = ogm.Store(graph_db)

@view_config(route_name='Registration', renderer='cuorewebpage:templates/registration.mako')
def Registration(request):
    if isUserLoggedOn(request):
        ctx = {}
        ctx['section'] = 'Registration'
        departments = list()
        for i in getCompany().getAllDepartments():
            departments.append({"department":i.name, "titles":i.getAllTitles()})
        ctx['departments'] = departments
        if not getCurrentUser(request):
            ctx['view'] = 'create'
        elif getCurrentUser(request).isAdmin():
            if request.POST:
                ctx['view'] = 'admin'
                ctx['user'] = getUser(request.POST.getone('user'))
            else:
                ctx['view'] = 'edit'
                ctx['user'] = getCurrentUser(request)
        else:
            ctx['view'] = 'edit'
            ctx['user'] = getCurrentUser(request)
        return ctx
    else:
        return redirectUser(request)


@view_config(route_name='SubmitRegistration', renderer='cuorewebpage:templates/Registration.mako')
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
                  sender = "kirby@cuore.io",                    # change to admin email later
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
            phone=re.sub("[^0-9\-() ]", "", request.POST.getone('phone'))
            address = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('street_address'))
            city = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('city'))
            state = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('state'))
            zipcode = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('zip_code'))
            about = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('about'))
            req_title = request.POST.getone('req_title')
            uid = request.session["uid"]

            # create flags and set to not confirmed
            # create user node in database, put in temporary zone
            user = User(uid, first_name, last_name, email, 0, phone, address, city, state, zipcode, about, req_title)
            store.save_unique(IND_USER, "uid", user.uid, user)
            unconfirmedNode=graph_db.get_or_create_indexed_node("Unconfirmed", "name", "unconfirmed", {"name":"unconfirmed"})
            userNode=graph_db.get_indexed_node(IND_USER, "uid", user.uid)
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
            # reg-ex, remove non-digit characters
            email=re.sub("[^A-Za-z0-9.@!#$%&'*+\-/=?^_`{|}~]", "", request.POST.getone('email'))
            phone=re.sub("[^0-9\-() ]", "", request.POST.getone('phone'))
            address = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('street_address'))
            city = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('city'))
            state = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('state'))
            zipcode = re.sub("[^A-Za-z0-9,.\-() ]", "", request.POST.getone('zip_code'))
            about = re.sub("[^A-Za-z0-9,.!?\-() ]", "", request.POST.getone('about'))
            photo = request.POST.getone('profile_image')
            # update info in database
            getCurrentUser(request).getNode().update_properties({"email":email, "phone":phone, "address":address, "city":city, "state":state, "zipcode":zipcode, "photo":photo, "about":about})
    return {}

@view_config(route_name="ConfirmRegistration", renderer="cuorewebpage:templates/Registration.mako")
def ConfirmRegistration(request):
    #email=request.GET.getone('email')
    userNode = graph_db.get_indexed_node(IND_USER, "uid", uid)
    # move from temp area of database to permanent area of database
    confirmed=userNode.get_properties()["confirmed"]
    if(confirmed!=1 and confirmed!=3):
        confirmed += 1
    userNode.update_properties({"confirmed":confirmed})
    return {}