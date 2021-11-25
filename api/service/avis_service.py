from typing import List
from api.service.client_service import ClientService
from api.dao.avis_DAO import AvisDao
from api.metier.avis import Avis


class AvisService:
    """
    La classe AvisService sert à communiquer avec notre API. Elle nous permettra de gerer les Avis sur l'API

    Attributes
    ---------


    Méthodes
    --------

    get_avis_by_id_restaurant  ():
        Cette méthodes permet de  consulter les avis dans la base de données
        retun : ???
    
    ajout_avis () :
    La fonction ajout_avis permet d'ajouter un avis dans la base deonnées SQL. 

    return : ??
    """
    @staticmethod
    def get_avis_by_id_restaurant(id_restaurant: str) -> List[Avis]:
        return AvisDao.find_avis_by_id_restaurant(id_restaurant=id_restaurant)

    @staticmethod
    def ajout_avis(avis: Avis) -> Avis:
        return AvisDao.add_avis(avis=avis)
       
    
  
        