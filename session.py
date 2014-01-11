from pyramid.httpexceptions import HTTPFound
from StringIO import StringIO
import json
from oneId import OneID
import simplejson
from urllib2 import urlopen


## This will verify if the user has logged on OneID AND in our system
def isUserLoggedOn(request):
    print request
    print request.session
    print request.session['uid']
    if request.session != {} and request.session["uid"] != "":
        return True
    else:
        return False

## This will redirect the user to the Login page.
def redirectUser(request):
        return HTTPFound(location=request.route_url('Login'))



# this will get the POST aswer when the oneID button is pressed and if the user is valid
# will create a new value in the session.
def authenticate(request):
        if request.text != "":
            #get body of keys sent by OneID signing process
            var = StringIO()
            var.write(request.text)
            body_of_the_request = simplejson.loads(var.getvalue())

            #Get API_ID and API_KEY from OneID
            jsonurl = urlopen("https://keychain.oneid.com/register")
            parsed_JSON_keys = json.loads(jsonurl.read())

            #Validate the obtained body with OneID service using the provided keys.
            body = body_of_the_request
            oneid_data = body
            oneid_connector = OneID(parsed_JSON_keys['API_ID'], parsed_JSON_keys['API_KEY'])
            valid = oneid_connector.validate(oneid_data)
            if oneid_connector.success(valid):
                #initiate session
                print "session will be initiated with UserId: " + body_of_the_request["uid"]
                request.session["uid"] = body_of_the_request["uid"]
                return True
            else:
                return False
        else:
            return False
