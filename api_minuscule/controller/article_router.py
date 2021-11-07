from fastapi import APIRouter, Header, HTTPException
from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.service.restaurateur_service import RestaurateurService
from typing import Optional
from api_minuscule.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api_minuscule.service.restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from api_minuscule.dao.article_dao import ArticleDao
from api_minuscule.metier.article import Article
from api_minuscule.metier.menu import Menu 

router = APIRouter()

@router.post("/articles/", tags = ['Articles'])
async def post_article(article : Article, restaurateurname: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # restaurateur = RestaurateurService.authenticate_and_get_restaurateur(
        #     restaurateurname=restaurateurname, password=password)
        # print(restaurateur)
        # # call your service here

        # Création de l'objet article

        return RestaurantsService.addArticle(article)

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")


@router.put("/articles/{id_article}", tags = ['Articles'])
async def put_article(id_article : int, article:Article, restaurateurname: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    # l'idée serait de mettre en valeur par défaut la composition et le type de base de l'identifiant article
    try:
        # restaurateur = RestaurateurService.authenticate_and_get_restaurateur(
        #     restaurateurname=restaurateurname, password=password)
        # print(restaurateur)
        # # call your service here
        if id_article == article.id_article : 
            return RestaurantsService.updateArticle(article = article)
        else : 
            raise HTTPException(stauts_code=401, detail = "Id has been changed")

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")

@router.delete("/articles/", tags = ['Articles'])
async def delete_article(id_article : int, restaurateurname: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # restaurateur = RestaurateurService.authenticate_and_get_restaurateur(
        #     restaurateurname=restaurateurname, password=password)
        # print(Restaurateur)
        # # call your service here
        article = ArticleDao.find_article_by_id_article(id_article) 
        return RestaurantsService.deleteArticle(article)

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")
