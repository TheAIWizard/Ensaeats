from Brouillon_Nikiema.Restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from brouillon.metier.menu import Menu

#RestaurantsService.getRestaurants()
menu=MenuDao()
menu_à_ajouter=Menu(10002,'Menu la spéciale',1000)
print(menu.add_menu(menu_à_ajouter))