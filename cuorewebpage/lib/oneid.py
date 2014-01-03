'''
#!/usr/bin/python

# OneID Python API Library
# Copyright 2013 by OneID
import json
import requests


class OneID:
    def __init__(self, api_id = None, api_key=None, server_flag=""):
        """server_flag
        :param api_id: Your OneID API ID credentials (from https://keychain.oneid.com/register)
        :param api_key: Your OneID API Key credentials (from https://keychain.oneid.com/register)
        :param server_flag: If you want to connect to a different API  should be (for example) "-test" when using a non-production server
        """
        self.repo_server = "https://account%s.oneid.com/repo/" % server_flag
        self.helper_server = "https://keychain%s.oneid.com" % server_flag
        self.script_header = '<script src="https://api%s.oneid.com/js/oneid.js" type="text/javascript"></script>' % server_flag
        self.server_flag = server_flag
        self.creds_file = "api_key" + server_flag + ".json"

        # Set the API credentials
        self.set_credentials(api_id, api_key)


    def _call_keychain(self, method, data={}):
        """Call the OneID Keychain Service. (i.e. to validate signatures)
        :param method: The OneID API call you wish to call
        :param data: Data for the OneID API CAll
        """
        url = "%s/%s" % (self.helper_server, method)
        r = requests.post(url, json.dumps(data), auth=(self.api_id, self.api_key))
        return r.json()

    def _call_repo(self, method, data={}):
        """Call the OneID Repo. (i.e. to do a OneID Confirm request)
        :param method: The OneID API call you wish to call
        :param data: Data for the OneID API CAll
        """
        url = "%s/%s" % (self.repo_server, method)
        r = requests.post(url, json.dumps(data), auth=(self.api_id, self.api_key))
        return r.json()

    def set_credentials(self, api_id="", api_key=""):
        """Set the credentials used for access to the OneID Helper Service
        :param api_id: Your OneID API ID
        :param api_key: Your OneID API key
        """
        if api_id != "":
            self.api_id = api_id
            self.api_key = api_key
        else:
            f = open(self.creds_file, 'r')
            creds = json.loads(f.read())
            f.close()
            self.api_id = creds["API_ID"]
            self.api_key = creds["API_KEY"]

    def validate(self, oneid_payload):
        """Validate the data received by a callback
        :param oneid_payload: The dictionary you want to validate, typically the payload from a OneID sign in call
        """
        if not isinstance(oneid_payload, dict):
            oneid_payload = json.loads(oneid_payload)

        data_to_validate = { "nonces" : oneid_payload["nonces"],
                             "uid" : oneid_payload["uid"] }

        if "attr_claim_tokens" in oneid_payload:
            data_to_validate["attr_claim_tokens"] = oneid_payload["attr_claim_tokens"]

        keychain_response = self._call_keychain("validate", data_to_validate)

        if not self.success(keychain_response):
            keychain_response["failed"] = "failed"
            return keychain_response

        oneid_payload.update(keychain_response)

        return oneid_payload

    def confirm(self, uid, token, message):
        data = {
            'two_factor_token' : token,
            'message' : message
        }

        confirm = self._call_repo("send_2fa", data)
        confirm.update({
            'uid' : uid
        })

        valid_response = self._call_keychain('validate', confirm)

        return valid_response



    def redirect(self, redirect_url, oneid_response):
        """Create the JSON string that instructs the AJAX code to redirect the browser to the account
        :param redirect_url: The URL of where you'd like to go
        :param oneid_response: The validated OneID response data
        :param sessionid: For the OneID example, your session ID
        """
        return json.dumps({"error" : oneid_response['error'],
                           "errorcode" : str(oneid_response['errorcode']),
                           "url" : redirect_url })

    def success(self, oneid_response):
        """Check errorcode in a response
        :param oneid_response:
        """
        return oneid_response.get("errorcode", None) == 0

'''

