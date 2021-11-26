from pydantic import BaseModel
from datetime import datetime
#date actuelle
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

class Avis(BaseModel):
    """
    Cette classe permet à un client de donner son avis sur le restaurant. Elle permet d'avoir une idée de l'appréciation d'un restaurant par le client


    Attributes 
    ----------
    avis : str
            Avis permet au client de donner son appréciation sur la qualité du service du restaurant. 

    identifiant_auteur : str
            Permet quel avis correspond à un tel client

    date : str
            Perùmet de connaître la date à laquelle le client à laisser un avis

    id_restaurant : str
            Permet de connaître l' avis concerne quel restaurant 


    """
    avis : str
    identifiant_auteur : str
    date: str = now #au format '13/11/2021 00:53:16'
    id_restaurant: str

