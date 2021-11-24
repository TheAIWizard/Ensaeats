from api.service.restaurateur_service import RestaurateurService
import hashlib


#print(RestaurateurService.authenticate_and_get_restaurateur('valmoulin2','valmoulin').id_restaurant)
print(hashlib.sha512(''.encode("utf-8")).hexdigest())
print(RestaurateurService.authenticate_and_get_restaurateur(identifiant="CrossMartin",mot_de_passe="CrossMartin"))