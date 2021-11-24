from fastapi import APIRouter, Header
from typing import Optional
from api.metier.client import Client
from api.service.client_service import ClientService

router = APIRouter()


@router.post("/clients/", tags=["Clients"])
async def create_client(client: Client):
    return ClientService.createClient(client)


@router.put("/clients/{ancien_identifiant_client}", tags=["Clients"])
async def update_client(ancien_identifiant_client: str, ancien_mot_de_passe_client:str, identifiant_client: Optional[str] = Header(None), mot_de_passe_client:Optional[str] = Header(None)):
    return ClientService.authenticate_and_update_client(ancien_identifiant_client, ancien_mot_de_passe_client, identifiant_client, mot_de_passe_client)


@router.get("/clients/{identifiant_client}", tags=["Clients"])
async def get_client(identifiant_client: str, mot_de_passe_client:str):
    return ClientService.authenticate_and_get_client(identifiant_client, mot_de_passe_client)

@router.delete("/clients/{identifiant_client}", tags=["Clients"])
async def delete_client(identifiant_client: str, mot_de_passe_client:str):
    return ClientService.authenticate_and_delete_client(identifiant_client, mot_de_passe_client)