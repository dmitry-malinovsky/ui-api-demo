from behave import given, when, then
from features.page_objects.main_page import LoginPage, HomePage
import logging

logger = logging.getLogger(__name__)


@given('I am on the login page')
def step_impl(context):
    context.login_page.load()


@given('I enter email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)


@given('I enter password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)


@given('I click the login button')
def step_impl(context):
    context.login_page.click_login()


@given('I am logged into the website')
def step_impl(context):
    context.login_page.load()
    context.login_page.set_email("dmitrii.malinovschii@gmail.com")
    context.login_page.set_password("9nkMZUZ5P!YT#Q2")
    context.login_page.click_login()

    assert context.home_page.is_at_home_page()
