from behave import given, when, then
import logging
from models.web_models import CheckoutData

logger = logging.getLogger(__name__)


@when('I fill in the checkout details as follows')
def step_impl(context):
    details = CheckoutData.parse_checkout_details(context.table)
    context.checkout_page.fill_details(details)


@when('I select "{delivery_type}" delivery')
def step_impl(context, delivery_type):
    context.checkout_page.select_shipping_method(delivery_type)


@then ('I confirm my order')
def step_impl(context):
    context.checkout_page.click_continue()


@then ('I see correct order price')
def step_impl(context):
    actual_total_price = format_label(context.payment_page.get_total_value())
    actual_shipping = format_label(context.payment_page.get_shipping_cost())

    expected_total_price = format_label(context.total_price)

    logger.info(expected_total_price)
    logger.info(actual_total_price)
    logger.info(actual_shipping)

    assert actual_total_price == expected_total_price, f"Expected total price {expected_total_price}, but got {actual_total_price}"


def format_label(str):
    return float(str.replace('$', '').replace(',', ''))
