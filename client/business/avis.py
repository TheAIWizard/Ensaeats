from pydantic import BaseModel

class Avis(BaseModel):
    #id_avis : int
    avis : str
    identifiant_auteur : str
    date: str #au format '13/11/2021 00:53:16'
    id_restaurant: str

        
        
    def __str__(self) -> str:
       output = self.avis
       output += '. '
       output += self.date
       return output