
from api.metier.commande import Commande
from datetime  import datetime
import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request

class Faire_commande:
    
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
    def valider_commande(identifiant, mot_de_passe, commande: Commande):
        """[Ajouter la commande de l'utilisateur]

        Args:
            commande ([Commande]): [Commande faite par l'utilisateur]
        """
        ## Requete post 
        output = False
        params_post_commande = {'identifiant_client': identifiant,
                                'mot_de_passe_client': mot_de_passe}
        post_commande = requests.post('http://localhost:5000/commande/',
                                     json = dict(commande),
                                     params = params_post_commande).json()
        if post_commande: 
            output = True
            return output
        return output    
   