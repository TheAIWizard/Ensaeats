from fastapi import APIRouter, Header
from typing import Optional
from api.metier.restaurateur import Restaurateur
from api.service.restaurateur_service import RestaurateurService

router = APIRouter()


@router.post("/restaurateurs/", tags=["Restaurateurs"])
async def create_restaurateur(restaurateur: Restaurateur):
    return RestaurateurService.createRestaurateur(restaurateur=restaurateur)


@router.put("/restaurateurs/{ancien_identifiant_restaurateur_restaurateur}", tags=["Restaurateurs"])
async def update_restaurateur(ancien_identifiant_restaurateur: str, ancien_mot_de_passe_restaurateur:str, identifiant_restaurateur: Optional[str] = Header(None), mot_de_passe_restaurateur:Optional[str] = Header(None)):
    return RestaurateurService.authenticate_and_update_restaurateur(ancien_identifiant=ancien_identifiant_restaurateur, ancien_mot_de_passe=ancien_mot_de_passe_restaurateur
    , identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)


@router.get("/restaurateurs/{identifiant_restaurateur}", tags=["Restaurateurs"])
async def get_restaurateur(identifiant_restaurateur: str, mot_de_passe_restaurateur:str):
    return RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)

@router.delete("/restaurateurs/{identifiant_restaurateur}", tags=["Restaurateurs"])
async def delete_restaurateur(identifiant_restaurateur: str, mot_de_passe_restaurateur:str):
    return RestaurateurService.authenticate_and_delete_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)