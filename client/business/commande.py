from datetime import datetime
from client.business.menu import Menu 
from pydantic import BaseModel
from typing import List, Optional
from client.business.adresse import Adresse

class Commande (BaseModel):

    """
    La classe commande permet de faire une commande

    Attribute
    ---------
    id_commande : int
                Permet d'identifier une commande

    date : str
            permet de connapitre la date à laquelle la commande a été effectuée

    statut_commande : str
            Permet de connaître le statut de la commande. Les statut d'une commande 
            dans notre application sont :  enregistrée, en préparation, en livraison, livrée
    
    liste_menu : list 
            Permet de connaître la liste des menus dans une commande

    Méthodes
    -------
    prix_total (): 
        Cette fonction calcul le prix total d'une commande
            return : float


    ajout_menu() :
        Cette fonction permet d'ajouter un menu dans notre commande
            return : renvoie rien 

    """
    id_commande : int
    id_restaurant : str
    date : str
    statut_commande : str
    liste_menu : List[Menu]
    liste_quantite : List[int]
        
    def prix_total(self):
        """
        Cette méthode sert donner le prix total d'une commande en fonction des prix des articles

        """
        #prix_total = 0
        #for menu,quantite in zip(self.liste_menu, self.liste_quantite):
            #prix_total += menu.prix*quantite
            
        #return prix_total
    
        prix_total = 0
        for menu,quantite in zip(self.liste_menu, self.liste_quantite):
            prix_total += menu.prix*quantite
            
        return prix_total
    
    def ajout_menu(self, menu):
        """
        Cette méthode permet l'ajout d'un menu dans la commande
        """
        self.liste_menu.append(menu)
    
    ## Affichage du contenu de la commande
    def __str__(self) -> str:
        output = ''
        output += "La Commande contient :"
        output += '\n'
        for menu,quantite in zip(self.liste_menu, self.liste_quantite):
            output += menu.__str__()
            output += '\n'
            output += 'Quantite : ' + str(quantite)
            output += '\n'
            output += '\n'
        
        output += "La somme à payer est : " + str(self.prix_total()) + " Euros"
        output += '\n'
        output += '\n'
        return output

            
        

