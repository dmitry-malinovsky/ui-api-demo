from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.page_objects.main_page import LoginPage, HomePage, NavigationModule
from features.page_objects.product_page import ProductPage
from features.page_objects.products_page import ProductsPage
from features.page_objects.checkout_page import CheckoutPage
from features.page_objects.payment_page import PaymentPage
import logging
import os
import base64


def before_all(context):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    context.logger = logging.getLogger()

    context.ui_url = "https://magento.softwaretestingboard.com"
    context.api_url = "https://restful-booker.herokuapp.com/"
    encoded_token = "QmFzaWMgWVdSaGFXNDZjam9rTlRBek5UWTFNalUw"
    context.auth_token = "YWRtaW46cGFzc3dvcmQxMjM="


def before_feature(context, feature):
    if 'UI' in feature.tags:
        start_browser(context)
        set_page_objects(context)


def before_scenario(context, scenario):
    if 'UI' in scenario.tags:
        if not hasattr(context, 'browser'):
            start_browser(context)
        set_page_objects(context)


def start_browser(context):
    chrome_options = Options()
    if os.getenv('HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.implicitly_wait(10)

def set_page_objects(context):
    context.product_page = ProductPage(context.browser)
    context.products_page = ProductsPage(context.browser)
    context.login_page = LoginPage(context.browser)
    context.home_page = HomePage(context.browser)
    context.navigation_page = NavigationModule(context.browser)
    context.checkout_page = CheckoutPage(context.browser)
    context.payment_page = PaymentPage(context.browser)

def after_scenario(context, scenario):
    if 'UI' in scenario.tags:
        if hasattr(context, 'browser'):
            context.browser.quit()
            del context.browser
    context.logger.info(f'Finished scenario: {scenario.name}')

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()
    context.logger.info('Finished all tests')