import os
import smtplib
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms_no_stops(self, cheapest_flight):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=f"Low price alert! Only £{cheapest_flight.price} to fly direct from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date}.",
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        print(message.sid)

    def send_sms_stops(self, cheapest_flight):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=f"Low price alert! Only DOLLARS{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, with {cheapest_flight.stops} stop(s), on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        print(message.sid)

    def send_email(self, cheapest_flight, to_email):
        if cheapest_flight.stops == 0:
            msg = (f"Low price alert! Only DOLARS{cheapest_flight.price} to fly direct "
                   f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                   f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        else:
            msg = (f"Low price alert! Only DOLLARS{cheapest_flight.price} to fly "
                   f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                   f"with {cheapest_flight.stops} stop(s), "
                   f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ.get("EMAIL_FROM"), password=os.environ.get("SMTP_PASSWORD"))
            connection.sendmail(
                from_addr=os.environ["EMAIL_FROM"],
                to_addrs=to_email,
                msg=msg
            )