from pydantic import BaseModel
from api.metier.adresse import Adresse

class Client(BaseModel):
    id_client: str
    nom: str
    prenom: str
    adresse: Adresse
    identifiant: str
    mot_de_passe: str
    telephone: str
