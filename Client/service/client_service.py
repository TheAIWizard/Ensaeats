from Client.exception.client_not_authenticated_exception import ClientNotAuthenticated
#from Client.exception.id_Client_already_exists_exception import ClientIDAlreadyExistsException
#from Client.exception.identifiant_already_exists_exception import IdentifiantAlreadyExistsException
#from Client.exception.id_Client_already_exists_exception import ClientIDAlreadyExistsException
#from Client.service.DAO_mapper import DAOMapper
from Client.business.client import Client
from Client.dao.client_dao import ClientDao


class ClientService:
    @staticmethod
    def createClient(client: Client) -> Client:
        if (ClientDao.checkClientIdUniqueness(client.id_restaurant))&(ClientDao.checkIdentifiantUniqueness(client.identifiant)):
            return ClientDao.createClient(client)
        #else:
           # raise RestaurantIDAlreadyExistsException(id_restaurant=client.id_restaurant) 
        
        

    @staticmethod
    def getClient(identifiant: str) -> Client:
        return ClientDao.getClient(identifiant)

    @staticmethod
    def updateClient(ancien_identifiant: str, ancien_mot_de_passe:str, identifiant: str, mot_de_passe:str) -> Client:
        return ClientDao.updateClient(ancien_identifiant, ancien_mot_de_passe, identifiant, mot_de_passe)

    @staticmethod
    def deleteClient(client_id: str) -> Client:
        return ClientDao.deleteClient(client_id)

    @staticmethod
    def authenticate_and_get_client(identifiant: str, password: str) -> Client:
        if (ClientDao.verifyPassword(identifiant, password)):
            return ClientDao.getClient(identifiant)
        else:
            raise ClientNotAuthenticated(identifiant=identifiant)

    @staticmethod
    def authenticate_and_create_client(identifiant: str, password: str, client:Client) -> Client:
        if (ClientDao.verifyPassword(identifiant, password)):
            #on vérifie si un autre client n'a pas déjà le même id_restaurant
            if (ClientDao.checkRestaurantIdUniqueness(client.id_restaurant)):
                return ClientDao.createClient(client)
            #else:
                #return RestaurantIDAlreadyExistsException
        else:
            raise ClientNotAuthenticated(identifiant=identifiant)
    
    @staticmethod
    def authenticate_and_update_client(ancien_identifiant: str, ancien_password: str, identifiant: str, password: str) -> Client:
        if (ClientDao.verifyPassword(ancien_identifiant, ancien_password)):
            return ClientDao.updateClient(ancien_identifiant, ancien_password, identifiant, password)
        else:
            raise ClientNotAuthenticated(identifiant=ancien_identifiant)
    
    @staticmethod
    def authenticate_and_delete_client(identifiant: str, password: str) -> Client:
        if (ClientDao.verifyPassword(identifiant, password)):
            return ClientDao.deleteClient(identifiant)
        else:
            raise ClientNotAuthenticated(identifiant=identifiant)