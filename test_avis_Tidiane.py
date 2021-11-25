
from client.business.avis import Avis
import requests



def getMenus_By_Id_restaurant(id_restaurant):
        # Requête vers api get menus
        menus_headers={'accept': 'application/json','identifiant': 'Tige','mot-de-passe': '1234',}
        menus_by_id_restaurant=requests.get('http://localhost:8000/menus/{}'.format(id_restaurant),headers=menus_headers).json()

        return menus_by_id_restaurant
    
    



id_restau = 'LTy9AUgMnLn8YS21KfFZ8g'
identifiant = 'Tige'
mdp = '1234'

menus = getMenus_By_Id_restaurant(id_restau)
print(menus)


""" CE QUI MARCHE SUR MA MACHINE

headers = {
    'accept': 'application/json',
    'identifiant': 'Tige',
    'mot-de-passe': '1234',
}

response = requests.get('http://localhost:8000/menus/LTy9AUgMnLn8YS21KfFZ8g', headers=headers)

print(response.json()) """