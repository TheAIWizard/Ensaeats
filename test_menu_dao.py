from brouillon.DAO.menu_DAO import MenuDao
from brouillon.metier.menu import Menu

test_menu=MenuDao()
menu_à_ajouter=Menu(333,"la spéciale",1000)

#print(test_menu.find_all_menus_by_id_restaurant(90072796))
print(MenuDao().add_menu_by_id_restaurant(menu_à_ajouter,9883186))
