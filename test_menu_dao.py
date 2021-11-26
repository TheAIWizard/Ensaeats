from api.service.yelp_api_service import YelpApiService
from api.service.yelp_mapper import YelpMapper
response = YelpApiService.get_businesses(location = "Bruz", radius = 2000)
print(YelpMapper.businesses_to_restaurants(response))


#print(test_menu.find_all_menus_by_id_restaurant(id_restaurant= 90072796))


#print(test_menu.find_all_menus_by_id_restaurant(90072796))

#print(MenuDao().add_menu_by_id_restaurant(menu_à_ajouter,9883186))
#print(MenuDao().find_menu_by_id_menu(333).nom_menu)

#print(MenuDao().add_menu_by_id_restaurant(menu_à_ajouter,9883186))
