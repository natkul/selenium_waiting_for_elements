from pages.home_page import MainPage
from pages.currency import Currency


def test_change_to_euro(browser):
    main_page = MainPage(browser)
    main_page.visit_home_page()
    currency = Currency(browser)
    currency.change_currency_click()
    currency.change_currency_to_euro()
    euro = currency.check_change()
    assert euro == "€"


def test_change_to_pound(browser):
    main_page = MainPage(browser)
    main_page.visit_home_page()
    currency = Currency(browser)
    currency.change_currency_click()
    currency.change_currency_to_pound_sterling()
    pound = currency.check_change()
    assert pound == "£"


def test_change_to_dollar(browser):
    main_page = MainPage(browser)
    main_page.visit_home_page()
    currency = Currency(browser)
    currency.change_currency_click()
    currency.change_currency_to_dollar()
    dollar = currency.check_change()
    assert dollar == "$"
