from api_minuscule.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api_minuscule.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
from api_minuscule.exception.identifiant_already_exists_exception import IdentifiantAlreadyExistsException
from api_minuscule.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
#from api_minuscule.service.DAO_mapper import DAOMapper
from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.dao.restaurateur_dao import RestaurateurDao


class RestaurateurService:
    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant))&(RestaurateurDao.checkIdentifiantUniqueness(restaurateur.identifiant)):
            return RestaurateurDao.createRestaurateur(restaurateur)
        else:
            raise RestaurantIDAlreadyExistsException(id_restaurant=restaurateur.id_restaurant) 
        
        

    @staticmethod
    def getRestaurateur(identifiant: str) -> Restaurateur:
        return RestaurateurDao.getRestaurateur(identifiant)

    @staticmethod
    def updateRestaurateur(ancien_identifiant: str, ancien_mot_de_passe:str, identifiant: str, mot_de_passe:str) -> Restaurateur:
        return RestaurateurDao.updateRestaurateur(ancien_identifiant, ancien_mot_de_passe, identifiant, mot_de_passe)

    @staticmethod
    def deleteRestaurateur(restaurateur_id: str) -> Restaurateur:
        return RestaurateurDao.deleteRestaurateur(restaurateur_id)

    @staticmethod
    def authenticate_and_get_restaurateur(identifiant: str, password: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant, password)):
            return RestaurateurDao.getRestaurateur(identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)

    @staticmethod
    def authenticate_and_create_restaurateur(identifiant: str, password: str, restaurateur:Restaurateur) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant, password)):
            #on vérifie si un autre restaurateur n'a pas déjà le même id_restaurant
            if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant)):
                return RestaurateurDao.createRestaurateur(restaurateur)
            else:
                return RestaurantIDAlreadyExistsException
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)
    
    @staticmethod
    def authenticate_and_update_restaurateur(ancien_identifiant: str, ancien_password: str, identifiant: str, password: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(ancien_identifiant, ancien_password)):
            return RestaurateurDao.updateRestaurateur(ancien_identifiant, ancien_password, identifiant, password)
        else:
            raise RestaurateurNotAuthenticated(identifiant=ancien_identifiant)
    
    @staticmethod
    def authenticate_and_delete_restaurateur(identifiant: str, password: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant, password)):
            return RestaurateurDao.deleteRestaurateur(identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)