from selenium.webdriver import ActionChains

from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class MainPage(Base):
    # Locators

    ACCOUNT_BUTTON = (By.XPATH, '//span[@class="userToolsText"]')
    ENTER_BUTTON = (By.XPATH, '//button[@data-testid="loginButton"]')
    EMAIL_FIELD = (By.XPATH, '//input[@label="Электронная почта"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@label="Пароль"]')
    AUTHORIZATION_BUTTON = (By.XPATH, '//*[@id="modal"]/div/div/div[2]/div/div/form/div/div[2]/div[3]/button')
    EXIT_BUTTON = (By.XPATH, '//div[@class="ProfileItem_item__7XkAH"]')
    ACCOUNT_LOGGED_BUTTON = (By.XPATH, '//*[@id="header"]/div/div[5]/div/div[3]/div/div/div/button')
    LOGIN = "alexanlevkin@gmail.com"
    PASSWORD = "85d8ce47"

    # Getters
    def get_account_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ACCOUNT_BUTTON))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ENTER_BUTTON))

    def get_email_field(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.EMAIL_FIELD))

    def get_password_field(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.PASSWORD_FIELD))

    def get_authorization_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.AUTHORIZATION_BUTTON))

    def get_account_logged_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ACCOUNT_LOGGED_BUTTON))

    def get_exit_from_account_button(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.EXIT_BUTTON))

    # Actions
    def click_account_button(self):
        self.get_account_button().click()
        print("CLICK ON THE ACCOUNT BUTTON")

    def click_enter_button(self):
        self.get_enter_button().click()
        print("CLICK ON THE ENTER BUTTON")

    def enter_email_field(self):
        self.get_email_field().send_keys(self.LOGIN)
        print("ENTER THE LOGIN")

    def enter_password_field(self):
        self.get_password_field().send_keys(self.PASSWORD)
        print("ENTER THE PASSWORD")

    def click_authorization_button(self):
        self.get_authorization_button().click()
        print("CLICK ON THE AUTHORIZATION BUTTON")

    def click_account_logged_button(self):
        self.get_account_logged_button().click()
        print("USER WAS LOGGED")

    # Methods

    def enter_to_account(self):
        self.get_current_url()
        self.click_account_button()
        self.click_enter_button()
        self.enter_email_field()
        self.enter_password_field()
        self.click_authorization_button()
        time.sleep(1)
        self.click_account_logged_button()
        time.sleep(2)
        self.get_exit_from_account_button()
