from client.service.mapper import BusinessMapper
import requests

class ClientService:

    @staticmethod
    def getClient(identifiant, mot_de_passe):
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
        