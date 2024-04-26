import pytest
from playwright.sync_api import Page
from pages.catalog import Catalog
from pages.shopping_cart import ShoppingCart
from pages.orders import OrdersHistory
from pages.payment import Payment


class BaseTest:

    catalog: Catalog
    shopping_cart: ShoppingCart
    orders: OrdersHistory
    payment: Payment

    @pytest.fixture(autouse=True)
    def setup(self, request, page: Page):
        request.cls.catalog = Catalog(page)
        request.cls.shopping_cart = ShoppingCart(page)
        request.cls.orders = OrdersHistory(page)
        request.cls.payment = Payment(page)

