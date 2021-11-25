from fastapi import APIRouter, Header, HTTPException
from api.metier.restaurateur import Restaurateur
from api.service.restaurateur_service import RestaurateurService
from typing import Optional
from api.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api.service.restaurant_service import RestaurantsService
from api.dao.menu_dao import MenuDao
from api.dao.article_dao import ArticleDao
from api.metier.article import Article
from api.metier.menu import Menu

router = APIRouter()

@router.post("/articles/", tags = ['Articles'])
async def post_article(article : Article, identifiant_restaurateur: str, mot_de_passe_restaurateur: str):
    try:
        restaurateur = RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)
        print(restaurateur)
        # # call your service here

        # Création de l'objet article

        return RestaurantsService.addArticle(article)

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Le restaurateur doit être connecté")


@router.put("/articles/{id_article}", tags = ['Articles'])
async def put_article(id_article : int, article:Article, identifiant_restaurateur: str, mot_de_passe_restaurateur: str):
    # l'idée serait de mettre en valeur par défaut la composition et le type de base de l'identifiant article
    try:
        restaurateur = RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)
        print(restaurateur)
        # # call your service here
        if id_article == article.id_article : 
            return RestaurantsService.updateArticle(article = article)
        else : 
            raise HTTPException(status_code=401, detail = "Vous n'avez pas le droit de changer l'identifiant de l'article")

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Vous devez être connecter en tant que restaurateur ")

@router.delete("/articles/", tags = ['Articles'])
async def delete_article(id_article : int, identifiant_restaurateur: str, mot_de_passe_restaurateur: str):
    try:
        restaurateur = RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)
        print(Restaurateur)
        # # call your service here
        article = ArticleDao.find_article_by_id_article(id_article) 
        return RestaurantsService.deleteArticle(article)

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")
