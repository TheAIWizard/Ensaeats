from typing import List
from api.metier.avis import Avis
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from datetime import datetime
#date actuelle
now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

 

class AvisDao(metaclass=Singleton):
    """
    Cette classe nous permet de gérer les avis laisser par les clients.

    fin_avis_by_restaurant (id_restaurant) :
        retourne la liste des restaurant

    add_avis (avis):
        retourne Vrai si un avis est ajouté dans la table avis de notre BD sinon Faux.
    """
    @staticmethod
    def find_avis_by_id_restaurant(id_restaurant : str)-> List:
        '''
        Cette fonction permet de voir les restaurant par id

        Attribute :
        -----------
        id_restaurant : str

        return : list
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    " FROM  ensaeats.avis "\
                    " WHERE id_restaurant = %(id_restaurant)s"
                    , {"id_restaurant": id_restaurant}
                )
                res = cursor.fetchall()
        avis_restau = []
        if res :
            for row in res : 
                avis_restau.append(Avis(avis=row["avis"],identifiant_auteur=row["nom_auteur"],date=str(row["date"]),id_restaurant=row['id_restaurant']))
        return avis_restau

    @staticmethod
    def add_avis(avis : Avis) -> Avis: 
        '''
        Ajout un avis dans la table avis de notre base de données ensaeats

        return bool 
        
        '''
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.avis (avis, date, nom_auteur, id_restaurant) VALUES "\
                    "(%(avis)s, %(date)s, %(nom_auteur)s, %(id_restaurant)s)"\
                    "RETURNING avis;"
                , {#"id_avis" : avis.id_avis,
                    "avis": avis.avis
                  , "date" : now   #on réactualise la date de publication de l'avis
                  , "nom_auteur" : avis.identifiant_auteur
                  , "id_restaurant": avis.id_restaurant})
                res = cursor.fetchone()
            
        if res :
            created = True
            return avis
        else : 
            return "Ajout d'avis échoué"

    # avis_routeur, consulterAvis(avec identifiant), modifierAvis(avec identifiant), supprimerAvis() 
