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
        },
        {'type': 'list','name': 'proximite','message': "Voulez vous être livré à votre adresse à moins de 20 km de chez vous? \n",
                                'choices': ['Oui', Separator(), 'Non']}]

        print("Bienvenue ", AbstractView.session.client['prenom'])
        print("\n")
        reponse = prompt(question)

        if reponse['Menu'] == 'Oui':
            #question_proximite = [{'type': 'list','name': 'proximite','message': "Voulez vous être livré à votre adresse à moins de 20 km de chez vous? \n",
                                #'choices': ['Oui', Separator(), 'Non']}]  
            #reponse_proximite = prompt(question_proximite)

            #headers={'accept: application/json'}
            

            if reponse['proximite'] == 'Oui':
                #paramètres pour obtenir les restaurants à proximité
                params_restaurants={'identifiant_client':AbstractView.session.identifiant,'mot_de_passe_client':AbstractView.session.mot_de_passe,
                                          'localisation':AbstractView.session.adresse, 'term': AbstractView.session.term,'radius': 20000}
            else:  
                self.localite = input("Entrer la localité (Obligatoire):  ") 
                #Question à caractère obligatoire, ne passe à l'étape suivante tant que celle là n'est pas remplie
                while self.localite=="":
                    self.localite = input("Entrer la localité (Obligatoire):  ")
            
                self.nom_restaurant = input("Entrer le nom du restaurant (Facultatif):   ")
            
                self.radius = input("Trouver restaurant dans quel rayon (m) par rapport à votre localite"\
                    "(Facultatif):  ")
                #paramètres restaurant où l'on précise sa localisation
                params_restaurants={'identifiant_client':AbstractView.session.identifiant,'mot_de_passe_client':AbstractView.session.mot_de_passe,
                                'localisation':self.localite, 'term': self.nom_restaurant,'radius': self.radius}

               
             ## Liste des restaurants
            self.liste_restaurant = requests.get('http://localhost:8000/restaurants',params=params_restaurants)
            ## Liste avec uniquement les noms
            self.liste_nom_restaurant = [restaurant for restaurant in self.liste_restaurant]
            #sauvegarde dans la session des listes de restaurants leurs noms et autres paramètres
            AbstractView.session.liste_restaurant=self.liste_restaurant
            AbstractView.session.liste_nom_restaurant=self.liste_nom_restaurant

            print("Rechercher un restaurant selon différents critères")
            
            #s'il n'y a pas d'erreur dans la requête, retourne le json des restaurants et passe à la view suivante
            if self.liste_restaurant.status_code !=200:
                self.liste_restaurant=self.liste_restaurant.json()
                return WelcomeView()
            return RestaurantListeView()
            
                
        else:
            ## Sortir de l'application
            return None
            
                

 

    
    
    