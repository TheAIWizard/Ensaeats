import os

import dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from api.utils.singleton import Singleton


class DBConnection(metaclass=Singleton):
    """
    La classe DBConnection est la super classe permettant de faire la
    connexion avec notre base de données.
    """
    def __init__(self):
        dotenv.load_dotenv(override=True)
        # Open the connection to the ENSAI postgres server.
        self.__connection = psycopg2.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DATABASE"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)
        # Connect to postgres docker
        """ self.__connection = psycopg2.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            database=os.environ["DATABASE"],
            # user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            cursor_factory=RealDictCursor)          
            self.__connection =psycopg2.connect(
            dbname = "SCRIPT_SQL_BDD",
            user = "postgres",
            host = "host.docker.internal",
            password = "postgres",
            cursor_factory=RealDictCursor
) """

    @property
    def connection(self):
        """
        return the opened connection.

        :return: the opened connection.
        """
        return self.__connection
