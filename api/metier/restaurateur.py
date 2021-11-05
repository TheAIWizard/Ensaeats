from pydantic import BaseModel

class Restaurateur(BaseModel):
    nom: str
    prenom: str
    mot_de_passe: str
