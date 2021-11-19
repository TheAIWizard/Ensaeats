from api.dao.menu_dao import MenuDao
from api.metier.menu import Menu

#test_menu=MenuDao()
#menu_à_ajouter=Menu(333,"la spéciale",1000)
#menu_à_modifier=Menu(333,"la spéciale",100)

print(MenuDao.get_id_restaurant_by_id_menu(1))
print(MenuDao.find_menu_by_id_menu(1))

#print(test_menu.find_all_menus_by_id_restaurant(id_restaurant= 90072796))


#print(test_menu.find_all_menus_by_id_restaurant(90072796))

#print(MenuDao().add_menu_by_id_restaurant(menu_à_ajouter,9883186))
#print(MenuDao().find_menu_by_id_menu(333).nom_menu)

#print(MenuDao().add_menu_by_id_restaurant(menu_à_ajouter,9883186))
