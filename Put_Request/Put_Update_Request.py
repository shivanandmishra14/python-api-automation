import requests
import json
import jsonpath

# Put request to Update resource or value in an existing API

url = 'https://reqres.in/api/users/2'

# Reading the request and stored in json format, like Post
file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Put_Request/UpdateUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make a Put request
response = requests.put(url, request_json)
assert response.status_code == 200
print(response.text)

# Parse response content into Json
response_json = json.loads(response.text)
print(response_json)


# Now want to fetch any value
updated_value = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_value[0])
