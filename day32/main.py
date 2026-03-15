import pandas
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
my_email=os.getenv('my_email')
password=os.getenv('password')

data=pandas.read_csv('day32/birthdays.csv')
info={row['name']:{'email':row['email'],'year':row['year'],'month':row['month'],'day':row['day']} for(index,row)in data.iterrows()}
print(info)
now=dt.datetime.now()
letters=['letter_1','letter_2','letter_3']

for name in info:
    if now.day == info[name]['day'] and now.month==info[name]['month']:
        letter=random.choice(letters)
        with open(f'day32/letter_templates/{letter}.txt')as file:
            template=file.read()
            new_letter = template.replace('[NAME]',name)
            print(new_letter)
            with smtplib.SMTP('smtp.gmail.com')as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=info[name]['email'],
                    msg=f'Subject: Happy Birthday!\n\n{new_letter}'
                    )        