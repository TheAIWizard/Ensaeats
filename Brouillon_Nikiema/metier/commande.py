from Brouillon_Nikiema.metier.menu import Menu 

from pydantic import BaseModel
class Commande (BaseModel):
    id_commande : int
    date : str
    paiement : float
    statut_commande : str
    list_menu : list
    menu : Menu

  