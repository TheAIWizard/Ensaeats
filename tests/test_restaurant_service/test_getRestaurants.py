from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
import requests

class TestgetRestaurants(TestCase):
    
    def test_get_restaurants(self):
        # GIVEN

        my_key = "jXH_gWewLB5gj0iJ6i55_TspH58WVWWTsKPZLJZej0SpLycR5Y_MWHnBwb5AcPMAUSYW3ud87VnSkxW2JMIb4xiEduf-KS0HpzEyB8wfWSw-q-Ko8u-38WtiPXFyYXYx"
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {"Authorization" : "Bearer "+my_key}
        term,location,radius='etudiant','Bruz','10000'

        expected_response = requests.get(url, params={"term": term, "location": location, "limit": 50, "sort_by" : 'rating', "categories":'Restaurants',"radius":radius}, 
                                headers={'Authorization': "bearer "+my_key}).json()
            
        # WHEN
        response = RestaurantsService.getRestaurants(term=term,location=location,radius=radius)
        # THEN
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()
