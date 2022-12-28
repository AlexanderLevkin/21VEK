from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class AppleFilterPage(Base):
    """Locators"""
    SMARTPHONES_APPLE_TAB = (
        By.XPATH, '//*[@id="header"]/div[1]/div[7]/div/div[2]/div[3]/div[1]/div[1]/div[1]/a[3]/span')
    WORD_APPLE_SMARTPHONES = (By.XPATH, '//h1[@class="content__header cr-category_header"]')
    COST_ITEM_FROM_FIELD = (By.XPATH, '//input[@name="filter[price][from]"]')
    COST_ITEM_TO_FIELD = (By.XPATH, '//input[@name="filter[price][to]"]')
    IN_STOCK_CHECKBOX = (By.XPATH, '//label[@class="g-form__checklabel cr-help-place"]')
    YEAR_FILTER = (By.XPATH, '//span[@class="g-pseudo_href j-filter__fold"]')
    CHECKBOX_2022_YEAR_FILTER = (By.XPATH, '//label[@title="2022 г."]')

    """Getters"""

    def get_smartphone_apple_category(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.SMARTPHONES_APPLE_TAB))

    def get_check_word_apple_smart(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.WORD_APPLE_SMARTPHONES))

    def get_cost_item_field_from(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.COST_ITEM_FROM_FIELD))

    def get_cost_item_field_to(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.COST_ITEM_TO_FIELD))

    def get_in_cart_checkbox(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.IN_STOCK_CHECKBOX))

    def get_year_filter(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.YEAR_FILTER))

    def get_2022_year_checkbox(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.CHECKBOX_2022_YEAR_FILTER))

    """Actions"""

    def click_smartphone_apple_category(self):
        self.click_element_emulate_human(self.get_smartphone_apple_category())
        print("CLICK ON THE APPLE TAB")

    def fill_in_cost_item_from(self):
        self.click_and_send_value(locator=self.get_cost_item_field_from(), value="1000")
        print("FILL IN THE COST FROM")

    def fill_in_cost_item_to(self):
        self.click_and_send_value(locator=self.get_cost_item_field_to(), value="3000")
        print("FILL IN THE COST TO")

    def click_on_in_stock_checkbox(self):
        self.click_element_emulate_human(locator=self.get_in_cart_checkbox())
        print("CLICK ON IN STOCK CHECKBOX")

    def move_and_click_the_year_filter(self):
        self.click_element_emulate_human(locator=self.get_year_filter())
        print("CLICK TO THE YEAR FILTER")

    def click_2022_year_checkbox(self):
        self.click_element_emulate_human(locator=self.get_2022_year_checkbox())
        print("CLICK YEAR 2022 CHECKBOX")

    def apple_filter_actions(self):
        self.click_smartphone_apple_category()
        time.sleep(1)
        self.assert_word(word=self.get_check_word_apple_smart(), result="Смартфоны Apple")
        self.fill_in_cost_item_from()
        self.fill_in_cost_item_to()
        self.click_on_in_stock_checkbox()
        self.move_and_click_the_year_filter()
        self.click_2022_year_checkbox()
        time.sleep(1)
