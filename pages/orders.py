import allure
from base.base_page import BasePage
from config.links import Links


class OrdersHistory(BasePage):
    PAGE_URL = Links.ORDERS_PAGE
    BUTTON_EDIT_STATUS = 'edit'
    BUTTON_EDIT_STATUS_XPATH = '//mat-icon[@data-mat-icon-type="font"]'
    STATUS_ORDER = '//tbody/tr/td/span'
    BUTTON_EDIT_MENUITEM = '//button[@role="menuitem"]'
    DELETE_ORDER = '//button[@color="warn"]'
    ORDER = '//tr[@class="mat-row cdk-row ng-star-inserted"]'
    CODE_ORDER = '//td[contains(@class, "cdk-column-payment_key")]'

    @allure.step("Button to change order status")
    def update_status_order(self, orderNumber=0):
        self.page.get_by_text(self.BUTTON_EDIT_STATUS).nth(orderNumber)\
            .and_(self.page.locator(self.BUTTON_EDIT_STATUS_XPATH)).click()

    @allure.step("Show order status")
    def status_order(self, orderNumber=0):
        status = self.page.locator(self.STATUS_ORDER).nth(orderNumber).inner_text()
        return status

    @allure.step("Selection paid/created")
    def choice_update_status_order(self):
        self.page.locator(self.BUTTON_EDIT_MENUITEM).click()

    @allure.step("Delete order")
    def delete_order(self, orderNumber=0):
        code = self.order_code(orderNumber)
        self.page.locator(self.DELETE_ORDER).nth(orderNumber).click()
        self.expect(self.page.get_by_text(code)).to_be_hidden()

    @allure.step("Total orders in order history")
    def total_orders(self):
        total = self.page.locator(self.ORDER).count()
        return total

    @allure.step("Order code")
    def order_code(self, orderNumber=0):
        code = self.page.locator(self.CODE_ORDER).nth(orderNumber).inner_text()
        return code