from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from six import reraise
from client.view.liste_restaurant_view import RestaurantListeView
from client.business.commande import Commande
from client.view.abstract_view import AbstractView
from datetime import datetime
from client.business.avis import Avis
from client.service.commande_service import Faire_commande
from client.service.avis_service import AvisService


class Valider(AbstractView):
    def __init__(self) -> None:
        list_choix = ["Valider la commande", Separator(), "Modifier la commande",Separator(), "Annuler"]
        self.question = [{
            'type': 'list',
            'name' : 'Menu',
            'message': 'Fenetre : ',
            'choices': list_choix
        }]
        
        ## Identifiant et mot de passe de l'utilisateur
        self.identifiant = AbstractView.session.identifiant
        self.mdp = AbstractView.session.mot_de_passe
       
    def display_info(self):
        print("-----------------------------------------")
        print(AbstractView.session.commande_active)
        print("-----------------------------------------")
    
    
    def make_choice(self):        
        choix = prompt(self.question)
        ## Si choix valider : appel commande insert dao
        if choix["Menu"] == 'Valider la commande':
            
            commande_active = AbstractView.session.commande_active
            commande_active = Faire_commande.command_avec_menu_serializable(commande_active)
            resultat_post_commande = Faire_commande.valider_commande(self.identifiant, self.mdp, commande_active)
            if resultat_post_commande == 200: 
                print("Commande ajoutée avec succès !")
                print('\n')
            else:
                from client.view.menu_list_view import MenuListView
                return MenuListView()
                
            
            
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

                avis_client = Avis(avis = avis_txt, identifiant_auteur = self.identifiant,
                id_restaurant = AbstractView.session.restaurant_actif.id_restaurant, date = today)
                ## Ajout avis dans la base de données
                result_post_avis = AvisService.post_avis_by_id_restaurant(self.identifiant,
                                                                self.mdp,
                                                                avis_client)
                if result_post_avis:
                    print("Avis ajouter avec succès ! ")
                                
                input("Appuyer sur Entrer pour revenir en accueil")
                from client.view.welcom_view import WelcomeView
                return WelcomeView()
            
            else: 
                input("Appuyer sur Entrer pour revenir en accueil")
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
            
            
            
        
    