import requests
import json


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
