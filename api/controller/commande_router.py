from fastapi import APIRouter, Header, HTTPException
from api.metier.commande import Commande
from api.service.client_service import ClientService
from api.service.restaurateur_service import RestaurateurService
from api.service.commande_service import CommandeService
from typing import Optional

from client.exception.client_not_authenticated_exception import ClientNotAuthenticated

router = APIRouter()

@router.post("/commandes/", tags=["Commandes"]) #post_commande(commande: Commande, identifiant: Optional[str] = Header(None), password: Optional[str] = Header(None)):
async def post_commande(commande: Commande, identifiant: str, password: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant, mot_de_passe=password)
        print(client)
        return CommandeService.valider_commande(commande)
        
    except : 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")
    

@router.get("/commandes/client", tags=["Commandes"])
async def get_commandes_client(identifiant_client: str, mot_de_passe_client: str):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=identifiant_client, mot_de_passe=mot_de_passe_client)
        print(client)
        return CommandeService.obtenir_commandes_client(client)
        
    except ClientNotAuthenticated: 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")

@router.get("/commandes/restaurant", tags=["Commandes"])
async def get_commandes_restaurant(id_restaurant: str, identifiant_restaurateur: str, mot_de_passe_restaurateur: str):
    try:
        restaurateur = RestaurateurService.authenticate_and_get_restaurateur(identifiant=identifiant_restaurateur, mot_de_passe=mot_de_passe_restaurateur)
        #On s'assure qu'il s'agit du bon id_restaurant pour le restaurateur sinon n'importe quel restaurateur peut accéder aux commandes
        if restaurateur.id_restaurant!=id_restaurant:
            return "Le restaurateur n'appartient pas à ce restaurant. Changez id_restaurant"
        return CommandeService.obtenir_commandes_id_restaurant(id_restaurant=id_restaurant)
        
    except ClientNotAuthenticated: 
        raise HTTPException(status_code=403, detail="Vous devez être connecté en tant que client")