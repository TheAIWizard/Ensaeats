
from client.business.avis import Avis
import requests
from client.service.mapper import BusinessMapper


def getMenus_By_Id_restaurant(id_restaurant, identifiant_client, mot_de_passe_client):
        # Requête vers api get menus
        params_menus_by_id_restaurant={'id_restaurant': id_restaurant, 'identifiant': identifiant_client, 'mot_de_passe': mot_de_passe_client}
        menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),
        params = params_menus_by_id_restaurant).json()

        return menus_by_id_restaurant
    
def getAvis_By_Id_Restaurant(id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get avis
        params_avis_by_restaurant = {'id_restaurant': id_restaurant, 'identifiant_client': identifiant, 'mot_de_passe_client': mot_de_passe}
        avis_json = requests.get('http://localhost:5000/avis/', params = params_avis_by_restaurant).json()
        avis = BusinessMapper.avis_mapper(avis_json)
        return avis



id_restau = 'LTy9AUgMnLn8YS21KfFZ8g'
identifiant = 'Tige'
mdp = '1234'

avis = getAvis_By_Id_Restaurant(id_restau, identifiant, mdp)
print(avis[5]) 

menus = getMenus_By_Id_restaurant(id_restau, identifiant, mdp)
print("\n")

print(menus[0]) 