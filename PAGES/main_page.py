from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class MainPage(Base):

    ACCOUNT_BUTTON = (By.XPATH, '//span[@class="userToolsText"]')
    ENTER_BUTTON = (By.XPATH, '//button[@data-testid="loginButton""]')

    # Getters
    def enter_to_the_account(self):
        self.verify_element_to_be_clickable(self.ACCOUNT_BUTTON).click()




    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click Select Product 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click Select Product 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click Select Product 3")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    def click_menu(self):
        self.get_menu().click()
        print("Click Menu")

    def click_link_about(self):
        self.get_link_about().click()
        print("Click Menu")

    # Methods
    def select_product1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url("https://saucelabs.com/")



