import time

from PAGES.main_page import MainPage
from conftest import brows


def test_enter_to_account(brows):
    MainPage(brows).enter_to_account()




