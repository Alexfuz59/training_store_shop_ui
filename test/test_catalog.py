import allure
import pytest
from base.base_test import BaseTest
from enums.error_enums import ErrorMessage


@allure.feature("Product catalog")
class TestCatalogPrice(BaseTest):

    @pytest.mark.parametrize('quantityAdd', [1, 2, 10])
    def test_add_item_to_cart(self, quantityAdd):
        allure.dynamic.title(f'Add {quantityAdd} items to cart')
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.add_item_to_cart(quantityAdd)
        self.catalog.open_windows_view_cart()
        self.catalog.open_shopping_cart()
        productCarte = self.shopping_cart.number_items_cart()
        assert quantityAdd == productCarte, ErrorMessage.INCORRECT_QUANTITY_ITEMS_CART

    @pytest.mark.run(order=-1)
    @allure.title("Price substitution")
    def test_price_list_substitution(self):
        self.catalog.substitution_price()
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.check_substitution_price()

    @allure.title("Sorting in ascending order")
    def test_sort_asc(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_sorting_click()
        self.catalog.button_asc_click()
        list_prices = self.catalog.list_prices()
        assert list_prices == sorted(list_prices), ErrorMessage.ERROR_SORTING_ASC

    @allure.title("Sorting in descending order")
    def test_sort_desc(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_sorting_click()
        self.catalog.button_asc_click()
        self.catalog.button_sorting_click()
        self.catalog.button_desc_click()
        list_prices = self.catalog.list_prices()
        assert list_prices == sorted(list_prices, reverse=True), ErrorMessage.ERROR_SORTING_DESC

    @allure.title("Show 12 products per page")
    def test_show12(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_show_click()
        self.catalog.button_show24_click()
        self.catalog.button_show_click()
        self.catalog.button_show12_click()
        self.catalog.check_show(12)

    @allure.title("Show 24 products per page")
    def test_show24(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_show_click()
        self.catalog.button_show24_click()
        self.catalog.check_show(24)

    @allure.title("Show 36 products per page")
    def test_show36(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_show_click()
        self.catalog.button_show36_click()
        self.catalog.check_show(36)

    @allure.title("Showing items from category Electronics")
    def test_categories_electronics(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_categories_click()
        self.catalog.button_electronics_click()
        categorie = self.catalog.categorie()
        assert len(categorie) == 1
        assert 'electronics' in categorie, ErrorMessage.ERROR_CATEGORY

    @allure.title("Showing items from category Jewelery")
    def test_categories_jewelery(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_categories_click()
        self.catalog.button_jewelery_click()
        categorie = self.catalog.categorie()
        assert len(categorie) == 1
        assert 'jewelery' in categorie, ErrorMessage.ERROR_CATEGORY

    @allure.title("Showing items from category Men clothing")
    def test_categories_men_clothing(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_categories_click()
        self.catalog.button_men_clothing_click()
        categorie = self.catalog.categorie()
        assert len(categorie) == 1
        assert "men's clothing" in categorie, ErrorMessage.ERROR_CATEGORY

    @allure.title("Showing items from category Women clothing")
    def test_categories_women_clothing(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_categories_click()
        self.catalog.button_women_clothing_click()
        categorie = self.catalog.categorie()
        assert len(categorie) == 1
        assert "women's clothing" in categorie, ErrorMessage.ERROR_CATEGORY

    @allure.title("Show items in the list view")
    def test_view_list_catalog(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_view_list_click()
        self.catalog.check_cols(1)

    @allure.title("Show items in a grid of 3")
    def test_view_grid_catalog_3product(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_view_grid_3products_click()
        self.catalog.check_cols(3)

    @allure.title("Show items in a grid of 4")
    def test_view_grid_catalog_4product(self):
        self.catalog.open()
        self.catalog.is_opened()
        self.catalog.button_view_grid_4products_click()
        self.catalog.check_cols(4)






