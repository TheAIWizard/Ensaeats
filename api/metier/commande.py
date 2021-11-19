from api.metier.menu import Menu 
from pydantic import BaseModel
from typing import List, Optional
from api.metier.adresse import Adresse

class Commande (BaseModel):

    """
    La classe commande permet de faire une commande

    Attribute
    ---------
    id_commande : int

    date : str

    statut_commande : str
    """
    id_commande : int
    date : str
    statut_commande : str
    liste_menu : List[Menu]
    liste_quantite : List[int]
        
    def prix_total(self):
        """Calcul du prix total
        """
        prix_total = 0
        for menu,quantite in zip(self.liste_menu, self.liste_quantite):
            prix_total += menu.prix*quantite
            
        return prix_total
    
    def ajout_menu(self, menu):
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
        
        output += "La somme à payer est : " + str(self.prix_total())
        output += '\n'
        output += '\n'
        return output

            
        

