
from PAGES.main_page import MainPage
from conftest import driver


def test_login_page(driver):
    ac = MainPage(driver=driver)
    ac.enter_to_account(email='alexanlevkin@gmail.com', password='85d8ce47')