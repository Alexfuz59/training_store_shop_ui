import pytest
import allure
from base.base_test import BaseTest
from enums.error_enums import ErrorMessage


@allure.feature("Shopping cart")
class TestShoppingCart(BaseTest):

    @pytest.fixture()
    def add_item_cart_plus(self, add_product_to_cart):
        self.shopping_cart.button_plus_click()

    @allure.title("Home button check")
    def test_home_button(self):
        self.shopping_cart.open()
        self.shopping_cart.is_opened()
        self.shopping_cart.button_home_click()
        self.catalog.is_opened()

    @allure.title("Checking the start button in an empty shopping cart")
    def test_empty_cart(self):
        self.shopping_cart.open()
        self.shopping_cart.is_opened()
        self.shopping_cart.button_empty_cart_click()
        self.catalog.is_opened()

    @pytest.mark.parametrize("add_product_to_cart", [1], indirect=True)
    @allure.title("Checking continue shopping button")
    def test_continue_shopping(self, add_product_to_cart):
        self.shopping_cart.is_opened()
        self.shopping_cart.button_continue_shopping_click()
        self.catalog.is_opened()

    @allure.title("Delete item from cart")
    def test_delete_items(self, add_product_to_cart):
        self.shopping_cart.is_opened()
        total_items_before = self.shopping_cart.total_product_positions()
        self.shopping_cart.button_delete_item_product_click()
        total_items_after = self.shopping_cart.total_product_positions()
        assert total_items_before == total_items_after + 1, ErrorMessage.ERROR_TOTAL_ITEMS

    @allure.title("Delete all items from the cart")
    def test_delete_all_cart(self, add_product_to_cart):
        self.shopping_cart.is_opened()
        total_items_before = self.shopping_cart.number_items_cart()
        self.shopping_cart.button_delete_all_product_click()
        total_items_after = self.shopping_cart.number_items_cart()
        assert total_items_before != 0, ErrorMessage.ERROR_TOTAL_ITEMS
        assert total_items_after == 0, ErrorMessage.ERROR_TOTAL_ITEMS

    @allure.title("+1 item in shopping cart")
    def test_add_item_via_plus(self, add_product_to_cart):
        self.shopping_cart.is_opened()
        total_items_before = self.shopping_cart.number_items_cart()
        price_item_before = self.shopping_cart.price_item()
        total_price_item_before = self.shopping_cart.total_price_item()
        total_quantity_before = self.shopping_cart.total_quantity()
        total_product_posit_before = self.shopping_cart.total_product_positions()
        total_all_price_before = self.shopping_cart.total_all_price()
        self.shopping_cart.button_plus_click()
        total_items_after = self.shopping_cart.number_items_cart()
        price_item_after = self.shopping_cart.price_item()
        total_price_item_after = self.shopping_cart.total_price_item()
        total_quantity_after = self.shopping_cart.total_quantity()
        total_all_price_after = self.shopping_cart.total_all_price()
        total_product_posit_after = self.shopping_cart.total_product_positions()
        assert total_items_before + 1 == total_items_after, ErrorMessage.ERROR_TOTAL_ITEMS
        assert price_item_before == price_item_after, ErrorMessage.ERROR_PRICE_ITEM
        assert total_price_item_before == total_price_item_after, ErrorMessage.ERROR_PRICE_PER_PIECE
        assert total_product_posit_before == total_product_posit_after, ErrorMessage.ERROR_POSITIONS
        assert total_all_price_before + price_item_before == total_all_price_after, ErrorMessage.ERROR_TOTAL_PRICE
        assert total_quantity_before + 1 == total_quantity_after, ErrorMessage.ERROR_TOTAL_ITEMS

    @allure.title("-1 item in shopping cart")
    def test_delete_item_via_minus(self, add_item_cart_plus):
        self.shopping_cart.is_opened()
        total_items_before = self.shopping_cart.number_items_cart()
        price_item_before = self.shopping_cart.price_item()
        total_price_item_before = self.shopping_cart.total_price_item()
        total_quantity_before = self.shopping_cart.total_quantity()
        total_product_posit_before = self.shopping_cart.total_product_positions()
        total_all_price_before = self.shopping_cart.total_all_price()
        self.shopping_cart.button_minus_click()
        total_items_after = self.shopping_cart.number_items_cart()
        price_item_after = self.shopping_cart.price_item()
        total_price_item_after = self.shopping_cart.total_price_item()
        total_quantity_after = self.shopping_cart.total_quantity()
        total_all_price_after = self.shopping_cart.total_all_price()
        total_product_posit_after = self.shopping_cart.total_product_positions()
        assert total_items_before == total_items_after + 1, ErrorMessage.ERROR_TOTAL_ITEMS
        assert price_item_before == price_item_after, ErrorMessage.ERROR_PRICE_ITEM
        assert total_price_item_before == total_price_item_after, ErrorMessage.ERROR_PRICE_PER_PIECE
        assert total_product_posit_before == total_product_posit_after, ErrorMessage.ERROR_POSITIONS
        assert total_all_price_before == total_all_price_after + price_item_before, ErrorMessage.ERROR_TOTAL_PRICE
        assert total_quantity_before == total_quantity_after + 1, ErrorMessage.ERROR_TOTAL_ITEMS

    @pytest.mark.parametrize("add_product_to_cart", [1], indirect=True)
    @allure.title("Proceed to checkout")
    def test_proceed_to_checkout(self, add_product_to_cart):
        self.shopping_cart.is_opened()
        self.shopping_cart.button_proceed_to_checkout_click()
        self.payment.current_url_payment()





