from pydantic import BaseModel

class Avis(BaseModel):
    #id_avis : int
    avis : str
    nom_auteur : str

        
        
    #def __str__(self) -> str:
       # print(self.avis)