from behave import given, when, then
from features.page_objects.main_page import NavigationModule
from features.page_objects.products_page import ProductsPage
from features.page_objects.product_page import ProductPage
import logging

logger = logging.getLogger(__name__)


@when('I navigate to {menu_path}')
def step_impl(context, menu_path):
    menu_items = menu_path.split(" -> ")
    context.navigation_page = NavigationModule(context.browser)
    context.navigation_page.navigate_through_menu(*menu_items)
    logger.info(f'Navigating to product from menu: {menu_path}')


@when('I click on the item with text "{item_text}"')
def step_impl(context, item_text):
    context.product_page.click_item_by_text(item_text)


@when('I search for "{product_name}"')
def step_impl(context, product_name):
    context.product_page.search_item(product_name)


@when('I click on the search result "{product_name}"')
def step_impl(context, product_name):
    context.product_page.click_search_result(product_name)


@then('I should see the product details page for "{product_name}"')
def step_impl(context, product_name):
    assert context.product_page.is_correct_product(product_name)


@when('I select the size "{size}"')
def step_impl(context, size):
    context.product_page.select_size(size)


@when('I select the color "{color}"')
def step_impl(context, color):
    context.product_page.select_color(color)


@when('I add the product to the cart')
def step_impl(context):
    context.product_page.add_to_cart()


@when('I add the following items to the basket')
def step_impl(context):
    context.total_price = 0.0
    for row in context.table:
        product_title = row['Product_title']
        size = row['Size']
        color = row['Color']

        context.products_page.search_item(product_title)
        context.products_page.click_search_result(product_title)
        assert context.product_page.is_correct_product(product_title)

        if size:
            context.product_page.select_size(size)
        if color:
            context.product_page.select_color(color)

        context.total_price += context.product_page.get_float_product_price()
        print(context.total_price)
        context.product_page.add_to_cart()


@when('I click on the basket icon')
def step_impl(context):
    context.product_page.click_basket_icon()


@when('I proceed to checkout')
def step_impl(context):
    context.product_page.click_basket_icon()
    context.product_page.proceed_to_checkout()

    ## This hack line also stores ACTUAL total price that is on checkout. Since we cannot clean basket on each run.
    context.total_price = context.product_page.get_total_price