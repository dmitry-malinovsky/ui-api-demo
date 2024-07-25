from selenium.webdriver.common.by import By
import logging

from features.page_objects.base_page_object import BasePageObject

logger = logging.getLogger(__name__)


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