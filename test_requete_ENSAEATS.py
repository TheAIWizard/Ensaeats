import requests

#requêtes pour obtenir les restaurants
""" params_restaurants={'localisation':'Rennes','radius':20000,'username':'KingAlex35','password':'KingAlex35'}
restaurants=requests.get('http://localhost/restaurants/',params=params_restaurants)
print(restaurants.json()) """
#requêtes pour obtenir les avis



#requêtes pour obtenir un restaurateur
params_restaurateur = {'restaurateur_id': 'TheSmith', 'password': 'TheSmith'}
restaurateurs=requests.get('http://localhost/restaurateurs/{}'.format('TheSmith'),params=params_restaurateur)
print(restaurateurs)