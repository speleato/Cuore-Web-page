from pyramid.httpexceptions import HTTPFound
from StringIO import StringIO
import json
from oneid import OneID
import simplejson
from urllib2 import urlopen


## This will verify if the user has logged on OneID AND in our system
def isUserLoggedOn(request):
    #if request.session != {}:
    #    if request.session["uid"] != "":
    #        return True
    #else:
    #    if authenticate(request):
    #        return True
    #    return False
    return True

## This will redirect the user to the Login page.
def redirectUser(request):
    return HTTPFound(location=request.route_url('Login'))

def redirectToRegistration(request):
    return HTTPFound(location=request.route_url('Registration'))



# this will get the POST aswer when the oneID button is pressed and if the user is valid
# will create a new value in the session.
def authenticate(request):
    if request.POST.get('json_data') is not None:
        #get body of keys sent by OneID signing process
        var = StringIO()
        var.write(request.POST.get('json_data', {}))
        body_of_the_request = simplejson.loads(var.getvalue())

        #Get API_ID and API_KEY from OneID
        jsonurl = urlopen("https://keychain.oneid.com/register")
        parsed_JSON_keys = json.loads(jsonurl.read())

        #Validate the obtained body with OneID service using the provided keys.
        body = body_of_the_request
        print body
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
