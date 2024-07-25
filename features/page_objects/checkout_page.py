from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging

from features.page_objects.base_page_object import BasePageObject

logger = logging.getLogger(__name__)


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
