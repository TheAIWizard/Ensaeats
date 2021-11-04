from brouillon.DAO.avis_DAO import AvisDao
from brouillon.metier.avis import Avis

test_avis = AvisDao()
avis = Avis(666, "Sah quel plaisir ce restaurant !")

print(test_avis.find_avis_by_id_restaurant(id_restaurant= 75115434))

print(test_avis.add_avis(avis, id_restaurant= 75115434))