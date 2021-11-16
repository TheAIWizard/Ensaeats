from api.service.restaurateur_service import RestaurateurService



print(RestaurateurService.authenticate_and_get_restaurateur('valmoulin2','valmoulin').id_restaurant)
