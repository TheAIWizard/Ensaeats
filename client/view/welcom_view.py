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

        print("Bienvenue ", AbstractView.session.client['prenom']) #ou plus simplement AbstractView.session.prenom au choix ...
        print("\n")
        reponse = prompt(question)

        if reponse['Menu'] == 'Oui':
            print("Rechercher un restaurant selon différents critères")
            
            self.localite = input("Entrer la localité (Obligatoire):  ") 
            #Question à caractère obligatoire, ne passe à l'étape suivante tant que celle là n'est pas remplie
            while self.localite=="":
                self.localite = input("Entrer la localité (Obligatoire):  ")
            
            self.nom_restaurant = input("Entrer le nom du restaurant (Facultatif):   ")
            
            self.radius = input("Trouver restaurant dans quel rayon (m) par rapport à votre localite"\
                "(Facultatif):  ")

            params_restaurants={'identifiant_client':AbstractView.session.identifiant,'mot_de_passe_client':AbstractView.session.mot_de_passe,
                                'localisation':self.localite, 'term': self.nom_restaurant,'radius': self.radius}

            AbstractView.session.localite = self.localite
            AbstractView.session.radius = self.radius
            AbstractView.session.nom_restaurant = self.nom_restaurant
            #s'il n'y a pas d'erreur dans la requête
            if requests.get('http://localhost:5000/restaurants',params=params_restaurants).status_code !=200:
                return RestaurantListeView()
            else: 
                return WelcomeView()
        else:
            ## Sortir de l'application
            return None
            
                

 

    
    
    