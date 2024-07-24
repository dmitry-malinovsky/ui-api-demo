from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import logging

from features.page_objects.base_page_object import BasePageObject

logger = logging.getLogger(__name__)


class NavigationModule(BasePageObject):
    def navigate_through_menu(self, *menu_items):
        for item in menu_items:
            menu_element = self.browser.find_element(By.XPATH, f'//*[text() = "{item}"]')
            self.actions.move_to_element(menu_element).perform()
        self.actions.click().perform()


class LoginPage(BasePageObject):
    URL = "https://magento.softwaretestingboard.com/customer/account/login/"

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "send2")

    def load(self):
        self.browser.get(self.URL)

    def set_email(self, email: str):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        logger.info(f'Set email: {email}')

    def set_password(self, password: str):
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        logger.info(f'Set password')

    def click_login(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        logger.info('Clicked login button')


class HomePage(BasePageObject):
    URL = "https://magento.softwaretestingboard.com/customer/account/"

    def load(self):
        self.browser.get(self.URL)

    def is_at_home_page(self):
        return self.browser.current_url == self.URL


class ProductsPage(BasePageObject):
    PRODUCTS = (By.XPATH, '//li[contains(@class, "product-item")]//a[@class="product-item-link"]')
    SEARCH_BOX = (By.ID, 'search')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.product-item .product-item-link')

    def search_item(self, item_name: str):
        search_box = self.browser.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(item_name)
        search_box.send_keys(Keys.RETURN)

    def click_search_result(self, item_name: str):
        results = self.browser.find_elements(*self.SEARCH_RESULTS)
        for result in results:
            if item_name in result.text:
                result.click()
                break

    def get_all_items(self):
        items = self.browser.find_elements(*self.PRODUCTS)
        return items

    def click_item_by_text(self, item_text):
        print(item_text)
        items = self.get_all_items()
        for item in items:
            if item_text in item.text:
                print("Test was found")
                item.click()
                break


class ProductPage(BasePageObject):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'span[itemprop="name"]')
    PRODUCT_PRICE = (By.XPATH, '//meta[@itemprop="price"]')
    ADD_TO_CART_BUTTON = (By.ID, 'product-addtocart-button')
    SIZE_OPTIONS = (By.XPATH, '//div[@class="swatch-attribute size"]/div/div')
    COLOR_OPTIONS = (By.XPATH, '//div[@class="swatch-attribute color"]/div/div')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.message-success')
    BASKET_ICON = (By.CSS_SELECTOR, 'a.action.showcart')
    PROCEED_TO_CHECKOUT_BUTTON = (By.ID, 'top-cart-btn-checkout')

    def get_product_title(self):
        return self.browser.find_element(*self.PRODUCT_TITLE).text

    def get_raw_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def get_float_product_price(self):
        price_meta_element = self.browser.find_element(*self.PRODUCT_PRICE)
        price_text = price_meta_element.get_attribute("content")
        if price_text:
            return float(price_text)
        raise ValueError("Price not found or invalid format")

    def select_size(self, size):
        sizes = self.browser.find_elements(*self.SIZE_OPTIONS)
        for size_option in sizes:
            if size_option.text == size:
                size_option.click()
                break

    def select_color(self, color):
        colors = self.browser.find_elements(*self.COLOR_OPTIONS)
        for color_option in colors:
            if color_option.get_attribute('aria-label') == color:
                color_option.click()
                break

    def add_to_cart(self):
        self.browser.find_element(*self.ADD_TO_CART_BUTTON).click()
        WebDriverWait(self.browser, 10)

    def get_success_message(self):
        return self.browser.find_element(*self.SUCCESS_MESSAGE).text

    def is_correct_product(self, product_title):
        return self.get_product_title() == product_title

    def click_basket_icon(self):
        self.browser.find_element(*self.BASKET_ICON).click()

    def proceed_to_checkout(self):
        self.browser.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON).click()


class CheckoutPage(BasePageObject):
    FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
    LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
    STREET_ADDRESS = (By.XPATH, '//input[@name="street[0]"]')
    CITY = (By.XPATH, '//input[@name="city"]')
    STATE = (By.XPATH, '//select[@name="region_id"]')
    ZIP_CODE = (By.XPATH, '//input[@name="postcode"]')
    COUNTRY = (By.XPATH, '//select[@name="country_id"]')
    PHONE = (By.XPATH, '//input[@name="telephone"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button.continue')
    CHEAP_DELIVERY = (By.XPATH,"//input[@value='tablerate_bestway']")

    def set_first_name(self, first_name: str):
        field = self.find_element(*self.FIRST_NAME)
        field.clear()
        field.send_keys(first_name)
        logger.info(f'Set first name: {first_name}')

    def set_last_name(self, last_name: str):
        field = self.find_element(*self.LAST_NAME)
        field.clear()
        field.send_keys(last_name)
        logger.info(f'Set last name: {last_name}')

    def set_street_address(self, street_address: str):
        field = self.find_element(*self.STREET_ADDRESS)
        field.clear()
        field.send_keys(street_address)
        logger.info(f'Set street address: {street_address}')

    def set_city(self, city: str):
        field = self.find_element(*self.CITY)
        field.clear()
        field.send_keys(city)
        logger.info(f'Set city: {city}')

    def set_state(self, state: str):
        select_element = self.find_element(*self.STATE)
        select = Select(select_element)
        select.select_by_visible_text(state)
        logger.info(f"Selected region: {state}")

    def set_zip_code(self, zip_code: str):
        field = self.find_element(*self.ZIP_CODE)
        field.clear()
        field.send_keys(zip_code)
        logger.info(f'Set zip code: {zip_code}')

    def set_country(self, country: str):
        select_element = self.find_element(*self.COUNTRY)
        select = Select(select_element)
        select.select_by_visible_text(country)
        logger.info(f"Selected region: {country}")

    def set_phone(self, phone: str):
        field = self.find_element(*self.PHONE)
        field.clear()
        field.send_keys(phone)
        logger.info(f'Set phone: {phone}')

    def select_shipping_method(self, value):
        radio_button = self.find_element(*self.CHEAP_DELIVERY)
        radio_button.click()
        logger.info(f"Selected shipping method: {value}")

    def fill_details(self, details: dict):
        self.set_first_name(details.get('First_name', ''))
        self.set_last_name(details.get('Last_name', ''))
        self.set_street_address(details.get('Street', ''))
        self.set_city(details.get('City', ''))
        self.set_state(details.get('State', ''))
        self.set_zip_code(details.get('Zip_code', ''))
        self.set_country(details.get('Country', ''))
        self.set_phone(details.get('Phone', ''))

    def click_continue(self):
        self.find_element(*self.CONTINUE_BUTTON).click()
        logger.info('Clicked continue button')


class PaymentPage(BasePageObject):
    CONFIRM_PAYMENT = (By.XPATH, '//button[@title="Place Order"]')
    TOTAL_VALUE_OF_PRODUCTS = (By.XPATH, '//span[@class="price" and @data-th="Cart Subtotal"]')
    SHIPPING_COST = (By.XPATH, '//span[@class="price" and @data-th="Shipping"]')

    def confirm_order(self):
        self.browser.find_element(*self.CONFIRM_PAYMENT).click()

    def get_total_value(self):
        return self.find_element(*self.TOTAL_VALUE_OF_PRODUCTS).text

    def get_shipping_cost(self):
        return self.find_element(*self.SHIPPING_COST).text
