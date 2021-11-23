import dotenv
from fastapi import FastAPI
from api.controller import auth_router, restaurant_router, article_router, menu_router, client_router, commande_router, avis_router
dotenv.load_dotenv(override=True)


app = FastAPI()

app.include_router(auth_router.router)
app.include_router(restaurant_router.router)
app.include_router(article_router.router)
app.include_router(menu_router.router)
app.include_router(client_router.router)
app.include_router(commande_router.router)
app.include_router(avis_router.router)
