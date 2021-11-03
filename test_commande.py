from Tidiane_client_brouillon.dao.commande_dao import CommandeDAO
from Tidiane_client_brouillon.metier.panier import Panier
from brouillon.metier.menu import Menu


menu1 = Menu(1500, "Menu 1", 5)
menu2 = Menu(1544,"Menu2", 7)

panier1 = Panier([menu1, menu2])


com = CommandeDAO()

com.add_commande(20, panier1,"03-11-2021", 'En cours')


