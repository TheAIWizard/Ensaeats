class RestaurateurNotFoundException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, nom: str, prenom:str):
        self.message = "User "+nom+" "+prenom+ " not found"
        super().__init__(self.message)
