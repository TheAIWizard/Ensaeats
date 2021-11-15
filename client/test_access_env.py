from client.business.client import Client
from client.service.client_service import ClientService
from client.business.avis import Avis
from datetime import datetime

# Tidiane --> pour avoir la date !!!
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#Alex=Client(nom="Martin",prenom="Alex",adresse="36 rue des coquelicots",identifiant="KingAlex35",mot_de_passe="1234",telephone="07.25.98.15.38")
#avis=Avis(avis="Sah quel plaisir ce restaurant, Une tuerie !", identifiant_auteur="KingAlex35", date='2021-11-13',id_restaurant="NL0ROvACBWrwYv1BZxBWtQ")

#print(ClientService.consulter_avis("NL0ROvACBWrwYv1BZxBWtQ"))
#print(ClientService.ajouter_avis(avis))
print(ClientService.consulter_menu("LTy9AUgMnLn8YS21KfFZ8g"))
print(ClientService.authenticate_and_get_client("KingAlex35","KingAlex35"))
