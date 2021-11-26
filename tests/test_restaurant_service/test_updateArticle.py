from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.metier.article import Article


class TestupdateArticle(TestCase):
    def test_update_article(self):
        """ The goal here is to test if an article is updated properly in the PostgreSQL database"""
        # GIVEN
        expected_article=Article(id_article=50, nom='frites sans herbes', composition='sans herbes de Provence', type='accompagnement')
        article_to_update =Article(id_article=50, nom='frites aux herbes', composition='herbes de Provence', type='accompagnement')

        # WHEN
        article = RestaurantsService.updateArticle(expected_article)
        #retrieve as an article business object
        article=Article(id_article=article['id_article'] ,composition=article['composition'] , type=article['type_article'],nom=article['nom']   )

        # THEN
        self.assertEqual(expected_article, article)

if __name__=='__main__':
    unittest.main()