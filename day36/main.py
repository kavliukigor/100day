import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = os.getenv(['SID'])
auth_token =os.getenv (['TOKEN'])

parameters1={
    'apikey':'X49BS1NC76HIDOR3',
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK
}

parameters2={
    'apiKey':'5a2a0777843e4476af3cc22fe8871fdf',
    'q':COMPANY_NAME,
    'pageSize':3,
    'sortBy':'publishedAt'
}

client = Client(account_sid, auth_token)
response=requests.get('https://www.alphavantage.co/query',params=parameters1)
data=response.json()
price_info=data['Time Series (Daily)']
list_data=list(price_info.keys())
change=round((float(price_info[list_data[0]]['4. close'])-float(price_info[list_data[1]]['4. close']))/float(price_info[list_data[1]]['4. close'])*100, 2)

if abs((float(price_info[list_data[0]]['4. close'])-float(price_info[list_data[1]]['4. close']))/float(price_info[list_data[1]]['4. close'])*100)>=5:
    response_news=requests.get('https://newsapi.org/v2/everything',params=parameters2)
    data_news=response_news.json()
    news=data_news['articles']
    if change>0:
        text1='Grow'
    else:
        text1='Drop'
    for items in news:
        
        message=client.messages.create(
            body=f"{text1}\n{items['title']}\n{items['description']}",
            from_='+16186932231',
            to='+380508841817'
        )