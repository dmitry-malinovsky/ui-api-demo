import requests

class ApiAdapter:
    @staticmethod
    def post(context, body, headers=None):
        response = requests.post(f"{context.api_url}/booking", json=body, headers=headers)
        return response

    @staticmethod
    def get(context, booking_id, headers=None):
        response = requests.get(f"{context.api_url}/booking/{booking_id}", headers=headers)
        return response

    @staticmethod
    def delete(context, booking_id):
        headers = {
            "Cookie": "token=" + context.auth_token,
            "Content-Type": "application/json"
        }
        response = requests.delete(f"{context.api_url}/booking/{booking_id}", headers=headers)
        return response

    @staticmethod
    def get_token(context):
        response = requests.post(
            f"{context.api_url}/auth",
            json={"username": "admin", "password": "password123"},
            headers={"Content-Type": "application/json"}
        )
        return response