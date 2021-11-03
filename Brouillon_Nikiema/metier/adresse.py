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


    def str(self):
           
        return "{} {} {} {} {}".format(str(self.num_rue), str(self.adresse), str(self.code_postal),
        str(self.ville), str(self.pays))

    def affiche(self):
        print(self.str()) 
        
    