from PyInquirer import prompt
from PyInquirer.separator import Separator
from client.view.abstract_view import AbstractView
from client.view.liste_restaurant_view import RestaurantListeView
import requests

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

        print("Bienvenue ", AbstractView.session.client.prenom) #ou plus simplement AbstractView.session.prenom au choix ...
        print("\n")
        reponse = prompt(question)

        if reponse['Menu'] == 'Oui':
            question_proximite = [{
                'type': 'list',
                'name': 'proximite',
                'message': "Voulez vous être livré à votre adresse ? \n",
                'choices': ['Oui', Separator(), 'Non']
            }] 

            print("Rechercher un restaurant selon différents critères \n")


            reponse_proxi = prompt(question_proximite)
            if reponse_proxi['proximite'] == 'Non':
                self.localite = input("Entrer la localité (Obligatoire):  ") 
                #Question à caractère obligatoire, ne passe à l'étape suivante tant que celle là n'est pas remplie
                while self.localite=="":
                    self.localite = input("Entrer la localité (Obligatoire):  ")
            else:
                self.localite = AbstractView.session.client.adresse
            
            self.nom_restaurant = input("Entrer le nom du restaurant (Facultatif):   ")
            
            self.radius = input("Trouver restaurant dans quel rayon (m) par rapport à votre localite"\
                "(Facultatif):  ")

            AbstractView.session.localite = self.localite # Correspond à l'adresse ou la localite saisie selon les choix de l'utilisateur
            AbstractView.session.radius = self.radius
            AbstractView.session.nom_restaurant = self.nom_restaurant
            return RestaurantListeView()
            
               
        else:
            ## Sortir de l'application
            return None
            
                

 

    
    
    