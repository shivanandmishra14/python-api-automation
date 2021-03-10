from selenium.webdriver import Chrome
import pytest


# pytest -k specific test case name and run on terminal
# pytest -k test_invalid_datest_conditional_invalid_data
# Can also run for specific just a word in the test cases Ex: pytest -k invalid or pytest -k registration

def test_conditional_valid_data():
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()


def test_conditional_invalid_data():
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')

    