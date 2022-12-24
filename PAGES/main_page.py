from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait
import time


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    account_button = (By.XPATH, '//span[@class="userToolsText"]')
    enter_to_account_button_from_main_page = (By.XPATH, '//button[@data-testid="loginButton"]')
    enter_to_account_button = (By.XPATH, '//button[@class="styles_reactButton__2olKd style_baseActionButton__2LQYJ '
                                         'styles_submitButton__lmwVK""]')
    email_field = (By.XPATH, '//input[@label="Электронная почта"]')
    password_field = (By.XPATH, '//input[@label="Пароль"]')
    smartphone_and_tv_category_button = "//a[@href='/electronics/']"
    smartphones_apple_category_button = "//a[@href='/mobile/apple/']"

    """Find elements on page"""
    def enter_to_account(self, email, password):
        time.sleep(2)
        self.verify_element_present(self.account_button).click()
        self.verify_element_present(self.enter_to_account_button_from_main_page).click()
        self.verify_element_present(self.email_field).send_keys(email)
        self.verify_element_present(self.password_field).send_keys(password)
        self.verify_element_present(self.enter_to_account_button).click()


