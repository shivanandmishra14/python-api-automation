import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get request
resp = requests.get(url)

# print the response
print(resp)

# Display response content
print("Content is : ", resp.content)

# Display Headers
print(resp.headers)

