
from requests.api import post
from client.business.article import Article
from client.business.avis import Avis
import requests
from client.service.mapper import BusinessMapper
from client.business.commande import Commande
from client.business.menu import Menu

def getMenus_By_Id_restaurant(id_restaurant, identifiant, mdp):
        # Requête vers api get menus
        headers = {
            'accept': 'application/json',
            'identifiant': identifiant,
            'mot-de-passe': mdp,
        }
        
        menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),headers= headers).json()

        return menus_by_id_restaurant



def getAvis_By_Id_Restaurant(id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get avis
        params_avis_by_restaurant = {
            'id_restaurant': id_restaurant, 
            'identifiant_client': identifiant, 
            'mot_de_passe_client': mot_de_passe
            }
        avis_json = requests.get('http://localhost:5000/avis/', params = params_avis_by_restaurant).json()
        avis = BusinessMapper.avis_mapper(avis_json)
        return avis



def getRestaurants(localite, term, radius, identifiant, mot_de_passe):
        
        params_restaurants = {'localisation':localite,'term': term,
                            'radius':radius,'identifiant_client': identifiant,
                            'mot_de_passe_client': mot_de_passe}
        restaurants_json = requests.get('http://localhost:5000/restaurants/',
                                 params = params_restaurants).json()
        restaurants = BusinessMapper.restaurant_mapper(restaurants_json)
        return restaurants


def getClient(identifiant, mot_de_passe):
    parametres = {
        'identifiant_client': identifiant,
        "mot_de_passe_client" : mot_de_passe}
    client_json=requests.get('http://localhost:5000/clients/{}'.format(identifiant), params=parametres, 
                                    headers = {'accept': 'application/json'}).json() 
    client_metier = BusinessMapper.client_mapper(client_json)

    return client_metier



def post_avis_by_id_restaurant(identifiant, mot_de_passe, avis):
        output = False
        param_avis_post = {
            'identifiant_client': identifiant,
            'mot_de_passe_client': mot_de_passe
            }
        post_avis = requests.post('http://localhost:5000/avis/', 
                                 json = dict(avis),
                                 params = param_avis_post).json()
        
        if post_avis:
            output = True
            return output
        return output


def valider_commande(identifiant, mot_de_passe, commande: Commande):
        """[Ajouter la commande de l'utilisateur]

        Args:
            commande ([Commande]): [Commande faite par l'utilisateur]
        """
        ## Requete post 
        output = False
        params_post_commande = {
            'identifiant_client': identifiant,
            'mot_de_passe_client': mot_de_passe
            }
        post_commande = requests.post('http://localhost:5000/commande/',
                                     json = dict(commande),
                                     params = params_post_commande).json()
        if post_commande: 
            output = True
            return output
        return output 





avis = Avis(
    avis = 'Test avis',
    identifiant_auteur = 'Tige',
    date = '26-11-2021',
    id_restaurant = 'LTy9AUgMnLn8YS21KfFZ8g'
)

article1 = Article(
    id_article = 5,
    nom = 'Le tout caramel',
    composition = 'Biscuit streusel noisette, pâte à choux et glac...',   
    type = 'dessert') 

article2 = Article(
id_article = 6,
nom = 'Carpaccio de betterave',
composition = 'Mariné soja et gingembre, betterave, framboise e...',   
type = 'entrée') 

article3 = Article(
    id_article = 7,
    nom = 'Les champignons',
    composition = 'Gâteau de girolles, cèpe rôti, artichaut poivr...',   
    type = 'plat') 

menu = Menu( 
    id_menu = 2,
    nom = 'Menu légumes',
    prix = 54,
    article1 = article1,
    article2= article2,
    article3 = article3

)

cmd = Commande(
    id_commande = 1,
    id_restaurant = 'LTy9AUgMnLn8YS21KfFZ8g',
    date = '26-11-2021',
    statut_commande = 'en cours',
    liste_menu = [dict(menu)],
    liste_quantite = [1]
)

localite = 'Rennes'
id_restau = 'LTy9AUgMnLn8YS21KfFZ8g'
identifiant = 'Tige'
mdp = '1234'

from client.service.commande_service import Faire_commande
cmd = Faire_commande.command_avec_menu_serializable(cmd)
reponse = getMenus_By_Id_restaurant(id_restau, identifiant, mdp)

print(reponse)


