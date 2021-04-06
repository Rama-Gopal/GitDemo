import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='/Users/peddinti.gopal/Downloads/chromedriver')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='/Users/peddinti.gopal/Downloads/geckodriver')
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome(executable_path='/Users/peddinti.gopal/Downloads/chromedriver')
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
