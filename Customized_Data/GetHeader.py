import requests

#  Will create the dictionary here and send it
headerdata = {'T1': 'First_header'}

response = requests.get('https://reqres.in/api/users', headers=headerdata)
print(response.text)

#  =========================================================================

# Try again WIl another url
headersdata = {'T1':'second_header', 'F2':'Third_header'}

# we can pass as an another argument with url
resp = requests.get('http://httpbin.org/get', headers=headersdata)
print(resp.text)

