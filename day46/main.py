from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")
bilboard_url=os.environ.get("BILBOARD_URL")

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

time=input(f'What time you want travel to? Enter in format YYYY-MM-DD ')
response=requests.get(url=bilboard_url + time,headers=header)
res=response.text

soup=BeautifulSoup(res, 'html.parser')
data=soup.select('li.o-chart-results-list__item h3.c-title')
songs=[song.text.strip() for song in data]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-modify-public"
))
user_id = sp.current_user()['id']

song_info=sp.search(songs[0])
print(song_info)