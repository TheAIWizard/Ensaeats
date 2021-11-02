from Brouillon_Nikiema.adresse import Adresse

class Restaurant():
    def __init__(self, id_restaurant : str, nom : str, adresse: Adresse, statut : bool): 
        self.id_restaurant = id_restaurant
        self.nom = self.nom 
        self.adresse = adresse
        self.statut = statut
    
