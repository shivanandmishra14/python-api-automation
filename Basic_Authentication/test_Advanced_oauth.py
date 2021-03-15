from wsgiref import headers

import requests
from requests.auth import HTTPBasicAuth
import json
import jsonpath


# Advanced authentication. In this will generate access token and then will proceed further

def test_o_authentications():
    # We need to use first token URL
    token_url = "http://thetestingworldapi.com/Token"

    # Send values here in form of dictionary
    data = {'grant_type': 'password', 'username': 'admin', 'password': '1234567890'}

    # Post the data
    resp = requests.post(token_url, data)

    # Get  the token value
    token_value = jsonpath.jsonpath(resp.json(), 'access_token')

    # Want to access the token and create one dictionary.Whatever the token we get from above will pass here.
    # Along with the bearer so will write bearer then value.

    auth = {'Authorization': 'Bearer' + token_value[0]}

    #  Now on main URL
    url = "http://thetestingworldapi.com/api/StDetails/1104"

    #  Send request with token value
    response = requests.get(url, headers=auth)

    # Print response
    print(response.text)
