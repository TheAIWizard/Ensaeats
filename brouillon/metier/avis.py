from pydantic import BaseModel

class Avis(BaseModel):
    #id_avis : int
    avis : str
    nom_auteur : str

        
        
    def __str__(self) -> str:
        output = self.avis
        output += '\n'
        output += 'Auteur: '
        output += '\n'
        output += self.nom_auteur

        return output