from bs4 import BeautifulSoup
import requests

response=requests.get('https://news.ycombinator.com/news')
res=response.text

soup=BeautifulSoup(res,'html.parser')
span=soup.find_all(name='span', class_='titleline')
texts=[]
links=[]
for i in span:
    a=i.find('a')
    links.append(a['href'])
    texts.append(a.getText())

score_find=soup.find_all(name='span',class_='score')
score=[score.getText() for score in score_find]

scores=[int(item.split()[0]) for item in score]

max_score=scores.index(max(scores))
max_text=texts[max_score]
max_link=links[max_score]
print(f'Most popular news is:\n{max_text}\n{max_link}\nScore:{scores[max_score]}')