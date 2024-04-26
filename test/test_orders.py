import allure
import pytest
from base.base_test import BaseTest
from enums.error_enums import ErrorMessage


@allure.feature("Order history")
class TestOrdersHistory(BaseTest):
    @pytest.mark.parametrize("add_product_to_cart", [2], indirect=True)
    @allure.title("Delete order")
    def test_delete_orders(self, proceed_to_payment):
        self.orders.open()
        self.orders.is_opened()
        before_orders = self.orders.total_orders()
        self.orders.delete_order()
        self.orders.refresh()
        after_orders = self.orders.total_orders()
        assert before_orders == after_orders + 1, ErrorMessage.ERROR_DELETE_ORDER

    @pytest.mark.parametrize("add_product_to_cart", [1], indirect=True)
    @allure.title("Change order status")
    def test_update_status_orders(self, proceed_to_payment):
        self.orders.open()
        self.orders.is_opened()
        before_status = self.orders.status_order()
        self.orders.update_status_order()
        self.orders.choice_update_status_order()
        self.orders.refresh()
        after_status = self.orders.status_order()
        assert before_status != after_status, ErrorMessage.ERROR_STATUS_ORDER