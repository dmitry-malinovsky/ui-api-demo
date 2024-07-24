class CheckoutData:
    # In case we need.want to use this default data
    checkout_details = {
        "First_name": "John",
        "Last_name": "Doe",
        "Email": "john.doe@example.com",
        "Street": "123 Main St",
        "City": "Anytown",
        "State": "California",
        "Zip_code": "90210",
        "Country": "United States",
        "Phone": "1234567890"
    }

    @staticmethod
    def parse_checkout_details(table):
        field_names = table.headings
        field_values = table.rows[0].cells
        return {field_names[i]: field_values[i] for i in range(len(field_names))}