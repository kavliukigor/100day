import smtplib
import datetime as dt
import random
my_email='kavliukigor@gmail.com'
password='ozmqgaefmqscamuz'
with open('day32/quotes.txt')as file:
    lines=file.readlines()
    line=random.choice(lines)
now= dt.datetime.now()
day=now.weekday()
days_in_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

with smtplib.SMTP('smtp.gmail.com')as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='vzarikov821@gmail.com',
        msg=f'Subject:Motivatsiya\n\n Motivation for {days_in_week[day]} is {line}'
        )