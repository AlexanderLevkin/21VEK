from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from PAGES.apple_filter_page import AppleFilterPage
from conftest import brows


class CartPage(Base):
    # CART
    ORDERING_BUTTON = (By.XPATH, '//button[@class="g-button cr-button__order j-ga_track"]')
    CART_INDENT = (By.XPATH, '//span[@class="BasketTabsScreen_title__2NSA4"]')
    ITEM_IN_CART = (By.LINK_TEXT, 'Смартфон Apple iPhone 13 128GB MLPG3 / MLMM3 (звездный свет)')
    COST_OF_ITEM_CART = (By.XPATH, '//span[@id="j-total_cost"]')
    NAME_FIELD = (By.XPATH, '//input[@name="data[private][name]"]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="data[private][email]"]')
    CITY_FIELD = (By.XPATH, '//input[@name="data[city]"]')
    SELECT_CITY_FROM_DROP_DOWN = (By.LINK_TEXT, "г. Минск")
    DELIVERY_RADIO_BUTTON = (By.CSS_SELECTOR, '#delivery_self > input')
    STREET_AND_HOUSE_FIELD = (By.XPATH, '//input[@name="data[addr]"]')
    STREET_AND_HOUSE_DROP_DOWN = (By.LINK_TEXT, "ул. Ульяновская, 3")
    ENTRANCE_FIELD = (By.XPATH, '//input[@name="data[entrance]"]')
    FLOOR_FIELD = (By.XPATH, '//input[@name="data[floor]"]')
    FLAT_FIELD = (By.XPATH, '//input[@name="data[flat]"]')
    PHONE_FIELD = (By.XPATH, '//input[@name="data[phone]"]')
    COST_FOR_PAY = (By.XPATH, '//span[@class="g-price"]')

    """Getters"""

    def get_ordering_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.ORDERING_BUTTON))

    def get_cart_identification_by_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.CART_INDENT))

    def get_item_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.ITEM_IN_CART))

    def get_cost_of_item_from_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.COST_OF_ITEM_CART))

    def get_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.NAME_FIELD))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.EMAIL_FIELD))

    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.CITY_FIELD))

    def get_city_from_drop_down_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.SELECT_CITY_FROM_DROP_DOWN))

    def get_delivery_method_radiobutton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.DELIVERY_RADIO_BUTTON))

    def get_street_and_house_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.STREET_AND_HOUSE_FIELD))

    def get_street_and_house_from_drop_down_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.STREET_AND_HOUSE_DROP_DOWN))

    def get_entrance_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.ENTRANCE_FIELD))

    def get_floor_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.FLOOR_FIELD))

    def get_flat_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.FLAT_FIELD))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.PHONE_FIELD))

    def get_cost_for_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.COST_FOR_PAY))

    """Actions"""

    def click_ordering_button(self):
        self.click_element_emulate_human(self.get_ordering_button())
        print("CLICK ON THE ORDERING BUTTON")

    def fill_name_field(self):
        self.click_and_send_value(locator=self.get_name_field(), value="ALEX")
        print("WRITE NAME")

    def fill_email_field(self):
        self.click_and_send_value(locator=self.get_email_field(), value="ALEX@TEST.BY")
        print("WRITE EMAIL")

    def fill_city_field(self):
        self.get_city_field().clear()
        self.click_and_send_value(locator=self.get_city_field(), value="Минск")
        self.click_element_emulate_human(self.get_city_from_drop_down_menu())
        print("WRITE AND SELECT CITY")

    def select_delivery_method_radiobutton(self):
        self.click_element_emulate_human(self.get_delivery_method_radiobutton())
        print("SELECT DELIVERY METHOD")

    def fill_entrance_field(self):
        self.click_and_send_value(locator=self.get_entrance_field(), value="2")
        print("WRITE ENTRANCE")

    def fill_street_and_house_field(self):
        self.click_and_send_value(locator=self.get_street_and_house_field(), value="ул. Ульяновская, 3")
        self.click_element_emulate_human(self.get_street_and_house_from_drop_down_menu())
        print("WRITE STREET AND HOUSE")

    def fill_floor_field(self):
        self.click_and_send_value(locator=self.get_floor_field(), value="9")
        print("WRITE FLOOR")

    def fill_flat_field(self):
        self.click_and_send_value(locator=self.get_flat_field(), value="77")
        print("WRITE FLAT")

    def fill_phone_field(self):
        self.get_phone_field().clear()
        self.click_and_send_value(locator=self.get_phone_field(), value="+375(12)3213213")
        print("WRITE PHONE NUMBER")

    def cost_from_cart(self):  # Cost from cart to compare with replace method
        self.get_text_with_replace(self.get_cost_of_item_from_cart(), what_to_replace="р.", replaced="  ")

    def cost_for_pay_final(self):  # Final cost in order to compare
        self.get_text(self.get_cost_for_pay())

    """METHOD"""

    def cart_actions(self):
        self.get_current_url()
        self.assert_word(word=self.get_cart_identification_by_word(), result='Корзина')
        self.assert_word(word=self.get_item_in_cart(), result='Смартфон Apple iPhone 13 '
                                                              '128GB MLPG3 / MLMM3 (звездный свет)')
        self.cost_from_cart()
        # self.get_screenshot()
        self.click_ordering_button()
        self.fill_name_field()
        self.fill_email_field()
        self.fill_city_field()
        self.fill_street_and_house_field()
        self.fill_entrance_field()
        self.fill_floor_field()
        self.fill_flat_field()
        self.fill_phone_field()
        self.assert_two_phrases(self.cost_from_cart(), self.cost_for_pay_final())
        self.get_screenshot()
        time.sleep(3)

