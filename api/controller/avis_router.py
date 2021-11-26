from fastapi import APIRouter, Header, HTTPException
from api.service.client_service import ClientService
from api.service.avis_service import AvisService
from api.metier.avis import Avis
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated

router = APIRouter()

@router.get("/avis/", tags=["Avis"])
async def get_avis_by_id_restaurant(id_restaurant: str, identifiant_client: str, mot_de_passe_client: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant_client, mot_de_passe=mot_de_passe_client)
        return AvisService.get_avis_by_id_restaurant(id_restaurant)
        
    except ClientNotAuthenticated: 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")

@router.post("/avis/", tags=["Avis"])
async def post_avis(avis:Avis, identifiant_client: str, mot_de_passe_client: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant_client, mot_de_passe=mot_de_passe_client)
        try : 
            return AvisService.ajout_avis(avis)
        except : 
            raise HTTPException(status_code=403, detail="Votre avis n'a pas été pris en compte")
    except : 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client") 
    


        
    