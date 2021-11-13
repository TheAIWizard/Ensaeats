import os
from client.service.client_service import ClientService

#print everything
#print(os.environ["HOST"])
print(ClientService.authenticate_and_get_client("KingAlex35","KingAlex35"))