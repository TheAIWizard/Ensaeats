from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.exception.restaurant_pas_trouve import RestaurantPasTrouveException

class TestgetRestaurant(TestCase):
    def test_get_restaurant(self):
        """ the goal is to show what kind of errors occurs when the id of the restorer is wrong"""
        # GIVEN
        mauvais_id_restaurant='faux-id'
        # WHEN
        expected_response=RestaurantPasTrouveException(mauvais_id_restaurant)
        # THEN
        response = RestaurantsService.getRestaurant(id=mauvais_id_restaurant).json()
        """the test should stop with the error: raise RestaurantPasTrouveException(id_restaurant=id) 
        api.exception.restaurant_pas_trouve.RestaurantPasTrouveException: Restaurant faux-id n'est pas dans l'API de Yelp """
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()
