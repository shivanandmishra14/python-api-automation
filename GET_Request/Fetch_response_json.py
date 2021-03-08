import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get request
response = requests.get(url)

# Need to print response in JSON, SO parse response to JSON Format
# Whatever the repsonse we are getting we are loading into json format by creating variable

json_resp = json.loads(response.text)
print(json_resp)


# Now need to fetch any specific value from JSONPATH and storing in a variable
per_page = jsonpath.jsonpath(json_resp, 'per_page')

# we can assert and validate
assert per_page[0] == 6

# Print with the index value because there could be the list of values
print("Total number of per page", per_page[0])




