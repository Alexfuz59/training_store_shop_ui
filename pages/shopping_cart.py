import allure
from base.base_page import BasePage
from config.links import Links
from decimal import Decimal


class ShoppingCart(BasePage):
    PAGE_URL = Links.SHOPPING_CART
    ITEMS_IN_CART = '#mat-badge-content-0'
    BUTTON_EMPTY_CART = '//button[@routerlink="/home"]'
    BUTTON_CONTINUE_SHOPPING = '//button[@routerlink="/home"]'
    BUTTON_PROCEED_TO_CHECKOUT = '//button[@color="primary"]'
    BUTTON_DELETE = '//button[@color="warn"]'
    BUTTON_CLEAR_ALL = 'Clear All'
    BUTTON_CLOSE = 'close'
    BUTTON_PLUS_MINUS = '//button[@class="mat-focus-indicator mat-icon-button mat-button-base"]'
    PRISE = '//td[contains(@class, "mat-column-price")]'
    TOTAL = '//td[contains(@class, "mat-column-total")]'
    QUANTITY = '//tbody/tr/td/span'

    @allure.step("Show the number of products in the shopping cart")
    def number_items_cart(self):
        quantity = self.page.locator(self.ITEMS_IN_CART).inner_text()
        return int(quantity)

    @allure.step("Click the button to start shopping")
    def button_empty_cart_click(self):
        self.page.locator(self.BUTTON_EMPTY_CART).click()

    @allure.step("Click the button to start shopping")
    def button_empty_cart_click(self):
        self.page.locator(self.BUTTON_EMPTY_CART).click()

    @allure.step("Click the delete all products button")
    def button_delete_all_product_click(self):
        self.page.locator(self.BUTTON_DELETE).nth(0).click()
        self.push_all_delete()

    @allure.step("Click to delete the product")
    def button_delete_item_product_click(self):
        self.page.locator(self.BUTTON_DELETE).nth(1).click()

    @allure.step("Click the Continue Shopping button")
    def button_continue_shopping_click(self):
        self.page.locator(self.BUTTON_CONTINUE_SHOPPING).click()

    @allure.step("Click the payment button")
    def button_proceed_to_checkout_click(self):
        button = self.page.locator(self.BUTTON_PROCEED_TO_CHECKOUT)
        button.click()
        self.expect(button).to_be_hidden(timeout=10000)
        self.page.wait_for_load_state("load")

    @allure.step("Click plus button")
    def button_plus_click(self):
        self.page.locator(self.BUTTON_PLUS_MINUS).nth(2).click()
        self.push_add_item()

    @allure.step("Click minus button")
    def button_minus_click(self):
        self.page.locator(self.BUTTON_PLUS_MINUS).nth(1).click()
        self.push_delete_item()

    @allure.step("Price per item")
    def price_item(self, itemNumber=0):
        price_str = self.page.locator(self.PRISE).nth(itemNumber).inner_text()
        price = Decimal(price_str.replace('$', ''))
        return price

    @allure.step("Price of the total order")
    def total_all_price(self):
        total_str = self.page.locator(self.TOTAL).last.inner_text()
        total_price = Decimal(total_str.replace('$', '').replace(',', ''))
        return total_price

    @allure.step("Total price per item")
    def total_price_item(self, itemNumber=0):
        total_item_str = self.page.locator(self.PRISE).nth(itemNumber).inner_text()
        total_item = Decimal(total_item_str.replace('$', ''))
        return total_item

    @allure.step("Number of product positions")
    def total_product_positions(self):
        positions = self.page.locator(self.QUANTITY).count()
        return positions

    @allure.step("Total goods in the order")
    def total_quantity(self):
        positions = self.total_product_positions()
        quantity_total = 0
        for item in range(0, positions):
            quantity = int(self.page.locator(self.QUANTITY).nth(item).inner_text())
            quantity_total += quantity
        return quantity_total


