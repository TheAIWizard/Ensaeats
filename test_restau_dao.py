from brouillon.DAO.restaurant_DAO import RestaurantDao
from brouillon.metier.restaurant import Restaurant

test_restau = RestaurantDao()

print(test_restau.find_id_restaurant_by_name('Falafel'))
print(test_restau.find_restaurant_by_id_restau())