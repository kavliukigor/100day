import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

params= {
    'appid':'29b9139773495e58be48957d98cc274c',
    'lat':50.447731,
    'lon':30.542721,
    'cnt':4
}
account_sid = os.getenv('[SID]')
auth_token = os.getenv(['TOKEN'])
rain=False

response=requests.get('https://api.openweathermap.org/data/2.5/forecast',params=params)
weather_data=response.json()

for item in weather_data:
    if item['weather'][0]['id']<700:
        rain=True
        break
if rain:
    client = Client(account_sid, auth_token)
    message=client.messages.create(
        body='You need umbrella',
        from_='+16186932231',
        to='+380508841817'
    )
