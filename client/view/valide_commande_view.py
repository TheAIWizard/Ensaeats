from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from client.view.liste_restaurant_view import RestaurantListeView
from client.dao.commande_dao import CommandeDAO
from brouillon.metier.commande import Commande
from client.view.abstract_view import AbstractView
from datetime import datetime
from client.service.client_service import ClientService
from client.business.avis import Avis


class Valider(AbstractView):
    def __init__(self) -> None:
        list_choix = ["Valider la commande", Separator(), "Modifier la commande",Separator(), "Annuler"]
        self.question = [{
            'type': 'list',
            'name' : 'Menu',
            'message': 'Fenetre : ',
            'choices': list_choix
        }]
       
    def display_info(self):
        print("-----------------------------------------")
        print(AbstractView.session.commande_active)
        print("-----------------------------------------")
    
    
    def make_choice(self):        
        choix = prompt(self.question)
        ## Si choix valider : appel commande insert dao
        if choix["Menu"] == 'Valider la commande':
            id_commande = CommandeDAO.add_commande(commande = AbstractView.session.commande_active)
            CommandeDAO.lien_commande_menus(AbstractView.session.commande_active, id_commande= id_commande)
            CommandeDAO.lien_commande_client(AbstractView.session.id_client, id_commande)
            if id_commande: print("Commande effectuée")
            ## Effacer les informations en session sur la commande
            AbstractView.session.commande_active = None
            AbstractView.session.list_menu = []
            AbstractView.session.list_quantite = []
            AbstractView.session.menu_actif = None
            #retour = input("Appuyer sur Entrer pour retourner à l'Accueil !")
            
            ## Demander d'ajouter son avis sur le restaurant
            avis_question = [{
                'type': 'list',
                'name': 'avis_choice',
                'message': 'Voulez vous donner votre avis sur le restaurant',
                'choices': ["Oui", Separator(), "Non"]
            }]
            avis_reponse = prompt(avis_question)
            
            if avis_reponse['avis_choice'] == 'Oui': 
                ## Ajoute ton avis sur le restaurant
                avis_txt = input('Donner votre avis : ')

                today = datetime.today().strftime('%Y-%m-%d') 

                avis_user = Avis(avis = avis_txt, identifiant_auteur = AbstractView.session.identifiant,
                id_restaurant = AbstractView.session.restaurant_actif.id_restaurant, date = today)
                ## Ajout avis dans la base de données
                result =  ClientService.ajouter_avis(avis_user)
                print(result)
                
                input("Appuyer sur Entrer pour revenir en accueil")
                from client.view.welcom_view import WelcomeView
                return WelcomeView()
            
            else: 
                from client.view.welcom_view import WelcomeView
                return WelcomeView()
            
        elif choix["Menu"] == 'Modifier la commande':
            ## Page de modification de la commande
            from client.view.commande_view import Modif_commande
            return Modif_commande()
        else:
            ## Suprimer les informations en session
            
            AbstractView.session.commande_active = None
            AbstractView.session.list_menu = []
            AbstractView.session.list_quantite = []
            AbstractView.session.menu_actif = None
            ## Revenir à la liste des menus
            from client.view.menu_list_view import MenuListView
            return MenuListView()
            
            
            
        
    