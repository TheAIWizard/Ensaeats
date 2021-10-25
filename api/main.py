from service.yelp_api_service import YelpApiService
from service.restaurant_service import RestaurantsService


print(YelpApiService.get_businesses('Bruz'))
print(RestaurantsService.getRestaurants(location = 'Bruz'))