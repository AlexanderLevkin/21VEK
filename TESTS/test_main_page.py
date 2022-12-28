import time

import pytest

from PAGES.catalog_page import FilterPage
from PAGES.main_page import MainPage
from conftest import brows


def test_enter_to_account(brows):
    MainPage(brows).enter_to_account()
    # FilterPage(brows).catalog_actions()

