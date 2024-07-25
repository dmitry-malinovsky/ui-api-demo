import requests
from behave import given, then, when
from pydantic import ValidationError
from models.api_booking_models import BookingDates, BookingDetails as BookingDetailsModel
from adapters.api_adapter import ApiAdapter

@given('I have a valid API token')
def step_given_valid_api_token(context):
    response = ApiAdapter.get_token(context)
    context.auth_token = response.json()["token"]
@given('I have the following booking details')
def step_given_booking_details(context):
    try:
        context.booking_details = BookingDetailsModel.map_table_to_booking_details(context.table)
    except ValidationError as e:
        context.error = e


@when('I create a new booking')
def step_when_create_booking(context):
    response = ApiAdapter.post(context, context.booking_details.dict())
    context.response = response
    context.booking_id = response.json().get('bookingid')

@then('I should be able to retrieve the booking and validate its content')
def step_then_validate_booking_content(context):
    response = ApiAdapter.get(context, context.booking_id)
    assert response.status_code == 200, "Failed to retrieve booking"

    try:
        booking_data = response.json()
        retrieved_booking = BookingDetailsModel(**booking_data)
        assert retrieved_booking == context.booking_details, "Booking details do not match"
    except ValidationError as e:
        context.error = e


@then('I delete the booking')
def step_then_delete_booking(context):
    response = ApiAdapter.delete(context, context.booking_id)
    context.response = response

@then('the booking should be deleted')
def step_then_booking_deleted(context):
    assert context.response.status_code == 201, "Failed to delete booking"