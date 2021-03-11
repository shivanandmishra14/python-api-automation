import requests
import json
import jsonpath
import pytest

#  ===================================================
# Fixtures

url = "https://reqres.in/api/users"


# We have scope to execute where we want to execute.scope="module" it means only once
# Yields for after method
@pytest.fixture(scope="module")
def start_execution():
    global file
    file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Post_Request/CreateUser.json', 'r')

    yield


#  ===================================================

# Break a testcase in two methods
# Add decorator to to skip
@pytest.mark.skip("This is not valida for validation")
def test_create_new_user():
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(url, request_json)
    assert response.status_code == 201
    print(response.headers)


#  ===================================================

# Conditional formatting
a = 89


@pytest.mark.skipif(a > 10, reason="Nothing")
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
