from selenium.webdriver import Chrome
import pytest

# Want to skipp test case but in specific case

a = 101


# We use @pytest.mark.skipif(condition, reason="")
@pytest.mark.skipif(a > 100, reason="No data")
def test_conditional_valid_data():
    path = "/Users/b0222643/node_modules/chromedriver/lib/chromedriver/chromedriver"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')
    driver.maximize_window()
