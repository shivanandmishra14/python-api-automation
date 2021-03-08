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
print("Header values", response.headers)

# Specific header content, such as Date, Content type, Server
print("Date is: ", response.headers.get('Date'))
print("Content type is : ", response.headers.get('Content-Type'))
print("Server is : ", response.headers.get('Server'))

# Fetch cookies
print("cookies are :", response.cookies)

# Fetch encoding
print("Encoding is :", response.encoding)

# Fetch Elapsed time, it means the time between request sent and response recieved
print("Elapsed time is", response.elapsed)