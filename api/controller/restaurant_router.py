from fastapi import APIRouter, Header, HTTPException
from API.metier.user import User
from API.service.user_service import UserService
from typing import Optional
from API.exception.user_not_authenticated_exception import UserNotAuthenticated
from API.service.restaurant_service import RestaurantsService
router = APIRouter()


@router.get("/restaurants/", tags=["restaurants"])
def get_restaurants(username: Optional[str] = Header(None), password: Optional[str] = Header(None), localisation:str="Bruz", term : str = ""):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getRestaurants(localisation)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.get("/restaurants/{id_restaurant}")
async def get_restaurants(username: Optional[str] = Header(None), password: Optional[str] = Header(None), localisation:str="Bruz"):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getRestaurants(localisation)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")
