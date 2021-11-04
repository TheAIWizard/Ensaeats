
class Avis:
    """Constructeur des avis
    """
    def __init__(self, id_avis: int, avis: str) -> None:
        self.id_avis = id_avis
        self.avis = avis
        
        
    def __str__(self) -> str:
        print(self.avis)