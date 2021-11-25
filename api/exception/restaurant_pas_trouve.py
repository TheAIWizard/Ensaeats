class RestaurantPasTrouveException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, id_restaurant : str):
        self.message = "Restaurant "+id_restaurant + " n'est pas dans l'API de Yelp"
        super().__init__(self.message)
