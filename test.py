from Brouillon_Nikiema.Restaurant_service import RestaurantsService

from brouillon.DAO.restaurant_DAO import RestaurantDao

#RestaurantsService.getRestaurants()
menu=RestaurantDao()
print(menu.find_id_restaurant_by_name("Falafel"))
