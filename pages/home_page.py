from driver.web_driver import WebDriver
import configs.config as config


class MainPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def visit_home_page(self):
        url = config.URL
        self._driver.driver.get(url)

    def img_opencart(self):
        self._driver.find_element_by_css_selector("img[title='Your Store']")

    def get_trash_button(self):
        self._driver.find_element_by_css_selector("button[data-loading-text='Loading...']")

    def get_search_field(self):
        self._driver.find_element_by_css_selector("input[name='search']")

    def get_swiper_button_next(self):
        self._driver.find_element_by_css_selector("div[class*='carousel'] div[class*='swiper-button-next']")

    def get_subtitle_featured(self):
        return self._driver.find_element_by_tag("h3").text
