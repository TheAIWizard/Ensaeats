from client.exception.client_not_authenticated_exception import ClientNotAuthenticated
#from Client.exception.id_Client_already_exists_exception import ClientIDAlreadyExistsException
#from Client.exception.identifiant_already_exists_exception import IdentifiantAlreadyExistsException
#from Client.exception.id_Client_already_exists_exception import ClientIDAlreadyExistsException
#from Client.service.DAO_mapper import DAOMapper
from client.business.client import Client
from client.business.avis import Avis
from client.dao.client_dao import ClientDao
from api.dao.menu_dao import MenuDao
from client.dao.avis_DAO import AvisDao

class ClientService:
    @staticmethod
    def createClient(client: Client) -> Client:
            return ClientDao.createClient(client)
        
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
    def authenticate_and_get_client(identifiant: str, mot_de_passe: str) -> Client:
        if (ClientDao.verifyPassword(identifiant, mot_de_passe)):
            return ClientDao.getClient(identifiant)
        else:
            raise ClientNotAuthenticated(identifiant=identifiant)

    @staticmethod
    def authenticate_and_create_client(identifiant: str, password: str, client:Client) -> Client:
        if (ClientDao.verifyPassword(identifiant, password)):
                return ClientDao.createClient(client)
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

    @staticmethod
    def consulter_menu(id_restaurant: str):
        """ Affiche au client la liste des menus suivis de leur composition"""
        return [(menu.nom, str(menu.prix)+' €', menu.article1.nom, menu.article2.nom, menu.article3.nom)for menu in MenuDao.find_all_menus_by_id_restaurant(id_restaurant)]

    @staticmethod
    def consulter_avis(id_restaurant: str):
        return AvisDao.find_avis_by_id_restaurant(id_restaurant)

    @staticmethod
    def ajouter_avis(avis: Avis):
        return AvisDao.add_avis(avis)
        
        