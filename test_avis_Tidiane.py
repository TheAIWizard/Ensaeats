
from client.business.avis import Avis
import requests
from client.service.mapper import BusinessMapper


""" def getMenus_By_Id_restaurant(id_restaurant):
        # Requête vers api get menus
        menus_headers={'accept': 'application/json','identifiant': 'Tige','mot-de-passe': '1234'}
        menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),headers=menus_headers).json()

        return menus_by_id_restaurant """
headers = {
    'accept': 'application/json',
    'identifiant': 'Tige',
    'mot-de-passe': '1234',
}

response = requests.get('http://localhost:5000/menus/LTy9AUgMnLn8YS21KfFZ8g', headers=headers)
print(response.json())

""" def getAvis_By_Id_Restaurant(id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get avis
        params_avis_by_restaurant = {'id_restaurant': id_restaurant, 'identifiant_client': identifiant, 'mot_de_passe_client': mot_de_passe}
        avis_json = requests.get('http://localhost:5000/avis/', params = params_avis_by_restaurant).json()
        avis = BusinessMapper.avis_mapper(avis_json)
        return avis """



""" id_restau = 'LTy9AUgMnLn8YS21KfFZ8g'
identifiant = 'Tige'
mdp = '1234' """

""" menus = getMenus_By_Id_restaurant(id_restau)
print(menus) """
""" 
avis = getAvis_By_Id_Restaurant(id_restau, identifiant, mdp)

print(avis[0]) """
""" CE QUI MARCHE SUR MA MACHINE

headers = {
    'accept': 'application/json',
    'identifiant': 'Tige',
    'mot-de-passe': '1234',
}

response = requests.get('http://localhost:8000/menus/LTy9AUgMnLn8YS21KfFZ8g', headers=headers)

print(response.json()) """
