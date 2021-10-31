from requests.models import Response
from service.yelp_mapper import YelpMapper
from service.yelp_api_service import YelpApiService
from service.restaurant_service import RestaurantsService

response = YelpApiService.get_businesses('Bruz')
#print(response)

#print(response['businesses'])
#print(YelpMapper.businesses_to_restaurants(response))

response = YelpApiService.get_business_by_id('CGAMpQITh8-6lAYuY-oD4A')
print(type(response['name']))

#print(RestaurantsService.getRestaurangitts(location = 'Bruz'))