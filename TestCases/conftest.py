import pytest
from selenium import webdriver
from Constants.config import TestData


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_DRIVER_EXEPATH)
        # return driver
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=TestData.CHROME_DRIVER_EXEPATH)
        # return driver
    request.cls.driver = web_driver
    yield
    web_driver.close()
