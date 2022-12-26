import time

from PAGES.main_page import MainPage
from conftest import brows


def test_ghj(brows):

    MainPage(brows).enter_to_account()
    time.sleep(2)




