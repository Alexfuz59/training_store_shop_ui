import allure
from base.base_page import BasePage
from config.links import Links
from random import randrange
from playwright.sync_api import Route
from enums.error_enums import ErrorMessage


class Catalog(BasePage):
    PAGE_URL = Links.CATALOG_PAGE
    BUTTON_SORTING = '.mat-button-wrapper'
    BUTTON_ASC = 'asc'
    BUTTON_DESC = 'desc'
    LIST_ELEMENTS_PRICE = '.text-red-400'
    SHOW = '//button[@aria-haspopup="menu"]'
    BUTTON_SHOW12 = '12'
    BUTTON_SHOW24 = '24'
    BUTTON_SHOW36 = '36'
    MENU_SHOW = '//div[@class="mat-menu-content ng-tns-c61-3"]'
    ITEMS = '.mat-grid-tile.ng-star-inserted'
    BUTTON_CATEGORIES = '#mat-expansion-panel-header-0'
    BUTTON_OPTIONS_CATEGORIES = '//mat-list-option[contains(@role, "option")]'
    CATEGORIE = '//h5'
    VIEW_LIST = 'view_list'
    VIEW_MODULE = 'view_module'
    VIEW_COMFY = 'view_comfy'
    GRID_LIST = '.mat-grid-list.ng-star-inserted'
    BUTTON_WINDOWS_VIEW_CART = '//mat-icon[@matbadgecolor="warn"]'
    WINDOWS_VIEW_CART = '//div[@id="mat-menu-panel-0"]'
    BUTTON_DELETE_VIEW_CART = '.bg-rose-600.text-white.rounded-full.w-9.h-9'
    OPEN_SHOPPING_CART = '//button[@routerlink="cart"]'
    BUTTON_ADD_ITEM = '//mat-icon[contains(@class, "text-gray-500")]'
    BUTTON_SHOW_MENUITEM = '//button[@role="menuitem"]'
    ADD_ITEMS = '//mat-grid-tile[@class="mat-grid-tile ng-star-inserted"]'
    PRICE = '//span[@class="text-red-400"]'

    @allure.step("Click the sort button")
    def button_sorting_click(self):
        self.page.locator(self.BUTTON_SORTING).nth(2).click()

    @allure.step("Click the sort in ascending order button")
    def button_asc_click(self):
        self.page.get_by_text(self.BUTTON_ASC).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click the sort by descending button")
    def button_desc_click(self):
        self.page.get_by_text(self.BUTTON_DESC).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Generate list of prices")
    def list_prices(self):
        elements_prices = self.page.locator(self.LIST_ELEMENTS_PRICE).all_inner_texts()
        list_price = [float(item.replace('$', '')) for item in elements_prices]
        return list_price

    @allure.step("Click the show button")
    def button_show_click(self):
        self.page.locator(self.SHOW).last.click()
        self.expect(self.page.locator(self.MENU_SHOW)).to_be_visible()

    @allure.step("Click button show by 12")
    def button_show12_click(self):
        self.page.get_by_text(self.BUTTON_SHOW12)\
            .and_(self.page.locator(self.BUTTON_SHOW_MENUITEM)).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click button show by 24")
    def button_show24_click(self):
        self.page.get_by_text(self.BUTTON_SHOW24)\
            .and_(self.page.locator(self.BUTTON_SHOW_MENUITEM)).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click button show by 36")
    def button_show36_click(self):
        self.page.get_by_text(self.BUTTON_SHOW36)\
            .and_(self.page.locator(self.BUTTON_SHOW_MENUITEM)).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Number of products on the page")
    def product_count(self):
        product_count = self.page.locator(self.ITEMS).count()
        return product_count

    @allure.step('Checking the quantity of goods on the page')
    def check_show(self, lenItems):
        try:
            self.expect(self.page.locator(self.ITEMS)).to_have_count(lenItems)
        except AssertionError:
            len_list = self.product_count()
            raise AssertionError(ErrorMessage.ERROR_SHOW(len_list))

    @allure.step("Click the Categories button")
    def button_categories_click(self):
        self.page.locator(self.BUTTON_CATEGORIES).click()

    @allure.step("Click the Electronics button")
    def button_electronics_click(self):
        self.page.locator(self.BUTTON_OPTIONS_CATEGORIES).nth(0).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click the Jewelery button")
    def button_jewelery_click(self):
        self.page.locator(self.BUTTON_OPTIONS_CATEGORIES).nth(1).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click the Men clothing button")
    def button_men_clothing_click(self):
        self.page.locator(self.BUTTON_OPTIONS_CATEGORIES).nth(2).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Click the Women clothing button")
    def button_women_clothing_click(self):
        self.page.locator(self.BUTTON_OPTIONS_CATEGORIES).nth(3).click()
        self.page.wait_for_load_state("networkidle")

    @allure.step('List of categories on the page')
    def categorie(self):
        list_categories = self.page.locator(self.CATEGORIE).all_inner_texts()
        return set(list_categories)

    @allure.step("Click button view list")
    def button_view_list_click(self):
        self.page.get_by_text(self.VIEW_LIST).click()

    @allure.step("Click button view grid 3 products")
    def button_view_grid_3products_click(self):
        self.page.get_by_text(self.VIEW_MODULE).click()

    @allure.step("Click button view grid 4 products")
    def button_view_grid_4products_click(self):
        self.page.get_by_text(self.VIEW_COMFY).click()

    @allure.step("Check grid on page")
    def check_cols(self, col):
        locatorGL = self.page.locator(self.GRID_LIST)
        self.expect(locatorGL, ErrorMessage.ERROR_GRID).to_have_attribute("cols", f'{col}')

    @allure.step("Open the cart view window")
    def open_windows_view_cart(self):
        self.page.locator(self.BUTTON_WINDOWS_VIEW_CART).click()
        view_cart = self.page.locator(self.WINDOWS_VIEW_CART)
        self.expect(view_cart).to_be_visible()

    @allure.step("Open shopping cart")
    def open_shopping_cart(self):
        self.page.locator(self.OPEN_SHOPPING_CART).click()
        self.expect(self.page).to_have_url(Links.SHOPPING_CART)

    @allure.step("Click delete item in cart view window")
    def button_delete_items(self):
        self.page.locator(self.BUTTON_DELETE_VIEW_CART).click()

    @allure.step("Add items to cart")
    def add_item_to_cart(self, quantity=1):
        self.page.wait_for_load_state("networkidle")
        amount_of_elem = self.product_count()
        for i in range(quantity):
            number_item = randrange(0, amount_of_elem - 1)
            self.page.locator(self.BUTTON_ADD_ITEM).nth(number_item).click()
            self.page.wait_for_selector(self.PUSH)
            self.push_add_item()

    @allure.step("Product price substitution")
    def substitution_price(self):
        def handle_route(route: Route):
            response = route.fetch()
            json = response.json()
            len_price = len(json)
            for i in range(0, len_price):
                json[i]['price'] = 10000
            route.fulfill(json=json)
        self.page.route("**/products?sort=desc&limit=12", handle_route)

    @allure.step("Checking the substituted price")
    def check_substitution_price(self):
        amount_of_elem = self.product_count()
        for i in range(0, amount_of_elem):
            price_str = self.page.locator(self.PRICE).nth(i).inner_text()
            price = float(price_str.replace('$', '').replace(',', ''))
            assert price == 10000, ErrorMessage.ERROR_PRICE_ITEM







