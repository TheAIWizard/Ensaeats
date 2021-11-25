from pydantic import BaseModel

class Adresse(BaseModel):
    """
    Cette classe permet d'avoir l'adresse d'un lieu (restaurant) ou d'une personne (client ou restaurateur)

    Attributes
    ----------
    code_postal : int
                désigne le code postale

    ville       : str
                 la ville ou se situe le restaurant ou celle ou le client ou le restaurateur réside

    pays        : str
                pays est le pays

    adresse     : str
                adresse  est le numero + la rue  

    
    Méthode
    -------
    __str__ () : 
                Permet l'affichage d'une adresse
    """
    adresse : str 
    code_postal : int 
    ville : str
    pays : str 

    def __str__(self) -> str:
        print(self.adresse + ' ' + str(self.code_postal) + ' ' + self.ville + ' ' + self.pays)
