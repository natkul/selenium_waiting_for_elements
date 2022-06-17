import pytest
import os
from driver.web_driver import WebDriver
import configs.config as config
from pages.admin_page import AdminPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
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


@pytest.fixture
def login(browser):
    login = AdminPage(browser)
    login.visit_admin_page()
    login.input_username_field()
    login.input_password_field()
    login.click_submit_button()
    config.TOKEN = 'YQxanueqnGrEvVHMhLlmvakOxsYcbuJM'
    return browser
