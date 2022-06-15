from pages.product_card_page import ProductPage


def test_catalog_page(browser):
    product_page = ProductPage(browser)
    product_page.visit_product_page()
    title = product_page.get_title_phones()
    assert title == "HTC Touch HD"
    product_page.input_quantity_field()
    product_page.add_to_card()
    tab = product_page.review_tab()
    assert tab == "Reviews (0)"
    product_page.input_name_field()
