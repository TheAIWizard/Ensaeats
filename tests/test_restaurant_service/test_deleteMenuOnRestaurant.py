from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.metier.menu import Menu
from api.metier.article import Article


class TestdeleteMenuonRestaurant(TestCase):
    def test_delete_menu_on_restaurant(self):
        """ The goal here is to test if a menu is deleted properly in the PostgreSQL database. 
        In fact, even if we want to delete a menu from a restaurant, we need to delete it in every tables of the database too. 
        That's why we don't need to give the restaurant id"""
        # GIVEN
       
        #The value 0 of the attibute id_article is given on purpose to be dealt by the auto-increment system of the database
        menu=Menu(  id_menu= 37,
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
        #we want to make sure menu,article1,article2 and article3 are erased from the database. 
        #The restorer will have to create new articles again if he wants a new menu
        expected_state=True,True,True

        # WHEN
        state = RestaurantsService.deleteMenuOnRestaurant(menu=menu)
        # THEN
        self.assertEqual(expected_state, state)

if __name__=='__main__':
    unittest.main()