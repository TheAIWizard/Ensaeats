from fastapi import APIRouter, Header
from typing import Optional
from api.metier.restaurateur import Restaurateur
from api.service.restaurateur_service import RestaurateurService

router = APIRouter()


@router.post("/restaurateurs/", tags=["Restaurateurs"])
async def create_restaurateur(restaurateur: Restaurateur):
    return RestaurateurService.createRestaurateur(restaurateur)


@router.put("/restaurateurs/{ancien_restaurateur_id}", tags=["Restaurateur"])
async def update_restaurateur(ancien_restaurateur_id: str, ancien_mot_de_passe:str, restaurateur_id: Optional[str] = Header(None), mot_de_passe:Optional[str] = Header(None)):
    return RestaurateurService.authenticate_and_update_restaurateur(ancien_restaurateur_id, ancien_mot_de_passe, restaurateur_id, mot_de_passe)


@router.get("/restaurateurs/{restaurateur_id}", tags=["Restaurateurs"])
async def get_restaurateur(restaurateur_id: str, password:str):
    return RestaurateurService.authenticate_and_get_restaurateur(restaurateur_id, password)

@router.delete("/restaurateurs/{restaurateur_id}", tags=["Restaurateurs"])
async def delete_restaurateur(restaurateur_id: str, password:str):
    return RestaurateurService.authenticate_and_delete_restaurateur(restaurateur_id, password)