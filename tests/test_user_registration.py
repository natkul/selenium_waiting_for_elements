from pages.user_registration_page import UserRegistration


def test_user_registration_page(browser):
    user_page = UserRegistration(browser)
    user_page.visit_user_page()
    title = user_page.get_account_title()
    assert title == "Register Account"
    user_page.first_name_field()
    user_page.password_field()
    user_page.telephone_field()
    user_page.continue_button()
