from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchLocators:
    LOCATOR_SEARCH_FIELD = (By.NAME, 'text')
    LOCATOR_HREF_CHEK = (By.CSS_SELECTOR, '[class="VanillaReact OrganicTitle OrganicTitle_wrap Typo Typo_text_l Typo_line_m organic__title-wrapper"] > a')




class SearchHelper(BasePage):
    """
        Производный класс от базового класса BasePage
        Реализация функций для Test.py
        """
    def is_search_field_on_page(self):
        self.is_elem_on_page(SearchLocators.LOCATOR_SEARCH_FIELD)
        return print('Поле поиска есть на странице')

    def input_tensor(self):
        return self.find_element(SearchLocators.LOCATOR_SEARCH_FIELD).send_keys("Тензор")

    def suggest_check(self):
        time.sleep(2)
        self.is_elem_on_page(SearchLocators.LOCATOR_SEARCH_FIELD)
        return print('Таблица с подсказакми появилась')

    def do_a_search(self):
        self.find_element(SearchLocators.LOCATOR_SEARCH_FIELD).send_keys(Keys.ENTER)
        return print('Таблица результатов поиска появилась')

    def href_check(self):
        """
        Проверка совпадения URL с tensor.ru
        """
        time.sleep(5)
        elements = self.find_elements(SearchLocators.LOCATOR_HREF_CHEK)
        sum = 0
        for i in range(5):
            hrefis = elements[i].get_attribute("href")
            neededhref = "tensor.ru"
            print(hrefis)
            if neededhref in hrefis:
                sum += 1
        if sum == 5:
            print('Ссылка на тензор есть в первых 5 результатах')
        else:
            print('Хотя бы одна ссылка не ведет на tensor.ru')


