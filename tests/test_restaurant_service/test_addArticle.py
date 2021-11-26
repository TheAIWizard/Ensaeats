from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.metier.article import Article


class TestaddArticle(TestCase):
    def test_add_article(self):
        """ The goal here is to test if an article is added properly in the PostgreSQL database"""
        # GIVEN
        
        #The value 0 of the attibute id_article is given on purpose to be dealt by the auto-increment system of the database
        article =Article(id_article=50, nom='frites aux herbes', composition='herbes de Provence', type='accompagnement')
        expected_state=True

        # WHEN
        state = RestaurantsService.addArticle(article=article)
        # THEN
        self.assertEqual(expected_state, state)

if __name__=='__main__':
    unittest.main()