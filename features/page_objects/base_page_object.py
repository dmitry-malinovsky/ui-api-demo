from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re
import logging

logger = logging.getLogger(__name__)


class BasePageObject(object):
    URL = ""

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.actions = ActionChains(browser)

    def load(self):
        self.browser.get(self.URL)

    def find_element(self, by: By, value: str):
        element = self.browser.find_element(by, value)
        logger.info(f'Element found by {by} with value "{value}"')
        return element

    def find_elements(self, by: By, value: str):
        elements = self.browser.find_elements(by, value)
        logger.info(f'Elements found by {by} with value "{value}"')
        return elements
