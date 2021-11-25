
from client.business.avis import Avis
import requests



def getMenus_By_Id_restaurant(id_restaurant):
        # Requête vers api get menus
        params_menus_by_id_restaurant={'id_restaurant':id_restaurant}
        menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),params=params_menus_by_id_restaurant).json()

        return menus_by_id_restaurant
    
    



id_restau = 'LTy9AUgMnLn8YS21KfFZ8g'
identifiant = 'Tige'
mdp = '1234'

menus = getMenus_By_Id_restaurant(id_restau)
print(menus)