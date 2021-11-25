class RestaurateurIDAlreadyExistsException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, identifiant:str):
        self.message = "Restauranteur identifiant "+identifiant+ " existe déjà"
        super().__init__(self.message)
