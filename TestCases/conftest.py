import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readproperties import Readconfig

get_URL = Readconfig.get_URL()

# @pytest.fixture()
# def setup():
#     url = "https://automation.credence.in"
#     chromedriver_path = ChromeDriverManager().install()
#     driver = webdriver.Chrome(service=ChromeServices(executable_path=chromedriver_path))
#     driver.get(url)
#     driver.maximize_window()
#     return driver

@pytest.fixture()
def setup():

    # chrome_opts = Options()
    # chrome_opts.add_experimental_option("detach", True)
    # chrome_opts.add_argument("headless")

    driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))  # options=chrome_opts
    driver.get(get_URL)
    driver.maximize_window()
    return driver

#To customize the Environment details in HTML reports:
def pytest_metadata(metadata):
    metadata["Project Name"] = "Credkart"
    metadata["Environment"] = "QA Test Env"
    metadata["Module"] = "User Profile"
    metadata["Test Engineer"] = "Akshay Sakhare"
    metadata.pop("Plugins", None)


#parameterization if limites number of credentials:
@pytest.fixture(params= [
    ("akshay@credence.com", "testing@123", "pass"),
    ("akshay@credence.com", "testing123", "fail"),
    ("akshay16@credence.com", "testing@123", "fail"),
    ("akshay16@credence.com", "testing123", "fail")
])
def getDataForLogin(request):
    return request.param