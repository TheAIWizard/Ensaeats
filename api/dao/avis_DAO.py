from typing import List
from api.metier.avis import Avis
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from datetime import datetime
#date actuelle
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

 

class AvisDao(metaclass=Singleton):
    """
    Cette classe nous permet de gerer les avis laisser par les clients sur la DAo.

    fin_avis_by_restaurant (id_restaurant) :
    Cette fonction permet de recuperer les avis sur les client dans l'api de yelp

    return : json 

    add_avis (avis):
    La fonction add_avis nous permet d'ajouter des avis dans la base de donnée

    return : void
    retuirn de message de confirmation 
        
    """
    @staticmethod
    def find_avis_by_id_restaurant(id_restaurant : str)-> List:
        '''
        Get all the reviews of a restaurant thanks to its id
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM  ensaeats.avis   "\
                    "\nWHERE id_restaurant = %(id_restaurant)s"
                    , {"id_restaurant": id_restaurant}
                )
                res = cursor.fetchall()
        avis_restau = []
        if res :
            for row in res : 
                avis_restau.append(Avis(avis=row["avis"],identifiant_auteur=row["identifiant_auteur"],date=str(row["date"]),id_restaurant=row['id_restaurant']))
        return avis_restau

    @staticmethod
    def add_avis(avis : Avis) -> Avis: 
        '''
        Add a restaurant review 
        
        '''
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.avis (avis, identifiant_auteur, date, id_restaurant) VALUES "\
                    "(%(avis)s, %(identifiant_auteur)s, %(date)s, %(id_restaurant)s)"\
                    "RETURNING avis;"
                , {#"id_avis" : avis.id_avis,
                    "avis": avis.avis
                  , "identifiant_auteur" : avis.identifiant_auteur
                  , "date" : now   #on réactualise la date de publication de l'avis
                  , "id_restaurant": avis.id_restaurant})
                res = cursor.fetchone()
        if res :
            created = True
        return ("Avis ajouté",avis) if created else "Ajout d'avis échoué"

    # avis_routeur, consulterAvis(avec identifiant), modifierAvis(avec identifiant), supprimerAvis() 
