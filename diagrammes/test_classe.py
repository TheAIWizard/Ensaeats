from Brouillon_Nikiema.metier.adresse import Adresse
from Brouillon_Nikiema.metier.article import Article
from Brouillon_Nikiema.metier.menu import Menu

test_adresse=Adresse(2,"rue d'alsace", "Rennes", 35000, "France")

test_article=Article(2, "Pasta", "Jean")


test_menu=Menu(65,"Menu japan","Feuille pilonne","fruits",
"coca", 25,test_article)
test_menu.affiche()