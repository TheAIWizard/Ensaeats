from PyInquirer import prompt, Separator, separator

from view.abstract_view import AbstractView

class RestaurantView(AbstractView):
    def __init__(self) -> None:
        self.questions = [
            {
                'type': 'list',
                'name': 'Menu',
                'Message': 'Choisir un option',
                'choices': ['Consulter Menus',
                Separator(),
                'Consulter les avis',
                Separator(),
                'Accueil']
            }
        ]
        self.restaurant_actif = AbstractView.session.restaurant_actif
    
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse["Menu"] == 'Accueil':
            ## Aller à l'accueil
            from view.welcom_view import WelcomeView
            return WelcomeView()
        
        elif reponse["Menu"] == 'Consulter Menus':
            ## Aller dans menus liste view
            from view.menu_list_view import MenuListView
            return MenuListView(self.restaurant_actif.id_restau)
        else :
            ## Aller dans avis liste view
            pass
    
    def display_info(self):
        pass