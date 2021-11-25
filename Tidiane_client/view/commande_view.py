from PyInquirer import prompt, Separator
from pydantic.errors import ListError
from api.metier.menu import Menu
from client.view.liste_restaurant_view import RestaurantListeView
from client.dao.commande_dao import CommandeDAO
from api.metier.commande import Commande
from client.view.abstract_view import AbstractView


class Modif_commande(AbstractView):
    def __init__(self) -> None:
        list_choix = ["Ajouter menu", Separator(), "Modifier la quantité d'un menu", Separator(),
                      "Retirer un menu", Separator(), 'Valider', Separator(), 'Annuler']
        self.question = [{
            'type': 'list',
            'name' : 'Menu',
            'message': 'Que voulez vous faire',
            'choices': list_choix
        }]
    
    def display_info(self):
        ## Afficher le contenu de la commande
        print("-----------------------------------------")
        print(AbstractView.session.commande_active)
        print("-----------------------------------------")
    
    
    
    def make_choice(self):
        choix = prompt(self.question)
        ## Ajouter un menu
        if choix["Menu"]== 'Ajouter menu':
            from client.view.menu_list_view import MenuListView
            return MenuListView()
        
        ## Modifier la quantité d'un menu
        if choix["Menu"] == "Modifier la quantité d'un menu":
            commande = AbstractView.session.commande_active
            list_nom_menu = [menu.nom for menu in commande.liste_menu]
            list_nom_menu.append(Separator())
            list_nom_menu.append("Annuler")
            question = [{
            'type': 'list',
            'name' : 'Menu',
            'message': 'Choisir un menu',
            'choices': list_nom_menu
            }]
            menu_quantite_modif = prompt(question)
            if menu_quantite_modif['Menu'] == 'Annuler':
                from client.view.commande_view import Modif_commande
                return Modif_commande()
            else : 
                index = list_nom_menu.index(menu_quantite_modif['Menu'])
                menu_cible = commande.liste_menu[index]
                print("La quantite associe à ce menu est : ", commande.liste_quantite[index])
                new_quantite = int(input("Nouvelle quantite: "))
                from client.service.commande_service import Faire_commande
                AbstractView.session.commande_active = Faire_commande.ajout_quantite_menu(commande, menu_cible, new_quantite)
                print("Modification effectuée")
                input("Appuyer sur entrer pour continuer")
                from client.view.commande_view import Modif_commande
                return Modif_commande()
        
        elif choix["Menu"]== 'Retirer un menu':
            ## Retirer menu
            commande = AbstractView.session.commande_active
            list_nom_menu = [menu.nom for menu in commande.liste_menu]
            list_nom_menu.append(Separator())
            list_nom_menu.append("Annuler")
            question = [{
            'type': 'list',
            'name' : 'Menu',
            'message': 'Choisir un menu',
            'choices': list_nom_menu
            }]
            menu_retire = prompt(question)
            if menu_retire['Menu'] == 'Annuler':
                from client.view.commande_view import Modif_commande
                return Modif_commande()
            else:
                idex_select = list_nom_menu.index(menu_retire['Menu'])
                menu_sup = commande.liste_menu[idex_select]
                          
                supprim_question = [{
                    'type': 'list',
                    'name': 'Supp',
                    'message': 'Voulez vous vraiment supprimez ce menu',
                    'choices': ['Oui', Separator(), 'Non']
                }]

                supprim_reponse = prompt(supprim_question)

                if supprim_reponse['Supp'] == 'Oui': 
                    from client.service.commande_service import Faire_commande
                    AbstractView.session.commande_active = Faire_commande.supprime_menu(commande, menu_sup)
                    print("Menu supprimer avec succès !")
                    input("Appuyer sur enter pour continuer")
                    from client.view.commande_view import Modif_commande
                    return Modif_commande()
                else:
                    from client.view.commande_view import Modif_commande
                    return Modif_commande()
          
        elif choix['Menu'] == 'Valider':
            ## Valider la commande
            from client.view.valide_commande_view import Valider
            return Valider() 
        else: 
            ## Annuler
            ## Effacer les informations en session sur la commande
            AbstractView.session.commande_active = None
            AbstractView.session.list_menu = []
            AbstractView.session.list_quantite = []
            AbstractView.session.menu_actif = None
            from client.view.menu_list_view import MenuListView
            return MenuListView()