from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
import requests

class TestgetRestaurant(TestCase):
    def test_get_restaurant(self):
        # GIVEN
        mauvais_id_restaurant='faux id'
        id_restaurant='LTy9AUgMnLn8YS21KfFZ8g'
        expected_response = {"id_restaurant": "LTy9AUgMnLn8YS21KfFZ8g", 
                            "adresse": {"adresse": "96 rue de la Poterie", "code_postal": 35700, "ville": "Rennes", "pays": "FR"}, 
                            "nom": "La Fontaine aux Perles", "statut": false}
            
        # WHEN
        response = RestaurantsService.getRestaurant(id=id_restaurant).json()
        # THEN
        print(response)
        print(expected_response)
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()
