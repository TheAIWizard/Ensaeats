from fastapi.exceptions import HTTPException
from api.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
from api.exception.identifiant_already_exists_exception import IdentifiantAlreadyExistsException
from api.exception.id_restaurant_already_exists_exception import RestaurantIDAlreadyExistsException
from api.exception.id_restaurateur_already_exists_exception import RestaurateurIDAlreadyExistsException
#from api_minuscule.service.DAO_mapper import DAOMapper
from api.metier.restaurateur import Restaurateur
from api.dao.restaurateur_dao import RestaurateurDao
from api.service.restaurant_service import RestaurantsService
from api.exception.restaurant_pas_trouve import RestaurantPasTrouveException

class RestaurateurService:
    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        try : 
            RestaurantsService.getRestaurant(restaurateur.id_restaurant) 
            if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant) == True):
                if RestaurateurDao.checkIdentifiantUniqueness(restaurateur.identifiant) == True :
                    return RestaurateurDao.createRestaurateur(restaurateur)
                else : 
                    raise RestaurateurIDAlreadyExistsException(identifant = restaurateur.identifiant)
            else:
                raise RestaurantIDAlreadyExistsException(id_restaurant=restaurateur.id_restaurant) 
        except :
            raise RestaurantPasTrouveException(restaurateur.id_restaurant)
    
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
                return RestaurantIDAlreadyExistsException(identifiant = restaurateur.identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)
    
    @staticmethod
    def authenticate_and_update_restaurateur(ancien_identifiant: str, ancien_mot_de_passe: str, restaurateur : Restaurateur) -> Restaurateur:
        # Vérification de l'identifiant et du mot de passe
        if (RestaurateurDao.verifyPassword(identifiant=ancien_identifiant, mot_de_passe=ancien_mot_de_passe) == True):
            ancien_client = RestaurateurDao.getRestaurateur(ancien_identifiant)
            # Vérification si l'identifiant du restaurateur est bien unique si modification 
            if (RestaurateurDao.checkIdentifiantUniqueness(restaurateur.identifiant) == True or ancien_identifiant == restaurateur.identifiant) :
                # Vérification si l'identifiant du restaurant est bien unique si modification
                try : 
                    RestaurantsService.getRestaurant(restaurateur.id_restaurant)
                    if (RestaurateurDao.checkRestaurantIdUniqueness(restaurateur.id_restaurant) == True or ancien_client.id_restaurant == restaurateur.id_restaurant):
                    # Si les trois vérifications sont faites -> update Restaurateur 
                        return RestaurateurDao.updateRestaurateur(ancien_identifiant, ancien_mot_de_passe, restaurateur)
                    else : 
                        raise RestaurantIDAlreadyExistsException(id_restaurant=restaurateur.id_restaurant)
                except : 
                    raise RestaurantPasTrouveException(id_restaurant= restaurateur.id_restaurant) 
            else : 
                raise RestaurateurIDAlreadyExistsException(identifiant = restaurateur.identifiant) 
        else:
            raise RestaurateurNotAuthenticated(identifiant=ancien_identifiant)
    
    @staticmethod
    def authenticate_and_delete_restaurateur(identifiant: str, mot_de_passe: str) -> Restaurateur:
        if (RestaurateurDao.verifyPassword(identifiant=identifiant, mot_de_passe=mot_de_passe)):
            return RestaurateurDao.deleteRestaurateur(identifiant)
        else:
            raise RestaurateurNotAuthenticated(identifiant=identifiant)