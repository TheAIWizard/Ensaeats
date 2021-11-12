from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.dao.configuration import DBConnection
from api_minuscule.exception.restaurateur_not_found_exception import RestaurateurNotFoundException
import hashlib

""" Par rapport aux risques d'injections SQL: notre code est protégé contre les injections SQL. 
La bibliothèque psycopg, en voyant %(identifiant)s va le remplacer par la valeur de l'entrée username du dictionnaire passé en second paramètre, 
effectuant toutes les transformations nécessaires pour que les caractères dangereux soient neutralisés"""

class RestaurateurDao:

    @staticmethod
    def verifyPassword(identifiant: str, mot_de_passe: str) -> bool:
        #on compare le hachage du mot de passe entré et stocké dans la base de données
        hash_mot_de_passe=hashlib.sha512(mot_de_passe.encode("utf-8")).hexdigest()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM ensaeats.restaurateur where identifiant=%(identifiant)s and mot_de_passe=%(mot_de_passe)s;"
                    ,{"identifiant": identifiant, "mot_de_passe": hash_mot_de_passe}
                )
                res = cursor.fetchone()
            if res != None:
                return True
            return False

    @staticmethod
    def checkRestaurantIdUniqueness(id_restaurant: str) -> bool:
        """ On aurait pu faire un try mais cette méthode est plus spécifique: faible couplage, forte cohésion"""
        """ vérifier qu'un id_restaurant n'existe pas déjà"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM ensaeats.restaurateur WHERE id_restaurant=%(id_restaurant)s;",
                    {"id_restaurant":id_restaurant}
                )
                res = cursor.fetchone()
            print(type(res))
            if res != None:
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
                    "\nFROM ensaeats.restaurateur WHERE identifiant=%(identifiant)s;",
                    {"identifiant":identifiant}
                )
                res = cursor.fetchone()
            if res != None:
                return False
            return True
    
    @staticmethod
    def getRestaurateur(identifiant: str) -> Restaurateur:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "\nFROM ensaeats.restaurateur WHERE identifiant=%(identifiant)s;",
                    {"identifiant":identifiant}
                )
                res = cursor.fetchone()
        if res != None:
            return Restaurateur(nom=res["nom"], prenom=res["prenom"], identifiant=res["identifiant"], mot_de_passe=res["mot_de_passe"], id_restaurant=res["id_restaurant"])
        else:
            raise RestaurateurNotFoundException(identifiant)

    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        #il faudrait hacher le mot de passe : hashlib.sha512(x.encode("utf-8")).hexdigest(), 16 : cet algo de hachage retourne le même hachage pour la même entrée
        #rien ne change en pratique, juste la colonne mot_de_passe qui n'est pas en clair, on compare les hash entre eux
        hash_mot_de_passe=hashlib.sha512(restaurateur.mot_de_passe.encode("utf-8")).hexdigest()
        #vérifie si le profil du restaurateur n'existe pas déjà
        try:
            RestaurateurDao.getRestaurateur(restaurateur.identifiant)
        except RestaurateurNotFoundException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    #on sauvegarde le mot de passe sous forme haché. Ce sont les hachages qui seront comparés pour l'authentification
                    cursor.execute(
                        "INSERT INTO ensaeats.restaurateur (nom, prenom, identifiant, mot_de_passe, id_restaurant) VALUES "
                        "(%(nom)s, %(prenom)s, %(identifiant)s, %(mot_de_passe)s, %(id_restaurant)s);", {"nom": restaurateur.nom, "prenom": restaurateur.prenom, "identifiant": restaurateur.identifiant, "mot_de_passe": hash_mot_de_passe, "id_restaurant": restaurateur.id_restaurant})
            print(hash_mot_de_passe)
            return RestaurateurDao.getRestaurateur(restaurateur.identifiant)

    @staticmethod
    def updateRestaurateur(ancien_identifiant:str, ancien_mot_de_passe:str, identifiant:str, mot_de_passe:str) -> Restaurateur:
        #on compare les mots de passe par leur hachage
        hash_ancien_mot_de_passe=hashlib.sha512(ancien_mot_de_passe.encode("utf-8")).hexdigest()
        hash_mot_de_passe=hashlib.sha512(mot_de_passe.encode("utf-8")).hexdigest()
        # le restaurateur peut changer n'importe quelle information qu'il souhaite sur son statut
        parameters_requests={}
        #Si l'identifiant n'est pas renseigné, on reprend l'ancien identifiant
        if identifiant is None:
            parameters_requests={"identifiant": ancien_identifiant, "mot_de_passe": hash_mot_de_passe, "ancien_identifiant":ancien_identifiant}
        #Si le mot de passe n'est pas renseigné, on reprend l'ancien mot de passe
        elif mot_de_passe is None:
            parameters_requests={"identifiant": identifiant, "mot_de_passe": hash_ancien_mot_de_passe, "ancien_identifiant":ancien_identifiant}
        #sinon, on met à jour identifiant et mot de passe
        else:
            parameters_requests={"identifiant": identifiant, "mot_de_passe": hash_mot_de_passe, "ancien_identifiant":ancien_identifiant}
        #on effectue la requête SQl sur Postgre
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE ensaeats.restaurateur SET identifiant=%(identifiant)s, mot_de_passe=%(mot_de_passe)s WHERE identifiant=%(ancien_identifiant)s;", parameters_requests)
        #retourner les modifications qui vont apparaître sur l'interface de fast-api
        return RestaurateurDao.getRestaurateur(identifiant) if identifiant else RestaurateurDao.getRestaurateur(ancien_identifiant)

    @staticmethod
    def deleteRestaurateur(identifiant:str) -> Restaurateur:
        restaurateur_to_delete: Restaurateur = RestaurateurDao.getRestaurateur(identifiant)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("Delete from ensaeats.restaurateur where identifiant=%(identifiant)s;", {"identifiant": restaurateur_to_delete.identifiant})
        return "User "+identifiant+" deleted"

   