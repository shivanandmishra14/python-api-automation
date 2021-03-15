import requests
from requests.auth import HTTPBasicAuth


def test_basic_authentications():
    # Basic authentication data will pass with URL
    resp = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('shiva','123456'))
    print(resp.text)


