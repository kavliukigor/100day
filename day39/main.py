import data_manager
import flight_data
import flight_search
import notification_manager

flight_search=flight_search.FlightSearch()
sheetboard=data_manager.DataManager()
notification=notification_manager.NotificationManager()
flight_data=flight_data.FlightData()

board_info=sheetboard.get_info_sheet()

for item in board_info:
    if item['iataCode']=='':
        index=flight_search.get_index(item['city'])
        id=item['id']
        sheetboard.add_index(index,id)
    
for item in board_info:
    index=item['iataCode']
    response_flight=flight_search.get_flight(index)
    lowest_price,best_arrive,best_date=flight_data.data_analys(response_flight)
    price=item['lowestPrice']
    if lowest_price<price:
        notification.send_message(lowest_price,best_arrive,best_date)
        print(best_arrive)
    else:
        print('No messages')