import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# We need to send payload body for creating new data. SO we have created a new json file
# Read Input json file and 'r' means read mode
file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Post_Request/CreateUser.json', 'r')

# Read the file with variable
json_input = file.read()

# Now pass the readable data into JSON format.
request_json = json.loads(json_input)

# print to view it
print(request_json)

# Now need to send post request to send the josn request as body. So will pass URl and request json and
# store into a response object
response = requests.post(url, request_json)

# status code validation
assert response.status_code == 201

# Fetch response from header
print(response.headers)

# Specific headers
print("Specific header", response.headers.get('Set-Cookie'))

# print the response whatever will get after sending payload body
print(response.content)

# parse response into json content
response_json = json.loads(response.text)

# Display Json response
print(response_json)

# Pick ID or job  using JSON Path by storing in a var
job_json = jsonpath.jsonpath(response_json, 'job')

# May be it will return a list so fetch first
print(job_json[0])

# Pick ID or job  using JSON Path by storing in a var
id_json = jsonpath.jsonpath(response_json, 'id')

# May be it will return a list so fetch first
print(id_json[0])





