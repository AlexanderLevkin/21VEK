import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])


url = "https://www.21vek.by/"


@pytest.fixture
def driver():
    print("START TEST")
    url1 = "https://www.21vek.by/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url1)
    driver.maximize_window()
    yield
    print("Finish TEST")
    return driver
