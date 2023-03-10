import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Collection of actions"""

    def hover_on_element_emulate_human(self, locator):  # Hover on element emulate human behavior
        ActionChains(self.driver).pause(0.3).move_to_element(locator).perform()

    def click_element_emulate_human(self, locator):  # Click on element emulate human behavior with chain MOVE
        ActionChains(self.driver).pause(0.3).move_to_element(locator).click().perform()

    def scroll_to_element_and_click(self, locator):  # Scroll and lick on element emulate human behavior
        ActionChains(self.driver).pause(0.3).scroll_to_element(locator).click().perform()

    def scroll_to_element(self, locator):  # Scroll to element without any actions
        ActionChains(self.driver).pause(0.3).move_to_element(locator).perform()

    def click_and_send_value(self, locator, value):  # Click to field (for instance) and send some values
        ActionChains(self.driver).pause(0.3).move_to_element(locator).click().send_keys(value).perform()

    def click_and_hold_slider(self, locator, x, y):  # Func to use slider
        ActionChains(self.driver).move_to_element(locator).perform()
        ActionChains(self.driver).click_and_hold(locator).move_by_offset(x, y).release().perform()

    def scrolling_page_to(self, x, y):  # Simple scrolling page without element
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"CURRENT URL: {get_url}")

    """Method get text"""

    def get_text(self, locator):
        text_word = locator.text
        print(f"{text_word}")

    def get_text_with_replace(self, locator, what_to_replace, replaced):
        text_word = locator.text
        text_word_rep = text_word.replace(f'{what_to_replace}', f'{replaced}')
        print(f"{text_word_rep}")

    """Method assert words"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f"GOOD VALUE WORLD: {value_word} CORRESPOND {result}")

    def assert_two_phrases(self, word, result):
        assert word == result
        print(f"GOOD VALUE WORLD: {word} CORRESPOND {result}")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"GOOD VALUE URL {get_url} CORRESPOND {result}")

    def get_param_url(self, param: str):
        self.driver.get(self.driver.current_url + param)
        print(f"TRANSFER TO {self.driver.current_url}")

    """Method screen shot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'SHOT ' + now_date + '.png'
        self.driver.save_screenshot('/Users/alexanderlevkin/Desktop/LESSONS/pythonProject/SCREEN/' + name_screenshot)
