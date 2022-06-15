from pages.home_page import MainPage


def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.visit_home_page()
    main_page.img_opencart()
    main_page.get_trash_button()
    main_page.get_search_field()
    main_page.get_swiper_button_next()
    subtitle = main_page.get_subtitle_featured()
    assert subtitle == "Featured"
