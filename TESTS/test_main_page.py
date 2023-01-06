import time

import pytest

from PAGES.apple_filter_page import AppleFilterPage
from PAGES.cart_page import CartPage
from PAGES.catalog_page import CatalogPage
from PAGES.main_page import MainPage
from conftest import brows


# def test_enter_to_account(brows):
#     MainPage(brows).enter_to_account()


def test_select_items_and_add_to_cart(brows):
    CatalogPage(brows).catalog_actions()
    AppleFilterPage(brows).apple_filter_actions()
    CartPage(brows).cart_actions()

