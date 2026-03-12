import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,uk;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
}

response=requests.get(url='https://appbrewery.github.io/instant_pot/', headers=headers)
res=response.text
soup=BeautifulSoup(res, 'html.parser')
price=soup.select('span.a-price-whole')
price_whole=price[0].getText().strip()
price_fract=soup.select('span.a-price-fraction')
price_fraction=price_fract[0].getText().strip()
price_final=float(f'{price_whole}{price_fraction}')
target=100

name_data=soup.select('span#productTitle')
name=' '.join(name_data[0].getText().split())
name=name.encode('ascii', 'ignore').decode('ascii')
if price_final<target:
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=os.environ.get("EMAIL_FROM"), password=os.environ.get("SMTP_PASSWORD"))
                    connection.sendmail(
                        from_addr=os.environ["EMAIL_FROM"],
                        to_addrs=os.environ['EMAIL_TO'],
                        msg="Subject: Price Alert!\n\n" + f"Price for {name} is lower than target: ${price_final}"
                    )
    except smtplib.SMTPAuthenticationError:
        print('Wrong email or password')
    except smtplib.SMTPException:
        print('Problems with server')
    except Exception as e:
        print(e)