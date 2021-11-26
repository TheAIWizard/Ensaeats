from PyInquirer import prompt, Separator

from client.view.abstract_view import AbstractView

from client.service.restaurant_service import RestaurantService
import requests

from client.view.select_param import selection


class RestaurantListeView(AbstractView):
    def __init__(self) -> None:
        self.identifiant = AbstractView.session.identifiant
        self.mot_de_passe = AbstractView.session.mot_de_passe
        self.term = AbstractView.session.term
        self.radius = AbstractView.session.radius
        self.localite = AbstractView.session.localite
   
        
        self.liste_restaurant = selection(self.localite, self.term, self.radius, 
                                            self.identifiant, self.mot_de_passe)
        ## Liste avec uniquement les noms
        self.liste_nom_restaurant = [restaurant.nom for restaurant in self.liste_restaurant]

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
            