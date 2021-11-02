from Restaurant_service import RestaurantsService
from typing import Optional

router = APIRouter()


@router.get("/restaurant/{id}")
async def get_buisness(id: str):
    buisness = RestaurantsService.getRestaurant(id)
    return buisness


@router.get("/restaurants")
async def get_buisnesses(term: Optional[str] = None, location: str = "Rennes", radius: int = 8):
    buisness = RestaurantsService.getRestaurants(term, location, radius)
    return buisness
