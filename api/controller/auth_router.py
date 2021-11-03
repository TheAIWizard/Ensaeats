from fastapi import APIRouter
from API.metier.user import User
from API.service.user_service import UserService

router = APIRouter()


@router.post("/users/", tags=["Utilisateurs"])
def create_user(user: User):
    return UserService.createUser(user)


@router.put("/users/{user_id}", tags=["Utilisateurs"])
def update_user(user_id: str, user: User):
    return UserService.updateUser(user_id, user)


@router.get("/users/{user_id}", tags=["Utilisateurs"])
def get_user(user_id: str):
    return UserService.getUser(user_id)
