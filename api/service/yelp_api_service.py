import requests

my_key = "jXH_gWewLB5gj0iJ6i55_TspH58WVWWTsKPZLJZej0SpLycR5Y_MWHnBwb5AcPMAUSYW3ud87VnSkxW2JMIb4xiEduf-KS0HpzEyB8wfWSw-q-Ko8u-38WtiPXFyYXYx"

class YelpApiService():
    # Permet de récupérer un json des restaurants selon id (get_business_by_id) ou par location et term

    @staticmethod
    def get_business_by_id(id : str):
        ''' Récupère un json du restaurant qui correspond à l'id pris en entrée '''
        
        url = "https://api.yelp.com/v3/businesses/{}".format(id)
        headers = {"Authorization" : "Bearer "+my_key}
        response = requests.get(url, params={"id": id}, headers={'Authorization': "bearer "+my_key})
        return response.json()

    @staticmethod
    def get_businesses(location : str, term : str = '', radius : int = 3000):

        # Cette fonction permet de récupérer les informations des restaurants en fonction de 
        # la localisation, du term : nom du restaurant, et du term 

        url = "https://api.yelp.com/v3/businesses/search"
        headers = {"Authorization" : "Bearer "+my_key}
        response = requests.get(url, params={"term": term, "location": location, "limit": 50, "sort_by" : 'rating', "categories":'Restaurants',"radius":radius}, headers={'Authorization': "bearer "+my_key})
        return response.json()



