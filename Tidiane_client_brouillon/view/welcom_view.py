from PyInquirer import prompt

from view.abstract_view import AbstractView
from view.liste_restaurant_view import RestaurantListeView

class WelcomeView(AbstractView):
    def __init__(self) -> None:
        self.localite = input("Entrer la localité: ")
        self.nom_restaurant = input("Entrer le nom du restaurant: ")
        self.radius = input("Trouver restaurant dans quel rayon (km) par rapport à votre localite: ")
        
     
     
    def make_choice(self):
        AbstractView.session.localite = self.localite
        AbstractView.session.radius = self.radius
        AbstractView.session.nom_restaurant = self.nom_restaurant
        
        return RestaurantListeView()
        
    def display_info(self):
        pass
    
    