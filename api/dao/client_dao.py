from api.metier.adresse import Adresse
from api.metier.client import Client
from api.exception.client_not_found_exception import ClientNotFoundException
from api.dao.db_connection import DBConnection


import hashlib

""" Par rapport aux risques d'injections SQL: notre code est protégé contre les injections SQL. 
La bibliothèque psycopg, en voyant %(identifiant)s va le remplacer par la valeur de l'entrée username du dictionnaire passé en second paramètre, 
effectuant toutes les transformations nécessaires pour que les caractères dangereux soient neutralisés"""

class ClientDao:

    @staticmethod
    def verifyPassword(identifiant: str, mot_de_passe: str) -> bool:
        #on compare le hachage du mot de passe entré et stocké dans la base de données
        print(mot_de_passe)
        hash_mot_de_passe=hashlib.sha512(mot_de_passe.encode("utf-8")).hexdigest()
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM ensaeats.client where identifiant=%(identifiant)s and mot_de_passe=%(mot_de_passe)s;"
                    ,{"identifiant": identifiant, "mot_de_passe": hash_mot_de_passe}
                )
                res = cursor.fetchone()
            if res != None:
                return True
            return False

    @staticmethod
    def getClient(identifiant: str) -> Client:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "\
                    "\nFROM ensaeats.client WHERE identifiant=%(identifiant)s;",
                    {"identifiant":identifiant}
                )
                res = cursor.fetchone()
        if res != None: 
            return Client(id_client = res["id_client"],nom=res["nom"], prenom=res["prenom"],identifiant=res["identifiant"], mot_de_passe=res["mot_de_passe"], telephone=res["telephone"], adresse = res["adresse"])
        else:
            raise ClientNotFoundException(identifiant)

    @staticmethod
    def verifierIdUnique(identifiant: str) -> bool:
        """ vérifier que l'identifiant proposé par un client s'inscrivant n'est pas déjà utilisé"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "\nFROM ensaeats.client WHERE identifiant=%(identifiant)s;",
                    {"identifiant":identifiant}
                )
                res = cursor.fetchone()
            if res != None:
                return False
            return True
    
    
    @staticmethod
    def createClient(client: Client) -> Client:
        #il faudrait hacher le mot de passe : hashlib.sha512(x.encode("utf-8")).hexdigest(), 16 : cet algo de hachage retourne le même hachage pour la même entrée
        #rien ne change en pratique, juste la colonne mot_de_passe qui n'est pas en clair, on compare les hash entre eux
        hash_mot_de_passe=hashlib.sha512(client.mot_de_passe.encode("utf-8")).hexdigest()
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                #on sauvegarde le mot de passe sous forme haché. Ce sont les hachages qui seront comparés pour l'authentification
                cursor.execute(
                    "INSERT INTO ensaeats.client (nom, prenom, identifiant, mot_de_passe, telephone, adresse) VALUES "
                    "(%(nom)s, %(prenom)s,%(identifiant)s, %(mot_de_passe)s, %(telephone)s, %(adresse)s);"
                    , {"nom": client.nom, "prenom": client.prenom, "identifiant": client.identifiant, "mot_de_passe": hash_mot_de_passe, "telephone": client.telephone, "adresse": client.adresse})
        return ClientDao.getClient(client.identifiant)

    @staticmethod
    def updateClient(ancien_identifiant:str, ancien_mot_de_passe:str, client : Client) -> Client:
        hash_mot_de_passe=hashlib.sha512(client.mot_de_passe.encode("utf-8")).hexdigest()
        # le client peut changer n'importe quelle information qu'il souhaite sur son statut
        #on effectue la requête SQl sur Postgre
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE ensaeats.client SET nom = %(nom)s, prenom = %(prenom)s, telephone = %(telephone)s, identifiant=%(identifiant)s, mot_de_passe=%(mot_de_passe)s, adresse= %(adresse)s WHERE identifiant=%(ancien_identifiant)s;"
                    , {"nom": client.nom, "prenom": client.prenom, "telephone": client.telephone, "identifiant": client.identifiant, "mot_de_passe": hash_mot_de_passe, "adresse": client.adresse, "ancien_identifiant": ancien_identifiant})
        #retourner les modifications qui vont apparaître sur l'interface de fast-api
        
        return ClientDao.getClient(client.identifiant)

    @staticmethod
    def deleteClient(identifiant:str) -> Client:
        client_to_delete: Client = ClientDao.getClient(identifiant)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("Delete from ensaeats.client where identifiant=%(identifiant)s;", {"identifiant": client_to_delete.identifiant})
        return "User "+identifiant+" deleted"