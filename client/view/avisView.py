from client.business.client import Client
from client.view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from brouillon.metier.avis import Avis
from client.dao.avis_DAO import AvisDao
from client.service.client_service import ClientService

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
        for avis in AbstractView.session.listeAvis:
            print(avis)
            print("\n")
    

    def make_choice(self):
        reponse = prompt(self.question)

        if reponse['Menu'] == 'Ajouter un avis':
            ## Ajoute ton avis sur le restaurant
            avis_txt = input('Donner votre avis : ')
            avis_user = Avis(avis = avis_txt, nom_auteur = AbstractView.session.client.prenom)
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
            