import requests
import datetime
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

basic= HTTPBasicAuth(USERNAME,PASSWORD)

URL ='https://app.100daysofpython.dev/v1/nutrition/natural/exercise'

headers = {
    'x-app-key':API_KEY,
    'x-app-id':APP_ID
}

data={
    'query':'lifted for 2 hours',
    'weight_kg':90,
    'height_cm':187,
    'age':20,
    'gender':'male'
}

exercise = requests.post(url=URL, json=data,headers=headers)
exercise_data=exercise.json()


data1 = {
    'аркуш1': {
        'date': datetime.datetime.now().strftime('%d/%m/%Y'),
        'time': datetime.datetime.now().strftime('%H:%M:%S'),
        'exercise': exercise_data['exercises'][0]['name'],
        'duration': exercise_data['exercises'][0]['duration_min'],
        'calories': exercise_data['exercises'][0]['nf_calories']
    }
}

add_info = requests.post(url=SHEET_ENDPOINT, json=data1, auth=basic)
print(add_info.status_code)
