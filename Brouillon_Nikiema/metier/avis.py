from pydantic.main import BaseModel
class Avis (BaseModel):
    id_avis : int
    avis : str
    nom_auteur : str
    