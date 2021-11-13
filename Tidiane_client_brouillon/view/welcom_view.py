from PyInquirer import prompt

from Tidiane_client_brouillon.view.abstract_view import AbstractView
from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView

class WelcomeView(AbstractView):
    
    def display_info(self):
        pass
     
    def make_choice(self):
        self.localite = input("Entrer la localité: ")
        self.nom_restaurant = input("Entrer le nom du restaurant: ")
        self.radius = input("Trouver restaurant dans quel rayon (km) par rapport à votre localite: ")
        
        AbstractView.session.localite = self.localite
        AbstractView.session.radius = self.radius
        AbstractView.session.nom_restaurant = self.nom_restaurant
       
        return RestaurantListeView()




    
    
    