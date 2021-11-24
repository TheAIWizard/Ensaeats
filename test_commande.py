
import api.metier.commande as Commande
import api.dao.menu_dao as menu_dao

menu = menu_dao.MenuDao.find_menu_by_id_menu(1)
command = Commande(id_commande = 0, date = "23-3-2021", statut_commande = "En cours", liste_menu = [menu], liste_quantite = [1])


#client = Client(id_client = 9999, nom = 'Moulin', prenom= 'Valentine', adresse= 'lalala', identifiant= 'valmoulin', mot_de_passe= 1234,telephone= '0621')

#comDAO = CommandeDAO()

#comDAO.add_commande(command)


