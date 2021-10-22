import requests

class ApiServices():
    # Permet de récupérer un json des restaurants selon id (get_business_by_id) ou par location et term
    def __init__(self):
        self.__my_key = "jXH_gWewLB5gj0iJ6i55_TspH58WVWWTsKPZLJZej0SpLycR5Y_MWHnBwb5AcPMAUSYW3ud87VnSkxW2JMIb4xiEduf-KS0HpzEyB8wfWSw-q-Ko8u-38WtiPXFyYXYx"

    def get_business_by_id(self, id : str):
        url = "https://api.yelp.com/v3/businesses/{}".format(id)
        headers = {"Authorization" : "Bearer "+self.__my_key}
        response = requests.get(url, params={"id": id}, headers={'Authorization': "bearer "+self.__my_key})
        return response.json

    def get_businesses(self, location : str, term : str = ''):
        # Cette fonction permet de récupérer les informations des restaurants en fonction de 
        # la localisation, du term : nom du restaurant, et du term 
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {"Authorization" : "Bearer "+self.__my_key}
        response = requests.get(url, params={"term": term, "location": location, "categories":'food'}, headers={'Authorization': "bearer "+self.__my_key})
        return response.json



