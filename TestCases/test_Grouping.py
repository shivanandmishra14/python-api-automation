import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"


@pytest.fixture(scope="module")
def start_execution():
    global file
    file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Post_Request/CreateUser.json', 'r')
    yield


#  ======================================================
# Grouping testing, We can give any name
@pytest.mark.Sanity
def test_create_new_user():
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    assert response.status_code == 201
    print(response.headers)


#  ======================================================
# Grouping testing, We can give any name

@pytest.mark.Smoke
def test_create_other_user():
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

#  ======================================================
# Execute for particular  pytest -m Sanity -v TestCase
#  pytest -m "not Sanity" -v TestCases

