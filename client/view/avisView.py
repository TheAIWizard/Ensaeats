from client.business.client import Client
from client.view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from api.metier.avis import Avis
from client.dao.avis_DAO import AvisDao
from client.service.client_service import ClientService
from datetime  import datetime

class AvisView(AbstractView):
    def __init__(self) -> None:
        list_choix = ['Ajouter un avis', Separator(), 'Voir les menus', Separator(), 'Liste des restaurants',Separator(), 'Accueil']
        self.question = [{
            'type': 'list',
            'name': 'Menu',
            'message': 'Que voulez vous faire',
            'choices': list_choix
        }]

    def display_info(self):
        if AbstractView.session.listeAvis: 
            for avis in AbstractView.session.listeAvis:
                print(avis)
                print("-----------------------------------------")
            print("\n")
        else:
            print("Aucun avis")
            print("-----------------------------------------")
            print("\n")
    

    def make_choice(self):
        reponse = prompt(self.question)

        if reponse['Menu'] == 'Ajouter un avis':
            ## Ajoute ton avis sur le restaurant
            avis_txt = input('Donner votre avis : ')

            today = datetime.today().strftime('%Y-%m-%d') 

            avis_user = Avis(avis = avis_txt, identifiant_auteur = AbstractView.session.identifiant,
             id_restaurant = AbstractView.session.restaurant_actif.id_restaurant, date = today)
            ## Ajout avis dans la base de données
            result =  ClientService.ajouter_avis(avis_user)
            print(result)
            input("Appuyer sur entrer pour retourner")
            from client.view.restaurant_view import RestaurantView
            return RestaurantView()

        elif reponse['Menu'] == 'Voir les menus':
            ## Voir menus
            from client.view.menu_list_view import MenuListView
            return MenuListView()
        elif reponse['Menu'] == 'Liste des restaurants':
            from client.view.liste_restaurant_view import RestaurantListeView
            return RestaurantListeView()
        else: 
            ## Retour à l'accueil
            from client.view.welcom_view import WelcomeView
            return WelcomeView()    
            