from selenium.webdriver import Chrome
import pytest


# File name should start from test
# Will write test cases in methods and methods should also start from test. We use def for methods.

# Add decorator for pytest skip when we need to skipp. For using decorator we need to import pytest

@pytest.mark.skip("don't want to execute in current build")
def test_registration_valid_data():
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()

# Multiple test cases data
# def test_invalid_data():
#     path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
#         driver = Chrome(executable_path=path)
#         driver.get('http://www.thetestingworld.com/testings')
#

# To execute more info use pytest -v on terminal
