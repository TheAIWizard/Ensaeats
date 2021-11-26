from fastapi import APIRouter, Header, HTTPException
from api.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api.service.client_service import ClientService
from api.service.avis_service import AvisService
from api.metier.avis import Avis
from api.exception.client_not_authenticated_exception import ClientNotAuthenticated
from api.service.restaurateur_service import RestaurateurService
router = APIRouter()

@router.get("/avis/", tags=["Avis"])
async def get_avis_by_id_restaurant(id_restaurant: str, identifiant: str, mot_de_passe: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant, mot_de_passe=mot_de_passe)
        return AvisService.get_avis_by_id_restaurant(id_restaurant)
    
    except :
        try : 
            restaurateur = RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant, mot_de_passe=mot_de_passe)
            return AvisService.get_avis_by_id_restaurant(id_restaurant)
        
        except : 
            raise HTTPException(status_code=401, detail="Vous devez être connecté en tant que restaurateur ou client")
    

@router.post("/avis/", tags=["Avis"])
async def post_avis(avis:Avis, identifiant_client: str, mot_de_passe_client: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant_client, mot_de_passe=mot_de_passe_client)
        if avis.avis == '' : 
            raise HTTPException(status_code=422, detail="Votre avis est vide")
        else : 
            return AvisService.ajout_avis(avis)
            
    except : 
        raise HTTPException(status_code=401, detail="Vous devez être connecté en tant que client") 
    


        
    