import allure
from playwright.sync_api import Page, expect
from enums.error_enums import ErrorMessage


class BasePage:
    PAGE_URL = None
    BUTTON_HOME = '//a[@routerlink="home"]'
    PUSH = '//span[@class="mat-simple-snack-bar-content"]'
    PUSH_OK = '//button[@class="mat-focus-indicator mat-button mat-button-base"]'
    PUSH_ADD_ITEM_MESSAGE = '1 item added to cart.'
    PUSH_DELETE_ITEM_MESSAGE = '1 item removed from cart.'
    PUSH_DELETE_ALL = 'Cart is cleared.'

    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    @allure.step('Open URL')
    def open(self):
        self.page.goto(self.PAGE_URL)
        self.page.wait_for_load_state('load', timeout=10000)

    @allure.step('Check is opened URL')
    def is_opened(self):
        self.expect(self.page).to_have_url(self.PAGE_URL)

    @allure.step('Refresh page')
    def refresh(self):
        self.page.reload()
        self.page.wait_for_load_state('load')

    @allure.step('Click button home')
    def button_home_click(self):
        self.page.locator(self.BUTTON_HOME).click()

    @allure.step('Push notification add item to cart')
    def push_add_item(self):
        push = self.page.locator(self.PUSH)
        assert push.inner_text() == self.PUSH_ADD_ITEM_MESSAGE, ErrorMessage.ERROR_PUSH_MESSAGE
        self.page.locator(self.PUSH_OK).click()
        self.expect(push).to_be_hidden()

    @allure.step('Push notification to remove an item from cart')
    def push_delete_item(self):
        push = self.page.locator(self.PUSH)
        assert push.inner_text() == self.PUSH_DELETE_ITEM_MESSAGE, ErrorMessage.ERROR_PUSH_MESSAGE
        self.page.locator(self.PUSH_OK).click()
        self.expect(push).to_be_hidden()

    @allure.step('Push notification to clear the cart')
    def push_all_delete(self):
        push = self.page.locator(self.PUSH)
        assert push.inner_text() == self.PUSH_DELETE_ALL, ErrorMessage.ERROR_PUSH_MESSAGE
        self.page.locator(self.PUSH_OK).click()
        self.expect(push).to_be_hidden()

