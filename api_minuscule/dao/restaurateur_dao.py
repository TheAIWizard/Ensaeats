from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.dao.configuration import DBConnection
from api_minuscule.exception.restaurateur_not_found_exception import RestaurateurNotFoundException
import hashlib


class RestaurateurDao:

    @staticmethod
    def verifyPassword(identifiant: str, mot_de_passe: str) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM restaurateur where restaurateur.identifiant=%(identifiant)s and restaurateur.mot_de_passe=%(mot_de_passe)s;"
                )
                res = cursor.fetchone()
            if res["nom"] != None:
                return True
            return False

    @staticmethod
    def checkRestaurantIdUniqueness(id_restaurant: str) -> bool:
        """ vérifier qu'un id_restaurant n'existe pas déjà"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM restaurateur where restaurateur.id_restaurant=%(id_restaurant)s;"
                )
                res = cursor.fetchone()
            if res["nom"] != None:
                return False
            return True
        

    @staticmethod
    def checkIdentifiantUniqueness(identifiant: str) -> bool:
        """ vérifier que l'identifiant proposé par le restaurateur s'authetifiant n'est pas déjà utilisé"""
        """ vérifier qu'un id_restaurant n'existe pas déjà"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM restaurateur where restaurateur.identifiant=%(identifiant)s;"
                )
                res = cursor.fetchone()
            if res["nom"] != None:
                return False
            return True
    


    @staticmethod
    def getRestaurateur(identifiant: str) -> Restaurateur:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM restaurateur where restaurateur.identifiant=%(identifiant)s;"
                )
                res = cursor.fetchone()
        if res:
            return Restaurateur(nom=res["nom"], prenom=res["prenom"], identifiant=res["identifiant"], mot_de_passe=res["mot_de_passe"], id_restaurant=res["id_restaurant"])
        else:
            raise RestaurateurNotFoundException(identifiant)

    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        #il faudrait hacher le mot de passe : hashlib.sha512(x.encode("utf-8")).hexdigest(), 16) : cet algo de hachage retourne le même hachage pour la même entrée
        #rien ne change en pratique, juste la colonne mot_de_passe qui n'est pas en clair, on compare les hash entre eux
        try:
            RestaurateurDao.getRestaurateur(restaurateur.identifiant)
        except RestaurateurNotFoundException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO restaurateur (nom, prenom, identifiant, mot_de_passe, id_restaurant) VALUES "
                        "(%(nom)s, %(prenom)s, %(identifiant)s, %(mot_de_passe)s, %(id_restaurant)s));", {"nom": restaurateur.nom, "prenom": restaurateur.prenom, "identifiant": restaurateur.identifiant, "mot_de_passe": restaurateur.mot_de_passe, "id_restaurant": restaurateur.id_restaurant})
            return RestaurateurDao.getRestaurateur(restaurateur.identifiant)

    @staticmethod
    def updateRestaurateur(identifiant:str, restaurateur: Restaurateur) -> Restaurateur:
        # le restaurateur peut changer n'importe quelle information qu'il souhaite sur son statut
        restaurateur_to_update: Restaurateur = RestaurateurDao.getRestaurateur(identifiant)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE identifiant=%(identifiant)s, mot_de_passe=%(mot_de_passe)s WHERE identifiant=%(ancien_identifiant)s, mot_de_passe=%(ancien_mot_de_passe)s;", {"identifiant": restaurateur_to_update.identifiant, "mot_de_passe": restaurateur.mot_de_passe, "ancien_identifiant":restaurateur.identifiant, "ancien_mot_de_passe":restaurateur.mot_de_passe})

    @staticmethod
    def deleteRestaurateur(identifiant:str) -> Restaurateur:
        restaurateur_to_delete: Restaurateur = RestaurateurDao.getRestaurateur(identifiant)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "Delete from restaurateur where identifiant=%(identifiant)s;", {"identifiant": restaurateur_to_delete.identifiant})

