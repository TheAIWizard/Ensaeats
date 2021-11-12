from pydantic.main import BaseModel
class Adresse(BaseModel):
    num : int
    adresse : str
    code_postal : str
    ville : str
    pays : str
    

        