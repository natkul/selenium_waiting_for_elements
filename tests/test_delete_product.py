from pages.admin_section_page import AdminSection


def test_add_product(login):
    product = AdminSection(login)
    product.product_tab()
    product.add_products()
    product.choose_product()
    product.delete_product()
