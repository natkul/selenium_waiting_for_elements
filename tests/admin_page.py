from pages.admin_page import AdminPage


def test_admin_page(browser):
    admin_page = AdminPage(browser)
    admin_page.visit_admin_page()
    admin_page.username_field()
    admin_page.password_field()
    admin_page.submit_button()
    password = admin_page.forgotten_password_link()
    assert password == "Forgotten Password"
    title = admin_page.get_panel_title()
    assert title == "Please enter your login details."
