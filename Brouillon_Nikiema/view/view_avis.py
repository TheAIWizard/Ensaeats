from PyInquirer import prompt, Separator, separator

from Tidiane_client_brouillon.view.abstract_view import AbstractView
from Brouillon_Nikiema.metier.avis import Avis
class AvisView(AbstractView):
    def __init__(self) -> None:
        self.questions = [
            {
                'type': 'list',
                'name': 'Menu',
                'Message': 'Choisir un option',
                'choices': 'choisir liste avis'
            }
        ]
       
    
    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse["Menu"] == 'Accueil':
            ## Aller à l'accueil
            from view.welcom_view import WelcomeView
            return WelcomeView()
        
        elif reponse["Menu"] == 'choisir liste avis':
            ## Aller dans menus liste view
            from Brouillon_Nikiema.metier.avis import Avis
            return Avis.recup_avis
        else :
            
            pass
    
    def display_info(self):
        pass