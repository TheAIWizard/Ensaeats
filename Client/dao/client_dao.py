from Client.business.client import Client
from Client.exception.client_not_found_exception import ClientNotFoundException
from api_minuscule.dao.configuration import DBConnection


import hashlib

""" Par rapport aux risques d'injections SQL: notre code est protégé contre les injections SQL. 
La bibliothèque psycopg, en voyant %(identifiant)s va le remplacer par la valeur de l'entrée username du dictionnaire passé en second paramètre, 
effectuant toutes les transformations nécessaires pour que les caractères dangereux soient neutralisés"""

class ClientDao:

    def consulter_menu():
        pass
    def consulter_avis():
        pass

    @staticmethod
    def verifyPassword(identifiant: str, mot_de_passe: str) -> bool:
        #on compare le hachage du mot de passe entré et stocké dans la base de données
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
    def checkIdentifiantUniqueness(identifiant: str) -> bool:
        """ vérifier que l'identifiant proposé par le client s'authetifiant n'est pas déjà utilisé"""
        """ vérifier qu'un id_restaurant n'existe pas déjà"""
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
            return Client(nom=res["nom"], prenom=res["prenom"], adresse=res["adresse"], identifiant=res["identifiant"], mot_de_passe=res["mot_de_passe"], telephone=res["telephone"])
        else:
            raise ClientNotFoundException(identifiant)

    @staticmethod
    def createClient(client: Client) -> Client:
        #il faudrait hacher le mot de passe : hashlib.sha512(x.encode("utf-8")).hexdigest(), 16 : cet algo de hachage retourne le même hachage pour la même entrée
        #rien ne change en pratique, juste la colonne mot_de_passe qui n'est pas en clair, on compare les hash entre eux
        hash_mot_de_passe=hashlib.sha512(client.mot_de_passe.encode("utf-8")).hexdigest()
        #vérifie si le profil du client n'existe pas déjà
        try:
            ClientDao.getClient(client.identifiant)
        except ClientNotFoundException:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    #on sauvegarde le mot de passe sous forme haché. Ce sont les hachages qui seront comparés pour l'authentification
                    cursor.execute(
                        "INSERT INTO ensaeats.client (nom, prenom, adresse, identifiant, mot_de_passe, telephone) VALUES "
                        "(%(nom)s, %(prenom)s, %(adresse)s,%(identifiant)s, %(mot_de_passe)s, %(telephone)s);", {"nom": client.nom, "prenom": client.prenom, "adresse":client.adresse, "identifiant": client.identifiant, "mot_de_passe": hash_mot_de_passe, "telephone": client.telephone})
            print(hash_mot_de_passe)
            return ClientDao.getClient(client.identifiant)

    @staticmethod
    def updateClient(ancien_identifiant:str, ancien_mot_de_passe:str, identifiant:str, mot_de_passe:str) -> Client:
        #on compare les mots de passe par leur hachage
        hash_ancien_mot_de_passe=hashlib.sha512(ancien_mot_de_passe.encode("utf-8")).hexdigest()
        hash_mot_de_passe=hashlib.sha512(mot_de_passe.encode("utf-8")).hexdigest()
        # le client peut changer n'importe quelle information qu'il souhaite sur son statut
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
                    "UPDATE ensaeats.client SET identifiant=%(identifiant)s, mot_de_passe=%(mot_de_passe)s WHERE identifiant=%(ancien_identifiant)s;", parameters_requests)
        #retourner les modifications qui vont apparaître sur l'interface de fast-api
        return ClientDao.getClient(identifiant) if identifiant else ClientDao.getClient(ancien_identifiant)

    @staticmethod
    def deleteClient(identifiant:str) -> Client:
        client_to_delete: Client = ClientDao.getClient(identifiant)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("Delete from ensaeats.client where identifiant=%(identifiant)s;", {"identifiant": client_to_delete.identifiant})
        return "User "+identifiant+" deleted"

   