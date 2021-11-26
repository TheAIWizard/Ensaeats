from unittest import TestCase
import unittest
import pandas as pd

from api.service.restaurant_service import RestaurantsService
import requests

class TestgetRestaurants(TestCase):
    
    def test_get_restaurants(self):
        # GIVEN
        term,location,radius='pizza','Bruz','5000'

        expected_response = [{"id_restaurant": "6lAItmD8hHO-VpwOmBJUvQ","adresse": {"adresse": "Place Marcel Pagnol","code_postal": 35170,"ville": "Bruz","pays": "FR"},
                             "nom": "Le Pagnol","statut": 'false'}
                             ,{"id_restaurant": "u-thZtaNQbLQkhFOR_AVHQ","adresse": {"adresse": "7 avenue de la Marionnais","code_postal": 35131,"ville": "Chartres-de-Bretagne","pays": "FR"},
                             "nom": "I Fratelli e la Mamma","statut": 'false'}
                             ,{"id_restaurant": "H_rFw63pi68Oq7V1eJSwCA","adresse": {"adresse": "58 Rue De La Poterie","code_postal": 35131,"ville": "Chartres De Bretagne","pays": "FR"},
                             "nom": "Le 58","statut": 'false'}
                             ]
        #suppress the column 'statut'
        expected_response=pd.DataFrame(expected_response)#[['id_restaurant','adresse','nom']].to_json()
            
        # WHEN
        response = RestaurantsService.getRestaurants(term=term,location=location,radius=radius)
        response = pd.DataFrame(response)#[['id_restaurant','adresse','nom']].to_json()
        print(expected_response)
        print(response)
        # THEN
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()
