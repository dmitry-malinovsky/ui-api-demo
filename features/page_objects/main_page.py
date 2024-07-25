from selenium.webdriver.common.by import By
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
