import requests
params = {'term': 'restaurant','location': 'Rennes', 'username': 'KingAlex35', 'password': 'KingAlex35'}
r=requests.get('http://localhost:5000/docs#/Restaurants/get_restaurants_restaurants__get',params=params)
print("5")