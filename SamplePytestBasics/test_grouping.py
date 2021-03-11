from selenium.webdriver import Chrome
import pytest

# Grouping is important because everytime we will not use the all test cases.
# Sometimes we need to execute only particular TC so we use grouping for the same.
# Can give Pytest.mark Somke/Sanity/Regression as pe the need. These are called as tag and can be anything
# Execute with pytest -m Smoke,  pytest -m Smoke -v to run in group
# Execute the tag pytest -m "not Sanity" -v so it will execute all TC other than sanity

@pytest.mark.Smoke
def test_conditional_valid_data():
   path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
   driver = Chrome(executable_path=path)
   driver.get('http://www.thetestingworld.com/testings')
   driver.maximize_window()


@pytest.mark.Sanity
def test_conditional_invalid_data():
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')

@pytest.mark.Smoke
def test_registration_valid_data():
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()

