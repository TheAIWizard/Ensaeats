class Adresse():
    def __init__(self, adresse : str, code_postal : int, ville : str, pays : str):
        self.adresse = adresse
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays
    
    def __str__(self) -> str:
        print(self.adresse + ' ' + self.code_postal + ' ' + self.ville + ' ' + self.pays)

