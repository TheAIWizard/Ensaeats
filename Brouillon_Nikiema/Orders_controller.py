from fastapi import FastAPI
from Restaurant_service import RestaurantsService
from typing import Optional

router = APIRouter()


@router.get("/restaurant/{id}")
async def get_business(id: str):
    business = RestaurantsService.getRestaurant(id)
    return business


@router.get("/restaurants")
async def get_businesses(term: Optional[str] = None, location: str = "Rennes", radius: int = 8):
    business = RestaurantsService.getRestaurants(term, location, radius)
    return business
