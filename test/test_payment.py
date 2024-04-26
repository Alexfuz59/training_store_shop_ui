import allure
import pytest
from enums.error_enums import ErrorMessage
from base.base_test import BaseTest


@allure.feature("Order payment")
class TestPayment(BaseTest):
    @pytest.mark.parametrize("add_product_to_cart", [1], indirect=True)
    @allure.title("Go back to the store")
    def test_back_to_store(self, proceed_to_payment):
        self.payment.button_back_click()
        self.payment.button_start_shopping()
        self.catalog.is_opened()

    @allure.title("Transfer total price from cart to payment")
    def test_transfer_price_cart_in_payment(self, add_product_to_cart):
        total_product_posit_cart = self.shopping_cart.total_product_positions()
        total_all_price_cart = self.shopping_cart.total_all_price()
        self.shopping_cart.button_proceed_to_checkout_click()
        self.payment.click_button_all_products()
        total_product_posit_pay = self.payment.total_product_positions_payment()
        total_all_price_pay = self.payment.total_all_price_payment()
        delivery = self.payment.cost_delivery()
        assert total_product_posit_cart == total_product_posit_pay, ErrorMessage.ERROR_POSITIONS
        assert total_all_price_cart == total_all_price_pay + delivery, ErrorMessage.ERROR_TOTAL_PRICE

    @allure.title("Price check with paid shipping")
    def test_price_cart_in_payment_delivery_paid(self, add_product_to_cart):
        total_product_posit_cart = self.shopping_cart.total_product_positions()
        total_all_price_cart = self.shopping_cart.total_all_price()
        self.shopping_cart.button_proceed_to_checkout_click()
        self.payment.click_paid_shipping()
        self.payment.click_button_all_products()
        total_product_posit_pay = self.payment.total_product_positions_payment()
        total_all_price_pay = self.payment.total_all_price_payment()
        delivery = self.payment.cost_delivery()
        assert delivery == 15.00
        assert total_product_posit_cart == total_product_posit_pay, ErrorMessage.ERROR_POSITIONS
        assert total_all_price_cart == total_all_price_pay - delivery, ErrorMessage.ERROR_TOTAL_PRICE

    @pytest.mark.parametrize("add_product_to_cart", [1], indirect=True)
    @allure.title("Checking successful payment")
    def test_successful_completion_delivery_data(self, proceed_to_payment):
        self.payment.set_email()
        self.payment.set_name()
        self.payment.click_button_manual_address()
        self.payment.select_country_usa()
        self.payment.set_address()
        self.payment.set_city()
        self.payment.set_postcode()
        self.payment.set_state()
        self.payment.check_free_shipping()
        self.payment.modal_window_close()
        self.payment.set_card()
        self.payment.set_date_card()
        self.payment.set_cvc_card()
        self.payment.check_address_matches()
        self.payment.check_state_button_submit()
        self.payment.modal_window_close()
        self.payment.click_button_submit()
        self.payment.payment_completed_successful()

