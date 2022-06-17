from pages.catalog_page import CatalogPage


def test_catalog_page(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.visit_catalog_page()
    catalog_page.add_to_wish_list()
    catalog_page.view_phones_by_list()
    subtitle = catalog_page.get_subtitle_phones()
    assert subtitle == "Phones & PDAs"
    catalog_page.img_product_htc()
    link = catalog_page.product_compare_link()
    assert link == "Product Compare (0)"
