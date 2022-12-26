from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time


class FilterPage(Base):
    # Locators

    CATALOG_TAB = (By.XPATH, '//div[@class="styles_catalogIcon__8Vgr8 styles_catalogIconAnimated__1wY28"]')
    SMARTPHONES_TAB = (By.XPATH, '//*[@id="header"]/div[1]/div[7]/div/div[1]/div[1]/div[2]/a/span')
    SMARTPHONES_APPLE_TAB = (By.XPATH, '//span[@class="styles_categoryName__28yR1"]')

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.CATALOG_TAB))

    def get_the_smartphone_category(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.SMARTPHONES_TAB))

    def get_smartphone_apple_category(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.SMARTPHONES_APPLE_TAB))

    # Actions

    def click_catalog_tab(self):
        self.click_element_emulate_human(self.get_catalog())
        print("CLICK ON THE AUTHORIZATION BUTTON")

    def hover_on_the_smartphone_category(self):
        self.hover_on_element_emulate_human(self.get_the_smartphone_category()).perform()
        print("HOVER ON THE SMARTPHONE CATEGORY")

    def click_smartphone_apple_category(self):
        self.click_element_emulate_human(self.get_smartphone_apple_category())
        print("CLICK ON THE APPLE TAB")
