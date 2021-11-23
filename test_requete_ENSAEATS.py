from fastapi import params
import requests

from api.metier.avis import Avis
from api.dao.avis_DAO import AvisDao

""" TESTS 
sur la VM: 'http: ... localhost:5000' 
sur ordi perso: 'http ... localhost' ou 'localhost:80'
"""

#requête API pour obtenir les restaurants
params_restaurants={'localisation':'Rennes','term':'','radius':20000,'username':'KingAlex35','password':'KingAlex35'}
restaurants=requests.get('http://localhost:5000/restaurants/',params=params_restaurants).json()
#print(restaurants)

#requête API pour obtenir un restaurateur
params_restaurateur = {'restaurateur_id': 'TheSmith', 'password': 'TheSmith'}
restaurateurs=requests.get('http://localhost:5000/restaurateurs/{}'.format('TheSmith'),params=params_restaurateur).json()
#print(restaurateurs)

""" DEMANDE REQUETE API TIDIANE"""

id_restaurant_fontaine_perles='LTy9AUgMnLn8YS21KfFZ8g'
id_restaurant='NL0ROvACBWrwYv1BZxBWtQ'
username=password='KingAlex35'

""" RECHERCHE GET """

#requête recherche restaurant by id_restaurant
params_restaurant_by_id_restaurant={'id_restaurant':id_restaurant,'username':username,'password':password}
restaurant_by_id_restaurant=requests.get('http://localhost:5000/restaurant/{}'.format(id_restaurant),params=params_restaurant_by_id_restaurant).json()
#print(restaurant_by_id_restaurant)

#requête recherche menus by id_restaurant
params_menus_by_id_restaurant={'id_restaurant':id_restaurant,'username':username,'password':password}
menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),params=params_menus_by_id_restaurant).json()
#print(menus_by_id_restaurant)

""" #requête recherche avis by id_restaurant
params_avis_by_id_restaurant={'id_restaurant':id_restaurant,'username':username,'password':password}
avis_by_id_restaurant=requests.get('http://localhost:5000/avis/{}'.format(id_restaurant),params=params_avis_by_id_restaurant).json()
print(avis_by_id_restaurant) """

#requête recherche commandes by id_restaurant
params_commandes_by_id_restaurant={'id_restaurant':id_restaurant,'username':username,'password':password}
commandes_by_id_restaurant=requests.get('http://localhost:5000/commandes/{}'.format(id_restaurant),params=params_commandes_by_id_restaurant).json()
#print(commandes_by_id_restaurant)

""" AJOUT: REQUETE POST """
avis=Avis(avis="l'EJR c'est quand même mieux" ,identifiant_auteur="l'EJR c'est quand même mieux",id_restaurant="NL0ROvACBWrwYv1BZxBWtQ")

#requête ajout avis by id_restaurant
params_ajout_avis_by_id_restaurant={'username':username,'password':password}
ajout_avis_by_id_restaurant=requests.post('http://localhost:5000/avis/?username=KingAlex35&password=KingAlex35',params=params_ajout_avis_by_id_restaurant,json=dict(avis)).json()
print(ajout_avis_by_id_restaurant)

""" #requête ajout commandes by id_restaurant: à venir
params_commandes_by_id_restaurant={'id_restaurant':id_restaurant,'username':username,'password':password}
commandes_by_id_restaurant=requests.post('http://localhost:5000/commandes/{}'.format(id_restaurant),params=params_commandes_by_id_restaurant).json()
#print(commandes_by_id_restaurant) """



""" TEST AVIS"""
"""
{
  "avis": "l'EJR c'est quand même mieux",
  "identifiant_auteur": "KingAlex35",
  "date": "23/11/2021 00:40:09",
  "id_restaurant": "NL0ROvACBWrwYv1BZxBWtQ"
}
"""

#print(AvisDao.find_avis_by_id_restaurant(id_restaurant=id_restaurant))