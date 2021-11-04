from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView

from view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService

class MenuListView(AbstractView):
    def __init__(self, id_restaurant) -> None:
        ## Liste des menus
        list_menu = RestaurantsService.getMenus_by_id_restaurant(id_restaurant)
        ## Liste des noms des menus
        list_nom_menu = [menu.nom for menu in list_menu]
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
            ## AJouter le menu à la commande
            index = self.list_menu.index(reponse['Menu'])
            menu_choix = 

        
        
    def display_info(self):
        pass