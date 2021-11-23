from typing import List
from api.service.client_service import ClientService
from api.dao.avis_DAO import AvisDao
from api.metier.avis import Avis


class AvisService:

    @staticmethod
    def get_avis_by_id_restaurant(id_restaurant: str) -> List[Avis]:
        return AvisDao.find_avis_by_id_restaurant(id_restaurant=id_restaurant)

    @staticmethod
    def ajout_avis(avis: Avis) -> Avis:
        return AvisDao.add_avis(avis=avis)
       
    
  
        