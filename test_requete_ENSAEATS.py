from fastapi import params
import requests
import pandas as pd

from api.metier.avis import Avis
from api.dao.avis_DAO import AvisDao

""" TESTS 
sur la VM: 'http: ... localhost:5000' 
sur ordi perso: 'http ... localhost' ou 'localhost:80'
"""

#requête API pour obtenir les restaurants
params_restaurants={'localisation':'Rennes','term':'','radius':20000,'identifiant_client':'KingAlex35','mot_de_passe_client':'KingAlex35'}
restaurants=requests.get('http://localhost:5000/restaurants/',params=params_restaurants).json()
#print(restaurants)

#requête API pour obtenir un restaurateur
params_restaurateur = {'restaurateur_id': 'TheSmith', 'mot_de_passe_client': 'TheSmith'}
restaurateurs=requests.get('http://localhost:5000/restaurateurs/{}'.format('TheSmith'),params=params_restaurateur).json()
#print(restaurateurs)

""" DEMANDE REQUETE API TIDIANE"""

id_restaurant_fontaine_perles='LTy9AUgMnLn8YS21KfFZ8g'
id_restaurant='NL0ROvACBWrwYv1BZxBWtQ'
identifiant_client=mot_de_passe_client='KingAlex35'#client
identifiant_restaurateur=mot_de_passe_restaurateur='CrossMartin' #restaurateur

""" RECHERCHE GET """

#requête recherche restaurant by id_restaurant
params_restaurant_by_id_restaurant={'id_restaurant':id_restaurant,'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
restaurant_by_id_restaurant=requests.get('http://localhost:5000/restaurant/{}'.format(id_restaurant),params=params_restaurant_by_id_restaurant).json()
#print(restaurant_by_id_restaurant)

#requête recherche menus by id_restaurant
params_menus_by_id_restaurant={'id_restaurant':id_restaurant,'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),params=params_menus_by_id_restaurant).json()
#print(menus_by_id_restaurant)

#requête recherche avis by id_restaurant
params_avis_by_id_restaurant={'id_restaurant':id_restaurant,'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
avis_by_id_restaurant=requests.get('http://localhost:5000/avis/',params=params_avis_by_id_restaurant).json()
#print(avis_by_id_restaurant) 

#requête recherche commandes by id_restaurant
""" params_commandes_by_id_restaurant={'id_restaurant':id_restaurant_fontaine_perles,'identifiant_restaurateur':identifiant_restaurateur,'mot_de_passe_restaurateur':mot_de_passe_restaurateur}
commandes_by_id_restaurant=requests.get('http://localhost:5000/commandes/restaurant',params=params_commandes_by_id_restaurant).json() """
#print(commandes_by_id_restaurant) 

#requête recherche commandes by client
""" params_commandes_by_client={'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
print(commandes_by_id_client)  """

""" AJOUT POST"""
avis=Avis(avis="l'EJR c'est quand même mieux" ,identifiant_auteur="l'EJR c'est quand même mieux",id_restaurant="NL0ROvACBWrwYv1BZxBWtQ")
#requête ajout avis by id_restaurant
params_ajout_avis_by_id_restaurant={'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
ajout_avis_by_id_restaurant=requests.post('http://localhost:5000/avis/',params=params_ajout_avis_by_id_restaurant,json=dict(avis)).json()
#print(ajout_avis_by_id_restaurant)


json_client={
  "id_client": 0,
  "nom": "string",
  "prenom": "string",
  "adresse": {
    "adresse": "string",
    "code_postal": 0,
    "ville": "string",
    "pays": "string"
  },
  "identifiant": "string",
  "mot_de_passe": "string",
  "telephone": "string"
}

#requête ajout client
params_ajout_client={'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
ajout_client=requests.post('http://localhost:5000/clients/',json=json_client).json()
#print(ajout_client)

params_ajout_client={'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
#print(requests.get('http://localhost:5000/clients/{}'.format(identifiant_client),params=params_ajout_client).json())

params_restaurant_by_id_restaurant={'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
restaurants=requests.get('http://localhost:5000/restaurants',params=params_restaurant_by_id_restaurant).json()

print(pd.DataFrame(requests.get('http://localhost:5000/restaurants',params=params_restaurant_by_id_restaurant).json())['nom'].to_list())
print(requests.get('http://localhost:5000/restaurants',params=params_restaurant_by_id_restaurant).json())

print([restaurant['nom'] for restaurant in restaurants])


""" #requête ajout commandes by id_restaurant: à venir
params_commandes_by_id_restaurant={'id_restaurant':id_restaurant,'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
commandes_by_id_restaurant=requests.post('http://localhost:5000/commandes/{}'.format(id_restaurant),params=params_commandes_by_id_restaurant).json()
#print(commandes_by_id_restaurant) """


""" #requête ajout commandes by id_client: à venir
params_commandes_by_id_restaurant={'id_restaurant':id_restaurant,'identifiant_client':identifiant_client,'mot_de_passe_client':mot_de_passe_client}
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