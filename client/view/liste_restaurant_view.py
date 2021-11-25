from PyInquirer import prompt, Separator

from client.view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService

from client.view.select_param import selection
import requests
import pandas as pd

#paramètres pour obtenir les restaurants à proximité
params_restaurants_proximite={'identifiant_client':AbstractView.session.identifiant,'mot_de_passe_client':AbstractView.session.mot_de_passe,
                                'localisation':AbstractView.session.adresse, 'term': AbstractView.session.term,'radius': AbstractView.session.radius}
#paramètres restaurant où l'on précise sa localisation
params_restaurants={'identifiant_client':AbstractView.session.identifiant,'mot_de_passe_client':AbstractView.session.mot_de_passe,
                                'localisation':AbstractView.session.localite, 'term': AbstractView.session.term,'radius': AbstractView.session.radius}


class RestaurantListeView(AbstractView):
    def __init__(self) -> None:
    
        question_proximite = [{
        'type': 'list',
        'name': 'proximite',
        'message': "Voulez vous être livré à votre adresse ? \n",
        'choices': ['Oui', Separator(), 'Non']
        }]    
        reponse = prompt(question_proximite)
        if reponse['proximite'] == 'Oui':
             ## Liste des restaurants à proximité
            self.liste_restaurant = requests.get('http://localhost:5000/restaurants',params=params_restaurants_proximite).json()
            ## Liste avec uniquement les noms des res restaurants à proximité
            self.liste_nom_restaurant = [restaurant for restaurant in self.liste_restaurant]#pd.DataFrame(requests.get('http://localhost:5000/restaurants',params=params_restaurants).json())['nom'].to_list()
        else:  
            ## Liste des restaurants
            self.liste_restaurant = requests.get('http://localhost:5000/restaurants',params=params_restaurants).json()
            ## Liste avec uniquement les noms
            self.liste_nom_restaurant = [restaurant for restaurant in self.liste_restaurant]#pd.DataFrame(requests.get('http://localhost:5000/restaurants',params=params_restaurants).json())['nom'].to_list()
        
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
            