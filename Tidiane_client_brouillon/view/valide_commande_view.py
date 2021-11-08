from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView

from view.abstract_view import AbstractView

class Valider(AbstractView):
    def __init__(self) -> None:
        list_choix = ["Valider la commande", "Modifier la commande", "Annuler"]
        self.question = [{
            'type': 'list',
            'name' : 'Menu',
            'Message': 'Que voulez vous faire',
            'choices': list_choix
        }]
    
    def make_choice(self):        
        choix = prompt(self.question)