import requests
import json

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

# print the response whatever will get after sending payload body
print(response.content)
