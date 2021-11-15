from Tidiane_client_brouillon.view.abstract_view import AbstractView
from PyInquirer import prompt, Separator
from brouillon.metier.avis import Avis
from Tidiane_client_brouillon.dao.avis_DAO import AvisDao

class AvisView(AbstractView):
    def __init__(self) -> None:
        list_choix = ['Ajouter un avis', Separator(), 'Voir les menus', Separator(), 'Liste des restaurants',Separator(), 'Accueil']
        self.question = [{
            'type': 'list',
            'name': 'Menu',
            'message': 'Que voulez vous faire',
            'choices': list_choix
        }]

    def display_info(self):
        for avis in AbstractView.session.listeAvis:
            print(avis)
            print("\n")
    

    def make_choice(self):
        reponse = prompt(self.question)

        if reponse['Menu'] == 'Ajouter un avis':
            ## Ajoute ton avis sur le restaurant
            avis_txt = input('Donner votre avis : ')
            avis_user = Avis(avis = avis_txt, nom_auteur = AbstractView.session.client.prenom)
            ## Ajout avis dans la base de données
            result =  AvisDao.add_avis(avis_user)
            print(result)
            input("Appuyer sur entrer pour retourner")
            from Tidiane_client_brouillon.view.restaurant_view import RestaurantView
            return RestaurantView()

        elif reponse['Menu'] == 'Voir les menus':
            ## Voir menus
            from Tidiane_client_brouillon.view.menu_list_view import MenuListView
            return MenuListView()
        elif reponse['Menu'] == 'Liste des restaurants':
            from Tidiane_client_brouillon.view.liste_restaurant_view import RestaurantListeView
            return RestaurantListeView()
        else: 
            ## Retour à l'accueil
            from Tidiane_client_brouillon.view.welcom_view import WelcomeView
            return WelcomeView()    
            