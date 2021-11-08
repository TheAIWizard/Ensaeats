from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView

from view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService
from brouillon.metier.commande import Commande




class MenuListView(AbstractView):
    def __init__(self, id_restaurant) -> None:
        ## Liste des menus
        self.list_menu = RestaurantsService.getMenus_by_id_restaurant(id_restaurant)
        ## Liste des noms des menus
        list_nom_menu = [menu.nom for menu in self.list_menu]
        list_nom_menu.append(Separator())
        list_nom_menu.append("Liste restaurant")
        list_nom_menu.append(Separator())
        list_nom_menu.append("Accueil")
        self.questions = [
            {
                'type': 'list',
                'name' : 'Menu',
                'Message': 'Choisir un menu',
                'choices': list_nom_menu
            }
        ]
        
    
        
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['Menu'] == "Accueil":
            ## Retourne à l'accueil
            from view.welcom_view import WelcomeView
            WelcomeView()
        elif reponse['Menu'] == "Liste restaurant":
            ## retourne à la liste des restaurants
            from view.liste_restaurant_view import RestaurantListeView
            return RestaurantListeView()
        else: 
            ## Ajouter le menu à la liste de menu en session
            index = self.list_nom_menu.index(reponse['Menu'])
            menu_choix = self.list_menu[index]
            quantite = input("Quantite de ce menu: ")
            AbstractView.session.menu_actif = menu_choix
            AbstractView.session.list_menu.append(menu_choix)
            AbstractView.session.quantite_menu = quantite
            AbstractView.session.list_quantite.append(quantite)
            ## Cree la commande en attente de validation
            import datetime
            aujourdui = datetime.date.today()
            AbstractView.session.commande_active = Commande(1, aujourdui, 'En cours', AbstractView.session.list_menu, 
                                                            AbstractView.session.quantite_menu)
            from view.valide_commande_view import Valider
            return Valider()
            
            
        
        
        
    def display_info(self):
        pass