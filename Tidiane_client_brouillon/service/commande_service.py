
from brouillon.metier.commande import Commande
from Tidiane_client_brouillon.dao.commande_dao import CommandeDAO
from datetime  import datetime

class Faire_commande:
    
    today = datetime.today()
    @staticmethod
    def faire_commande(id_commande, liste_menu, liste_quantite, date= , statut_commande = 'En cours'):
        return Commande(id_commande, date, statut_commande, liste_menu, liste_quantite)
    
    @staticmethod
    def supprime_menu(commande: Commande, menu_sup):
        index_sup = commande.liste_menu.index(menu_sup)
        commande.liste_menu.remove(menu_sup)
        del commande.list_quantite[index_sup]
        return commande
    
    @staticmethod
    def ajout_menu(commande: Commande,menu, quantite):
        commande.liste_menu.append(menu)
        commande.list_quantite.append(quantite)
        
    @staticmethod 
    def valider_commande(commande: Commande):
        """[Ajouter la commande de l'utilisateur]

        Args:
            commande ([Commande]): [Commande faite par l'utilisateur]
        """
        CommandeDAO.add_commande(commande)