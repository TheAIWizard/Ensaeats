from fastapi import APIRouter, Header, HTTPException
from api.metier.commande import Commande
from api.service.client_service import ClientService
from api.service.commande_service import Faire_commande
from typing import Optional

from client.exception.client_not_authenticated_exception import ClientNotAuthenticated

router = APIRouter()

@router.post("/commandes/", tags=["Commandes"])
async def post_commande(commande: Commande, identifiant: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant, password=password)
        print(client)
        return Faire_commande.valider_commande(commande)
        
    except : 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")
    

@router.get("/commandes/", tags=["Commandes"])
async def get_commandes_client(identifiant: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant, password=password)
        print(client)
        return Faire_commande.obtenir_commandes(client)
        
    except ClientNotAuthenticated: 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")