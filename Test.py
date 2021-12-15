from PageObject import SearchHelper

"""
Файл для тестирования.
Определения функций в PageObject.py
"""

def test_search_yandex(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.is_search_field_on_page()
    yandex_main_page.input_tensor()
    yandex_main_page.suggest_check()
    yandex_main_page.do_a_search()
    yandex_main_page.href_check()