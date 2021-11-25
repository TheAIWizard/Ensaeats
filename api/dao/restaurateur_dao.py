from api.metier.restaurateur import Restaurateur
from api.dao.db_connection import DBConnection
from api.exception.restaurateur_not_found_exception import RestaurateurNotFoundException
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
            print(res)
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
            print(type(res))
            print(res)
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


    staticmethod
    def checkidRestaurant(id_restaurant: str) -> bool:
        """ vérifier que l'identifiant proposé par le restaurateur s'authetifiant n'est pas déjà utilisé"""
        """ vérifier qu'un id_restaurant n'existe pas déjà"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM ensaeats.restaurant WHERE id_restaurant=%(id_restaurant)s;",
                    {"id_restaurant":id_restaurant}
                )
                res = cursor.fetchone()
            if res != None:
                return False
            return True
        
    @staticmethod
    def createRestaurateur(restaurateur: Restaurateur) -> Restaurateur:
        #il faudrait hacher le mot de passe : hashlib.sha512(x.encode("utf-8")).hexdigest(), 16 : cet algo de hachage retourne le même hachage pour la même entrée
        #rien ne change en pratique, juste la colonne mot_de_passe qui n'est pas en clair, on compare les hash entre eux
        hash_mot_de_passe=hashlib.sha512(restaurateur.mot_de_passe.encode("utf-8")).hexdigest()
        #vérifie si le profil du restaurateur n'existe pas déjà
        if RestaurateurDao.checkidRestaurant(restaurateur.id_restaurant) == True :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO ensaeats.restaurant (id_restaurant) VALUES "
                        "(%(id_restaurant)s);", {"id_restaurant" : restaurateur.id_restaurant})
            
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                #on sauvegarde le mot de passe sous forme haché. Ce sont les hachages qui seront comparés pour l'authentification
                cursor.execute(
                    "INSERT INTO ensaeats.restaurateur (nom, prenom, identifiant, mot_de_passe, id_restaurant) VALUES "
                    "(%(nom)s, %(prenom)s, %(identifiant)s, %(mot_de_passe)s, %(id_restaurant)s);"
                    , {"nom": restaurateur.nom, "prenom": restaurateur.prenom, "identifiant": restaurateur.identifiant, "mot_de_passe": hash_mot_de_passe, "id_restaurant": restaurateur.id_restaurant})
        
        print(RestaurateurDao.getRestaurateur(restaurateur.identifiant))
        return RestaurateurDao.getRestaurateur(restaurateur.identifiant)

            
    @staticmethod
    def updateRestaurateur(ancien_identifiant:str, ancien_mot_de_passe:str, restaurateur : Restaurateur) -> Restaurateur:
        #on compare les mots de passe par leur hachage
        hash_mot_de_passe=hashlib.sha512(restaurateur.mot_de_passe.encode("utf-8")).hexdigest()
        # le restaurateur peut changer n'importe quelle information qu'il souhaite sur son statut
        #on effectue la requête SQl sur Postgre
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                print ("ok")
                print(restaurateur.id_restaurant, restaurateur.nom, restaurateur.prenom, restaurateur.identifiant)
                cursor.execute(
                    "UPDATE ensaeats.restaurateur SET id_restaurant = %(id_restaurant)s, nom = %(nom)s, prenom = %(prenom)s, identifiant=%(identifiant)s, mot_de_passe=%(mot_de_passe)s WHERE identifiant=%(ancien_identifiant)s;"
                    , {"id_restaurant": restaurateur.id_restaurant, "nom": restaurateur.nom, "prenom": restaurateur.prenom, "identifiant": restaurateur.identifiant, "mot_de_passe": hash_mot_de_passe, "ancien_identifiant": ancien_identifiant})
                print("okkkk")
        #retourner les modifications qui vont apparaître sur l'interface de fast-api
        return RestaurateurDao.getRestaurateur(restaurateur.identifiant)
    
    @staticmethod
    def deleteRestaurateur(identifiant:str) -> Restaurateur:
        restaurateur_to_delete: Restaurateur = RestaurateurDao.getRestaurateur(identifiant)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("Delete from ensaeats.restaurateur where identifiant=%(identifiant)s;", {"identifiant": restaurateur_to_delete.identifiant})
        return "User "+identifiant+" deleted"

   