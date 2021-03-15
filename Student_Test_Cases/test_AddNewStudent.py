import requests
import json
import jsonpath


def test_add_student():
    # Base url
    url = "http://thetestingworldapi.com/api/studentsDetails"

    # Opening the file
    file = open('/restApi/Student_Test_Cases/student_data.json', 'r')

    # Loading the file
    json_req = json.loads(file.read())

    # Post call
    response = requests.post(url, json_req)

    print(response.text)


def test_get_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/300"
    resp = requests.get(api_url)
    json_resp = json.loads(resp.text)
    # We can approach either above option or below both will work as same.
    id = jsonpath.jsonpath(json_resp, 'data.id')
    assert id[0] == 300
    print(resp)
    print(id)


def test_Update_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/300"
    file = open('/restApi/Student_Test_Cases/update_student_data.json', 'r')
    json_req = json.loads(file.read())
    response = requests.put(api_url, json_req)
    print(response.text)


def test_delete_student_data():
    delete_url = "http://thetestingworldapi.com/api/studentsDetails/300"
    delete_response = requests.delete(delete_url)
    print(delete_response)


#     After delete will fetch the details It should get failed.
def test_fetch_student_data():
    api_url = "http://thetestingworldapi.com/api/studentsDetails/300"
    resp = requests.get(api_url)
    json_resp = json.loads(resp.text)
    # We can approach either above option or below both will work as same.
    id = jsonpath.jsonpath(json_resp, 'data.id')
    assert id[0] == 300
    print(resp)
    print(id)



