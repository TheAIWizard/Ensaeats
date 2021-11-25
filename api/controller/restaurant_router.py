from fastapi import APIRouter, Header, HTTPException
from api.metier.user import User
from api.service.restaurateur_service import RestaurateurService
from typing import Optional
from api.exception.user_not_authenticated_exception import UserNotAuthenticated
from api.service.restaurant_service import RestaurantsService
from api.dao.menu_dao import MenuDao
from api.dao.article_dao import ArticleDao
from api.metier.article import Article
from api.metier.menu import Menu 
from api.service.client_service import ClientService

router = APIRouter()


@router.get("/restaurants/", tags=["Restaurants"])
#async def get_restaurants(identifiant_client: Optional[str] = Header(None), mot_de_passe_client: Optional[str] = Header(None), localisation:str="Bruz", term : str = "", radius : int = 2000):
async def get_restaurants(identifiant_client: str, mot_de_passe_client: str, localisation:str="Bruz", term : str = "", radius : int = 2000):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant_client, mot_de_passe=mot_de_passe_client)
        print(client)
        # # call your service here
        return RestaurantsService.getRestaurants(localisation, term, radius)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="Vous devez vous connecter ou créer un compte en tant que client")


@router.get("/restaurant/{id_restaurant}", tags=["Restaurants"])
async def get_restaurant(identifiant_client: str, mot_de_passe_client: str, id_restaurant: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant_client, mot_de_passe=mot_de_passe_client)
        print(client)
        # # call your service here
        try : 
            return RestaurantsService.getRestaurant(id_restaurant)
        except : 
            raise HTTPException(status_code=403, detail = "Le restaurant n'est pas dans l'API de Yelp")
            
    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="Vous devez vous connecter ou créer un compte en tant que client")




