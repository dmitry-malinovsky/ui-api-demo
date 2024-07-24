import requests
from behave import given, then
from pydantic import ValidationError
from models.api_models import Person, PlanetResponse, FilmResponse, SpeciesResponse


@given('I make a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    print(f"{context.api_url}{endpoint}")
    context.logger.info(f"{context.api_url}{endpoint}")
    context.response = requests.get(f"{context.api_url}{endpoint}")


@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == status_code


@then('the response should include "{key}": "{value}"')
def step_impl(context, key, value):
    response_json = context.response.json()
    assert response_json[key] == value


@then('the response should match the character model')
def step_impl(context):
    response_json = context.response.json()
    try:
        Person(**response_json)
    except ValidationError as e:
        assert False, f"Response validation error: {e}"


@then('the response should match the planet model')
def step_impl(context):
    response_json = context.response.json()
    try:
        PlanetResponse(**response_json)
    except ValidationError as e:
        assert False, f"Response validation error: {e}"


@then('the response should match the film model')
def step_impl(context):
    response_json = context.response.json()
    try:
        FilmResponse(**response_json)
    except ValidationError as e:
        assert False, f"Response validation error: {e}"


@then('the response should match the species model')
def step_impl(context):
    response_json = context.response.json()
    try:
        SpeciesResponse(**response_json)
    except ValidationError as e:
        assert False, f"Response validation error: {e}"