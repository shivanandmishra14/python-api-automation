import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get request
response = requests.get(url)

# Fetch a data which is inside an array of response json
json_resp = json.loads(response.text)

# First name is inside a data array
first_name = jsonpath.jsonpath(json_resp, 'data[0].first_name')
print(first_name[0])

first_name1 = jsonpath.jsonpath(json_resp, 'data[2].first_name')
print(first_name1[0])


# Now to fetch all First name, Start a loop then replace any index with variable i and print i in form of string in
# form of concatenation
for i in range(0, 4):
    all_first_name = jsonpath.jsonpath(json_resp, 'data['+str(i)+'].first_name')
    print(all_first_name)
    
