from api.metier.commande import Commande
from api.dao.commande_dao import CommandeDAO
from api.metier.client import Client
from api.metier.restaurant import Restaurant
from datetime  import datetime

class CommandeService:
    
    today = datetime.today().strftime('%Y-%m-%d')
    @staticmethod
    def faire_commande(liste_menu, liste_quantite, date= today, statut_commande = 'En cours', id_commande = 1):
        return Commande(id_commande = id_commande, date = date, statut_commande=statut_commande, liste_menu=liste_menu, liste_quantite = liste_quantite)
    
    @staticmethod
    def supprime_menu(commande: Commande, menu_sup):
        index_sup = commande.liste_menu.index(menu_sup)
        commande.liste_menu.remove(menu_sup)
        del commande.liste_quantite[index_sup]
        return commande
    
    @staticmethod
    def ajout_menu(commande: Commande, menu, quantite):
        commande.liste_menu.append(menu)
        commande.liste_quantite.append(quantite)
        return commande
    
    @staticmethod
    def ajout_quantite_menu(commande: Commande, menu_choisi, nouvelle_quant):
        index_menu = commande.liste_menu.index(menu_choisi)
        commande.liste_quantite[index_menu] = nouvelle_quant
        return commande       
        
    @staticmethod 
    def valider_commande(commande: Commande, id_client : int):
        """[Ajouter la commande de l'utilisateur]

        Args:
            commande ([Commande]): [Commande faite par l'utilisateur]
        """
        CommandeDAO.add_commande(commande, id_client)
        
    
    @staticmethod 
    def obtenir_commandes_client(client : Client) : 
        return CommandeDAO.obtenir_commandes_par_client(client)

    @staticmethod 
    def obtenir_commandes_id_restaurant(id_restaurant : str) : 
        return CommandeDAO.obtenir_commandes_par_id_restaurant(id_restaurant=id_restaurant)