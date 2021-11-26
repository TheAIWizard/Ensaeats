from client.service.mapper import BusinessMapper
import requests

class ClientService:

    @staticmethod
    def getClient(identifiant, mot_de_passe):
        parametres = {
            'identifiant_client': identifiant,
            "mot_de_passe_client" : mot_de_passe}
        client_json=requests.get('http://localhost:5000/clients/{}'.format(identifiant), params=parametres, 
                                        headers = {'accept': 'application/json'}).json() 
        client_metier = BusinessMapper.client_mapper(client_json)

        return client_metier