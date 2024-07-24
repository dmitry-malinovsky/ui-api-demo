from behave import given, when, then
from features.page_objects.page_objects import NavigationModule, ProductsPage, ProductPage, CheckoutPage
import logging
from models.web_models import CheckoutData

logger = logging.getLogger(__name__)


@then('I fill in the checkout details as follows')
def step_impl(context):
    details = CheckoutData.parse_checkout_details(context.table)
    context.checkout_page.fill_details(details)
    context.checkout_page.click_continue()