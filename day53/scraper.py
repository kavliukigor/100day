import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
load_dotenv()

class Scraper:
    def __init__(self):
        self.link=os.getenv('LINK')
        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(self.link, headers=self.headers)
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.elements_list=self.soup.select("article[data-test='property-card']")

    def get_bookings(self):
        links=[element.select_one('a')['href'] for element in self.elements_list]
        prices=[element.select_one('span[data-test="property-card-price"]').text.replace('/','+').split('+')[0] for element in self.elements_list]
        adresses=[element.select_one('address[data-test="property-card-addr"]').text.strip() for element in self.elements_list]
        return links, prices, adresses