from pydantic import BaseModel

class Client(BaseModel):
    nom: str
    prenom: str
    adresse: str
    identifiant: str
    mot_de_passe: str
    telephone: str
