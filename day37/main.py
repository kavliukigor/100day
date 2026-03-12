import requests
import datetime

USERNAME = 'igor1568'
TOKEN = 'qwertyuiop'

pixela_endpoint = 'https://pixe.la/v1/users'

params={
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

#response= requests.post(url=pixela_endpoint,json=params)

graph_endpoint=f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config={
    'id': 'graph1',
    'name':'Gym',
    'unit':'reps',
    'type':'float',
    'color':'momiji'
}

headers={
    'X-USER-TOKEN':TOKEN
}

id=graph_config['id']
params1={
    'quantity':'100',
    'date':datetime.datetime.now().strftime('%Y%m%d')
}

response=requests.post(url=f'{graph_endpoint}/{id}', json=params1,headers=headers)

params2={
    'quantity':'100',
    
}
date=datetime.datetime.now().strftime('%Y%m%d')
response=requests.put(url=f'{graph_endpoint}/{id}/{date}',headers=headers)

# response= requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)


