import dotenv
from fastapi import FastAPI
from api.controller import restaurant_router, article_router, menu_router, client_router, commande_router, avis_router, restaurateur_router
dotenv.load_dotenv(override=True)


app = FastAPI(title='EnsaEats',version='2.0',description="un micro-serviceayant pour objectif de rapprocher restaurant et restaurateur"
              ,contact={'name':'Groupe n°x'})

app.include_router(restaurateur_router.router)
app.include_router(restaurant_router.router)
app.include_router(article_router.router)
app.include_router(menu_router.router)
app.include_router(client_router.router)
app.include_router(commande_router.router)
app.include_router(avis_router.router)
