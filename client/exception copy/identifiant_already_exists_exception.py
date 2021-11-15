class IdentifiantAlreadyExistsException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, identifiant:str):
        self.message = "Username "+identifiant+ " already exists"
        super().__init__(self.message)
