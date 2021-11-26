from unittest import TestCase
import unittest

<<<<<<< HEAD
from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
=======
from api.service.restaurant_service import RestaurantsService
import requests
>>>>>>> 9015b71f8b21648a7cd030bce05e2900515fa5d0

class TestgetRestaurant(TestCase):
    def test_get_restaurant(self):
        # GIVEN
        id_restaurant='LTy9AUgMnLn8YS21KfFZ8g'
        expected_response = {"id_restaurant": "LTy9AUgMnLn8YS21KfFZ8g", 
                            "adresse": {"adresse": "96 rue de la Poterie", "code_postal": 35700, "ville": "Rennes", "pays": "FR"}, 
                            "nom": "La Fontaine aux Perles", "statut": false}
            
        # WHEN
        response = RestaurantsService.getRestaurant(id=id_restaurant).json()
        # THEN
<<<<<<< HEAD
        self.assertEqual(power, damage)

=======
        print(response)
        print(expected_response)
        self.assertEqual(expected_response, response)

if __name__=='__main__':
    unittest.main()
>>>>>>> 9015b71f8b21648a7cd030bce05e2900515fa5d0
