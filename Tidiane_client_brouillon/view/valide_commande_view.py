from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView
from Tidiane_client_brouillon.dao.commande_dao import CommandeDAO
from brouillon.metier.commande import Commande
from Tidiane_client_brouillon.view.abstract_view import AbstractView

class Valider(AbstractView):
    def __init__(self) -> None:
        list_choix = ["Valider la commande", "Modifier la commande", "Annuler"]
        self.question = [{
            'type': 'list',
            'name' : 'Menu',
            'message': 'Fenetre : ',
            'choices': list_choix
        }]
       
    def display_info(self):
        print(AbstractView.session.commande_active)
    
    
    def make_choice(self):        
        choix = prompt(self.question)
        ## Si choix valider : appel commande insert dao
        if choix["Menu"] == 'Valider la commande':
            id_commande = CommandeDAO.add_commande(commande = AbstractView.session.commande_active)
            CommandeDAO.lien_commande_menus(AbstractView.session.commande_active, id_commande= id_commande)
            CommandeDAO.lien_commande_client(AbstractView.session.id_client, id_commande)
            if id_commande: print("Commande effectuée")
            retour = input("Appuyer sur Entrer pour retourner à l'Accueil !")
            from Tidiane_client_brouillon.view.welcom_view import WelcomeView
            return WelcomeView()
            
        if choix["Menu"] == 'Modifier la commande':
            ## Page de modification de la commande
            from Tidiane_client_brouillon.view.modif_commande import Modif_commande
            return Modif_commande()
        if choix['Menu'] == 'Annuler':
            ## Suprimer les informations en session
            AbstractView.session.list_menu = []
            AbstractView.session.list_quantite = []
            AbstractView.session.menu_actif = None
            AbstractView.session.quantite = None
            ## Revenir à la liste des menus
            from Tidiane_client_brouillon.view.menu_list_view import MenuListView
            return MenuListView()
            
            
            
        
    