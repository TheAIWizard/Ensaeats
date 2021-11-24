from unittest import TestCase

from api.service.re


class TestBasicFormulaAttack(TestCase):
    def test_compute_damage(self):
        # GIVEN
        power = 100
        basic_hit = FixedDamageAttack(power=power)

        pikachu = AttackerPokemon()

        venusaur = AttackerPokemon()
        # WHEN
        damage = basic_hit.compute_damage(pikachu, venusaur)
        # THEN
        self.assertEqual(power, damage)
