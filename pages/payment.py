import allure
import os
from base.base_page import BasePage
from faker import Faker
from random import choice
from config.links import Links
from enums.error_enums import ErrorMessage
from dotenv import load_dotenv
from decimal import Decimal

fake = Faker()
load_dotenv()


class Payment(BasePage):
    BUTTON_BACK = '//div[@class="flex-container align-items-center"]'
    BUTTON_START_SHOPPING = '//button[text()="Start shopping"]'
    INPUT_EMAIL = '#email'
    INPUT_NAME = '#shippingName'
    INPUT_ADDRESS1 = '#shippingAddressLine1'
    INPUT_CITY = '#shippingLocality'
    INPUT_POSTAL_CODE = '#shippingPostalCode'
    INPUT_CARD_NUMBER = '#cardNumber'
    INPUT_CARD_CVC = '#cardCvc'
    INPUT_CARD_EXPIRY = '#cardExpiry'
    DROPDOWN_COUNTRY = "#shippingCountry"
    DROPDOWN_STATE = '#shippingAdministrativeArea'
    BUTTON_MANUAL_ADDRESS_ENTRY = '//div[@class="flex-container justify-content-center align-items-center"]'
    RADIOBUTTON_FREE_SHIPPING = '//input[@name="shipping-rate"]'
    RADIOBUTTON_PAID_SHIPPING = '//input[@name="shipping-rate"]'
    CHECKBOX_SHIPPING_AS_BILLING = "#cardUseShippingAsBilling"
    BUTTON_SUBMIT = '//div[@class="SubmitButton-IconContainer"]'
    CURRENCY = '//span[@class="CurrencyAmount"]'
    QUANTITY_ITEM_PAYMENT = '//li[@class="OrderDetails-item"]'
    DELIVERY_PRICE = '//span[@class="Text Text-color--gray400 Text-fontSize--14 Text--tabularNumbers"]'
    BUTTON_ALL_ELEMENTS = '//button[@class="Button OrderDetails-showHideButton Button--link Button--sm"]'
    MENU_ALL_ELEMENTS = '//section[@class="OrderDetails App-Overview-OrderDetails my6 is-expanded"]'
    MODAL_WINDOW = '//div[contains(@class, "ModalContent--afterOpen")]'
    BUTTON_CLOSE_MODAL = '//button[@class="Button Button--secondary Button--md Button--fullWidth"]'
    BUTTON_CLOSE_MODAL_LINUX = '//button[@class="Button LearnMoreInfoModalContentV2-header-closeButton Button--link Button--md"]'

    EMAIL = fake.ascii_free_email()
    NAME = fake.name()
    STATE = fake.state()
    ADDRESS = fake.street_address()
    CITY = fake.city()
    INDEX = fake.postcode()
    CARD = os.getenv('CARD')
    DATE = fake.credit_card_expire()
    CVC = fake.credit_card_security_code()

    @allure.step("Checking the site payment domain")
    def current_url_payment(self):
        self.page.wait_for_load_state('load', timeout=10000)
        assert 'checkout.stripe.com' in self.page.url

    @allure.step("Click the back button")
    def button_back_click(self):
        button = self.page.locator(self.BUTTON_BACK)
        button.hover()
        button.click()

    @allure.step("Click the start shopping button")
    def button_start_shopping(self):
        self.page.locator(self.BUTTON_START_SHOPPING).click()

    @allure.step("Set email")
    def set_email(self):
        self.page.locator(self.INPUT_EMAIL).fill(self.EMAIL)

    @allure.step("Set name")
    def set_name(self):
        self.page.locator(self.INPUT_NAME).fill(self.NAME)

    @allure.step("Set country usa")
    def select_country_usa(self):
        self.page.locator(self.DROPDOWN_COUNTRY).select_option(value='US')

    @allure.step("Click the button to enter an address manually")
    def click_button_manual_address(self):
        self.page.locator(self.BUTTON_MANUAL_ADDRESS_ENTRY).last.click()

    @allure.step("Set address")
    def set_address(self):
        self.page.locator(self.INPUT_ADDRESS1).fill(self.ADDRESS)

    @allure.step("Set city")
    def set_city(self):
        self.page.locator(self.INPUT_CITY).fill(self.CITY)

    @allure.step("Set postcode")
    def set_postcode(self):
        self.page.locator(self.INPUT_POSTAL_CODE).fill(self.INDEX)

    @allure.step("Set card")
    def set_card(self):
        self.page.locator(self.INPUT_CARD_NUMBER).fill(self.CARD)

    @allure.step("Set date card")
    def set_date_card(self):
        self.page.locator(self.INPUT_CARD_EXPIRY).fill(self.DATE)

    @allure.step("Set cvc card")
    def set_cvc_card(self):
        self.page.locator(self.INPUT_CARD_CVC).fill(self.CVC)

    @allure.step("Set state")
    def set_state(self):
        options = self.page.query_selector(self.DROPDOWN_STATE)\
            .eval_on_selector_all('option', 'elements => elements.map(e => e.textContent)')
        self.page.locator(self.DROPDOWN_STATE).select_option(f'{choice(options)}')

    @allure.step("Click button submit")
    def click_button_submit(self):
        self.page.locator(self.BUTTON_SUBMIT).click()

    @allure.step("Click button all products")
    def click_button_all_products(self):
        button = self.page.locator(self.BUTTON_ALL_ELEMENTS)
        if button.is_visible():
            button.click()
            self.expect(self.page.locator(self.MENU_ALL_ELEMENTS)).to_be_visible()
        else:
            pass

    @allure.step("Number of product positions in payment")
    def total_product_positions_payment(self):
        self.expect(self.page.locator(self.QUANTITY_ITEM_PAYMENT).first).to_be_visible()
        positions = self.page.locator(self.QUANTITY_ITEM_PAYMENT).count()
        return positions

    @allure.step("Price of the total order in payment")
    def total_all_price_payment(self):
        total = self.page.locator(self.CURRENCY).first
        self.expect(total).to_be_visible()
        total_str = total.inner_text()
        total_price = Decimal(total_str.replace('$', '')\
                            .replace(',', '')\
                            .replace('\xa0', ''))
        return total_price

    @allure.step("Delivery price")
    def cost_delivery(self):
        free_shipping = self.page.locator(self.RADIOBUTTON_FREE_SHIPPING).nth(0)
        paid_shipping = self.page.locator(self.RADIOBUTTON_PAID_SHIPPING).nth(1)
        if free_shipping.is_checked():
            price = self.page.locator(self.DELIVERY_PRICE).inner_text()
            assert price == 'Free'
            return 0
        elif paid_shipping.is_checked():
            len_price = self.page.locator(self.CURRENCY).count()
            price_str = self.page.locator(self.CURRENCY).nth(len_price - 3).inner_text()
            price = Decimal(price_str.replace('$', '') \
                          .replace(',', '.') \
                          .replace('\xa0', ''))
            return price
        else:
            raise AssertionError('Broken delivery payment')

    @allure.step("Click radio button paid shipping")
    def click_paid_shipping(self):
        self.page.locator(self.RADIOBUTTON_PAID_SHIPPING).nth(1).click()
        self.page.wait_for_load_state("load")

    @allure.step("Checking for free delivery")
    def check_free_shipping(self):
        free_shipping = self.page.locator(self.RADIOBUTTON_FREE_SHIPPING).nth(0)
        assert free_shipping.is_checked()

    @allure.step("Сheck address matches")
    def check_address_matches(self):
        checkbox = self.page.locator(self.CHECKBOX_SHIPPING_AS_BILLING)
        assert checkbox.is_checked()

    @allure.step("Check submit button is inactive")
    def check_state_button_submit(self):
        button = self.page.locator(self.BUTTON_SUBMIT)
        self.expect(button).to_be_enabled()

    @allure.step("Checking successful payment")
    def payment_completed_successful(self):
        self.expect(self.page, ErrorMessage.ERROR_URL). \
            to_have_url(Links.PAYMENT_COMPLETED, timeout=10000)

    @allure.step("Close modal window")
    def modal_window_close(self):
        try:
            modal = self.page.locator(self.MODAL_WINDOW)
            self.expect(modal).to_be_visible()
            if modal.is_visible():
                button = self.page.locator(self.BUTTON_CLOSE_MODAL_LINUX)
                button.click()
                self.expect(button).to_be_hidden()
        except AssertionError:
            pass
