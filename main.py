import requests
from requests_oauthlib import OAuth2Session
import json
import datetime

OAUTH_CLIENT_ID = "82PLaXpAb8hUjPOt8h8o"
OAUTH_CLIENT_SECRET = "c8pplnZlVpYxztsCAs9e"
RETURN_URL = "https://localhost/" #return user here when complete, needed for call, but irrelevant
AUTH_ENDPOINT = "https://eou.formassembly.com/oauth/login"
TOKEN_REQUEST = "https://eou.formassembly.com/oauth/access_token"

ADMIN_INDEX = "https://eou.tfaforms.net/api_v1/forms/index.json"

API_AUTH_QUERY = {"type": "web",
                  "client_id": OAUTH_CLIENT_ID,
                  "return_uri": RETURN_URL,
                  "response_type":"code"}

oauth = OAuth2Session(OAUTH_CLIENT_ID, redirect_uri=RETURN_URL)

authorization_url, state = oauth.authorization_url(AUTH_ENDPOINT,
        type="web", response_type="code")

print 'Please go to %s and authorize access.' % authorization_url
authorization_response = raw_input('Enter the full callback URL')

## Build our authorization endpoint to display to user
#AUTH_URI=AUTH_ENDPOINT+"?"+API_AUTH_QUERY

## Since we're on the commandline, display authorization url to user ('Adam').
#print "Go to URL: "+AUTH_URI
#print "When directed to https://localhost/?code=XXXXXXXXXX copy and paste code here: (do not include the ending #)\n"


