from unittest import TestCase
import unittest

from api.service.restaurant_service import RestaurantsService
from api.metier.menu import Menu
from api.metier.article import Article


class TestgetMenusbyidrestaurant(TestCase):
    def test_get_menus_by_id_restaurant(self):
        # GIVEN
        id_restaurant='LTy9AUgMnLn8YS21KfFZ8g'
        expected_menus=[
        Menu(id_menu=1, nom='Menu retour du marché du 26 au 30 Octobre 2021', prix=34, article1=Article(id_article=2, nom='frites aux herbes', composition='herbes de Provence', type='accompagnement'), article2=Article(id_article=3, nom='Cannelloni de courge', composition='Butternut, farce boudin, pommes et vinaigrette au jus de viande', type='entrée'), article3=Article(id_article=4, nom='Aile de raie', composition='Rôtie au beurre noisette, chou-fleur et choux de Bruxelles, sauce crémeuse au chorizo', type='plat'))
        ,Menu(id_menu=2, nom='Menu légumes', prix=54, article1=Article(id_article=5, nom='Le tout caramel', composition='Biscuit streusel noisette, pâte à choux et glace caramel ', type='dessert'), article2=Article(id_article=6, nom='Carpaccio de betterave', composition='Mariné soja et gingembre, betterave, framboise et café', type='entrée'), article3=Article(id_article=7, nom='Les champignons', composition='Gâteau de girolles, cèpe rôti, artichaut poivrade et jus de viande truffé', type='plat'))
        ,Menu(id_menu=3, nom='Menu plaisir', prix=51, article1=Article(id_article=8, nom='L’agrume', composition='Crème diplomate au citron, chocolat blanc, pomelos et sorbet mandarine/estragon', type='dessert'), article2=Article(id_article=9, nom='Radis colorés', composition='Cuits, crus en pickles, navets glacés, lentilles Beluga, vinaigrette au jus de blue meat', type='entrée'), article3=Article(id_article=10, nom='Coquilles Saint Jacques', composition='Cuites au bouillon, anguille fumée, pak choï et poivre des mers', type='plat'))
        ,Menu(id_menu=4, nom='Menu épicurien', prix=89, article1=Article(id_article=14, nom='Sélection de 3 Fromages\\xa0de la Maison Bordier', composition='Citron vert et crème glacée au poivre Andaliman ', type='dessert'), article2=Article(id_article=15, nom='Les huîtres', composition='Cuisinées en trois façons : épinard/fruits de la passion, calamansi/sancho, poudre des Indes/poire', type='entrée'), article3=Article(id_article=16, nom='Le flétan', composition='Radis colorés de notre maraîcher, lentilles Beluga et fumet corsé au vin rouge', type='plat'))
        ]

        # WHEN
        menus = RestaurantsService.getMenus_by_id_restaurant(id_restaurant=id_restaurant)
        # THEN
        self.assertEqual(expected_menus, menus)

if __name__=='__main__':
    unittest.main()