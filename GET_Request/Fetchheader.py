import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send get request
response = requests.get(url)

# print the response
print(response)


# Validate status code
print(response.status_code)
assert response.status_code == 200


# Display response content
print("Content is : ", response.content)


# Display Headers
print(response.headers)


# Fetch Response headers
print( "Header values", response.headers)


# Specific header content, such as Date, Content type, Server
print(response.headers.get('Date'))
print(response.headers.get('Content-Type'))
print(response.headers.get('Server'))


