from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class AppleFilterPage(Base):
    """Locators"""
    UNDERSTAND_BUTTON = (By.XPATH, '//button[@class="styles_reactButton__2olKd styles_button__2N0fI"]')
    SMARTPHONES_APPLE_TAB = (
        By.XPATH, '//*[@id="header"]/div[1]/div[7]/div/div[2]/div[3]/div[1]/div[1]/div[1]/a[3]/span')
    WORD_APPLE_SMARTPHONES = (By.XPATH, '//h1[@class="content__header cr-category_header"]')
    SLIDER_FROM = (By.XPATH, '//a[@style="left: 0%;"]')
    SLIDER_TO = (By.XPATH, '//a[@style="left: 100%;"]')
    # COST_ITEM_FROM_FIELD = (By.XPATH, '//input[@name="filter[price][from]"]') This locator for use field of
    # cost from instead slider
    # COST_ITEM_TO_FIELD = (By.XPATH, '//input[@name="filter[price][to]"]') This locator for use field of
    # cost to instead slider
    IN_STOCK_CHECKBOX = (By.XPATH, '//label[@title="В наличии"]')
    COLOR_FILTER = (By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/div[1]/form/div[4]/dl[21]/dt/span')
    CHECKBOX_COLOR_WHITE = (By.XPATH,
                            '/html/body/div[5]/div[2]/div[2]/div[2]/div[1]/form/div[4]/dl[21]/div/dd[3]/label')
    BUTTON_SHOW_GOODS = (By.XPATH, '//button[@class="filter-controls__submit filter__button g-button"]')
    IPHONE13_128_WHITE = (By.XPATH, '//form[@action="/to_basket/?item=7116374&special=0&price=2799.00"]')
    COST_OF_IPHONE13_128_WHITE = (By.XPATH, '//span[@class="g-item-data j-item-data j-item-data7116374 '
                                            'j-item-data-real7116374 "]')
    IPHONE_NAME_IN_CATALOG = (By.LINK_TEXT, 'Смартфон Apple iPhone 13 128GB MLPG3 / MLMM3 (звездный свет)')
    CART_BUTTON = (By.XPATH, '//a[@class="headerCartBox"]')

    """Getters Common"""

    def get_smartphone_apple_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.SMARTPHONES_APPLE_TAB))

    def get_understand_button(self):  # close pop-up about cookies
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.UNDERSTAND_BUTTON))

    def get_check_word_apple_smart(self):  # get item word to compare
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.WORD_APPLE_SMARTPHONES))

    """Getters Operation with filter"""

    # You can use it if you want to choose cost filter by fields from and to instead slider. To use it you need to
    # disable slider getters and actions
    # def get_cost_item_field_from(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.COST_ITEM_FROM_FIELD))
    #
    # def get_cost_item_field_to(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.COST_ITEM_TO_FIELD))

    def get_in_cart_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.IN_STOCK_CHECKBOX))

    def get_color_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.COLOR_FILTER))

    def get_color_white_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.CHECKBOX_COLOR_WHITE))

    def get_slider_from(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.SLIDER_FROM))

    def get_slider_to(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.SLIDER_TO))

    def get_button_show_goods(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.BUTTON_SHOW_GOODS))

    def get_iphone_13_128_white(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.IPHONE13_128_WHITE))

    def get_iphone_13_128_cost(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.COST_OF_IPHONE13_128_WHITE))

    def get_iphone_name(self):  # Item name from filter page to compare
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.IPHONE_NAME_IN_CATALOG))

    def get_cart_button(self):  # Item cost from filter page to compare
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.CART_BUTTON))

    """Actions"""

    def click_understand_button(self):
        self.get_understand_button().click()
        print("CLICK ON THE UNDERSTAND BUTTON")

    def click_smartphone_apple_category(self):
        self.click_element_emulate_human(self.get_smartphone_apple_category())
        print("CLICK ON THE APPLE TAB")

    # You can use it if you want to choose cost filter fields from and to instead slider, now are disabled because
    # I use slider getters and actions
    # def fill_in_cost_item_from(self):
    #     self.click_and_send_value(locator=self.get_cost_item_field_from(), value="2000")
    #     print("FILL IN THE COST FROM")
    #
    # def fill_in_cost_item_to(self):
    #     self.click_and_send_value(locator=self.get_cost_item_field_to(), value="3000")
    #     print("FILL IN THE COST TO")
    def click_hold_move_slider_from(self):
        self.click_and_hold_slider(self.get_slider_from(), x=70, y=0)
        print(f"COST FROM SLIDER")

    def click_hold_move_slider_to(self):
        self.click_and_hold_slider(self.get_slider_to(), x=-50, y=0)
        print("COST TO SLIDER")

    def click_on_in_stock_checkbox(self):
        self.click_element_emulate_human(locator=self.get_in_cart_checkbox())
        print("CLICK ON IN STOCK CHECKBOX")

    def move_and_click_color_filter(self):
        self.scrolling_page_to(x=0, y=1200)
        self.click_element_emulate_human(locator=self.get_color_filter())
        print("CLICK TO THE COLOR FILTER")

    def click_white_color(self):
        self.click_element_emulate_human(locator=self.get_color_white_checkbox())
        print("SELECT WHITE COLOR")

    def click_button_show_goods(self):
        self.click_element_emulate_human(locator=self.get_button_show_goods())
        print("CLICK TO SHOW GOODS BUTTON")

    def add_iphone13_to_cart(self):
        self.scrolling_page_to(x=0, y=600)
        self.click_element_emulate_human(locator=self.get_iphone_13_128_white())
        print("ADD IPHONE 13 TO CART")

    def transfer_to_cart(self):
        self.click_element_emulate_human(locator=self.get_cart_button())
        print("TRANSFER TO CART")

    def name_item_from_filter_page(self):    # Item name from filter page to compare
        self.get_text(self.get_iphone_name())

    def cost_item_from_filter_page(self):   # Item cost from filter page to compare
        self.get_text(self.get_iphone_13_128_cost())

    """METHOD"""

    def apple_filter_actions(self):
        self.click_understand_button()
        self.click_smartphone_apple_category()
        self.assert_url(result="https://www.21vek.by/mobile/apple/")
        time.sleep(1)
        self.assert_word(word=self.get_check_word_apple_smart(), result="Смартфоны Apple")
        # self.fill_in_cost_item_from()
        # self.fill_in_cost_item_to()
        self.click_hold_move_slider_from()
        self.click_hold_move_slider_to()
        self.click_on_in_stock_checkbox()
        self.move_and_click_color_filter()
        self.click_white_color()
        self.click_button_show_goods()
        self.name_item_from_filter_page()
        self.cost_item_from_filter_page()
        self.add_iphone13_to_cart()
        self.transfer_to_cart()
        time.sleep(5)
