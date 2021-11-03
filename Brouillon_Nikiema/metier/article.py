class Article :
    def __init__(self, id_article : int, nom_article : str, 
     type_article : str) -> None :
        self.id_article=id_article
        self.nom_article=nom_article
        self.type_article=type_article
    
    def str(self):
           
        return "{} {} {}".format(str(self.id_article), 
        str(self.nom_article), str(self.type_article))

    def affiche(self):
        print(self.str()) 