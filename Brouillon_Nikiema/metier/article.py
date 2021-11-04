from pydantic import BaseModel
class Article (BaseModel):
    id_article : int
    nom_article : str
    type_article : str
    