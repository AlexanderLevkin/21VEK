from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Collection of actions"""

    def verify_link_text_presence(self, link_text):
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    def verify_element_present(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def element(self, locator: tuple):
        return self.verify_element_present(locator)

    def click_element(self, element):
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def simple_click_element(self, element):
        element.click()

    def click(self, locator: tuple):
        element = self.element(locator)
        ActionChains(self.driver).pause(0.3).move_to_element(element).click().perform()

    def click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self.click_element(element)

    def click_link(self, link_text):
        self.click((By.LINK_TEXT, link_text))
        return self

    def get_param_url(self, param: str):
        self.driver.get(self.driver.url + param)

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
