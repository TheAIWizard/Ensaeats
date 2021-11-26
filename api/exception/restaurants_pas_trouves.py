class RestaurantsPasTrouvesException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, location : str):
        self.message = "Aucun restaurant n'a été trouvé autour de  "+location + ". Veuillez réessayez  "
        super().__init__(self.message)
