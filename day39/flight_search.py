import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import datetime
import json

class FlightSearch:
    def __init__(self):
        self.key=os.environ.get('AMADEUS_KEY')
        self.endpoint=os.environ.get('AMADEUS_URL')
        self.secret=os.environ.get('AMADEUS_SECRET')
        self.token_url=os.environ.get('TOKEN_URL')
        self.flight_url=os.environ.get('FLIGHT_URL')
        self.token_info={
            'grant_type':'client_credentials',
            'client_id':self.key,
            'client_secret':self.secret
        }
        self.token_request=requests.post(url=self.token_url,data=self.token_info)
        self.token = self.token_request.json()['access_token']
        self.headers={
            'Authorization':f'Bearer {self.token}'
        }
    pass

    def get_index(self, city_name):
        params={
            'keyword':city_name
        }
        
        response=requests.get(url=self.endpoint,headers=self.headers,params=params)
        data=response.json()
        index=data['data'][0]['iataCode']
        return index

    def get_flight(self,id):
        today=datetime.datetime.now()
        param_flight={
            'originLocationCode':'WAW',
            'destinationLocationCode':id,
            'departureDate':today.strftime('%Y-%m-%d'),
            'adults':1
        }
        response=requests.get(url=self.flight_url,params=param_flight,headers=self.headers)
        response_flight=response.json()
        return response_flight