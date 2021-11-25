from api.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
from api.exception.identifiant_already_exists_exception import IdentifiantAlreadyExistsException
from api.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
from api.exception.id_restaurateur_already_exists_exception import RestaurateurIDAlreadyExistsException
#from api_minuscule.service.DAO_mapper import DAOMapper
from api.metier.restaurateur import Restaurateur
from api.dao.restaurateur_dao import RestaurateurDao
from api.service.restaurant_service import RestaurantsService

class RestaurateurService:
    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        #if (RestaurantsService.getRestaurant())
        if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant) == True):
            if RestaurateurDao.checkIdentifiantUniqueness(restaurateur.identifiant) == True :
                return RestaurateurDao.createRestaurateur(restaurateur)
            else : 
                raise RestaurateurIDAlreadyExistsException(identifant = restaurateur.identifiant)
        else:
            raise RestaurantIDAlreadyExistsException(id_restaurant=restaurateur.id_restaurant) 

    @staticmethod
    def getAvis(identifiant: str) -> Restaurateur:
        return RestaurateurDao.getRestaurateur(identifiant)

    @staticmethod
    def updateRestaurateur(ancien_identifiant: str, ancien_mot_de_passe:str, identifiant: str, mot_de_passe:str) -> Restaurateur:
        return RestaurateurDao.updateRestaurateur(ancien_identifiant, ancien_mot_de_passe, identifiant, mot_de_passe)

    @staticmethod
    def deleteRestaurateur(restaurateur_id: str) -> Restaurateur:
        return RestaurateurDao.deleteRestaurateur(restaurateur_id)

    @staticmethod
    def authenticate_and_get_restaurateur(identifiant: str, mot_de_passe: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant=identifiant, mot_de_passe=mot_de_passe)):
            return RestaurateurDao.getRestaurateur(identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)

    @staticmethod
    def authenticate_and_create_restaurateur(identifiant: str, mot_de_passe: str, restaurateur:Restaurateur) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant=identifiant, mot_de_passe=mot_de_passe)):
            #on vérifie si un autre restaurateur n'a pas déjà le même id_restaurant
            if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant)):
                return RestaurateurDao.createRestaurateur(restaurateur)
            else:
                return RestaurantIDAlreadyExistsException
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)
    
    @staticmethod
    def authenticate_and_update_restaurateur(ancien_identifiant: str, ancien_mot_de_passe: str, identifiant: str, mot_de_passe: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant=ancien_identifiant, mot_de_passe=ancien_mot_de_passe)):
            return RestaurateurDao.updateRestaurateur(ancien_identifiant, ancien_mot_de_passe, identifiant, mot_de_passe)
        else:
            raise RestaurateurNotAuthenticated(identifiant=ancien_identifiant)
    
    @staticmethod
    def authenticate_and_delete_restaurateur(identifiant: str, mot_de_passe: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant=identifiant, mot_de_passe=mot_de_passe)):
            return RestaurateurDao.deleteRestaurateur(identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)