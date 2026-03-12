from twilio.rest import Client
import os
class NotificationManager:
    def __init__(self):
        self.sid=os.environ.get('TWILIO_SID')
        self.token=os.environ.get('TWILIO_TOKEN')
        self.number=os.environ.get('TWILIO_NUM')
        self.ownNum=os.environ.get('MY_NUM')
    def send_message(self,lowest_price,best_arrive,best_date):
        client = Client(self.sid, self.token)
        message=client.messages.create(
            body=f"Низька ціна! Рейс до {best_arrive} за ${lowest_price}. Дата вильоту: {best_date}. Летимо з WAW!",
            from_=self.number,
            to=self.ownNum
        )
        pass
    pass