import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    
    flights = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], tomorrow, six_month_from_today)
    cheapest_flight = find_cheapest_flight(flights)
    
    if cheapest_flight.price:
        if cheapest_flight.stops==0:
            notification_manager.send_sms_no_stops(cheapest_flight)
        else:
            notification_manager.send_sms_stops(cheapest_flight)

emails=data_manager.users_email()
for email in emails:
    notification_manager.send_email(cheapest_flight, email['whatIsYourEmail?'])