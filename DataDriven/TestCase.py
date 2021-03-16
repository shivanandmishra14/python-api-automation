import requests
import json
import openpyxl
import pytest
from DataDriven import Library


# to Use Library. In another folder will use from Data_Driven import Library
# For reading data from excel we need library calle Openpyxl.
# Pip install openpyxl

def test_read_data_from_excel():
    url = "http://thetestingworldapi.com/api/studentsDetails"

    # Open file
    file = open('/Users/b0222643/Documents/PythonAutomationAPI/restApi/Data_Driven_TC/TestDataFIle.json', 'r')

    # Read file and typecast in json format
    json_request = json.loads(file.read())

    # Object of the class. packagename.classname and we need to pass two arguments FileNamePath and SheetName
    obj = Library.RowCount("/Users/b0222643/Documents/PythonAutomationAPI/restApi/Data_Driven_TC/Data.xlsx", "Sheet1")

    # Find how many columns row and keys we are having
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    KeyList = obj.fetch_key_names()

    # Start from 2nd row because first is header
    for i in range(2, row + 1):
        updated_json_req = obj.update_req_json_data(i, json_request, KeyList)
        response = requests.post(url, updated_json_req)
        print(response)
