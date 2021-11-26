from unittest import TestCase
import unittest
import pandas as pd

from api.exception.restaurant_pas_trouve import RestaurantPasTrouveException
from api.service.restaurant_service import RestaurantsService
import requests

class TestgetRestaurants(TestCase):
    
    def test_get_restaurants(self):
        # GIVEN
        term,location,radius='pizza','Bruz','20000000'
        mauvais_id_restaurant='faux-id'

        expected_response = []
        # WHEN
        response = RestaurantsService.getRestaurants(term=term,location=location,radius=radius)
        # THEN
        print(response)
        """when the radius is too high the programm should stop"""
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()
