from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time

from features.page_objects.base_page_object import BasePageObject

logger = logging.getLogger(__name__)


class ProductPage(BasePageObject):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'span[itemprop="name"]')
    PRODUCT_PRICE = (By.XPATH, '//meta[@itemprop="price"]')
    ADD_TO_CART_BUTTON = (By.ID, 'product-addtocart-button')
    SIZE_OPTIONS = (By.XPATH, '//div[@class="swatch-attribute size"]/div/div')
    COLOR_OPTIONS = (By.XPATH, '//div[@class="swatch-attribute color"]/div/div')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.message-success')
    BASKET_ICON = (By.CSS_SELECTOR, 'a.action.showcart')
    PROCEED_TO_CHECKOUT_BUTTON = (By.ID, 'top-cart-btn-checkout')
    CURRENT_TOTAL_PRICE = (By.XPATH, "//span[@class='price-wrapper']/span[@class='price']")

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
        time.sleep(3)

    def proceed_to_checkout(self):
        self.browser.find_element(*self.PROCEED_TO_CHECKOUT_BUTTON).click()

    def get_total_price(self):
        return self.browser.find_element(*self.CURRENT_TOTAL_PRICE).text