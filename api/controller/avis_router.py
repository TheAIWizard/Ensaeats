from fastapi import APIRouter, Header, HTTPException
from api.service.client_service import ClientService
from api.service.avis_service import AvisService
from api.metier.avis import Avis
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated

router = APIRouter()

@router.get("/avis/", tags=["Avis"])
async def get_avis_by_id_restaurant(id_restaurant: str, username: str, password: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=username, mot_de_passe=password)
        return AvisService.get_avis_by_id_restaurant(id_restaurant)
        
    except ClientNotAuthenticated: 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")

@router.post("/avis/", tags=["Avis"])
async def post_avis(avis:Avis, username: str, password: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=username, mot_de_passe=password)
        return AvisService.ajout_avis(avis)
        
    except : 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client") 
    


        
    