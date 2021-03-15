import requests
import json


# import jsonpath

def test_multiple_student():
    url = "http://thetestingworldapi.com/api/studentsDetails"

    # Open file
    file = open('restApi/Data_Driven_TC/TestDataFIle.json', 'r')

    # Read the file
    json_request = json.loads(file.read())

    # Response after requesting
    response = requests.post(url, json_request)

    # Print status code
    print(response.status_code)

    # Assert the status code
    assert response.status_code == 201
