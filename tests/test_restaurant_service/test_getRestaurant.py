from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
import requests

class TestgetRestaurant(TestCase):
    def test_get_restaurant(self):
        # GIVEN
        id_restaurant='LTy9AUgMnLn8YS21KfFZ8g'
        my_key = "jXH_gWewLB5gj0iJ6i55_TspH58WVWWTsKPZLJZej0SpLycR5Y_MWHnBwb5AcPMAUSYW3ud87VnSkxW2JMIb4xiEduf-KS0HpzEyB8wfWSw-q-Ko8u-38WtiPXFyYXYx"
        url = "https://api.yelp.com/v3/businesses/{}".format(id_restaurant)
        headers = {"Authorization" : "Bearer "+my_key}

        expected_response = requests.get(url, params={"id": id_restaurant}, headers={'Authorization': "bearer "+my_key}).json()
            
        # WHEN
        response = RestaurantsService.getRestaurant(id=id_restaurant)
        # THEN
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()