class FlightData:
    def data_analys(self,info):
        lowest_price=float('inf')
        best_arrive=''
        best_date=''
        for item in info['data']:
            price=float(item['price']['total'])
            arrive=item['itineraries'][0]['segments'][-1]['arrival']['iataCode']
            departureDate=item['itineraries'][0]['segments'][0]['departure']['at']
            if price<lowest_price:
                lowest_price=price
                best_arrive=arrive
                best_date=departureDate

        return lowest_price,best_arrive,best_date
    pass