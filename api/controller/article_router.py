from fastapi import APIRouter, Header, HTTPException
from API.metier.user import User
from API.service.user_service import UserService
from typing import Optional
from API.exception.user_not_authenticated_exception import UserNotAuthenticated
from API.service.restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from API.dao.article_dao import ArticleDao
from API.metier.article import Article
from API.metier.menu import Menu 

router = APIRouter()


@router.post("/articles/", tags = ['Articles'])
async def post_article(nom : str, composition : str, type: str, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here

        # Création de l'objet article
        article = Article(nom, composition, type)

        return RestaurantsService.addArticle(article)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")


@router.put("/articles/{id_article}", tags = ['Articles'])
async def put_article(id_article : int, article:Article, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    # l'idée serait de mettre en valeur par défaut la composition et le type de base de l'identifiant article
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        if id_article == article.id_article : 
            return RestaurantsService.updateArticle(article = article)
        else : 
            raise HTTPException(stauts_code=401, detail = "Id has been changed")

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")

@router.delete("/articles/", tags = ['Articles'])
async def delete_article(id_article : int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        article = ArticleDao.find_article_by_id_article(id_article) 
        return RestaurantsService.deleteArticle(article)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")

