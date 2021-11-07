from fastapi import APIRouter
from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.service.restaurateur_service import RestaurateurService

router = APIRouter()


@router.post("/restaurateurs/", tags=["Restaurateurs"])
def create_restaurateur(restaurateur: Restaurateur):
    return RestaurateurService.createRestaurateur(restaurateur)


@router.put("/restaurateurs/{restaurateur_id}", tags=["Restaurateur"])
def update_restaurateur(restaurateur_id: str, restaurateur: Restaurateur):
    return RestaurateurService.updateRestaurateur(restaurateur_id, restaurateur)


@router.get("/restaurateurs/{restaurateur_id}", tags=["Restaurateurs"])
def get_restaurateur(restaurateur_id: str):
    return RestaurateurService.getRestaurateur(restaurateur_id)
