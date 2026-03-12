import requests
from datetime import datetime
import smtplib
import time

my_email='kavliukigor@gmail.com'
password='ozmqgaefmqscamuz'
MY_LAT = 50.619900
MY_LONG = 26.251617
def iis_cor():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_longitude,iss_latitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def check(iss_latitude,iss_longitude):
    if MY_LAT-5 <iss_latitude<MY_LAT+5 and MY_LONG-5<iss_longitude<MY_LONG+5:
        hour=time_now.hour
        if hour<sunrise or hour>sunset:
            with smtplib.SMTP('smtp.gmail.com')as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                from_addr=my_email,
                to_addrs='igor2018kavl@gmail.com',
                msg=f'Subject:International Space Ship\n\n Look up'
                )

while True:
    iss_latitude,iss_longitude=iis_cor()
    check(iss_latitude,iss_longitude)
    time.sleep(60)