import dotenv
from fastapi import FastAPI
from api.controller import restaurant_router, article_router, \
     menu_router, avis_router, restaurateur_router
from client.controller import client_router
from api.controller import commande_router
dotenv.load_dotenv(override=True)


app = FastAPI(title='EnsaEats', version='2.0', description="un micro-service\
    /ayant pour objectif de rapprocher\
    / restaurant et restaurateur", contact={'name': 'Groupe n°x'})

app.include_router(restaurateur_router.router)
app.include_router(restaurant_router.router)
app.include_router(article_router.router)
app.include_router(menu_router.router)
app.include_router(client_router.router)
app.include_router(commande_router.router)
app.include_router(avis_router.router)


""" @app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id} """
