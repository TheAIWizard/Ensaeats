from fastapi import APIRouter, Header
from typing import Optional

from fastapi.exceptions import HTTPException
from api.metier.restaurateur import Restaurateur
from api.service.restaurateur_service import RestaurateurService

router = APIRouter()


@router.post("/restaurateurs/", tags=["Restaurateurs"])
async def create_restaurateur(restaurateur: Restaurateur):
    if (restaurateur.identifiant == '' or restaurateur.mot_de_passe == ''):
        raise HTTPException(status_code=422, detail="Vous ne pouvez pas rentré un identifiant ou mot de passe vide")
    else :   
        try : 
            return RestaurateurService.createRestaurateur(restaurateur=restaurateur)
        except : 
            raise HTTPException(status_code=422, detail="Vous n'avez pas pu créer votre compte")


@router.put("/restaurateurs/{ancien_identifiant_restaurateur}", tags=["Restaurateurs"])
async def update_restaurateur(restaurateur : Restaurateur, identifiant_restaurateur: Optional[str] = Header(None), mot_de_passe_restaurateur:Optional[str] = Header(None)):
    if (restaurateur.identifiant == '' or restaurateur.mot_de_passe == '') : 
         raise HTTPException(status_code=422, detail = "Vous ne pouvez pas avoir un identifiant ou mot de passe vide")
    else : 
        try : 
            return RestaurateurService.authenticate_and_update_restaurateur(ancien_identifiant=identifiant_restaurateur, ancien_mot_de_passe=mot_de_passe_restaurateur, restaurateur = restaurateur)
        except : 
            raise HTTPException(status_code=422, detail= "La modification n'a pas été prise en compte") 

      

@router.get("/restaurateurs/{identifiant_restaurateur}", tags=["Restaurateurs"])
async def get_restaurateur(identifiant_restaurateur: str, mot_de_passe_restaurateur:str):
    return RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)

@router.delete("/restaurateurs/{identifiant_restaurateur}", tags=["Restaurateurs"])
async def delete_restaurateur(identifiant_restaurateur: str, mot_de_passe_restaurateur:str):
    return RestaurateurService.authenticate_and_delete_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)