import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT =os.environ.get("SHEET_URL")


class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._users_endpoint = os.environ.get("SHEET_USERS")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.headers={
            "Authorization": os.environ.get("SHEET_AUTHORIZATION")
        }
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, headers=self.headers
            )

    def users_email(self):
        response = requests.get(url=self._users_endpoint, headers=self.headers)
        data = response.json()
        self.users_emails = data['users']
        return self.users_emails
