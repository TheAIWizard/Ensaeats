from PyInquirer import prompt, Separator

from Tidiane_client_brouillon.view.abstract_view import AbstractView
from Tidiane_client_brouillon.dao.avis_DAO import AvisDao
from brouillon.metier.avis import Avis

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
                Separator(), ## Ajouter : consulter les commandes
                'Accueil']
            }
        ]
        
    
    def display_info(self):
        pass
    
    
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse["Menu"] == 'Accueil':
            ## Aller à l'accueil
            from Tidiane_client_brouillon.view.welcom_view import WelcomeView
            return WelcomeView()
        
        elif reponse["Menu"] == 'Consulter Menus':
            ## Aller dans menus liste view
            from Tidiane_client_brouillon.view.menu_list_view import MenuListView
            return MenuListView()
        else :
            ## Aller dans avis liste view
            id_restaurant = AbstractView.session.restaurant_actif.id_restaurant
            AbstractView.session.listeAvis = AvisDao.find_avis_by_id_restaurant(id_restaurant)
            from Tidiane_client_brouillon.view.avisView import AvisView
            return AvisView()
            
    
    