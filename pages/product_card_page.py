from driver.web_driver import WebDriver
import configs.config as config


class ProductPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def visit_product_page(self):
        url = config.URL + '/smartphone/htc-touch-hd'
        self._driver.driver.get(url)

    def get_title_phones(self):
        return self._driver.find_element_by_tag("h1").text

    def input_quantity_field(self):
        self._driver.find_element_by_css_selector("div[class*='form'] input[name='quantity']")

    def add_to_card(self):
        self._driver.find_element_by_css_selector("button[id='button-cart']")

    def review_tab(self):
        return self._driver.find_element_by_css_selector("a[href$='review']").text

    def input_name_field(self):
        self._driver.find_element_by_id("input-name")
