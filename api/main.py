from requests.models import Response
from service.yelp_mapper import YelpMapper
from service.yelp_api_service import YelpApiService
from service.restaurant_service import RestaurantsService

response = YelpApiService.get_businesses('Bruz')
#print(response)

#print(response['businesses'])


response = YelpApiService.get_business_by_id('CGAMpQITh8-6lAYuY-oD4A')
print(response)

response = YelpApiService.get_businesses(location = 'Bruz')
print(response)

print(YelpMapper.businesses_to_restaurants(response))
print(RestaurantsService.getRestaurants(location ='Bruz'))
