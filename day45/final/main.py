import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response=requests.get(URL)
res=response.text

soup=BeautifulSoup(res, 'html.parser')
elements=soup.find_all('h3', class_='title')

movies=[element.getText() for element in elements]
movies.reverse()
with open ('day45/final/movies.txt','w', encoding='utf-8')as f:
    for movie in movies:
        f.write(f'{movie}\n')