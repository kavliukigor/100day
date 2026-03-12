import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


load_dotenv()

class DataManager:
    def __init__(self) -> None:
        self.endpoint=os.environ.get('SHEET_URL')
        self.endpoint_put=os.environ.get('SHEET_PUT')
        self.user=os.environ.get('USERNAME')
        self.password=os.environ.get('PASSWORD')
        self.destination_data=[]
        self.basic=HTTPBasicAuth(self.user,self.password)
    pass

    def get_info_sheet(self):
        response=requests.get(url=self.endpoint,auth=self.basic)
        self.destination_data=response.json()
        self.destination_data=self.destination_data['prices']
        return self.destination_data

    def add_index(self,index,id):
        response=requests.put(url=f'{self.endpoint}/{id}', json={'price':{'iataCode':index}},auth=self.basic)