from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from Brouillon_Nikiema.metier.menu import Menu
from client.view.liste_restaurant_view import RestaurantListeView

from client.view.abstract_view import AbstractView

from client.service.restaurant_service import RestaurantService
from brouillon.metier.commande import Commande




class MenuListView(AbstractView):
    def __init__(self) -> None:
        id_restaurant = AbstractView.session.restaurant_actif.id_restaurant
        ## Liste des menus
        identifiant = AbstractView.session.identifiant
        mdp = AbstractView.session.mot_de_passe
        self.list_menu = RestaurantService.getMenus_By_Id_restaurant(id_restaurant, identifiant, mdp)
        ## Liste des noms des menus
        self.list_nom_menu = [menu.nom for menu in self.list_menu]
        self.list_nom_menu.append(Separator())
        self.list_nom_menu.append("Liste restaurant")
        self.list_nom_menu.append(Separator())
        self.list_nom_menu.append("Accueil")

        self.list_nom_menu2 = self.list_nom_menu.copy()
        self.list_nom_menu2.append(Separator())
        self.list_nom_menu2.append('Valider la commande active')
        if AbstractView.session.commande_active:
            choix = self.list_nom_menu2
        else: 
            choix = self.list_nom_menu

        self.questions = [
            {
                'type': 'list',
                'name' : 'Menu',
                'message': 'Choix menu : ',
                'choices': choix
            }
        ]
        
    def display_info(self):
        if AbstractView.session.commande_active : 
            print("-----------------------------------------")
            print(AbstractView.session.commande_active)
            print("-----------------------------------------")
        
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['Menu'] == "Accueil":
            ## Retourne à l'accueil
            from client.view.welcom_view import WelcomeView
            return  WelcomeView()
        elif reponse['Menu'] == "Liste restaurant":
            ## retourne à la liste des restaurants
            from client.view.liste_restaurant_view import RestaurantListeView
            return RestaurantListeView()
        elif reponse['Menu'] == 'Valider la commande active':
            from client.view.valide_commande_view import Valider
            return Valider()

        else: 
            ## Ajouter le menu à la liste de menu en session
            index = self.list_nom_menu.index(reponse['Menu'])
            AbstractView.session.menu_actif = self.list_menu[index]
            from client.view.menu_view import MenuView
            return MenuView()
             
            
            
            
        
        
        
    