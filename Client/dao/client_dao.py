from api.metier.client import Client
from api.dao.configuration import DBConnection
from client.exception.client_not_found_exception import ClientNotFoundException


class ClientDao:

    @staticmethod
    def verifyPassword(nom: str, prenom: str, mot_de_passe: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM client where client.nom=%(nom)s and client.prenom=%(prenom)s and client.mot_de_passe=%(mot_de_passe)s;"
                )
                res = cursor.fetchone()
            if res["nom"] != None:
                return True
            return False

    @staticmethod
    def getClient(nom: str, prenom: str) -> Client:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM client where client.nom=%(nom)s and client.prenom=%(prenom)s;"
                )
                res = cursor.fetchone()
        if res:
            return Client(nom=res["nom"], prenom=res["prenom"], mot_de_passe=res["mot_de_passe"])
        else:
            raise ClientNotFoundException(nom)

    @staticmethod
    def createClient(client: Client) -> Client:
        try:
            ClientDao.getClient(client.nom, client.prenom)
        except ClientNotFoundException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO client (nom, prenom, mot_de_passe) VALUES "
                        "(%(nom)s, %(prenom)s, %(mot_de_passe)s);", {"nom": client.nom, "prenom": client.prenom, "mot_de_passe": client.mot_de_passe})
            return ClientDao.getClient(client.nom, client.prenom)

    @staticmethod
    def updateClient(nom:str, prenom:str , client: Client) -> Client:
        client_to_update: Client = ClientDao.getClient(client.nom, client.prenom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE client SET nom=%(nom)s, prenom=%(prenom)s, mot_de_passe=%(mot_de_passe)s WHERE nom=%(ancien_nom)s, prenom=%(ancien_prenom)s;", {"nom": client_to_update.nom, "prenom": client_to_update.prenom, "mot_de_passe": client_to_update.mot_de_passe, "ancien_nom": client.nom, "ancien_prenom": client.prenom})

    @staticmethod
    def deleteclient(nom: str, prenom:str) -> Client:
        client_to_delete: Client = ClientDao.getClient(nom, prenom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Delete from client where nom=%(nom)s and prenom=%(prenom)s;", {"nom": client_to_delete.nom, "prenom": client_to_delete.prenom})
