import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"


# Break a testcase in two methods
def test_create_new_user():
    file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Post_Request/CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    assert response.status_code == 201
    print(response.headers)


def test_create_other_user():
    file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Post_Request/CreateUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    print(response.headers)
    print("Specific header", response.headers.get('Set-Cookie'))
    print(response.content)
    response_json = json.loads(response.text)
    print(response_json)
    job_json = jsonpath.jsonpath(response_json, 'job')
    print(job_json[0])
    id_json = jsonpath.jsonpath(response_json, 'id')
    print(id_json[0])
