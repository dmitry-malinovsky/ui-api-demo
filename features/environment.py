from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from features.page_objects.page_objects import LoginPage, HomePage, ProductPage, ProductsPage, NavigationModule,CheckoutPage,PaymentPage
import logging


def before_all(context):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    context.logger = logging.getLogger()

    context.ui_url = "https://magento.softwaretestingboard.com"
    context.api_url = "https://swapi.dev/api"


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
    # chrome_options.add_argument("--headless")  # Uncomment if headless mode is needed
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