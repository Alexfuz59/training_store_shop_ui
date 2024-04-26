import pytest
import allure
from pages.catalog import Catalog
from pages.shopping_cart import ShoppingCart
from pages.payment import Payment
from playwright.sync_api import Page
from config.environment_allure import EnvironmentAllure


@pytest.fixture(scope="function", autouse=True)
def page(context, request):
    page: Page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        take_screenshot(page, request.node.name)
    page.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@allure.title("Screenshot on error")
def take_screenshot(page, test_name):
    screenshot_name = f"{test_name}.png"
    allure.attach(page.screenshot(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)


@pytest.fixture(params=[1, 5, 10])
def add_product_to_cart(request,  page):
    allure.dynamic.title(f'Add {request.param} items to cart')
    catalog = Catalog(page)
    shopping_cart = ShoppingCart(page)
    catalog.open()
    catalog.is_opened()
    catalog.add_item_to_cart(request.param)
    catalog.open_windows_view_cart()
    catalog.open_shopping_cart()
    shopping_cart.is_opened()


@allure.title("Go to payment")
@pytest.fixture()
def proceed_to_payment(page, add_product_to_cart):
    shopping_cart_page = ShoppingCart(page)
    payment_page = Payment(page)
    shopping_cart_page.button_proceed_to_checkout_click()
    payment_page.current_url_payment()


@allure.title('Creating allure environments')
@pytest.fixture(autouse=True, scope='session')
def environment_allure(browser):
    EnvironmentAllure.create_environment(browser)






