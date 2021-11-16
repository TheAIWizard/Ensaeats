from pydantic import BaseModel

class Client(BaseModel):
    id_client: str
    nom: str
    prenom: str
    adresse: str
    identifiant: str
    mot_de_passe: str
    telephone: str
