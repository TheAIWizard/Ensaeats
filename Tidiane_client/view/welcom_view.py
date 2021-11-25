from PyInquirer import prompt
from PyInquirer.separator import Separator

from client.view.abstract_view import AbstractView
from client.view.liste_restaurant_view import RestaurantListeView

class WelcomeView(AbstractView):
    
    def display_info(self):
        pass
     
    def make_choice(self):
        question = [{
            'type': 'list',
            'name': 'Menu',
            'message': "Entrer dans l'application \n",
            'choices': ['Oui', Separator(), 'Non']
        }]

        print("Bienvenue ", AbstractView.session.client.prenom)
        print("\n")
        reponse = prompt(question)

        if reponse['Menu'] == 'Oui':
            print("Rechercher un restaurant selon différents critères")
            
            self.localite = input("Entrer la localité (Obligatoire):  ")
            
            self.nom_restaurant = input("Entrer le nom du restaurant (Facultatif):   ")
            
            self.radius = input("Trouver restaurant dans quel rayon (m) par rapport à votre localite"\
                "(Facultatif):  ")
            
            AbstractView.session.localite = self.localite
            AbstractView.session.radius = self.radius
            AbstractView.session.nom_restaurant = self.nom_restaurant
        
            if self.localite != '':
                return RestaurantListeView()
            else: 
                return WelcomeView()
        else:
            ## Sortir de l'application
            return None
            



    
    
    