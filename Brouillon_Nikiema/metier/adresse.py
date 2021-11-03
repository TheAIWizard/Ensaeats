class Adresse():
    """
    This class define the adress

attribute
 num : int 
 num : it is the number street
    """

    def __init__(self, num: int, adresse : str,
         code_postal : int, ville : str, pays : str):
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays
        self.num_rue=num
        
    