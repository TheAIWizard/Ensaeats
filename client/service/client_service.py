from client.service.mapper import BusinessMapper
import requests

class ClientService:

    @staticmethod
    def getClient(identifiant, mot_de_passe):
        """[Permet de recupérer les informations sur un utilisateur c
        onnaissant sont identifiant et mot de passe]

        Args:
            identifiant ([str]): [L'identifiant de l'utilisateur]
            mot_de_passe ([str]): [Le mot de passe de l'utilisateur]

        Returns:
            [Client]: [description]
        """
        headers_client = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}
        parametres = {
            'identifiant_client': identifiant,
            "mot_de_passe_client" : mot_de_passe}

        result = requests.get('http://localhost:5000/clients/{}'.format(identifiant), 
                            params=parametres, 
                            headers = headers_client)
        if result.status_code == 200:
            client_json = result.json()
            client_metier = BusinessMapper.client_mapper(client_json)
            return client_metier
        return False
    
    @staticmethod
    def postClient(client):
        """[Ajout d'un client dans la base de données]

        Args:
            client ([Client]): [Le nouveau client qui vient de créer un compte]

        Returns:
            [int]: [Status code : code indiquant l'état de l'insertion]
        """
        headers_client = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}
        result_post = requests.post('http://localhost:5000/clients/', 
                            json = dict(client), 
                            headers = headers_client)
        return result_post.status_code
        