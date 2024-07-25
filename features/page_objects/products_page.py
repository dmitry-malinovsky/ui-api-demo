from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

from features.page_objects.base_page_object import BasePageObject

logger = logging.getLogger(__name__)


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