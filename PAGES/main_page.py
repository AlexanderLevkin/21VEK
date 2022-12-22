from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    start_agree_button = "//button[@data-testid='agreementBtn']"
    start_catalog_button = "/html/body/div[5]/div[1]/header/div/div[5]/div/button/span"
    smartphone_and_tv_category_button = "//a[@href='/electronics/']"
    smartphones_apple_category_button = "//a[@href='/mobile/apple/']"

    """GETTERS"""

    def get_agree_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_agree_button)))

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_catalog_button)))

    def get_smartphone_and_tv_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.smartphone_and_tv_category_button)))

    def get_smartphones_apple_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.smartphones_apple_category_button)))

    """ACTIONS"""

    def click_to_agree_button(self):
        self.get_agree_button().click()
        print("CLICK TO AGREE BUTTON")

    def click_to_catalog_button(self):
        self.get_catalog().click()
        print("SELECT THE CATALOG")
