import uvicorn

from api_minuscule.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
    """ exemple post
{
  "nom": "Delacroix",
  "prenom": "Martin",
  "identifiant": "CrossMartin",
  "mot_de_passe": "1234",
  "id_restaurant": "LTy9AUgMnLn8YS21KfFZ8g"
}
 """