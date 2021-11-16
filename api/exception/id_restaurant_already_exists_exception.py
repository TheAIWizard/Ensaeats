class RestaurantIDAlreadyExistsException(Exception):
    """Exception raised for errors when user not found

    Attributes:
        username -- username of the searched user
    """

    def __init__(self, id_restaurant:str):
        self.message = "Restaurant ID "+id_restaurant+ " already exists"
        super().__init__(self.message)
