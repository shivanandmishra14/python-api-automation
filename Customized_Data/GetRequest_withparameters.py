import requests

# Parameter we can send in form of key value pair
# Can create param in form of key value pair like dictionary

# param = {'name': "Shivanand", 'number': '+91987654321'}
# we can pass as an another argument with url
# response = requests.get('https://reqres.in/api/users?page=2', params=param)
# print(response.text)

# =====================================================

param = {'name': "Shivanand", 'number': '+91987654321'}
resp = requests.get('http://httpbin.org/get', params=param)
print(resp.text)

