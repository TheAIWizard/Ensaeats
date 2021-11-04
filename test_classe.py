from Brouillon_Nikiema.metier.adresse import Adresse
from Brouillon_Nikiema.metier.article import Article
from Brouillon_Nikiema.metier.menu import Menu
from Brouillon_Nikiema.metier.avis import Avis
from Brouillon_Nikiema.metier.restaurant import Restaurant

test_adresse=Adresse(2,"rue d'alsace", "Rennes", 35000, "France")
test_article=Article(2,"piza","conl")
test_avis= Avis(89, "Tres bon","jean")

test_menu=Menu(65,"Menu japan","Feuille pilonne","fruits",
"coca", 25,test_article)

test_restaurant=Restaurant(100,test_adresse, "KFC", "ferme", "fast food", 
test_avis, test_menu)
