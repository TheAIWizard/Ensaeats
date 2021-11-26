from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.metier.article import Article


class TestdeleteArticle(TestCase):
    def test_delete_article(self):
        """ The goal here is to test if an article is deleted properly in the PostgreSQL database (by its id)
        when an article is deleted, it shall not appear in table_menu_article and article. We check its presence with a couple of booleans"""
        # GIVEN
        expected_state=True,True
        article_to_delete =Article(id_article=2, nom='frites sans herbes', composition='sans herbes de Provence', type='accompagnement')

        # WHEN
        article = RestaurantsService.deleteArticle(article_to_delete)
        # THEN
        self.assertEqual(expected_state, article)

if __name__=='__main__':
    unittest.main()