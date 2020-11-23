from selenium import webdriver
from Utilities.readProperty import ReadConfig
import pytest

@pytest.fixture()
def setUp(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='IE':
        driver=webdriver.Ie()
    else:
        driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(ReadConfig.getAppURL())
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")
   
@pytest.fixture() 
def browser(request):
    request.config.getoption("--browser")
    
def pytest_configure(config):
    config._metadata['Project Name']='Nop Commerce'
    config._metadata['Module Name']='Login'
    config._metadata['Tester']='Rakshit'
    
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME")
    metadata.pop("Plugins")
    

