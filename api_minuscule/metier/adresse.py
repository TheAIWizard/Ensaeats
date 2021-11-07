from pydantic import BaseModel

class Adresse(BaseModel):
    adresse : str
    code_postal : int
    ville : str
    pays : str

    def __str__(self) -> str:
        print(self.adresse + ' ' + self.code_postal + ' ' + self.ville + ' ' + self.pays)
