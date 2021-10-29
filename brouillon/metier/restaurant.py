
class Restaurant :
    """Constructeur des restaurants
    
    """
    
    def __init__(self, id_restau,
                 nom_restau,
                 statut_restau,
                 specialite) -> None:
        self.id_restau = id_restau
        self.nom_restau = nom_restau
        self.statut_restau = statut_restau
        self.specialite = specialite
        
    def ajout_menu(self, menu):
        pass
    
    def enleve_menu(self, menu):
        pass
    
    def ajout_avis(self):
        pass