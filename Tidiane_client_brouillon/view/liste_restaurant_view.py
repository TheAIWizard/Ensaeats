from PyInquirer import prompt, Separator

from view.abstract_view import AbstractView

from api.service.restaurant_service import RestaurantsService

class RestaurantListeView(AbstractView):
    def __init__(self) -> None:
        ## Liste des restaurants
        liste_restaurant = RestaurantsService.getRestaurants(AbstractView.session.localite,
                        AbstractView.session.nom_restaurant, AbstractView.session.radius)
        
        ## Liste avec uniquement les noms
        self.liste_nom_restaurant = [restaurant.nom for restaurant in liste_restaurant]
        
        ## Creation de la liste de choix
        choix_restaurant = self.liste_nom_restaurant
        choix_restaurant.append(Separator())
        choix_restaurant.append("Retour Accueil")
        self.questions = [
            {
                'type': 'list',
                'name': 'restaurant',
                'message': 'Veuillez choisir un restaurant',
                'choices': choix_restaurant
            }
        ]
        
        def display_info(self):
            pass

        def make_choice(self):
            reponse = prompt(self.questions)
            if reponse["restaurant"] == "Retour Accueil":
                from view.welcom_view import WelcomeView
                return WelcomeView()
            else: 
                ## Recuperons le restaurant actif et renvoi la page restaurant view
                index = self.liste_nom_restaurant.index(reponse["restaurant"])
                AbstractView.session.restaurant_actif = liste_restaurant[index]
                from view.restaurant_view import RestaurantView
                return RestaurantView()
            
            
            