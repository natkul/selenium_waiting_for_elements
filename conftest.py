import pytest
import os
from driver.web_driver import WebDriver
import configs.config as config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://192.168.220.130:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    config.URL = url
    drivers = request.config.getoption("--drivers")
    web_driver = WebDriver(browser=browser, url=url, drivers=drivers)
    web_driver.driver_init()
    yield web_driver
    web_driver.driver.close()
