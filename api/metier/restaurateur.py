from pydantic import BaseModel

""" class Restaurateur(BaseModel):
    nom: str
    prenom: str
    mot_de_passe: str """

class Restaurateur(BaseModel):
    nom: str
    prenom: str
    identifiant: str
    mot_de_passe: str
    id_restaurant: str