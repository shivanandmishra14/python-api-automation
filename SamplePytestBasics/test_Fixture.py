from selenium.webdriver import Chrome
import pytest


# Before and after the test cases we can put in fixtures.
#  We created separate method for for fixture.
#  We use fixture for after and before test.

# Fixture wil execute before and after but scope will execute only once everything.
@pytest.fixture(scope="module")
def setPath():
    # We are declaring driver global use it anywhere because it has to be used other places.

    global driver
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)

    # After each test case I have to execute something
    yield
    driver.quit()


# Now to use the fixture will pass the name of the method in each test case. setPath
@pytest.mark.Smoke
def test_conditional_valid_data(setPath):
    driver.get('http://www.thetestingworld.com/testings')
    # Assert to assert data
    assert driver.title == "Login and Signup Forms"


@pytest.mark.Sanity
def test_conditional_invalid_data(setPath):
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    assert driver.current_url == "http://www.thetestingworld.com/testings"



# After everything now we need just once browser should open and execute all test cases one by one so for that we have
# scope. Scope will mention in @ pytest.fixture(scope="")
#  Fixture wil execute before and after but scope will execute only once everything.
