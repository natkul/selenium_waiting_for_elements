from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


class WebDriver:
    TIMEOUT_STEP = 0.5
    MAX_TIMEOUT = 10

    def __init__(self, browser: str, url: str, drivers: str):
        self.browser = browser
        self.url = url
        self.drivers = drivers
        self.driver = None

    def driver_init(self):
        if self.browser == "chrome":
            service = ChromiumService(executable_path=self.drivers + "/chromedriver")
            driver = webdriver.Chrome(service=service)
        elif self.browser == "firefox":
            service = FFService(executable_path=self.drivers + "/geckodriver")
            driver = webdriver.Firefox(service=service)
        elif self.browser == "opera":
            driver = webdriver.Opera(executable_path=self.drivers + "/operadriver")
        else:
            driver = webdriver.Safari()

        driver.maximize_window()
        driver.url = self.url
        self.driver = driver

    def allert_accept(self):
        return self.driver.switch_to.alert.accept()

    def get_url(self):
        return self.driver.current_url

    def __custom_find(self, method, elem, timeout):
        sleep(self.TIMEOUT_STEP)
        try:
            element = WebDriverWait(self.driver, timeout, self.TIMEOUT_STEP).until(EC.presence_of_element_located(
                (method, elem)))
            return element
        except TimeoutException as e:
            print(e)
            return None

    def __custom_find_all_elements(self, method, elem, timeout):
        sleep(self.TIMEOUT_STEP)
        try:
            element = WebDriverWait(self.driver, timeout, self.TIMEOUT_STEP).until(EC.presence_of_all_elements_located(
                (method, elem)))
            return element
        except TimeoutException as e:
            print(e)
            return None

    def find_element_by_css_selector(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find(By.CSS_SELECTOR, elem, timeout)

    def find_elements_by_css_selector(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find_all_elements(By.CSS_SELECTOR, elem, timeout)

    def find_element_by_tag(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find(By.TAG_NAME, elem, timeout)

    def find_element_by_id(self, elem, timeout=MAX_TIMEOUT):
        return self.__custom_find(By.ID, elem, timeout)

    def wait_until_clickable(self, element, timeout=MAX_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))

    def wait_until_visible(self, element, timeout=MAX_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_until_invisible(self, element, timeout=MAX_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, element)))

