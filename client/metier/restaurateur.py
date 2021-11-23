from pydantic import BaseModel

class Restaurateur(BaseModel):
    """
    La classe restaurateur permet de connaître les information sur le restaurateur

    Attributes
    --------
    nom : str
        Le nom de famille du restaurateur

    prenom : str
        Le prenom du restaurateur

    identifiant : str
        Identifiant du restaurateur

    mot_de_pass : str
        Le mot de passe du restaurateur

    id_restaurant : str
    Identifiant du restaurant
    """
    nom: str
    prenom: str
    identifiant: str
    mot_de_passe: str
    id_restaurant: str
