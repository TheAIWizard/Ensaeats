from PyInquirer import prompt, Separator
from client.business.client import Client

from client.view.abstract_view import AbstractView
from client.service.client_service import ClientService
from api.metier.avis import Avis

class RestaurantView(AbstractView):
    def __init__(self) -> None:
        self.questions = [
            {
                'type': 'list',
                'name': 'Menu',
                'message': 'Choix option :',
                'choices': ['Consulter Menus',
                Separator(),
                'Consulter les avis',
                Separator(),
                'Liste des restaurants',
                Separator(), 
                'Accueil']
            }
        ]
        
    
    def display_info(self):
        print("Restaurant", AbstractView.session.restaurant_actif.nom)
        print('\n')
    
    
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse["Menu"] == 'Accueil':
            ## Aller à l'accueil
            from client.view.welcom_view import WelcomeView
            return WelcomeView()
        
        elif reponse["Menu"] == 'Consulter Menus':
            ## Aller dans menus liste view
            from client.view.menu_list_view import MenuListView
            return MenuListView()
        
        elif reponse['Menu'] == "Liste des restaurants":
            from client.view.liste_restaurant_view import RestaurantListeView
            return RestaurantListeView()
        else :
            ## Aller dans avis liste view
            id_restaurant = AbstractView.session.restaurant_actif.id_restaurant
            AbstractView.session.listeAvis = ClientService.consulter_avis(id_restaurant)
                     
            from client.view.avisView import AvisView
            return AvisView()
            
    
    