from pydantic import BaseModel

class Avis(BaseModel):
    """
    avis : str

    identifiant
    """
    #id_avis : int
    avis : str
    identifiant_auteur : str
    date: str #au format '13/11/2021 00:53:16'
    id_restaurant: str

        
        
    #def __str__(self) -> str:
       # print(self.avis)