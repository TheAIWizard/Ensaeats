from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.metier.menu import Menu
from api.metier.article import Article


class TestaddMenuonRestaurant(TestCase):
    def test_add_menu_on_restaurant(self):
        """ The goal here is to test if a menu is added properly in the PostgreSQL database"""
        # GIVEN
        id_restaurant='LTy9AUgMnLn8YS21KfFZ8g'
        #The value 0 of the attibute id_article is given on purpose to be dealt by the auto-increment system of the database
        menu=Menu(  id_menu= 0,
                nom= "Menu printannier",
                prix= 54,
                article1= Article(
                id_article= 5,
                nom= "Le tout caramel",
                composition= "Biscuit streusel noisette, pâte à choux et glace caramel ",
                type= "dessert"
                ),
                article2= Article(
                id_article= 6,
                nom= "Carpaccio de betterave",
                composition= "Mariné soja et gingembre, betterave, framboise et café",
                type= "entrée"
                ),
                article3= Article(
                id_article= 7,
                nom= "Les champignons",
                composition= "Gâteau de girolles, cèpe rôti, artichaut poivrade et jus de viande truffé",
                type= "plat"
                )
        )
        expected_state=True

        # WHEN
        state = RestaurantsService.addMenuOnRestaurant(id_restaurant=id_restaurant,menu=menu)
        # THEN
        self.assertEqual(expected_state, state)

if __name__=='__main__':
    unittest.main()