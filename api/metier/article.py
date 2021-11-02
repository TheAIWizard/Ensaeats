class Article(): 
    def __init__(self, nom : str, composition : str, type : str):
        self.nom = nom
        self.composition = composition
        self.type = type
        self.id = 1 #implementer avec la base de données 