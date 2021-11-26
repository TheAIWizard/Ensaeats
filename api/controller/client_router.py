from fastapi import APIRouter, Header, HTTPException
from typing import Optional
from api.metier.client import Client
from api.service.client_service import ClientService
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
router = APIRouter()


@router.post("/clients/", tags=["Clients"])
async def create_client(client: Client):
    if (client.identifiant == '' or client.mot_de_passe == '') : 
        raise HTTPException(status_code=401, detail = "Vous ne pouvez pas rentré un identifiant ou mot de passe vide")
    else : 
        try : 
            return ClientService.createClient(client)
        except : 
            raise HTTPException(status_code=401, detail="L'identifiant que vous avez rentré est déjà pris")
        
@router.put("/clients/{ancien_identifiant_client}", tags=["Clients"])
async def update_client(client : Client, identifiant_client: Optional[str] = Header(None), mot_de_passe_client:Optional[str] = Header(None)):
    if (client.identifiant == '' or client.mot_de_passe == '') : 
         raise HTTPException(status_code=401, detail = "Vous ne pouvez pas avoir un identifiant ou mot de passe vide")
    else : 
        try : 
            return ClientService.authenticate_and_update_client(identifiant_client,mot_de_passe_client, client)
        except : 
            raise HTTPException(status_code=401, detail= "La modification n'a pas été prise en compte") 


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