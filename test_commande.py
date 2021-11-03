from Tidiane_client_brouillon.dao.commande_dao import CommandeDAO
from Tidiane_client_brouillon.metier.panier import Panier
from brouillon.metier.menu import Menu


menu1 = Menu("Menu 1", 5)
menu2 = Menu("Menu2", 7)

panier1 = Panier([menu1, menu2])


com = CommandeDAO()

com.add_commande(panier1, "03/11/2021", "En cours")


