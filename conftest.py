import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
@pytest.fixture
def brows():
    print("START TEST")
    url1 = "https://www.21vek.by/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url1)
    driver.maximize_window()
    yield
    print("FINISH TEST")
    return driver
