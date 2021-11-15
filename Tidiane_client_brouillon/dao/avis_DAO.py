from typing import List
from brouillon.metier.avis import Avis
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection

 

class AvisDao(metaclass=Singleton):
    @staticmethod
    def find_avis_by_id_restaurant(id_restau : str)-> List:
        '''
        Get all the reviews of a restaurant thanks to its id
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM  ensaeats.avis   "\
                    "\nWHERE id_restaurant = %(id_restaurant)s"
                    , {"id_restaurant": id_restau}
                )
                res = cursor.fetchall()
        avis_restau = []
        if res :
            for row in res : 
                avis_restau.append(row["avis"])
        return avis_restau

    @staticmethod
    def add_avis(avis : Avis) -> bool: 
        '''
        Add a restaurant review 
        
        '''
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.avis (avis, identifiant_auteur, id_restaurant) VALUES "\
                    "(%(avis)s, %(identifiant_auteur)s, %(id_restaurant)s)"\
                    "RETURNING avis;"
                , {#"id_avis" : avis.id_avis,
                    "avis": avis.avis
                  , "identifiant_auteur" : avis.identifiant_auteur
                  , "date" : avis.date
                  , "id_restaurant": avis.id_restaurant})
                res = cursor.fetchone()
        if res :
            created = True
        return "Avis ajouté" if created else "Ajout d'avis échoué"

    # avis_routeur, consulterAvis(avec identifiant), modifierAvis(avec identifiant), supprimerAvis() 