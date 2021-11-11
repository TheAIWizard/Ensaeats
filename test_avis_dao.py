from brouillon.DAO.avis_DAO import AvisDao
from brouillon.metier.avis import Avis

test_avis = AvisDao
avis = Avis(avis="Sah quel plaisir ce restaurant !", nom_auteur="Martin")

print(test_avis.find_avis_by_id_restaurant(id_restau="NL0ROvACBWrwYv1BZxBWtQ"))

print(test_avis.add_avis(avis, id_restau= "NL0ROvACBWrwYv1BZxBWtQ")) 