import requests
import json
import jsonpath


# The data we get in response we are going to use it for further as an input. This process called request
# chaining.

def test_add_new_student():
    global id
    url = "http://thetestingworldapi.com/api/studentsDetails"
    file = open('restApi/Student_Test_Cases/add_new_student.json', 'r')
    json_request = json.loads(file.read())
    response = requests.post(url, json_request)
    # We know json path so
    id = jsonpath.jsonpath(response.json(), 'id')
    # We know it will return a list of ID so will oprint with index
    print(id[0])


def test_get_details():
    # Because ID will not work as in input here directly so we can global the ide in previous test case
    api_url = "http://thetestingworldapi.com/api/studentsDetails" + id[0]
    response = requests.get(api_url)
    print(api_url)

# What happens here whatever the id we are getting in first cases is we are using and fetching the data of same id
# This is called chaining
