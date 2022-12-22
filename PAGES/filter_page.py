from BASE.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class FilterPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    filter_cost_from = "//span[.//input[@placeholder='879']]"
    filter_cost_to = "//span[.//input[@placeholder='5 399']]"
    check_box_in_stock = "//dd[.//input[@value='in']]"


def get_filter_cost_from(self):
    return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_cost_from)))


def get_filter_cost_to(self):
    return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_cost_to)))


def get_check_box_in_stock(self):
    return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_in_stock)))
