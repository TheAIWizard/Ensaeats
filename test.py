from Brouillon_Nikiema.Restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao


#RestaurantsService.getRestaurants()
menu=MenuDao()
print(menu.find_all_menus()[0].nom_menu)