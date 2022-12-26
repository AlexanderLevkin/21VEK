from datetime import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Collection of actions"""

    def verify_element_to_be_clickable(self, locator: tuple):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator: tuple):
        return self.verify_element_to_be_clickable(locator)

    def hover_on_element_emulate_human(self, element):
        ActionChains(self.driver).pause(0.3).move_to_element(element).perform()

    def click_element_emulate_human(self, element):
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()


    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("GOOD VALUE WORLD")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("GOOD VALUE URL")

    """Method screen shot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('/Users/alexanderlevkin/Desktop/LESSONS/main_project/screen/' + name_screenshot)
