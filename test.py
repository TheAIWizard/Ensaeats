from api.service.restaurateur_service import RestaurateurService
import hashlib
from datetime import datetime
#format date 
now = datetime.now().strptime(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"%d/%m/%Y %H:%M:%S")
 
#print(RestaurateurService.authenticate_and_get_restaurateur('valmoulin2','valmoulin').id_restaurant)
print(hashlib.sha512(''.encode("utf-8")).hexdigest())
print(RestaurateurService.authenticate_and_get_restaurateur(identifiant="CrossMartin",mot_de_passe="CrossMartin"))
print(now)