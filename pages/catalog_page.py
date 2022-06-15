from driver.web_driver import WebDriver
import configs.config as config


class CatalogPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def visit_catalog_page(self):
        url = config.URL + '/smartphone'
        self._driver.driver.get(url)

    def get_subtitle_phones(self):
        return self._driver.find_element_by_tag("h2").text

    def product_compare_link(self):
        return self._driver.find_element_by_css_selector("a[href$='compare']").text

    def img_product_htc(self):
        self._driver.find_element_by_css_selector("a[href$='htc-touch-hd'] img[class='img-responsive']")

    def view_phones_by_list(self):
        self._driver.find_element_by_id("list-view")

    def add_to_wish_list(self):
        self._driver.find_element_by_css_selector("div[class='button-group']")
