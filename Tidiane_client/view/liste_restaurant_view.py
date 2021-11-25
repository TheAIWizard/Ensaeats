from PyInquirer import prompt, Separator

from client.view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService

from client.view.select_param import selection
import requests
import pandas as pd

params_restaurants={'identifiant_client':AbstractView.session.identifiant,'mot_de_passe_client':AbstractView.session.mot_de_passe,
                                'localisation':AbstractView.session.localite, 'term': AbstractView.session.term,'radius': AbstractView.session.radius}

class RestaurantListeView(AbstractView):
    def __init__(self) -> None:
        ## Liste des restaurants
        self.liste_restaurant = requests.get('http://localhost:5000/restaurants',params=params_restaurants).json()
        ## Liste avec uniquement les noms
        self.liste_nom_restaurant = list(pd.DataFrame(requests.get('http://localhost:5000/restaurants',params=params_restaurants).json())['nom'])
        
        ## Creation de la liste de choix
        choix_restaurant = self.liste_nom_restaurant
        choix_restaurant.append(Separator())
        choix_restaurant.append("Retour Accueil")
        self.questions = [
            {
                'type': 'list',
                'name': 'restaurant',
                'message': 'Choix restaurant : ',
                'choices': choix_restaurant
            }
        ]
        
    def display_info(self):
        pass

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse["restaurant"] == "Retour Accueil":
            from client.view.welcom_view import WelcomeView
            return WelcomeView()
        else: 
            ## Recuperons le restaurant actif et renvoi la page restaurant view
            index = self.liste_nom_restaurant.index(reponse["restaurant"])
            AbstractView.session.restaurant_actif = self.liste_restaurant[index]
            from client.view.restaurant_view import RestaurantView
            return RestaurantView()
            
            
            