class Avis :
    def __init__(self, id_avis : int, avis : str, nom_auteur : str) -> None :
        self.id_avis=id_avis
        self.avis=avis
        self.nom_auteur=nom_auteur

    def str(self):
           
        return "{} {} {}".format(str(self.id_avis), 
        str(self.avis), str(self.nom_auteur))

    def affiche(self):
        print(self.str()) 
        