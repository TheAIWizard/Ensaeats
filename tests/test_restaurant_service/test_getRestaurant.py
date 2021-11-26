from unittest import TestCase

from api.service.restaurant_service import RestaurantsService
from api.metier.restaurateur

class TestgetRestaurants(TestCase):
    def test_compute_damage(self):
        # GIVEN
        restaurateur=Restaurateur(id_restaurateur=)
        basic_hit = FixedDamageAttack(power=power)

        pikachu = AttackerPokemon()

        venusaur = AttackerPokemon()
        # WHEN
        damage = basic_hit.compute_damage(pikachu, venusaur)
        # THEN
        self.assertEqual(power, damage)
