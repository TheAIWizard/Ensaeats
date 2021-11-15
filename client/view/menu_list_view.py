from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from client.view.liste_restaurant_view import RestaurantListeView

from client.view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService
from brouillon.metier.commande import Commande




class MenuListView(AbstractView):
    def __init__(self) -> None:
        id_restaurant = AbstractView.session.restaurant_actif.id_restaurant
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
                'message': 'Choisir un menu',
                'choices': list_nom_menu
            }
        ]
        
    def display_info(self):
        pass
        
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['Menu'] == "Accueil":
            ## Retourne à l'accueil
            from Tidiane_client_brouillon.view.welcom_view import WelcomeView
            WelcomeView()
        elif reponse['Menu'] == "Liste restaurant":
            ## retourne à la liste des restaurants
            from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView
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
            ## Cree la commande en attente de validation avec le service faire commande
            from Tidiane_client_brouillon.service.commande_service import Faire_commande
            AbstractView.session.commande_active = Faire_commande.faire_commande(AbstractView.session.list_menu, 
                                                            AbstractView.session.quantite_menu)
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
            
            
        
        
        
    