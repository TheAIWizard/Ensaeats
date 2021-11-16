class ClientNotFoundException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, identifiant: str):
        self.message = "User "+identifiant + " not found"
        super().__init__(self.message)
