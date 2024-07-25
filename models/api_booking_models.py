from pydantic import BaseModel

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class BookingDetails(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


    def map_table_to_booking_details(table):
        booking_details_data = {}
        for row in table:
            field = row['field']
            value = row['value']

            if field in ['checkin', 'checkout']:
                if 'bookingdates' not in booking_details_data:
                    booking_details_data['bookingdates'] = {}
                booking_details_data['bookingdates'][field] = value
            elif field == 'totalprice':
                booking_details_data[field] = int(value)
            elif field == 'depositpaid':
                booking_details_data[field] = value.lower() == 'true'
            else:
                booking_details_data[field] = value

        return BookingDetails(**booking_details_data)