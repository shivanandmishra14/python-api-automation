import json

# How to pass string into jason format in python
var = '{ "firstName": "John", "lastName" : "doe", "age" : 26, "address" : "#qwerty"}'
json_result = json.loads(var)
print(json_result)
