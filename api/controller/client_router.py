from fastapi import APIRouter, Header, HTTPException
from typing import Optional
from api.metier.client import Client
from api.service.client_service import ClientService
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
router = APIRouter()


@router.post("/clients/", tags=["Clients"])
async def create_client(client: Client):
    return ClientService.createClient(client)


@router.put("/clients/{ancien_identifiant_client}", tags=["Clients"])
async def update_client(ancien_identifiant_client: str, ancien_mot_de_passe_client:str, identifiant_client: Optional[str] = Header(None), mot_de_passe_client:Optional[str] = Header(None)):
    return ClientService.authenticate_and_update_client(ancien_identifiant_client, ancien_mot_de_passe_client, identifiant_client, mot_de_passe_client)


@router.get("/clients/{identifiant_client}", tags=["Clients"])
async def get_client(identifiant_client: str, mot_de_passe_client:str):
    try : 
        client = ClientService.authenticate_and_get_client(identifiant_client, mot_de_passe_client)
        print(client)
        # # call your service here
        return client
    
    except ClientNotAuthenticated: 
        raise HTTPException(status_code=403, detail= "Vous n'avez pas pu vous connecter")

@router.delete("/clients/{identifiant_client}", tags=["Clients"])
async def delete_client(identifiant_client: str, mot_de_passe_client:str):
    return ClientService.authenticate_and_delete_client(identifiant_client, mot_de_passe_client)