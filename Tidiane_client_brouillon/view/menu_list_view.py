from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView

from Tidiane_client_brouillon.view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService
from brouillon.metier.commande import Commande




class MenuListView(AbstractView):
    def __init__(self) -> None:
        id_restaurant = AbstractView.session.restaurant_actif.id_restaurant
        ## Liste des menus
        self.list_menu = RestaurantsService.getMenus_by_id_restaurant(id_restaurant)
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
        if AbstractView.session.commande_active : print(AbstractView.session.commande_active)
        
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['Menu'] == "Accueil":
            ## Retourne à l'accueil
            from Tidiane_client_brouillon.view.welcom_view import WelcomeView
            return  WelcomeView()
        elif reponse['Menu'] == "Liste restaurant":
            ## retourne à la liste des restaurants
            from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView
            return RestaurantListeView()
        elif reponse['Menu'] == 'Valider la commande active':
            from Tidiane_client_brouillon.view.valide_commande_view import Valider
            return Valider()

        else: 
            ## Ajouter le menu à la liste de menu en session
            index = self.list_nom_menu.index(reponse['Menu'])
            menu_choix = self.list_menu[index]
            quantite = int(input("Quantite de ce menu: "))
            AbstractView.session.menu_actif = menu_choix
            AbstractView.session.list_menu.append(menu_choix)
            AbstractView.session.quantite_menu = quantite
            AbstractView.session.list_quantite.append(quantite)
            ## Cree la commande en attente de validation avec le service faire commande
            from Tidiane_client_brouillon.service.commande_service import Faire_commande
            AbstractView.session.commande_active = Faire_commande.faire_commande(AbstractView.session.list_menu, 
                                                            AbstractView.session.list_quantite)
            question2 = [{
                'type': 'list',
                'name': 'Menu',
                'message': 'Que voulez vous faire',
                'choices': ['Ajouter un autre menu', Separator(), 'Valider la commande']
            }]
            reponse2 = prompt(question2)
            if reponse2['Menu'] == 'Ajouter un autre menu':
                from Tidiane_client_brouillon.view.menu_list_view import MenuListView
                return MenuListView()
            else: 
                from Tidiane_client_brouillon.view.valide_commande_view import Valider
                return Valider()
            
            
        
        
        
    