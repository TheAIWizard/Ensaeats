from API.metier.restaurateur import Restaurateur
from API.dao.configuration import DBConnection
from API.exception.restaurateur_not_found_exception import RestaurateurNotFoundException

class RestaurateurDao:

    @staticmethod
    def verifyPassword(nom: str, prenom: str, mot_de_passe: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM restaurateur where restaurateur.nom=%(nom)s and restaurateur.prenom=%(prenom)s and restaurateur.mot_de_passe=%(mot_de_passe)s;"
                )
                res = cursor.fetchone()
            if res["nom"] != None:
                return True
            return False

    @staticmethod
    def getRestaurateur(nom: str, prenom: str) -> Restaurateur:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM restaurateur where restaurateur.nom=%(nom)s and restaurateur.prenom=%(prenom)s;"
                )
                res = cursor.fetchone()
        if res:
            return Restaurateur(nom=res["nom"], prenom=res["prenom"], mot_de_passe=res["mot_de_passe"])
        else:
            raise RestaurateurNotFoundException(nom)

    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        try:
            RestaurateurDao.getRestaurateur(restaurateur.nom, restaurateur.prenom)
        except RestaurateurNotFoundException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO restaurateur (nom, prenom, mot_de_passe) VALUES "
                        "(%(nom)s, %(prenom)s, %(mot_de_passe)s);", {"nom": restaurateur.nom, "prenom": restaurateur.prenom, "mot_de_passe": restaurateur.mot_de_passe})
            return RestaurateurDao.getRestaurateur(restaurateur.nom, restaurateur.prenom)

    @staticmethod
    def updateRestaurateur(nom:str, prenom:str , restaurateur: Restaurateur) -> Restaurateur:
        restaurateur_to_update: Restaurateur = RestaurateurDao.getRestaurateur(restaurateur.nom, restaurateur.prenom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE restaurateur SET nom=%(nom)s, prenom=%(prenom)s, mot_de_passe=%(mot_de_passe)s WHERE nom=%(ancien_nom)s, prenom=%(ancien_prenom)s, ;", {"nom": restaurateur_to_update.nom, "prenom": restaurateur_to_update.prenom, "mot_de_passe": restaurateur.mot_de_passe, "ancien_nom":restaurateur.nom, "ancien_prenom":restaurateur.prenom})

    @staticmethod
    def deleteRestaurateur(nom: str, prenom:str) -> Restaurateur:
        restaurateur_to_delete: Restaurateur = RestaurateurDao.getRestaurateur(nom, prenom)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Delete from restaurateur where nom=%(nom)s and prenom=%(prenom)s;", {"nom": restaurateur_to_delete.nom, "prenom": restaurateur_to_delete.prenom})
