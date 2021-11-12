from fastapi import APIRouter, Header
from typing import Optional
from client.business.client import Client
from client.service.client_service import ClientService

router = APIRouter()


@router.post("/clients/", tags=["Clients"])
async def create_client(client: Client):
    return ClientService.createClient(client)


@router.put("/clients/{ancien_client_id}", tags=["Client"])
async def update_client(ancien_client_id: str, ancien_mot_de_passe:str, client_id: Optional[str] = Header(None), mot_de_passe:Optional[str] = Header(None)):
    return ClientService.authenticate_and_update_client(ancien_client_id, ancien_mot_de_passe, client_id, mot_de_passe)


@router.get("/clients/{client_id}", tags=["Clients"])
async def get_client(client_id: str, password:str):
    return ClientService.authenticate_and_get_client(client_id, password)

@router.delete("/clients/{client_id}", tags=["Clients"])
async def delete_client(client_id: str, password:str):
    return ClientService.authenticate_and_delete_client(client_id, password)