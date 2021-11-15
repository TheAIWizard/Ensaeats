import uvicorn
from api_minuscule.app import app

if __name__ == "__main__":
    #sur la VM
    #uvicorn.run(app, host="0.0.0.0", port=5000)
    #si vous avez comme erreur que le port 5000 est déjà utilisé, relancer le terminal sinon tentez uvicorn.run(app, host="0.0.0.0", port=5000).shutdown() avant relance
    
    #sur son ordinateur personnel
    uvicorn.run(app, host="0.0.0.0", port=80)





""" exemple post
{
  "nom": "Delacroix",
  "prenom": "Martin",
  "identifiant": "CrossMartin",
  "mot_de_passe": "1234",
  "id_restaurant": "LTy9AUgMnLn8YS21KfFZ8g"
}

{
  "nom": "Smith",
  "prenom": "Leonard",
  "identifiant": "TheSmith",
  "mot_de_passe": "TheSmith",
  "id_restaurant": "kFHkpnV7JI_P--xORaIazw"
}
 """