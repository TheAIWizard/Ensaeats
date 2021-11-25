from PyInquirer import prompt, Separator

from client.view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService

from client.view.select_param import selection
import requests


class RestaurantListeView(AbstractView):
    def __init__(self) -> None:
        ## Liste des restaurants
        
        self.liste_restaurant = requests.get('http://localhost:8000/restaurants/?identifiant_client=oui&mot_de_passe_client=oui&localisation=rennes&radius=2000',headers={'accept': 'application/json'}).json()
        ## Liste avec uniquement les noms
        self.liste_nom_restaurant = [restaurant['nom'] for restaurant in self.liste_restaurant]
        
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
    #voulez vous commander près de chez vous
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
            