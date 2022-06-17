from pages.admin_page import AdminPage


def test_admin_page(browser):
    admin_page = AdminPage(browser)
    admin_page.visit_admin_page()
    admin_page.input_username_field()
    admin_page.input_password_field()
    admin_page.click_submit_button()
    password = admin_page.forgotten_password_link()
    assert password == "Forgotten Password"
    title = admin_page.get_panel_title()
    assert title == "Please enter your login details."
