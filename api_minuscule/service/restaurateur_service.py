from api_minuscule.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api_minuscule.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
from api_minuscule.exception.identifiant_already_exists_exception import IdentifiantAlreadyExistsException
from api_minuscule.service.DAO_mapper import DAOMapper
from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.dao.restaurateur_dao import RestaurateurDao


class RestaurateurService:
    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        return RestaurateurDao.createRestaurateur(restaurateur)
        #if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant))&(RestaurateurDao.checkIdentifiantUniqueness(restaurateur.identifiant)):
        #    return RestaurateurDao.createRestaurateur(restaurateur)
        #else:
           # raise RestaurantIDAlreadyExistsException(id_restaurant=restaurateur.id_restaurant) 
        
        

    @staticmethod
    def getRestaurateur(identifiant: str) -> Restaurateur:
        return RestaurateurDao.getRestaurateur(identifiant)

    @staticmethod
    def updateRestaurateur(identifiant: str, restaurateur: Restaurateur) -> Restaurateur:
        return RestaurateurDao.updateRestaurateur(identifiant, restaurateur)

    @staticmethod
    def deleteRestaurateur(restaurateur_id: str) -> Restaurateur:
        return RestaurateurDao.deleteRestaurateur(restaurateur_id)

    @staticmethod
    def authenticate_and_get_restaurateur(identifiant: str, password: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant, password)):
            return RestaurateurDao.getRestaurateur(identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)
