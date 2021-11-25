from client.view.abstract_view import AbstractView
from PyInquirer import prompt, Separator

from client.view.session import Session

class MenuView(AbstractView):
    def __init__(self) -> None:
        self.menu_choix = AbstractView.session.menu_actif
        
        
    def display_info(self):
        print('--------------------------------')
        print(self.menu_choix)
        
        
    
    def make_choice(self):
        question_ajout = [{
            'type': 'list',
            'name': 'ajout_choix',
            'message': "Voulez vous l'ajouter au panier ?",
            'choices': ['Oui', Separator(), 'Non']
        }]
        reponse_ajout = prompt(question_ajout)
        if reponse_ajout['ajout_choix'] == 'Oui':
            print("\n")
            quantite = int(input("Quantite de ce menu: "))
            ## Ajouter le menu à la liste des menus en session et faire
            ## une commande en attente de validation
            AbstractView.session.list_menu.append(self.menu_choix)
            AbstractView.session.quantite_menu = quantite
            AbstractView.session.list_quantite.append(quantite)
            
            from client.service.commande_service import Faire_commande
            AbstractView.session.commande_active = Faire_commande.faire_commande(AbstractView.session.list_menu, 
                                                            AbstractView.session.list_quantite)
            print("\n")
            print("Menu ajouté à la commande")
            print("\n")
            
            ## Demande d'ajout d'autre menu si l'utilisateur le souhaite
            question2 = [{
                'type': 'list',
                'name': 'Menu',
                'message': 'Que voulez vous faire',
                'choices': ['Ajouter un autre menu', Separator(), 'Voir la commande', 
                            Separator(), 'Annuler la commande']
            }]
            reponse2 = prompt(question2)
            if reponse2['Menu'] == 'Ajouter un autre menu':
                from client.view.menu_list_view import MenuListView
                return MenuListView()
            elif reponse2['Menu'] == 'Voir la commande': 
                from client.view.commande_view import Modif_commande
                return Modif_commande()
            else: 
                AbstractView.session.list_menu = []
                AbstractView.session.list_quantite = []
                AbstractView.session.commande_active = None
                from client.view.menu_list_view import MenuListView
                return MenuListView()
            
        else:
            ## Revenir à la liste des menus
            from client.view.menu_list_view import MenuListView
            return MenuListView()
            
        
        