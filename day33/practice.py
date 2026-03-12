import requests

my_lat=50.619900
my_lon=26.251617
# response= requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()

# longitude=response.json()['iss_position']['longitude']
# latitude=response.json()['iss_position']['latitude']

# position=(longitude,latitude)
# print(position)

parameters= {
    'lat':my_lat,
    'lng':my_lon,
    'formatted':0
    }

response = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data['results']['sunrise'].split('T')[1].split('+')[0]
sunset=data['results']['sunset'].split('T')[1].split('+')[0]

print(f'{sunrise}\n{sunset}')