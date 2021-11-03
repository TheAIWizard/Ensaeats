from Tidiane_client_brouillon.dao.commande_dao import CommandeDAO
from brouillon.metier.commande import Commande
from brouillon.metier.menu import Menu


menu1 = Menu(1500, "Menu 1", 5)
menu2 = Menu(1544,"Menu2", 7)
list_menu = [menu1, menu2]

command = Commande(21, "23-3-2021", "En cour", list_menu)



comDAO = CommandeDAO()

comDAO.add_commande(command)


