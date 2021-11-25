from pydantic import BaseModel
from client.business.adresse import Adresse
class Client(BaseModel):
    """
    La classe client permet d'identifier un client dans notre application

    Attribute
    --------
    id_client : int
                Permet d'identifier un client

    nom : str
         Le nom du client

    prenom : str
            Le prenom du client

    adresse : Adresse
            Prendre l'adresse du client.

    identifiant : str
            Est un identifiant servant à identifier le client

    mot_de_passe : str
            Le mot de passe du client

    telephone : str
             Le numero de telephone du client
    """
    id_client: int
    nom: str
    prenom: str
    adresse: Adresse = None
    identifiant: str
    mot_de_passe: str
    telephone: str
